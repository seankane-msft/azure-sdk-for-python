from azure.core.pipeline.policies import BearerTokenCredentialPolicy
from azure.core.tracing.decorator import distributed_trace

from datetime import datetime
from msrest import Serializer

from ._version import VERSION
from ._utils import parse_connection_string
from ._authentication import AppConfigRequestsCredentialsPolicy

import six


class AppConfigurationClient(object):
    """A Client for the AppConfiguration Service.

    :param str account_url: The URL for the service.
    :param TokenCredential credential: The credentials to authenticate with the service.
    """

    def __init__(self, account_url, credential, **kwargs):
        # type: (str, TokenCredential) -> None
        try:
            if not account_url.lower().startswith('http'):
                full_url = "https://" + account_url
            else:
                full_url = account_url
        except AttributeError:
            raise ValueError("Base URL must be a string.")

        user_agent_moniker = "appconfiguration/{}".format(VERSION)
        scopes, policy = self._setup_credential(account_url, credential, kwargs)
        self._client = AzureAppConfiguration(
            credential=credential,
            endpoint=full_url,
            credential_scopes=scopes,
            authentication_policy=policy,
            sdk_moniker=user_agent_moniker,
            **kwargs)

    @classmethod
    def from_connection_string(cls, connection_string, **kwargs):
        # type: (str) -> AppConfigurationClient
        """Build an AppConfigurationClient from a connection string.

        :param str connection_string: A connection string, as retrieved
         from the Azure portal.
        """
        account_url, credential, secret = parse_connection_string(connection_string)
        return cls(account_url, credential, secret=secret, **kwargs)

    def _setup_credential(self, account_url, credential, kwargs):
        if not credential:
            raise ValueError("Missing credential")
        policy = None
        if isinstance(credential, six.string_types):
            policy = AppConfigRequestsCredentialsPolicy(
                host=account_url,
                credential=credential,
                secret=kwargs.pop('secret')
            )
        return [account_url.strip("/") + "/.default"], policy

    @distributed_trace
    def get_configuration_setting(self, key, label=None, **kwargs):
        # type: (str, Optional[str]) -> ConfigurationSetting
        """Get the value of a particular configuration settings.

        :param str key: The key name of the setting.
        :param str label: The label of the setting.
        :raises ~azure.core.exceptions.ResourceNotFoundError: If no matching configuration setting exists.
        """
        accept_datetime = kwargs.pop('accept_datetime', None)
        if isinstance(accept_datetime, datetime):
            accept_datetime = Serializer.serialize_rfc(accept_datetime)
        result = self._client.get_key_value(
            key=key,
            label=label,
            accept_datetime=accept_datetime,
            **kwargs)
        return ConfigurationSetting(
            key=result.key,
            label=result.label,
            value=result.value,
            etag=result.etag,
            last_modified=result.last_modified,
            read_only=result.locked,
            content_type=result.content_type,
            tags=result.tags
        )