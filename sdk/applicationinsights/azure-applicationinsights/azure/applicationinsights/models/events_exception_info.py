# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EventsExceptionInfo(Model):
    """The exception info.

    :param severity_level: The severity level of the exception
    :type severity_level: int
    :param problem_id: The problem ID of the exception
    :type problem_id: str
    :param handled_at: Indicates where the exception was handled at
    :type handled_at: str
    :param assembly: The assembly which threw the exception
    :type assembly: str
    :param method: The method that threw the exception
    :type method: str
    :param message: The message of the exception
    :type message: str
    :param type: The type of the exception
    :type type: str
    :param outer_type: The outer type of the exception
    :type outer_type: str
    :param outer_method: The outer method of the exception
    :type outer_method: str
    :param outer_assembly: The outer assmebly of the exception
    :type outer_assembly: str
    :param outer_message: The outer message of the exception
    :type outer_message: str
    :param innermost_type: The inner most type of the exception
    :type innermost_type: str
    :param innermost_message: The inner most message of the exception
    :type innermost_message: str
    :param innermost_method: The inner most method of the exception
    :type innermost_method: str
    :param innermost_assembly: The inner most assembly of the exception
    :type innermost_assembly: str
    :param details: The details of the exception
    :type details:
     list[~azure.applicationinsights.models.EventsExceptionDetail]
    """

    _attribute_map = {
        'severity_level': {'key': 'severityLevel', 'type': 'int'},
        'problem_id': {'key': 'problemId', 'type': 'str'},
        'handled_at': {'key': 'handledAt', 'type': 'str'},
        'assembly': {'key': 'assembly', 'type': 'str'},
        'method': {'key': 'method', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'outer_type': {'key': 'outerType', 'type': 'str'},
        'outer_method': {'key': 'outerMethod', 'type': 'str'},
        'outer_assembly': {'key': 'outerAssembly', 'type': 'str'},
        'outer_message': {'key': 'outerMessage', 'type': 'str'},
        'innermost_type': {'key': 'innermostType', 'type': 'str'},
        'innermost_message': {'key': 'innermostMessage', 'type': 'str'},
        'innermost_method': {'key': 'innermostMethod', 'type': 'str'},
        'innermost_assembly': {'key': 'innermostAssembly', 'type': 'str'},
        'details': {'key': 'details', 'type': '[EventsExceptionDetail]'},
    }

    def __init__(self, **kwargs):
        super(EventsExceptionInfo, self).__init__(**kwargs)
        self.severity_level = kwargs.get('severity_level', None)
        self.problem_id = kwargs.get('problem_id', None)
        self.handled_at = kwargs.get('handled_at', None)
        self.assembly = kwargs.get('assembly', None)
        self.method = kwargs.get('method', None)
        self.message = kwargs.get('message', None)
        self.type = kwargs.get('type', None)
        self.outer_type = kwargs.get('outer_type', None)
        self.outer_method = kwargs.get('outer_method', None)
        self.outer_assembly = kwargs.get('outer_assembly', None)
        self.outer_message = kwargs.get('outer_message', None)
        self.innermost_type = kwargs.get('innermost_type', None)
        self.innermost_message = kwargs.get('innermost_message', None)
        self.innermost_method = kwargs.get('innermost_method', None)
        self.innermost_assembly = kwargs.get('innermost_assembly', None)
        self.details = kwargs.get('details', None)
