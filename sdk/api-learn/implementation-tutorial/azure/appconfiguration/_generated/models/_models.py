# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Error(msrest.serialization.Model):
    """Azure App Configuration error object.

    :param type: The type of the error.
    :type type: str
    :param title: A brief summary of the error.
    :type title: str
    :param name: The name of the parameter that resulted in the error.
    :type name: str
    :param detail: A detailed description of the error.
    :type detail: str
    :param status: The HTTP status code that the error maps to.
    :type status: int
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'detail': {'key': 'detail', 'type': 'str'},
        'status': {'key': 'status', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Error, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.title = kwargs.get('title', None)
        self.name = kwargs.get('name', None)
        self.detail = kwargs.get('detail', None)
        self.status = kwargs.get('status', None)


class Key(msrest.serialization.Model):
    """Key.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name:
    :vartype name: str
    """

    _validation = {
        'name': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Key, self).__init__(**kwargs)
        self.name = None


class KeyListResult(msrest.serialization.Model):
    """The result of a list request.

    :param items: The collection value.
    :type items: list[~azure.appconfiguration.models.Key]
    :param next_link: The URI that can be used to request the next set of paged results.
    :type next_link: str
    """

    _attribute_map = {
        'items': {'key': 'items', 'type': '[Key]'},
        'next_link': {'key': '@nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(KeyListResult, self).__init__(**kwargs)
        self.items = kwargs.get('items', None)
        self.next_link = kwargs.get('next_link', None)


class KeyValue(msrest.serialization.Model):
    """KeyValue.

    :param key:
    :type key: str
    :param label:
    :type label: str
    :param content_type:
    :type content_type: str
    :param value:
    :type value: str
    :param last_modified:
    :type last_modified: ~datetime.datetime
    :param tags: A set of tags. Dictionary of :code:`<string>`.
    :type tags: dict[str, str]
    :param locked:
    :type locked: bool
    :param etag:
    :type etag: str
    """

    _attribute_map = {
        'key': {'key': 'key', 'type': 'str'},
        'label': {'key': 'label', 'type': 'str'},
        'content_type': {'key': 'content_type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'last_modified': {'key': 'last_modified', 'type': 'iso-8601'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'locked': {'key': 'locked', 'type': 'bool'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(KeyValue, self).__init__(**kwargs)
        self.key = kwargs.get('key', None)
        self.label = kwargs.get('label', None)
        self.content_type = kwargs.get('content_type', None)
        self.value = kwargs.get('value', None)
        self.last_modified = kwargs.get('last_modified', None)
        self.tags = kwargs.get('tags', None)
        self.locked = kwargs.get('locked', None)
        self.etag = kwargs.get('etag', None)


class KeyValueListResult(msrest.serialization.Model):
    """The result of a list request.

    :param items: The collection value.
    :type items: list[~azure.appconfiguration.models.KeyValue]
    :param next_link: The URI that can be used to request the next set of paged results.
    :type next_link: str
    """

    _attribute_map = {
        'items': {'key': 'items', 'type': '[KeyValue]'},
        'next_link': {'key': '@nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(KeyValueListResult, self).__init__(**kwargs)
        self.items = kwargs.get('items', None)
        self.next_link = kwargs.get('next_link', None)


class Label(msrest.serialization.Model):
    """Label.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name:
    :vartype name: str
    """

    _validation = {
        'name': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Label, self).__init__(**kwargs)
        self.name = None


class LabelListResult(msrest.serialization.Model):
    """The result of a list request.

    :param items: The collection value.
    :type items: list[~azure.appconfiguration.models.Label]
    :param next_link: The URI that can be used to request the next set of paged results.
    :type next_link: str
    """

    _attribute_map = {
        'items': {'key': 'items', 'type': '[Label]'},
        'next_link': {'key': '@nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(LabelListResult, self).__init__(**kwargs)
        self.items = kwargs.get('items', None)
        self.next_link = kwargs.get('next_link', None)