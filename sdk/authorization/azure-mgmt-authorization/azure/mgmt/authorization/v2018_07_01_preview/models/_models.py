# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class DenyAssignment(msrest.serialization.Model):
    """Deny Assignment.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The deny assignment ID.
    :vartype id: str
    :ivar name: The deny assignment name.
    :vartype name: str
    :ivar type: The deny assignment type.
    :vartype type: str
    :param deny_assignment_name: The display name of the deny assignment.
    :type deny_assignment_name: str
    :param description: The description of the deny assignment.
    :type description: str
    :param permissions: An array of permissions that are denied by the deny assignment.
    :type permissions:
     list[~azure.mgmt.authorization.v2018_07_01_preview.models.DenyAssignmentPermission]
    :param scope: The deny assignment scope.
    :type scope: str
    :param do_not_apply_to_child_scopes: Determines if the deny assignment applies to child scopes.
     Default value is false.
    :type do_not_apply_to_child_scopes: bool
    :param principals: Array of principals to which the deny assignment applies.
    :type principals: list[~azure.mgmt.authorization.v2018_07_01_preview.models.Principal]
    :param exclude_principals: Array of principals to which the deny assignment does not apply.
    :type exclude_principals: list[~azure.mgmt.authorization.v2018_07_01_preview.models.Principal]
    :param is_system_protected: Specifies whether this deny assignment was created by Azure and
     cannot be edited or deleted.
    :type is_system_protected: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'deny_assignment_name': {'key': 'properties.denyAssignmentName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'permissions': {'key': 'properties.permissions', 'type': '[DenyAssignmentPermission]'},
        'scope': {'key': 'properties.scope', 'type': 'str'},
        'do_not_apply_to_child_scopes': {'key': 'properties.doNotApplyToChildScopes', 'type': 'bool'},
        'principals': {'key': 'properties.principals', 'type': '[Principal]'},
        'exclude_principals': {'key': 'properties.excludePrincipals', 'type': '[Principal]'},
        'is_system_protected': {'key': 'properties.isSystemProtected', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DenyAssignment, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.deny_assignment_name = kwargs.get('deny_assignment_name', None)
        self.description = kwargs.get('description', None)
        self.permissions = kwargs.get('permissions', None)
        self.scope = kwargs.get('scope', None)
        self.do_not_apply_to_child_scopes = kwargs.get('do_not_apply_to_child_scopes', None)
        self.principals = kwargs.get('principals', None)
        self.exclude_principals = kwargs.get('exclude_principals', None)
        self.is_system_protected = kwargs.get('is_system_protected', None)


class DenyAssignmentFilter(msrest.serialization.Model):
    """Deny Assignments filter.

    :param deny_assignment_name: Return deny assignment with specified name.
    :type deny_assignment_name: str
    :param principal_id: Return all deny assignments where the specified principal is listed in the
     principals list of deny assignments.
    :type principal_id: str
    :param gdpr_export_principal_id: Return all deny assignments where the specified principal is
     listed either in the principals list or exclude principals list of deny assignments.
    :type gdpr_export_principal_id: str
    """

    _attribute_map = {
        'deny_assignment_name': {'key': 'denyAssignmentName', 'type': 'str'},
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'gdpr_export_principal_id': {'key': 'gdprExportPrincipalId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DenyAssignmentFilter, self).__init__(**kwargs)
        self.deny_assignment_name = kwargs.get('deny_assignment_name', None)
        self.principal_id = kwargs.get('principal_id', None)
        self.gdpr_export_principal_id = kwargs.get('gdpr_export_principal_id', None)


class DenyAssignmentListResult(msrest.serialization.Model):
    """Deny assignment list operation result.

    :param value: Deny assignment list.
    :type value: list[~azure.mgmt.authorization.v2018_07_01_preview.models.DenyAssignment]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[DenyAssignment]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DenyAssignmentListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class DenyAssignmentPermission(msrest.serialization.Model):
    """Deny assignment permissions.

    :param actions: Actions to which the deny assignment does not grant access.
    :type actions: list[str]
    :param not_actions: Actions to exclude from that the deny assignment does not grant access.
    :type not_actions: list[str]
    :param data_actions: Data actions to which the deny assignment does not grant access.
    :type data_actions: list[str]
    :param not_data_actions: Data actions to exclude from that the deny assignment does not grant
     access.
    :type not_data_actions: list[str]
    """

    _attribute_map = {
        'actions': {'key': 'actions', 'type': '[str]'},
        'not_actions': {'key': 'notActions', 'type': '[str]'},
        'data_actions': {'key': 'dataActions', 'type': '[str]'},
        'not_data_actions': {'key': 'notDataActions', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DenyAssignmentPermission, self).__init__(**kwargs)
        self.actions = kwargs.get('actions', None)
        self.not_actions = kwargs.get('not_actions', None)
        self.data_actions = kwargs.get('data_actions', None)
        self.not_data_actions = kwargs.get('not_data_actions', None)


class Principal(msrest.serialization.Model):
    """Deny assignment principal.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Object ID of the Azure AD principal (user, group, or service principal) to which the
     deny assignment applies. An empty guid '00000000-0000-0000-0000-000000000000' as principal id
     and principal type as 'Everyone' represents all users, groups and service principals.
    :vartype id: str
    :ivar type: Type of object represented by principal id (user, group, or service principal). An
     empty guid '00000000-0000-0000-0000-000000000000' as principal id and principal type as
     'Everyone' represents all users, groups and service principals.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Principal, self).__init__(**kwargs)
        self.id = None
        self.type = None
