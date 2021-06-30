# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import logging
import os

from azure.containerregistry.aio import (
    ContainerRegistryClient,
)

from azure.core.credentials import AccessToken
from azure.identity.aio import DefaultAzureCredential, ClientSecretCredential
from azure.identity import AzureAuthorityHosts

from testcase import ContainerRegistryTestClass, get_authorization_scope, get_authority

logger = logging.getLogger()

class AsyncFakeTokenCredential(object):
    """Protocol for classes able to provide OAuth tokens.
    :param str scopes: Lets you specify the type of access needed.
    """

    def __init__(self):
        self.token = AccessToken("YOU SHALL NOT PASS", 0)

    async def get_token(self, *args):
        return self.token


class AsyncContainerRegistryTestClass(ContainerRegistryTestClass):
    def __init__(self, method_name):
        super(AsyncContainerRegistryTestClass, self).__init__(method_name)

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
        return AsyncFakeTokenCredential()

    def create_registry_client(self, endpoint, **kwargs):
        authority = get_authority(endpoint)
        credential_scopes = kwargs.pop("credential_scopes", None)
        if not credential_scopes:
            credential_scopes = get_authorization_scope(authority)
        credential = self.get_credential(authority=authority)
        return ContainerRegistryClient(endpoint=endpoint, credential=credential, credential_scopes=credential_scopes, **kwargs)

    def create_anon_client(self, endpoint, **kwargs):
        authority = get_authority(endpoint)
        credential_scopes = get_authorization_scope(authority)
        return ContainerRegistryClient(endpoint=endpoint, credential=None, credential_scopes=credential_scopes, **kwargs)
