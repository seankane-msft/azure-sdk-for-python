# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------


class ContainerRegistryClient(object):
    def __init__(self, base_url, credential, **kwargs):
        # type: (str, TokenCredential) -> None

        pass

    def delete_repository(self, name, **kwargs):
        # type: (str) -> DeletedRepositoryResult

        pass

    def list_repositories(self, **kwargs):
        # type: (...) -> Pageable[str]

        pass

    def get_repository_client(self, name, **kwargs):
        # type: (str) -> ContainerRepositoryClient

        pass

    def get_repository_attributes(self, name, **kwargs):
        # type: (str) -> RepositoryAttributes

        pass
