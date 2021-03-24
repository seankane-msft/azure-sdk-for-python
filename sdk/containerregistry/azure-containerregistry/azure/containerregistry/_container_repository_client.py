# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from typing import TYPE_CHECKING

from ._base_client import ContainerRegistryBaseClient
from ._models import RepositoryProperties, TagProperties, RegistryArtifactProperties

if TYPE_CHECKING:
    from typing import Any, Dict
    from azure.core.paging import ItemPaged
    from azure.core.credentials import TokenCredential
    from ._models import ContentPermissions


class ContainerRepositoryClient(ContainerRegistryBaseClient):
    def __init__(self, endpoint, repository, credential, **kwargs):
        # type: (str, str, TokenCredential, Dict[str, Any]) -> None
        """Create a ContainerRepositoryClient from an endpoint, repository name, and credential

        :param endpoint: An ACR endpoint
        :type endpoint: str
        :param repository: The name of a repository
        :type repository: str
        :param credential: The credential with which to authenticate
        :type credential: TokenCredential
        :returns: None
        :raises: None
        """
        if not endpoint.startswith("https://"):
            endpoint = "https://" + endpoint
        self._endpoint = endpoint
        self.repository = repository
        super(ContainerRepositoryClient, self).__init__(endpoint=self._endpoint, credential=credential, **kwargs)

    def delete(self, **kwargs):
        # type: (...) -> None
        """Delete a repository

        :returns: None
        :raises: :class:~azure.core.exceptions.ResourceNotFoundError
        """
        self._client.container_registry.delete_repository(self.repository, **kwargs)

    def delete_registry_artifact(self, digest):
        # type: (str) -> None
        """Delete a registry artifact

        :param digest: The digest of the artifact to be deleted
        :type digest: str
        :returns: None
        :raises: :class:~azure.core.exceptions.ResourceNotFoundError
        """
        raise NotImplementedError("Has not been implemented")

    def delete_tag(self, tag):
        # type: (str) -> None
        """Delete a tag

        :param tag: The digest of the artifact to be deleted
        :type tag: str
        :returns: None
        :raises: :class:~azure.core.exceptions.ResourceNotFoundError
        """
        raise NotImplementedError("Has not been implemented")

    def get_digest_from_tag(self, tag):
        # type: (str) -> str
        for t in self.list_tags():
            if t.name == tag:
                return t.digest
        raise ValueError("Could not find a digest for tag {}".format(tag))

    def get_properties(self):
        # type: (...) -> RepositoryProperties
        """Get the properties of a repository

        :returns: :class:~azure.containerregistry.RepositoryProperties
        :raises: None
        """
        # GET '/acr/v1/{name}'
        return RepositoryProperties._from_generated(self._client.container_registry_repository.get_properties(self.repository))

    def get_registry_artifact_properties(self, tag_or_digest, **kwargs):
        # type: (str, Dict[str, Any]) -> RegistryArtifactProperties
        """Get the properties of a registry artifact

        :param tag_or_digest: The tag/digest of a registry artifact
        :type tag_or_digest: str
        :returns: :class:~azure.containerregistry.RegistryArtifactProperties
        :raises: :class:~azure.core.exceptions.ResourceNotFoundError
        """
        # GET '/acr/v1/{name}/_manifests/{digest}'
        if self._is_tag(tag_or_digest):
            tag_or_digest = self.get_digest_from_tag(tag_or_digest)

        return RegistryArtifactProperties._from_generated(
            self._client.container_registry_repository.get_registry_artifact_properties(
                self.repository, tag_or_digest, **kwargs
            )
        )

    def get_tag_properties(self, tag, **kwargs):
        # type: (str, Dict[str, Any]) -> TagProperties
        """Get the properties for a tag

        :param tag: The tag to get properties for
        :type tag: str
        :returns: :class:~azure.containerregistry.TagProperties
        :raises: :class:~azure.core.exceptions.ResourceNotFoundError
        """
        # GET '/acr/v1/{name}/_tags/{reference}'
        return TagProperties._from_generated(  # pylint: disable=protected-access
            self._client.container_registry_repository.get_tag_properties(self.repository, tag, **kwargs)
        )

    def list_registry_artifacts(self, **kwargs):
        # type: (...) -> ItemPaged[RegistryArtifactProperties]
        """List the artifacts for a repository

        :keyword last: Query parameter for the last item in the previous query
        :type last: str
        :keyword n: Max number of items to be returned
        :type n: int
        :keyword orderby: Order by query parameter
        :type orderby: :class:~azure.containerregistry.RegistryArtifactOrderBy
        :returns: ~azure.core.paging.ItemPaged[RegistryArtifactProperties]
        :raises: None
        """
        # GET /acr/v1/{name}/_manifests
        last = kwargs.pop("last", None)
        n = kwargs.pop("top", None)
        orderby = kwargs.pop("order_by", None)
        return self._client.container_registry_repository.get_manifests(
            self.repository, last=last, n=n, orderby=orderby,
            cls=lambda objs: [RegistryArtifactProperties._from_generated(x) for x in objs]
        )

    def list_tags(self, **kwargs):
        # type: (...) -> ItemPaged[TagProperties]
        """List the tags for a repository

        :param last: Query parameter for the last item in the previous call. Ensuing
            call will return values after last lexically
        :type last: str
        :param order_by: Query paramter for ordering by time ascending or descending
        :returns: ~azure.core.paging.ItemPaged[TagProperties]
        :raises: None
        """
        return self._client.container_registry_repository.get_tags(
            self.repository,
            last=kwargs.pop("last", None),
            n=kwargs.pop("top", None),
            orderby=kwargs.pop("order_by", None),
            digest=kwargs.pop("digest", None),
            cls=lambda objs: [TagProperties._from_generated(o) for o in objs],
            **kwargs
        )

    def set_manifest_properties(self, digest, permissions):
        # type: (str, ContentPermissions) -> None
        """Set the properties for a manifest

        :param digest: Digest of a manifest
        :type digest: str
        :param permissions: The property's values to be set
        :type permissions: ContentPermissions
        :returns: ~azure.core.paging.ItemPaged[TagProperties]
        :raises: None
        """

        self._client.container_registry_repository.update_manifest_attributes(
            self.repository, digest, permissions.to_generated()
        )

    def set_tag_properties(self, tag_or_digest, permissions):
        # type: (str, ContentPermissions) -> None
        """Set the properties for a tag

        :param tag: Tag to set properties for
        :type tag: str
        :param permissions: The property's values to be set
        :type permissions: ContentPermissions
        :returns: ~azure.core.paging.ItemPaged[TagProperties]
        :raises: None
        """
        if self._is_tag(tag_or_digest):
            tag_or_digest = self.get_digest_from_tag(tag_or_digest)

        self._client.container_registry_repository.update_manifest_attributes(
            self.repository, tag_or_digest, permissions.to_generated()
        )
