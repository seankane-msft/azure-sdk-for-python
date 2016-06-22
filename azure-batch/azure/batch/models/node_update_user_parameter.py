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

from msrest.serialization import Model


class NodeUpdateUserParameter(Model):
    """Parameters for a ComputeNodeOperations.UpdateUser request.

    :param password: The password of the account.
    :type password: str
    :param expiry_time: The time at which the account should expire. If
     omitted, the default is 1 day from the current time.
    :type expiry_time: datetime
    :param ssh_public_key: The SSH public key that can be used for remote
     login to the compute node.
    :type ssh_public_key: str
    """ 

    _attribute_map = {
        'password': {'key': 'password', 'type': 'str'},
        'expiry_time': {'key': 'expiryTime', 'type': 'iso-8601'},
        'ssh_public_key': {'key': 'sshPublicKey', 'type': 'str'},
    }

    def __init__(self, password=None, expiry_time=None, ssh_public_key=None):
        self.password = password
        self.expiry_time = expiry_time
        self.ssh_public_key = ssh_public_key
