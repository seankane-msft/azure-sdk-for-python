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


class DependencyLevel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    DIRECT = "Direct"
    DESCENDANT = "Descendant"

class DependencyType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Defines the dependency type.
    """

    REQUIRED_FOR_PREPARE = "RequiredForPrepare"
    REQUIRED_FOR_MOVE = "RequiredForMove"

class JobName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Defines the job name.
    """

    INITIAL_SYNC = "InitialSync"

class MoveResourceInputType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Defines the move resource input type.
    """

    MOVE_RESOURCE_ID = "MoveResourceId"
    MOVE_RESOURCE_SOURCE_ID = "MoveResourceSourceId"

class MoveState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Defines the MoveResource states.
    """

    ASSIGNMENT_PENDING = "AssignmentPending"
    PREPARE_PENDING = "PreparePending"
    PREPARE_IN_PROGRESS = "PrepareInProgress"
    PREPARE_FAILED = "PrepareFailed"
    MOVE_PENDING = "MovePending"
    MOVE_IN_PROGRESS = "MoveInProgress"
    MOVE_FAILED = "MoveFailed"
    DISCARD_IN_PROGRESS = "DiscardInProgress"
    DISCARD_FAILED = "DiscardFailed"
    COMMIT_PENDING = "CommitPending"
    COMMIT_IN_PROGRESS = "CommitInProgress"
    COMMIT_FAILED = "CommitFailed"
    COMMITTED = "Committed"
    DELETE_SOURCE_PENDING = "DeleteSourcePending"
    RESOURCE_MOVE_COMPLETED = "ResourceMoveCompleted"

class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Defines the provisioning states.
    """

    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"
    CREATING = "Creating"
    FAILED = "Failed"

class ResolutionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Defines the resolution type.
    """

    MANUAL = "Manual"
    AUTOMATIC = "Automatic"

class ResourceIdentityType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity used for the resource mover service.
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"

class TargetAvailabilityZone(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Gets or sets the target availability zone.
    """

    ONE = "1"
    TWO = "2"
    THREE = "3"
    NA = "NA"

class ZoneRedundant(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Defines the zone redundant resource setting.
    """

    ENABLE = "Enable"
    DISABLE = "Disable"
