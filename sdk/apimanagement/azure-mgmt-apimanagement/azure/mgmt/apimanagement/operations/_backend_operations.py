# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class BackendOperations(object):
    """BackendOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.apimanagement.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_by_service(
        self,
        resource_group_name,  # type: str
        service_name,  # type: str
        filter=None,  # type: Optional[str]
        top=None,  # type: Optional[int]
        skip=None,  # type: Optional[int]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.BackendCollection"]
        """Lists a collection of backends in the specified service instance.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param filter: |     Field     |     Usage     |     Supported operators     |     Supported
         functions     |</br>|-------------|-------------|-------------|-------------|</br>| name |
         filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith |</br>| title |
         filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith |</br>| url |
         filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith |</br>.
        :type filter: str
        :param top: Number of records to return.
        :type top: int
        :param skip: Number of records to skip.
        :type skip: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either BackendCollection or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.apimanagement.models.BackendCollection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.BackendCollection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-06-01-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_by_service.metadata['url']  # type: ignore
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'serviceName': self._serialize.url("service_name", service_name, 'str', max_length=50, min_length=1, pattern=r'^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$'),
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int', minimum=1)
                if skip is not None:
                    query_parameters['$skip'] = self._serialize.query("skip", skip, 'int', minimum=0)
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('BackendCollection', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(_models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_service.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/backends'}  # type: ignore

    def get_entity_tag(
        self,
        resource_group_name,  # type: str
        service_name,  # type: str
        backend_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> bool
        """Gets the entity state (Etag) version of the backend specified by its identifier.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param backend_id: Identifier of the Backend entity. Must be unique in the current API
         Management service instance.
        :type backend_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bool, or the result of cls(response)
        :rtype: bool
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-06-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.get_entity_tag.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str', max_length=50, min_length=1, pattern=r'^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$'),
            'backendId': self._serialize.url("backend_id", backend_id, 'str', max_length=80, min_length=1),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers['ETag']=self._deserialize('str', response.headers.get('ETag'))

        if cls:
            return cls(pipeline_response, None, response_headers)

        return 200 <= response.status_code <= 299
    get_entity_tag.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/backends/{backendId}'}  # type: ignore

    def get(
        self,
        resource_group_name,  # type: str
        service_name,  # type: str
        backend_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.BackendContract"
        """Gets the details of the backend specified by its identifier.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param backend_id: Identifier of the Backend entity. Must be unique in the current API
         Management service instance.
        :type backend_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BackendContract, or the result of cls(response)
        :rtype: ~azure.mgmt.apimanagement.models.BackendContract
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.BackendContract"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-06-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str', max_length=50, min_length=1, pattern=r'^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$'),
            'backendId': self._serialize.url("backend_id", backend_id, 'str', max_length=80, min_length=1),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers['ETag']=self._deserialize('str', response.headers.get('ETag'))
        deserialized = self._deserialize('BackendContract', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/backends/{backendId}'}  # type: ignore

    def create_or_update(
        self,
        resource_group_name,  # type: str
        service_name,  # type: str
        backend_id,  # type: str
        parameters,  # type: "_models.BackendContract"
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.BackendContract"
        """Creates or Updates a backend.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param backend_id: Identifier of the Backend entity. Must be unique in the current API
         Management service instance.
        :type backend_id: str
        :param parameters: Create parameters.
        :type parameters: ~azure.mgmt.apimanagement.models.BackendContract
        :param if_match: ETag of the Entity. Not required when creating an entity, but required when
         updating an entity.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BackendContract, or the result of cls(response)
        :rtype: ~azure.mgmt.apimanagement.models.BackendContract
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.BackendContract"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-06-01-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str', max_length=50, min_length=1, pattern=r'^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$'),
            'backendId': self._serialize.url("backend_id", backend_id, 'str', max_length=80, min_length=1),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'BackendContract')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            response_headers['ETag']=self._deserialize('str', response.headers.get('ETag'))
            deserialized = self._deserialize('BackendContract', pipeline_response)

        if response.status_code == 201:
            response_headers['ETag']=self._deserialize('str', response.headers.get('ETag'))
            deserialized = self._deserialize('BackendContract', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/backends/{backendId}'}  # type: ignore

    def update(
        self,
        resource_group_name,  # type: str
        service_name,  # type: str
        backend_id,  # type: str
        if_match,  # type: str
        parameters,  # type: "_models.BackendUpdateParameters"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.BackendContract"
        """Updates an existing backend.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param backend_id: Identifier of the Backend entity. Must be unique in the current API
         Management service instance.
        :type backend_id: str
        :param if_match: ETag of the Entity. ETag should match the current entity state from the header
         response of the GET request or it should be * for unconditional update.
        :type if_match: str
        :param parameters: Update parameters.
        :type parameters: ~azure.mgmt.apimanagement.models.BackendUpdateParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BackendContract, or the result of cls(response)
        :rtype: ~azure.mgmt.apimanagement.models.BackendContract
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.BackendContract"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-06-01-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str', max_length=50, min_length=1, pattern=r'^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$'),
            'backendId': self._serialize.url("backend_id", backend_id, 'str', max_length=80, min_length=1),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'BackendUpdateParameters')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers['ETag']=self._deserialize('str', response.headers.get('ETag'))
        deserialized = self._deserialize('BackendContract', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/backends/{backendId}'}  # type: ignore

    def delete(
        self,
        resource_group_name,  # type: str
        service_name,  # type: str
        backend_id,  # type: str
        if_match,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes the specified backend.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param backend_id: Identifier of the Backend entity. Must be unique in the current API
         Management service instance.
        :type backend_id: str
        :param if_match: ETag of the Entity. ETag should match the current entity state from the header
         response of the GET request or it should be * for unconditional update.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-06-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str', max_length=50, min_length=1, pattern=r'^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$'),
            'backendId': self._serialize.url("backend_id", backend_id, 'str', max_length=80, min_length=1),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/backends/{backendId}'}  # type: ignore

    def reconnect(
        self,
        resource_group_name,  # type: str
        service_name,  # type: str
        backend_id,  # type: str
        parameters=None,  # type: Optional["_models.BackendReconnectContract"]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Notifies the APIM proxy to create a new connection to the backend after the specified timeout.
        If no timeout was specified, timeout of 2 minutes is used.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param backend_id: Identifier of the Backend entity. Must be unique in the current API
         Management service instance.
        :type backend_id: str
        :param parameters: Reconnect request parameters.
        :type parameters: ~azure.mgmt.apimanagement.models.BackendReconnectContract
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-06-01-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.reconnect.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str', max_length=50, min_length=1, pattern=r'^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$'),
            'backendId': self._serialize.url("backend_id", backend_id, 'str', max_length=80, min_length=1),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        if parameters is not None:
            body_content = self._serialize.body(parameters, 'BackendReconnectContract')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    reconnect.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/backends/{backendId}/reconnect'}  # type: ignore
