# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import functools
from typing import Any, Union
from azure.core.exceptions import HttpResponseError, ResourceExistsError
from azure.core.paging import ItemPaged
from azure.core.tracing.decorator import distributed_trace
from azure.core.pipeline import Pipeline
from ._models import TableItem

from ._generated import AzureTable
from ._generated.models import TableProperties, TableServiceProperties, QueryOptions
from ._models import TablePropertiesPaged, service_stats_deserialize, service_properties_deserialize
from ._base_client import parse_connection_str, TransportWrapper
from ._models import LocationMode
from ._error import _process_table_error
from ._table_client import TableClient
from ._table_service_client_base import TableServiceClientBase


class TableServiceClient(TableServiceClientBase):
    """ :ivar str account_name: Name of the storage account (Cosmos or Azure)"""
    def __init__(
            self, account_url,  # type: str
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
            key.
        :type credential: Union[str,~azure.core.credentials.TokenCredential]
        :returns: None

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_authentication.py
                :start-after: [START auth_from_sas]
                :end-before: [END auth_from_sas]
                :language: python
                :dedent: 8
                :caption: Authenticating a TableServiceClient from a Shared Access Key

            .. literalinclude:: ../samples/sample_authentication.py
                :start-after: [START auth_from_shared_key]
                :end-before: [END auth_from_shared_key]
                :language: python
                :dedent: 8
                :caption: Authenticating a TableServiceClient from a Shared Account Key
        """

        super(TableServiceClient, self).__init__(account_url, service='table', credential=credential, **kwargs)
        self._client = AzureTable(self.url, pipeline=self._pipeline)

    @classmethod
    def from_connection_string(
            cls, conn_str,  # type: str
            **kwargs  # type: Any
    ):  # type: (...) -> TableServiceClient
        """Create TableServiceClient from a connection string.

        :param conn_str:
            A connection string to an Azure Storage or Cosmos account.
        :type conn_str: str
        :returns: A Table service client.
        :rtype: ~azure.data.tables.TableServiceClient

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_authentication.py
                :start-after: [START auth_from_connection_string]
                :end-before: [END auth_from_connection_string]
                :language: python
                :dedent: 8
                :caption: Authenticating a TableServiceClient from a connection_string
        """
        account_url, credential = parse_connection_str(
            conn_str=conn_str, credential=None, service='table', keyword_args=kwargs)
        return cls(account_url, credential=credential, **kwargs)

    @distributed_trace
    def get_service_stats(self, **kwargs):
        # type: (...) -> dict[str,object]
        """Retrieves statistics related to replication for the Table service. It is only available on the secondary
        location endpoint when read-access geo-redundant replication is enabled for the account.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Dictionary of service stats
        :rtype: ~azure.data.tables.models.TableServiceStats
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        try:
            timeout = kwargs.pop('timeout', None)
            stats = self._client.service.get_statistics(  # type: ignore
                timeout=timeout, use_location=LocationMode.SECONDARY, **kwargs)
            return service_stats_deserialize(stats)
        except HttpResponseError as error:
            _process_table_error(error)

    @distributed_trace
    def get_service_properties(self, **kwargs):
        # type: (...) -> dict[str,Any]
        """Gets the properties of an account's Table service,
        including properties for Analytics and CORS (Cross-Origin Resource Sharing) rules.

        :return: Dictionary of service properties
        :rtype:dict[str, Any]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        timeout = kwargs.pop('timeout', None)
        try:
            service_props = self._client.service.get_properties(timeout=timeout, **kwargs)  # type: ignore
            return service_properties_deserialize(service_props)
        except HttpResponseError as error:
            _process_table_error(error)

    @distributed_trace
    def set_service_properties(
            self,
            analytics_logging=None,  # type: Optional[TableAnalyticsLogging]
            hour_metrics=None,  # type: Optional[Metrics]
            minute_metrics=None,  # type: Optional[Metrics]
            cors=None,  # type: Optional[CorsRule]
            **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Sets properties for an account's Table service endpoint,
        including properties for Analytics and CORS (Cross-Origin Resource Sharing) rules.

       :param analytics_logging: Properties for analytics
       :type analytics_logging: ~azure.data.tables.TableAnalyticsLogging
       :param hour_metrics: Hour level metrics
       :type hour_metrics: ~azure.data.tables.Metrics
       :param minute_metrics: Minute level metrics
       :type minute_metrics: ~azure.data.tables.Metrics
       :param cors: Cross-origin resource sharing rules
       :type cors: ~azure.data.tables.CorsRule
       :return: None
       :rtype: None
       :raises ~azure.core.exceptions.HttpResponseError:
       """
        props = TableServiceProperties(
            logging=analytics_logging,
            hour_metrics=hour_metrics,
            minute_metrics=minute_metrics,
            cors=cors
        )
        try:
            return self._client.service.set_properties(props, **kwargs)  # type: ignore
        except HttpResponseError as error:
            _process_table_error(error)

    @distributed_trace
    def create_table(
            self,
            table_name,  # type: str
            **kwargs  # type: Any
    ):
        # type: (...) -> TableClient
        """Creates a new table under the current account.

        :param table_name: The Table name.
        :type table_name: str
        :return: TableClient
        :rtype: ~azure.data.tables.TableClient
        :raises ~azure.core.exceptions.ResourceExistsError:

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_create_delete_table.py
                :start-after: [START create_table_from_tc]
                :end-before: [END create_table_from_tc]
                :language: python
                :dedent: 8
                :caption: Creating a table from the TableServiceClient object
        """
        table = self.get_table_client(table_name=table_name)
        table.create_table(**kwargs)
        return table

    @distributed_trace
    def create_table_if_not_exists(
        self,
        table_name, # type: str
        **kwargs # type: Any
    ):
        # type: (...) -> TableClient
        """Creates a new table if it does not currently exist.
        If the table currently exists, the current table is
        returned.

        :param table_name: The Table name.
        :type table_name: str
        :return: TableClient
        :rtype: ~azure.data.tables.TableClient
        :raises ~azure.core.exceptions.HttpResponseError:

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_create_delete_table.py
                :start-after: [START create_table_if_not_exists]
                :end-before: [END create_table_if_not_exists]
                :language: python
                :dedent: 8
                :caption: Deleting a table from the TableServiceClient object
        """
        table = self.get_table_client(table_name=table_name)
        try:
            table.create_table(**kwargs)
        except ResourceExistsError:
            pass
        return table

    @distributed_trace
    def delete_table(
            self,
            table_name,  # type: str
            **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes the table under the current account

        :param table_name: The Table name.
        :type table_name: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.ResourceNotFoundError:

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_create_delete_table.py
                :start-after: [START delete_table_from_tc]
                :end-before: [END delete_table_from_tc]
                :language: python
                :dedent: 8
                :caption: Deleting a table from the TableServiceClient object
        """
        table = self.get_table_client(table_name=table_name)
        table.delete_table(**kwargs)

    @distributed_trace
    def query_tables(
            self,
            filter,  # pylint: disable=W0622
            **kwargs  # type: Any
    ):
        # type: (...) -> ItemPaged[TableItem]
        """Queries tables under the given account.

        :param filter: Specify a filter to return certain tables.
        :type filter: str
        :keyword int results_per_page: Number of tables per page in return ItemPaged
        :keyword Union[str,list(str)] select: Specify desired properties of a table to return certain tables
        :keyword dict[str,str] parameters: Dictionary for formatting query with additional, user defined parameters
        :return: An ItemPaged of tables
        :rtype: ItemPaged[TableItem]
        :raises ~azure.core.exceptions.HttpResponseError:

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_query_tables.py
                :start-after: [START tsc_query_tables]
                :end-before: [END tsc_query_tables]
                :language: python
                :dedent: 8
                :caption: Querying tables in a storage account
        """
        parameters = kwargs.pop('parameters', None)
        filter = self._parameter_filter_substitution(parameters, filter)  # pylint: disable=W0622

        user_select = kwargs.pop('select', None)
        if user_select and not isinstance(user_select, str):
            user_select = ", ".join(user_select)

        query_options = QueryOptions(top=kwargs.pop('results_per_page', None), select=user_select,
                                     filter=filter)
        command = functools.partial(self._client.table.query, query_options=query_options,
                                    **kwargs)
        return ItemPaged(
            command,
            page_iterator_class=TablePropertiesPaged
        )

    @distributed_trace
    def list_tables(
            self,
            **kwargs  # type: Any
    ):
        # type: (...) -> ItemPaged[TableItem]
        """Queries tables under the given account.

        :keyword int results_per_page: Number of tables per page in return ItemPaged
        :keyword Union[str,list(str)] select: Specify desired properties of a table to return certain tables
        :return: A query of tables
        :rtype: ItemPaged[TableItem]
        :raises ~azure.core.exceptions.HttpResponseError:

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_query_tables.py
                :start-after: [START tsc_list_tables]
                :end-before: [END tsc_list_tables]
                :language: python
                :dedent: 8
                :caption: Listing all tables in a storage account
        """
        user_select = kwargs.pop('select', None)
        if user_select and not isinstance(user_select, str):
            user_select = ", ".join(user_select)

        query_options = QueryOptions(top=kwargs.pop('results_per_page', None), select=user_select)

        command = functools.partial(
            self._client.table.query,
            query_options=query_options,
            **kwargs)
        return ItemPaged(
            command,
            page_iterator_class=TablePropertiesPaged
        )

    def get_table_client(self, table_name, **kwargs):
        # type: (Union[TableProperties, str], Optional[Any]) -> TableClient
        """Get a client to interact with the specified table.

       The table need not already exist.

       :param table_name:
           The table name
       :type table_name: str
       :returns: A :class:`~azure.data.tables.TableClient` object.
       :rtype: ~azure.data.tables.TableClient

       """

        _pipeline = Pipeline(
            transport=TransportWrapper(self._pipeline._transport),  # pylint: disable = protected-access
            policies=self._pipeline._impl_policies  # pylint: disable = protected-access
        )

        return TableClient(
            self.url, table_name=table_name, credential=self.credential,
            key_resolver_function=self.key_resolver_function, require_encryption=self.require_encryption,
            key_encryption_key=self.key_encryption_key, api_version=self.api_version, _pipeline=_pipeline,
            _configuration=self._config, _location_mode=self._location_mode, _hosts=self._hosts, **kwargs)
