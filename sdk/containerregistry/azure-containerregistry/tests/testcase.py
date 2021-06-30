# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import copy
import json
import logging
import os
import pytest
import six
import time

from azure.containerregistry import (
    ContainerRegistryClient,
)
from azure.containerregistry._helpers import _is_tag

from azure.core.credentials import AccessToken
from azure.mgmt.containerregistry import ContainerRegistryManagementClient
from azure.mgmt.containerregistry.models import ImportImageParameters, ImportSource, ImportMode
from azure.identity import DefaultAzureCredential, AzureAuthorityHosts

from devtools_testutils import AzureTestCase, is_live
from azure_devtools.scenario_tests import (
    OAuthRequestResponsesFilter,
    RecordingProcessor,
)
from azure_devtools.scenario_tests import RecordingProcessor


REDACTED = "REDACTED"
logger = logging.getLogger()


class OAuthRequestResponsesFilterACR(RecordingProcessor):
    """Remove oauth authentication requests and responses from recording."""

    def process_request(self, request):
        # We want to leave Azure Container Registry challenge auth requests alone
        import re

        if not re.search("/oauth2(?:/v2.0)?/token", request.uri) or "azurecr.io" in request.uri:
            return request
        return None


class ManagementRequestReplacer(RecordingProcessor):
    """Remove oauth authentication requests and responses from recording."""

    # Don't need to save the import image requests

    def process_request(self, request):
        if "management.azure.com" not in request.uri:
            return request
        return None


class AcrBodyReplacer(RecordingProcessor):
    """Replace request body for oauth2 exchanges"""

    def __init__(self):
        self._401_replacement = 'Bearer realm="https://fake_url.azurecr.io/oauth2/token",service="fake_url.azurecr.io",scope="fake_scope",error="invalid_token"'

    def _scrub_body(self, body):
        # type: (bytes) -> bytes
        if isinstance(body, dict):
            return self._scrub_body_dict(body)
        if not isinstance(body, six.binary_type):
            return body
        s = body.decode("utf-8")
        if "access_token" not in s and "refresh_token" not in s:
            return body
        s = s.split("&")
        for idx, pair in enumerate(s):
            [k, v] = pair.split("=")
            if k == "access_token" or k == "refresh_token":
                v = REDACTED
            if k == "service":
                v = "fake_url.azurecr.io"
            s[idx] = "=".join([k, v])
        s = "&".join(s)
        return s.encode("utf-8")

    def _scrub_body_dict(self, body):
        new_body = copy.deepcopy(body)
        for k in ["access_token", "refresh_token"]:
            if k in new_body.keys():
                new_body[k] = REDACTED
        return new_body

    def process_request(self, request):
        if request.body:
            request.body = self._scrub_body(request.body)

        return request

    def process_response(self, response):
        try:
            headers = response["headers"]

            if "www-authenticate" in headers:
                headers["www-authenticate"] = (
                    [self._401_replacement] if isinstance(headers["www-authenticate"], list) else self._401_replacement
                )

            body = response["body"]
            try:
                if body["string"] == b"" or body["string"] == "null":
                    return response

                refresh = json.loads(body["string"])
                if "refresh_token" in refresh.keys():
                    refresh["refresh_token"] = REDACTED
                if "access_token" in refresh.keys():
                    refresh["access_token"] = REDACTED
                body["string"] = json.dumps(refresh)
            except ValueError:
                pass
            except json.decoder.JSONDecodeError:
                pass

            return response
        except (KeyError, ValueError):
            return response


class FakeTokenCredential(object):
    """Protocol for classes able to provide OAuth tokens.
    :param str scopes: Lets you specify the type of access needed.
    """

    def __init__(self):
        self.token = AccessToken("YOU SHALL NOT PASS", 0)

    def get_token(self, *args):
        return self.token


