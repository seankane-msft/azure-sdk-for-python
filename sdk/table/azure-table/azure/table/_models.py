# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from azure.table._deserialization import _convert_to_entity
from azure.table._entity import Entity
from azure.table._shared.response_handlers import return_context_and_deserialized, process_storage_error
from azure.core.exceptions import HttpResponseError
from azure.core.paging import PageIterator
from ._generated.models import AccessPolicy as GenAccessPolicy
from ._generated.models import Logging as GeneratedLogging
from ._generated.models import Metrics as GeneratedMetrics
from ._generated.models import RetentionPolicy as GeneratedRetentionPolicy
from ._generated.models import CorsRule as GeneratedCorsRule
from ._shared.models import Services


class AccessPolicy(GenAccessPolicy):
    """Access Policy class used by the set and get access policy methods.

    A stored access policy can specify the start time, expiry time, and
    permissions for the Shared Access Signatures with which it's associated.
    Depending on how you want to control access to your resource, you can
    specify all of these parameters within the stored access policy, and omit
    them from the URL for the Shared Access Signature. Doing so permits you to
    modify the associated signature's behavior at any time, as well as to revoke
    it. Or you can specify one or more of the access policy parameters within
    the stored access policy, and the others on the URL. Finally, you can
    specify all of the parameters on the URL. In this case, you can use the
    stored access policy to revoke the signature, but not to modify its behavior.

    Together the Shared Access Signature and the stored access policy must
    include all fields required to authenticate the signature. If any required
    fields are missing, the request will fail. Likewise, if a field is specified
    both in the Shared Access Signature URL and in the stored access policy, the
    request will fail with status code 400 (Bad Request).

    :param str permission:
        The permissions associated with the shared access signature. The
        user is restricted to operations allowed by the permissions.
        Required unless an id is given referencing a stored access policy
        which contains this field. This field must be omitted if it has been
        specified in an associated stored access policy.
    :param expiry:
        The time at which the shared access signature becomes invalid.
        Required unless an id is given referencing a stored access policy
        which contains this field. This field must be omitted if it has
        been specified in an associated stored access policy. Azure will always
        convert values to UTC. If a date is passed in without timezone info, it
        is assumed to be UTC.
    :type expiry: ~datetime.datetime or str
    :param start:
        The time at which the shared access signature becomes valid. If
        omitted, start time for this call is assumed to be the time when the
        storage service receives the request. Azure will always convert values
        to UTC. If a date is passed in without timezone info, it is assumed to
        be UTC.
    :type start: ~datetime.datetime or str
    """

    def __init__(self, permission=None, expiry=None, start=None, **kwargs):  # pylint:disable=W0231
        self.start = start
        self.expiry = expiry
        self.permission = permission


class TableAnalyticsLogging(GeneratedLogging):
    """Azure Analytics Logging settings.

    All required parameters must be populated in order to send to Azure.

    :keyword str version: Required. The version of Storage Analytics to configure.
    :keyword bool delete: Required. Indicates whether all delete requests should be logged.
    :keyword bool read: Required. Indicates whether all read requests should be logged.
    :keyword bool write: Required. Indicates whether all write requests should be logged.
    :keyword ~azure.storage.queue.RetentionPolicy retention_policy: Required.
        The retention policy for the metrics.
    """

    def __init__(self, **kwargs):  # pylint:disable=W0231
        self.version = kwargs.get('version', u'1.0')
        self.delete = kwargs.get('delete', False)
        self.read = kwargs.get('read', False)
        self.write = kwargs.get('write', False)
        self.retention_policy = kwargs.get('retention_policy') or RetentionPolicy()

    @classmethod
    def _from_generated(cls, generated):
        if not generated:
            return cls()
        return cls(
            version=generated.version,
            delete=generated.delete,
            read=generated.read,
            write=generated.write,
            retention_policy=RetentionPolicy.from_generated(generated.retention_policy) # pylint:disable=W0212
            # pylint: disable=protected-access
        )


class Metrics(GeneratedMetrics):
    """A summary of request statistics grouped by API in hour or minute aggregates.

    All required parameters must be populated in order to send to Azure.

    :keyword str version: The version of Storage Analytics to configure.
    :keyword bool enabled: Required. Indicates whether metrics are enabled for the service.
    :keyword bool include_ap_is: Indicates whether metrics should generate summary
        statistics for called API operations.
    :keyword ~azure.storage.queue.RetentionPolicy retention_policy: Required.
        The retention policy for the metrics.
    """

    def __init__(self, **kwargs):  # pylint:disable=W0231
        self.version = kwargs.get('version', u'1.0')
        self.enabled = kwargs.get('enabled', False)
        self.include_apis = kwargs.get('include_apis')
        self.retention_policy = kwargs.get('retention_policy') or RetentionPolicy()

    @classmethod
    def _from_generated(cls, generated):
        if not generated:
            return cls()
        return cls(
            version=generated.version,
            enabled=generated.enabled,
            include_apis=generated.include_apis,
            retention_policy=RetentionPolicy.from_generated(generated.retention_policy)
            # pylint: disable=protected-access
        )


