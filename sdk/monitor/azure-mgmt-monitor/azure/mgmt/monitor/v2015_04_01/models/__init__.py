# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AutoscaleNotification
    from ._models_py3 import AutoscaleProfile
    from ._models_py3 import AutoscaleSettingResource
    from ._models_py3 import AutoscaleSettingResourceCollection
    from ._models_py3 import AutoscaleSettingResourcePatch
    from ._models_py3 import EmailNotification
    from ._models_py3 import ErrorResponse
    from ._models_py3 import EventCategoryCollection
    from ._models_py3 import EventData
    from ._models_py3 import EventDataCollection
    from ._models_py3 import HttpRequestInfo
    from ._models_py3 import LocalizableString
    from ._models_py3 import MetricTrigger
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import Recurrence
    from ._models_py3 import RecurrentSchedule
    from ._models_py3 import Resource
    from ._models_py3 import ScaleAction
    from ._models_py3 import ScaleCapacity
    from ._models_py3 import ScaleRule
    from ._models_py3 import ScaleRuleMetricDimension
    from ._models_py3 import SenderAuthorization
    from ._models_py3 import TimeWindow
    from ._models_py3 import WebhookNotification
except (SyntaxError, ImportError):
    from ._models import AutoscaleNotification  # type: ignore
    from ._models import AutoscaleProfile  # type: ignore
    from ._models import AutoscaleSettingResource  # type: ignore
    from ._models import AutoscaleSettingResourceCollection  # type: ignore
    from ._models import AutoscaleSettingResourcePatch  # type: ignore
    from ._models import EmailNotification  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import EventCategoryCollection  # type: ignore
    from ._models import EventData  # type: ignore
    from ._models import EventDataCollection  # type: ignore
    from ._models import HttpRequestInfo  # type: ignore
    from ._models import LocalizableString  # type: ignore
    from ._models import MetricTrigger  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import Recurrence  # type: ignore
    from ._models import RecurrentSchedule  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ScaleAction  # type: ignore
    from ._models import ScaleCapacity  # type: ignore
    from ._models import ScaleRule  # type: ignore
    from ._models import ScaleRuleMetricDimension  # type: ignore
    from ._models import SenderAuthorization  # type: ignore
    from ._models import TimeWindow  # type: ignore
    from ._models import WebhookNotification  # type: ignore

from ._monitor_management_client_enums import (
    ComparisonOperationType,
    EventLevel,
    MetricStatisticType,
    RecurrenceFrequency,
    ScaleDirection,
    ScaleRuleMetricDimensionOperationType,
    ScaleType,
    TimeAggregationType,
)

__all__ = [
    'AutoscaleNotification',
    'AutoscaleProfile',
    'AutoscaleSettingResource',
    'AutoscaleSettingResourceCollection',
    'AutoscaleSettingResourcePatch',
    'EmailNotification',
    'ErrorResponse',
    'EventCategoryCollection',
    'EventData',
    'EventDataCollection',
    'HttpRequestInfo',
    'LocalizableString',
    'MetricTrigger',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'Recurrence',
    'RecurrentSchedule',
    'Resource',
    'ScaleAction',
    'ScaleCapacity',
    'ScaleRule',
    'ScaleRuleMetricDimension',
    'SenderAuthorization',
    'TimeWindow',
    'WebhookNotification',
    'ComparisonOperationType',
    'EventLevel',
    'MetricStatisticType',
    'RecurrenceFrequency',
    'ScaleDirection',
    'ScaleRuleMetricDimensionOperationType',
    'ScaleType',
    'TimeAggregationType',
]
