# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AccessToken
    from ._models_py3 import AcrErrorInfo
    from ._models_py3 import AcrErrors
    from ._models_py3 import AcrManifests
    from ._models_py3 import Annotations
    from ._models_py3 import ChangeableAttributes
    from ._models_py3 import DeletedRepository
    from ._models_py3 import Descriptor
    from ._models_py3 import FsLayer
    from ._models_py3 import History
    from ._models_py3 import ImageSignature
    from ._models_py3 import JWK
    from ._models_py3 import JWKHeader
    from ._models_py3 import Manifest
    from ._models_py3 import ManifestAttributes
    from ._models_py3 import ManifestAttributesBase
    from ._models_py3 import ManifestAttributesManifest
    from ._models_py3 import ManifestAttributesManifestReferences
    from ._models_py3 import ManifestChangeableAttributes
    from ._models_py3 import ManifestList
    from ._models_py3 import ManifestListAttributes
    from ._models_py3 import ManifestWrapper
    from ._models_py3 import OCIIndex
    from ._models_py3 import OCIManifest
    from ._models_py3 import Paths108HwamOauth2ExchangePostRequestbodyContentApplicationXWwwFormUrlencodedSchema
    from ._models_py3 import PathsV3R3RxOauth2TokenPostRequestbodyContentApplicationXWwwFormUrlencodedSchema
    from ._models_py3 import Platform
    from ._models_py3 import RefreshToken
    from ._models_py3 import Repositories
    from ._models_py3 import RepositoryAttributes
    from ._models_py3 import RepositoryTags
    from ._models_py3 import TagAttributes
    from ._models_py3 import TagAttributesBase
    from ._models_py3 import TagAttributesTag
    from ._models_py3 import TagList
    from ._models_py3 import V1Manifest
    from ._models_py3 import V2Manifest
except (SyntaxError, ImportError):
    from ._models import AccessToken  # type: ignore
    from ._models import AcrErrorInfo  # type: ignore
    from ._models import AcrErrors  # type: ignore
    from ._models import AcrManifests  # type: ignore
    from ._models import Annotations  # type: ignore
    from ._models import ChangeableAttributes  # type: ignore
    from ._models import DeletedRepository  # type: ignore
    from ._models import Descriptor  # type: ignore
    from ._models import FsLayer  # type: ignore
    from ._models import History  # type: ignore
    from ._models import ImageSignature  # type: ignore
    from ._models import JWK  # type: ignore
    from ._models import JWKHeader  # type: ignore
    from ._models import Manifest  # type: ignore
    from ._models import ManifestAttributes  # type: ignore
    from ._models import ManifestAttributesBase  # type: ignore
    from ._models import ManifestAttributesManifest  # type: ignore
    from ._models import ManifestAttributesManifestReferences  # type: ignore
    from ._models import ManifestChangeableAttributes  # type: ignore
    from ._models import ManifestList  # type: ignore
    from ._models import ManifestListAttributes  # type: ignore
    from ._models import ManifestWrapper  # type: ignore
    from ._models import OCIIndex  # type: ignore
    from ._models import OCIManifest  # type: ignore
    from ._models import Paths108HwamOauth2ExchangePostRequestbodyContentApplicationXWwwFormUrlencodedSchema  # type: ignore
    from ._models import PathsV3R3RxOauth2TokenPostRequestbodyContentApplicationXWwwFormUrlencodedSchema  # type: ignore
    from ._models import Platform  # type: ignore
    from ._models import RefreshToken  # type: ignore
    from ._models import Repositories  # type: ignore
    from ._models import RepositoryAttributes  # type: ignore
    from ._models import RepositoryTags  # type: ignore
    from ._models import TagAttributes  # type: ignore
    from ._models import TagAttributesBase  # type: ignore
    from ._models import TagAttributesTag  # type: ignore
    from ._models import TagList  # type: ignore
    from ._models import V1Manifest  # type: ignore
    from ._models import V2Manifest  # type: ignore

from ._azure_container_registry_enums import (
    PostContentSchemaGrantType,
)

__all__ = [
    'AccessToken',
    'AcrErrorInfo',
    'AcrErrors',
    'AcrManifests',
    'Annotations',
    'ChangeableAttributes',
    'DeletedRepository',
    'Descriptor',
    'FsLayer',
    'History',
    'ImageSignature',
    'JWK',
    'JWKHeader',
    'Manifest',
    'ManifestAttributes',
    'ManifestAttributesBase',
    'ManifestAttributesManifest',
    'ManifestAttributesManifestReferences',
    'ManifestChangeableAttributes',
    'ManifestList',
    'ManifestListAttributes',
    'ManifestWrapper',
    'OCIIndex',
    'OCIManifest',
    'Paths108HwamOauth2ExchangePostRequestbodyContentApplicationXWwwFormUrlencodedSchema',
    'PathsV3R3RxOauth2TokenPostRequestbodyContentApplicationXWwwFormUrlencodedSchema',
    'Platform',
    'RefreshToken',
    'Repositories',
    'RepositoryAttributes',
    'RepositoryTags',
    'TagAttributes',
    'TagAttributesBase',
    'TagAttributesTag',
    'TagList',
    'V1Manifest',
    'V2Manifest',
    'PostContentSchemaGrantType',
]