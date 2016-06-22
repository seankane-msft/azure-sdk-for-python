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


class ContentLink(Model):
    """ContentLink.

    :param uri: Gets or sets the content link URI.
    :type uri: str
    :param content_version: Gets or sets the content version.
    :type content_version: str
    :param content_size: Gets or sets the content size.
    :type content_size: long
    :param content_hash: Gets or sets the content hash.
    :type content_hash: :class:`ContentHash
     <azure.mgmt.logic.models.ContentHash>`
    :param metadata: Gets or sets the metadata.
    :type metadata: object
    """ 

    _attribute_map = {
        'uri': {'key': 'uri', 'type': 'str'},
        'content_version': {'key': 'contentVersion', 'type': 'str'},
        'content_size': {'key': 'contentSize', 'type': 'long'},
        'content_hash': {'key': 'contentHash', 'type': 'ContentHash'},
        'metadata': {'key': 'metadata', 'type': 'object'},
    }

    def __init__(self, uri=None, content_version=None, content_size=None, content_hash=None, metadata=None):
        self.uri = uri
        self.content_version = content_version
        self.content_size = content_size
        self.content_hash = content_hash
        self.metadata = metadata
