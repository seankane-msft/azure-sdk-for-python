# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import functools

from azure.core.paging import ItemPaged

from ._base_client import ContainerRegistryBaseClient


class ContainerRegistryClient(ContainerRegistryBaseClient):
    def __init__(self, endpoint, credential, **kwargs):
        # type: (str, TokenCredential) -> None
        """Create a ContainerRegistryClient from an ACR endpoint and a credential

        :param endpoint: An ACR endpoint
        :type endpoint: str
        :param credential: The credential with which to authenticate
        :type credential: TokenCredential
        :returns: None
        :raises: None
        """
        super(ContainerRegistryClient, self).__init__(
            endpoint=endpoint, credential=credential, **kwargs
        )

        pass

    def delete_repository(self, repository, **kwargs):
        # type: (str) -> DeletedRepositoryResult
        """Delete a repository

        :param repository: The repository to delete
        :type repository: str
        :returns: None
        :raises: :class:~azure.core.exceptions.ResourceNotFoundError
        """
        pass

    def list_repositories(self, **kwargs):
        # type: (...) -> ItemPaged[str]
        """List all repositories

        :keyword max: Maximum number of repositories to return
        :type max: int
        :keyword last: Query parameter for the last item in previous query
        :type last: str
        :returns: ~azure.core.paging.ItemPaged[str]
        :raises: None
        """
        command = functools.partial(self._client.repository.get_list, **kwargs)
        repos = self._client.repository.get_list(
            last=kwargs.get("last", None), n=kwargs.get("max", None)
        )
        return ItemPaged(
            command
            # page_iterator_class=s
        )
        pass

    def get_repository_client(self, repository, **kwargs):
        # type: (str) -> ContainerRepositoryClient
        """Get a repository client

        :param repository: The repository to create a client for
        :type repository: str
        :returns: :class:~azure.containerregistry.ContainerRepositoryClient
        """
        pass