class ContainerRegistryTestClass(AzureTestCase):
    def __init__(self, method_name):
        super(ContainerRegistryTestClass, self).__init__(method_name)
        self.repository = "library/busybox"
        self.recording_processors.append(AcrBodyReplacer())
        self.recording_processors.append(ManagementRequestReplacer())
        for idx, p in enumerate(self.recording_processors):
            if isinstance(p, OAuthRequestResponsesFilter):
                self.recording_processors[idx] = OAuthRequestResponsesFilterACR()

    def sleep(self, t):
        if self.is_live:
            time.sleep(t)

    def import_image(self, endpoint, repository, tags):
        # repository must be a docker hub repository
        # tags is a List of repository/tag combos in the format <repository>:<tag>
        if not self.is_live:
            return
        authority = get_authority(endpoint)
        import_image(authority, repository, tags)

    def get_credential(self, authority=None, **kwargs):
        if self.is_live:
            if authority != AzureAuthorityHosts.AZURE_PUBLIC_CLOUD:
                return ClientSecretCredential(
                    tenant_id=os.environ["CONTAINERREGISTRY_TENANT_ID"],
                    client_id=os.environ["CONTAINERREGISTRY_CLIENT_ID"],
                    client_secret=os.environ["CONTAINERREGISTRY_CLIENT_SECRET"],
                    authority=authority
                )
            return DefaultAzureCredential(**kwargs)
        return FakeTokenCredential()

    def create_registry_client(self, endpoint, **kwargs):
        authority = get_authority(endpoint)
        credential_scopes = kwargs.pop("credential_scopes", None)
        if not credential_scopes:
            credential_scopes = get_authorization_scope(authority)
        credential = self.get_credential(authority=authority)
        logger.warning("Authority: {} \nAuthorization scope: {}".format(authority, credential_scopes))
        return ContainerRegistryClient(endpoint=endpoint, credential=credential, credential_scopes=credential_scopes, **kwargs)

    def create_anon_client(self, endpoint, **kwargs):
        authority = get_authority(endpoint)
        credential_scopes = get_authorization_scope(authority)
        return ContainerRegistryClient(endpoint=endpoint, credential=None, credential_scopes=credential_scopes, **kwargs)

    def set_all_properties(self, properties, value):
        properties.can_delete = value
        properties.can_read = value
        properties.can_write = value
        properties.can_list = value
        return properties

    def assert_all_properties(self, properties, value):
        assert properties.can_delete == value
        assert properties.can_read == value
        assert properties.can_write == value
        assert properties.can_list == value

    def create_fully_qualified_reference(self, registry, repository, digest):
        return "{}/{}{}{}".format(
            registry,
            repository,
            ":" if _is_tag(digest) else "@",
            digest.split(":")[-1]
        )


    def is_public_endpoint(self, endpoint):
        return ".azurecr.io" in endpoint


def get_authority(endpoint):
    if ".azurecr.io" in endpoint:
        logger.warning("Public cloud Authority:")
        return AzureAuthorityHosts.AZURE_PUBLIC_CLOUD
    if ".azurecr.cn" in endpoint:
        logger.warning("China Authority:")
        return AzureAuthorityHosts.AZURE_CHINA
    if ".azurecr.us" in endpoint:
        logger.warning("US Gov Authority:")
        return AzureAuthorityHosts.AZURE_GOVERNMENT
    raise ValueError("Endpoint ({}) could not be understood".format(endpoint))


def get_authorization_scope(authority):
    if authority == AzureAuthorityHosts.AZURE_PUBLIC_CLOUD:
        logger.warning("Public auth scope")
        return "https://management.core.windows.net/.default"
    if authority == AzureAuthorityHosts.AZURE_CHINA:
        logger.warning("China scope")
        return "https://management.chinacloudapi.cn/.default"
    if authority == AzureAuthorityHosts.AZURE_GOVERNMENT:
        logger.warning("US Gov scope")
        return "https://management.usgovcloudapi.net/.default"

