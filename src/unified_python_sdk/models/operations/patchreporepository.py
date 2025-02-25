"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.models.shared import reporepository as shared_reporepository
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)


class PatchRepoRepositoryRequestTypedDict(TypedDict):
    repo_repository: shared_reporepository.RepoRepositoryTypedDict
    connection_id: str
    r"""ID of the connection"""
    id: str
    r"""ID of the Repository"""
    fields: NotRequired[List[str]]
    r"""Comma-delimited fields to return"""


class PatchRepoRepositoryRequest(BaseModel):
    repo_repository: Annotated[
        shared_reporepository.RepoRepository,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    connection_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the connection"""

    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the Repository"""

    fields: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Comma-delimited fields to return"""


class PatchRepoRepositoryResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    repo_repository: NotRequired[shared_reporepository.RepoRepositoryTypedDict]
    r"""Successful"""


class PatchRepoRepositoryResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    repo_repository: Optional[shared_reporepository.RepoRepository] = None
    r"""Successful"""
