# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class DataSourceKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Datasource kind
    """

    PERFORMANCE_COUNTER = "PerformanceCounter"
    ETW_PROVIDERS = "ETWProviders"
    WINDOWS_EVENT_LOGS = "WindowsEventLogs"

class GuestDiagnosticSettingsOsType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Operating system type for the configuration
    """

    WINDOWS = "Windows"
    LINUX = "Linux"

class SinkConfigurationKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    EVENT_HUB = "EventHub"
    APPLICATION_INSIGHTS = "ApplicationInsights"
    LOG_ANALYTICS = "LogAnalytics"