def get_base_url(authority):
    if authority == AzureAuthorityHosts.AZURE_PUBLIC_CLOUD:
        logger.warning("Public auth scope")
        return AZURE_PUBLIC_CLOUD
    if authority == AzureAuthorityHosts.AZURE_CHINA:
        logger.warning("China scope")
        return AZURE_CHINA_CLOUD
    if authority == AzureAuthorityHosts.AZURE_GOVERNMENT:
        logger.warning("US Gov scope")
        return AZURE_US_GOV_CLOUD



from azure.identity import ClientSecretCredential
from msrestazure.azure_cloud import AZURE_CHINA_CLOUD, AZURE_US_GOV_CLOUD, AZURE_PUBLIC_CLOUD

# Moving this out of testcase so the fixture and individual tests can use it
def import_image(authority, repository, tags):
    logger.warning("Import image authority: {}".format(authority))
    credential = ClientSecretCredential(
        tenant_id=os.environ["CONTAINERREGISTRY_TENANT_ID"],
        client_id=os.environ["CONTAINERREGISTRY_CLIENT_ID"],
        client_secret=os.environ["CONTAINERREGISTRY_CLIENT_SECRET"],
        authority=authority
    )
    sub_id = os.environ["CONTAINERREGISTRY_SUBSCRIPTION_ID"]
    base_url = get_base_url(authority)
    credential_scopes = [base_url.endpoints.resource_manager + "/.default"]
    mgmt_client = ContainerRegistryManagementClient(
        credential, sub_id, api_version="2019-05-01", base_url=base_url.endpoints.resource_manager, credential_scopes=credential_scopes
    )
    logger.warning("LOGGING: {}{}".format(os.environ["CONTAINERREGISTRY_SUBSCRIPTION_ID"], os.environ["CONTAINERREGISTRY_TENANT_ID"]))
    registry_uri = "registry.hub.docker.com"
    rg_name = os.environ["CONTAINERREGISTRY_RESOURCE_GROUP"]
    registry_name = os.environ["CONTAINERREGISTRY_REGISTRY_NAME"]

    import_source = ImportSource(source_image=repository, registry_uri=registry_uri)

    import_params = ImportImageParameters(mode=ImportMode.Force, source=import_source, target_tags=tags)

    result = mgmt_client.registries.begin_import_image(
        rg_name,
        registry_name,
        parameters=import_params,
    )

    while not result.done():
        pass

    # Do the same for anonymous
    mgmt_client = ContainerRegistryManagementClient(
        credential, sub_id, api_version="2019-05-01", base_url=base_url.endpoints.resource_manager, credential_scopes=credential_scopes
    )
    registry_uri = "registry.hub.docker.com"
    rg_name = os.environ["CONTAINERREGISTRY_RESOURCE_GROUP"]
    registry_name = os.environ["CONTAINERREGISTRY_ANONREGISTRY_NAME"]

    import_source = ImportSource(source_image=repository, registry_uri=registry_uri)

    import_params = ImportImageParameters(mode=ImportMode.Force, source=import_source, target_tags=tags)

    result = mgmt_client.registries.begin_import_image(
        rg_name,
        registry_name,
        parameters=import_params,
    )

    while not result.done():
        pass


@pytest.fixture(scope="session")
def load_registry():
    return
    if not is_live():
        return
    authority = get_authority(os.environ.get("CONTAINERREGISTRY_ENDPOINT"))
    repos = [
        "library/hello-world",
        "library/alpine",
        "library/busybox",
    ]
    tags = [
        [
            "library/hello-world:latest",
            "library/hello-world:v1",
            "library/hello-world:v2",
            "library/hello-world:v3",
            "library/hello-world:v4",
        ],
        ["library/alpine"],
        ["library/busybox"],
    ]
    for repo, tag in zip(repos, tags):
        try:
            import_image(authority, repo, tag)
        except Exception as e:
            print(e)
