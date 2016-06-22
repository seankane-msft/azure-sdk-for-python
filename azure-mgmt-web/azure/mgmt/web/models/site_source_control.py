# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class SiteSourceControl(Resource):
    """Describes the source control configuration for web app.

    :param id: Resource Id
    :type id: str
    :param name: Resource Name
    :type name: str
    :param kind: Kind of resource
    :type kind: str
    :param location: Resource Location
    :type location: str
    :param type: Resource type
    :type type: str
    :param tags: Resource tags
    :type tags: dict
    :param repo_url: Repository or source control url
    :type repo_url: str
    :param branch: Name of branch to use for deployment
    :type branch: str
    :param is_manual_integration: Whether to manual or continuous integration
    :type is_manual_integration: bool
    :param deployment_rollback_enabled: Whether to manual or continuous
     integration
    :type deployment_rollback_enabled: bool
    :param is_mercurial: Mercurial or Git repository type
    :type is_mercurial: bool
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'repo_url': {'key': 'properties.repoUrl', 'type': 'str'},
        'branch': {'key': 'properties.branch', 'type': 'str'},
        'is_manual_integration': {'key': 'properties.isManualIntegration', 'type': 'bool'},
        'deployment_rollback_enabled': {'key': 'properties.deploymentRollbackEnabled', 'type': 'bool'},
        'is_mercurial': {'key': 'properties.isMercurial', 'type': 'bool'},
    }

    def __init__(self, location, id=None, name=None, kind=None, type=None, tags=None, repo_url=None, branch=None, is_manual_integration=None, deployment_rollback_enabled=None, is_mercurial=None):
        super(SiteSourceControl, self).__init__(id=id, name=name, kind=kind, location=location, type=type, tags=tags)
        self.repo_url = repo_url
        self.branch = branch
        self.is_manual_integration = is_manual_integration
        self.deployment_rollback_enabled = deployment_rollback_enabled
        self.is_mercurial = is_mercurial
