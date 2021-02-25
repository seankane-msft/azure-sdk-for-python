# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------


class ContainerRepositoryClient(object):
    def __init__(self, endpoint, repository_name, credential, **kwargs):
        # type: (str, str, TokenCredential) -> None
        pass

    def delete(self):
        # type: (...) -> None
        pass

    def delete_manifest(self, name, digest):
        # type: (str, str) -> None
        pass

    def delete_tag(self, name):
        # type: (str) -> None
        pass

    def get_artifact_storage_client(self):
        # type: (...) -> ArtifactStorageClient
        pass

    def get_attributes(self):
        # type: (...) -> RepositoryAttributes
        pass

    def get_manifest(self, tag_or_digest):
        # type: (str) -> ArtifactAttributes
        pass

    def get_tag(self, tag_name):
        # type: (str) -> TagAttributes
        pass

    def list_manifests(self, **kwargs):
        # type: (...) -> Pageable[ArtifactAttributes]
        pass

    def list_tags(self, **kwargs):
        # type: (...) -> Pageable[TagAttributes]
        pass

    def set_manifest_permissions(self, tag_or_digest, value):
        # type: (str, ContentPermissions) -> None
        pass

    def set_permissions(self, value):
        # type: (ContentPermissions) -> None
        pass

    def set_tag_permissions(self, tag, permissions):
        # type: (str, ContentPermissions) -> None
        pass
