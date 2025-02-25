"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.models.shared import repoorganization as shared_repoorganization
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)


class UpdateRepoOrganizationRequestTypedDict(TypedDict):
    repo_organization: shared_repoorganization.RepoOrganizationTypedDict
    connection_id: str
    r"""ID of the connection"""
    id: str
    r"""ID of the Organization"""
    fields: NotRequired[List[str]]
    r"""Comma-delimited fields to return"""


class UpdateRepoOrganizationRequest(BaseModel):
    repo_organization: Annotated[
        shared_repoorganization.RepoOrganization,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    connection_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the connection"""

    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the Organization"""

    fields: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Comma-delimited fields to return"""


class UpdateRepoOrganizationResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    repo_organization: NotRequired[shared_repoorganization.RepoOrganizationTypedDict]
    r"""Successful"""


class UpdateRepoOrganizationResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    repo_organization: Optional[shared_repoorganization.RepoOrganization] = None
    r"""Successful"""