class RetentionPolicy(GeneratedRetentionPolicy):
    """The retention policy which determines how long the associated data should
    persist.

    All required parameters must be populated in order to send to Azure.

    :param bool enabled: Required. Indicates whether a retention policy is enabled
        for the storage service.
    :param int days: Indicates the number of days that metrics or logging or
        soft-deleted data should be retained. All data older than this value will
        be deleted.
    """

    def __init__(self, enabled=False, days=None, **kwargs):  # pylint:disable=W0231
        self.enabled = enabled
        self.days = days
        if self.enabled and (self.days is None):
            raise ValueError("If policy is enabled, 'days' must be specified.")

    @classmethod
    def from_generated(cls, generated):
        if not generated:
            return cls()
        return cls(
            enabled=generated.enabled,
            days=generated.days,
        )


class CorsRule(GeneratedCorsRule):
    """CORS is an HTTP feature that enables a web application running under one
    domain to access resources in another domain. Web browsers implement a
    security restriction known as same-origin policy that prevents a web page
    from calling APIs in a different domain; CORS provides a secure way to
    allow one domain (the origin domain) to call APIs in another domain.

    All required parameters must be populated in order to send to Azure.

    :param list(str) allowed_origins:
        A list of origin domains that will be allowed via CORS, or "*" to allow
        all domains. The list of must contain at least one entry. Limited to 64
        origin domains. Each allowed origin can have up to 256 characters.
    :param list(str) allowed_methods:
        A list of HTTP methods that are allowed to be executed by the origin.
        The list of must contain at least one entry. For Azure Storage,
        permitted methods are DELETE, GET, HEAD, MERGE, POST, OPTIONS or PUT.
    :keyword int max_age_in_seconds:
        The number of seconds that the client/browser should cache a
        pre-flight response.
    :keyword list(str) exposed_headers:
        Defaults to an empty list. A list of response headers to expose to CORS
        clients. Limited to 64 defined headers and two prefixed headers. Each
        header can be up to 256 characters.
    :keyword list(str) allowed_headers:
        Defaults to an empty list. A list of headers allowed to be part of
        the cross-origin request. Limited to 64 defined headers and 2 prefixed
        headers. Each header can be up to 256 characters.
    """

    def __init__(self, allowed_origins, allowed_methods, **kwargs):  # pylint:disable=W0231
        self.allowed_origins = ','.join(allowed_origins)
        self.allowed_methods = ','.join(allowed_methods)
        self.allowed_headers = ','.join(kwargs.get('allowed_headers', []))
        self.exposed_headers = ','.join(kwargs.get('exposed_headers', []))
        self.max_age_in_seconds = kwargs.get('max_age_in_seconds', 0)

    @classmethod
    def _from_generated(cls, generated):
        return cls(
            [generated.allowed_origins],
            [generated.allowed_methods],
            allowed_headers=[generated.allowed_headers],
            exposed_headers=[generated.exposed_headers],
            max_age_in_seconds=generated.max_age_in_seconds,
        )


class TablePropertiesPaged(PageIterator):
    """An iterable of Table properties.

    :ivar str service_endpoint: The service URL.
    :ivar str prefix: A queue name prefix being used to filter the list.
    :ivar str marker: The continuation token of the current page of results.
    :ivar int results_per_page: The maximum number of results retrieved per API call.
    :ivar str next_marker: The continuation token to retrieve the next page of results.
    :ivar str location_mode: The location mode being used to list results. The available
        options include "primary" and "secondary".
    :param callable command: Function to retrieve the next page of items.
    :param str prefix: Filters the results to return only queues whose names
        begin with the specified prefix.
    :param int results_per_page: The maximum number of queue names to retrieve per
        call.
    :param str continuation_token: An opaque continuation token.
    """

    def __init__(self, command, prefix=None, results_per_page=None, continuation_token=None):
        super(TablePropertiesPaged, self).__init__(
            self._get_next_cb,
            self._extract_data_cb,
            continuation_token=continuation_token or ""
        )
        self._command = command
        self.prefix = prefix
        self.service_endpoint = None
        self.next_table_name = None
        self._headers = None
        self.results_per_page = results_per_page
        self.location_mode = None

    def _get_next_cb(self, continuation_token):
        try:
            return self._command(
                next_table_name=continuation_token or None,
                query_options=self.results_per_page or None,
                cls=return_context_and_deserialized,
                use_location=self.location_mode
            )
        except HttpResponseError as error:
            process_storage_error(error)

    def _extract_data_cb(self, get_next_return):
        self.location_mode, self._response, self._headers = get_next_return
        props_list = [t for t in self._response.value]
        # props_list = [TableProperties._from_generated(q) for q in self._response.value] # pylint: disable=protected-access
        # return self._response.next_marker or None, props_list
        return self._headers['x-ms-continuation-NextTableName'] or None, props_list


