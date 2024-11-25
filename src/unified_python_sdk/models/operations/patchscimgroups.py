"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.models.shared import scimgroup as shared_scimgroup
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata


class PatchScimGroupsRequestTypedDict(TypedDict):
    connection_id: str
    r"""ID of the connection"""
    id: str
    r"""ID of the Group"""
    scim_group: NotRequired[shared_scimgroup.ScimGroupTypedDict]


class PatchScimGroupsRequest(BaseModel):
    connection_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the connection"""

    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the Group"""

    scim_group: Annotated[
        Optional[shared_scimgroup.ScimGroup],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


class PatchScimGroupsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    scim_group: NotRequired[shared_scimgroup.ScimGroupTypedDict]
    r"""Successful"""


class PatchScimGroupsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    scim_group: Optional[shared_scimgroup.ScimGroup] = None
    r"""Successful"""
