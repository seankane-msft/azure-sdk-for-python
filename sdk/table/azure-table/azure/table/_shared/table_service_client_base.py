# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from .._shared.response_handlers import return_headers_and_deserialized
from .base_client import StorageAccountHostsMixin

class TableServiceClientBase(StorageAccountHostsMixin):
    """ :ivar str account_name: Name of the storage account (Cosmos or Azure)"""
    def __init__(
            self, 
            parsed_url,  # type: Any
            # account_url,  # type: str
            service, # type: str
            credential=None,  # type: Union[str,TokenCredential]
            **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Create TableServiceClient from a Credential.

        :param account_url:
            A url to an Azure Storage account.
        :type account_url: str
        :param credential:
            The credentials with which to authenticate. This is optional if the
            account URL already has a SAS token, or the connection string already has shared
            access key values. The value can be a SAS token string, an account shared access
            key, or an instance of a TokenCredentials class from azure.identity.
        :type credential: Union[str,TokenCredential]
        :returns: None
        """

        # try:
        #     if not account_url.lower().startswith('http'):
        #         account_url = "https://" + account_url
        # except AttributeError:
        #     raise ValueError("Account URL must be a string.")
        # parsed_url = urlparse(account_url.rstrip('/'))
        # if not parsed_url.netloc:
        #     raise ValueError("Invalid URL: {}".format(account_url))

        # _, sas_token = parse_query(parsed_url.query)
        # if not sas_token and not credential:
        #     raise ValueError("You need to provide either a SAS token or an account shared key to authenticate.")
        # self._query_str, credential = self._format_query_string(sas_token, credential)
        super(TableServiceClientBase, self).__init__(parsed_url, service='table', credential=credential, **kwargs)
        # self._client = AzureTable(self.url, pipeline=self._pipeline)
        # self._client._config.version = kwargs.get('api_version', VERSION)  # pylint: disable=protected-access