class TableEntityPropertiesPaged(PageIterator):
    """An iterable of TableEntity properties.

    :ivar str service_endpoint: The service URL.
    :ivar str prefix: A queue name prefix being used to filter the list.
    :ivar str marker: The continuation token of the current page of results.
    :ivar int results_per_page: The maximum number of results retrieved per API call.
    :ivar str next_marker: The continuation token to retrieve the next page of results.
    :ivar str location_mode: The location mode being used to list results. The available
        options include "primary" and "secondary".
    :param callable command: Function to retrieve the next page of items.
    :param str prefix: Filters the results to return only queues whose names
        begin with the specified prefix.
    :param int results_per_page: The maximum number of queue names to retrieve per
        call.
    :param str continuation_token: An opaque continuation token.
    """

    def __init__(self, command, results_per_page=None, table=None,
                 continuation_token=None):
        super(TableEntityPropertiesPaged, self).__init__(
            self._get_next_cb,
            self._extract_data_cb,
            continuation_token=continuation_token or ""
        )
        self._command = command
        self._headers = None
        self.results_per_page = results_per_page
        self.table = table
        self.location_mode = None

    def _get_next_cb(self, continuation_token):
        row_key = None
        partition_key = None
        if continuation_token:
            tokens = continuation_token.split(" ")
            row_key = tokens[1]
            partition_key = tokens[0]
        try:
            return self._command(
                query_options=self.results_per_page or None,
                next_row_key=row_key or None,
                next_partition_key=partition_key or None,
                table=self.table,
                cls=return_context_and_deserialized,
                use_location=self.location_mode
            )
        except HttpResponseError as error:
            process_storage_error(error)

    def _extract_data_cb(self, get_next_return):
        self.location_mode, self._response, self._headers = get_next_return
        props_list = [Entity(_convert_to_entity(t)) for t in self._response.value]
        pk = self._headers['x-ms-continuation-NextPartitionKey']
        rk = self._headers['x-ms-continuation-NextRowKey']
        next_entity = ''
        if pk and rk:
            next_entity = pk + " " + rk
        elif pk:
            next_entity = pk
        elif rk:
            next_entity = " " + rk
        return next_entity or None, props_list


class TableSasPermissions(object):

    def __init__(self, query=False, add=False, update=False, delete=False, _str=None):
        """
        :param bool query:
            Get entities and query entities.
        :param bool add:
            Add entities. Add and Update permissions are required for upsert operations.
        :param bool update:
            Update entities. Add and Update permissions are required for upsert operations.
        :param bool delete:
            Delete entities.
        :param str _str:
            A string representing the permissions.
        """
        if not _str:
            _str = ''
        self.query = query or ('r' in _str)
        self.add = add or ('a' in _str)
        self.update = update or ('u' in _str)
        self.delete = delete or ('d' in _str)

    def __or__(self, other):
        return TableSasPermissions(_str=str(self) + str(other))

    def __add__(self, other):
        return TableSasPermissions(_str=str(self) + str(other))

    def __str__(self):
        return (('r' if self.query else '') +
                ('a' if self.add else '') +
                ('u' if self.update else '') +
                ('d' if self.delete else ''))


TableSasPermissions.QUERY = TableSasPermissions(query=True)
TableSasPermissions.ADD = TableSasPermissions(add=True)
TableSasPermissions.UPDATE = TableSasPermissions(update=True)
TableSasPermissions.DELETE = TableSasPermissions(delete=True)


def service_stats_deserialize(generated):
    """Deserialize a ServiceStats objects into a dict.
    """
    return {
        'geo_replication': {
            'status': generated.geo_replication.status,
            'last_sync_time': generated.geo_replication.last_sync_time,
        }
    }


def service_properties_deserialize(generated):
    """Deserialize a ServiceProperties objects into a dict.
    """
    return {
        'analytics_logging': TableAnalyticsLogging._from_generated(generated.logging),
        # pylint: disable=protected-access
        'hour_metrics': Metrics._from_generated(generated.hour_metrics),  # pylint: disable=protected-access
        'minute_metrics': Metrics._from_generated(generated.minute_metrics),  # pylint: disable=protected-access
        'cors': [CorsRule._from_generated(cors) for cors in generated.cors],  # pylint: disable=protected-access
    }


class TableServices():
    def __init__(self):
        """
        :param bool table:
            Access to the `.TableService`
        :param str _str:
            A string representing the services.
        """
        super().__init__()
        self.table = True

    def __str__(self):
        return 't'


class TablePayloadFormat(object):
    '''
    Specifies the accepted content type of the response payload. More information
    can be found here: https://msdn.microsoft.com/en-us/library/azure/dn535600.aspx
    '''

    JSON_NO_METADATA = 'application/json;odata=nometadata'
    '''Returns no type information for the entity properties.'''

    JSON_MINIMAL_METADATA = 'application/json;odata=minimalmetadata'
    '''Returns minimal type information for the entity properties.'''

    JSON_FULL_METADATA = 'application/json;odata=fullmetadata'
    '''Returns minimal type information for the entity properties plus some extra odata properties.'''
