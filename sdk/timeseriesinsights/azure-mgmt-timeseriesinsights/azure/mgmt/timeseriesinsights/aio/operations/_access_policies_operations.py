# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class AccessPoliciesOperations:
    """AccessPoliciesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.timeseriesinsights.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def create_or_update(
        self,
        resource_group_name: str,
        environment_name: str,
        access_policy_name: str,
        parameters: "_models.AccessPolicyCreateOrUpdateParameters",
        **kwargs
    ) -> "_models.AccessPolicyResource":
        """Create or update an access policy in the specified environment.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param environment_name: The name of the Time Series Insights environment associated with the
         specified resource group.
        :type environment_name: str
        :param access_policy_name: Name of the access policy.
        :type access_policy_name: str
        :param parameters: Parameters for creating an access policy.
        :type parameters: ~azure.mgmt.timeseriesinsights.models.AccessPolicyCreateOrUpdateParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessPolicyResource, or the result of cls(response)
        :rtype: ~azure.mgmt.timeseriesinsights.models.AccessPolicyResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AccessPolicyResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-05-15"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'environmentName': self._serialize.url("environment_name", environment_name, 'str'),
            'accessPolicyName': self._serialize.url("access_policy_name", access_policy_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
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
        body_content = self._serialize.body(parameters, 'AccessPolicyCreateOrUpdateParameters')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('AccessPolicyResource', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('AccessPolicyResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/accessPolicies/{accessPolicyName}'}  # type: ignore

    async def get(
        self,
        resource_group_name: str,
        environment_name: str,
        access_policy_name: str,
        **kwargs
    ) -> "_models.AccessPolicyResource":
        """Gets the access policy with the specified name in the specified environment.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param environment_name: The name of the Time Series Insights environment associated with the
         specified resource group.
        :type environment_name: str
        :param access_policy_name: The name of the Time Series Insights access policy associated with
         the specified environment.
        :type access_policy_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessPolicyResource, or the result of cls(response)
        :rtype: ~azure.mgmt.timeseriesinsights.models.AccessPolicyResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AccessPolicyResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-05-15"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'environmentName': self._serialize.url("environment_name", environment_name, 'str'),
            'accessPolicyName': self._serialize.url("access_policy_name", access_policy_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AccessPolicyResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/accessPolicies/{accessPolicyName}'}  # type: ignore

    async def update(
        self,
        resource_group_name: str,
        environment_name: str,
        access_policy_name: str,
        description: Optional[str] = None,
        roles: Optional[List[Union[str, "_models.AccessPolicyRole"]]] = None,
        **kwargs
    ) -> "_models.AccessPolicyResource":
        """Updates the access policy with the specified name in the specified subscription, resource
        group, and environment.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param environment_name: The name of the Time Series Insights environment associated with the
         specified resource group.
        :type environment_name: str
        :param access_policy_name: The name of the Time Series Insights access policy associated with
         the specified environment.
        :type access_policy_name: str
        :param description: An description of the access policy.
        :type description: str
        :param roles: The list of roles the principal is assigned on the environment.
        :type roles: list[str or ~azure.mgmt.timeseriesinsights.models.AccessPolicyRole]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessPolicyResource, or the result of cls(response)
        :rtype: ~azure.mgmt.timeseriesinsights.models.AccessPolicyResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AccessPolicyResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        _access_policy_update_parameters = _models.AccessPolicyUpdateParameters(description=description, roles=roles)
        api_version = "2020-05-15"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'environmentName': self._serialize.url("environment_name", environment_name, 'str'),
            'accessPolicyName': self._serialize.url("access_policy_name", access_policy_name, 'str'),
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
        body_content = self._serialize.body(_access_policy_update_parameters, 'AccessPolicyUpdateParameters')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AccessPolicyResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/accessPolicies/{accessPolicyName}'}  # type: ignore

    async def delete(
        self,
        resource_group_name: str,
        environment_name: str,
        access_policy_name: str,
        **kwargs
    ) -> None:
        """Deletes the access policy with the specified name in the specified subscription, resource
        group, and environment.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param environment_name: The name of the Time Series Insights environment associated with the
         specified resource group.
        :type environment_name: str
        :param access_policy_name: The name of the Time Series Insights access policy associated with
         the specified environment.
        :type access_policy_name: str
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
        api_version = "2020-05-15"
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'environmentName': self._serialize.url("environment_name", environment_name, 'str'),
            'accessPolicyName': self._serialize.url("access_policy_name", access_policy_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/accessPolicies/{accessPolicyName}'}  # type: ignore

    async def list_by_environment(
        self,
        resource_group_name: str,
        environment_name: str,
        **kwargs
    ) -> "_models.AccessPolicyListResponse":
        """Lists all the available access policies associated with the environment.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param environment_name: The name of the Time Series Insights environment associated with the
         specified resource group.
        :type environment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessPolicyListResponse, or the result of cls(response)
        :rtype: ~azure.mgmt.timeseriesinsights.models.AccessPolicyListResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AccessPolicyListResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-05-15"
        accept = "application/json"

        # Construct URL
        url = self.list_by_environment.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'environmentName': self._serialize.url("environment_name", environment_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AccessPolicyListResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    list_by_environment.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/accessPolicies'}  # type: ignore
