"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.models.shared import hrislocation as shared_hrislocation
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)


class PatchHrisLocationRequestTypedDict(TypedDict):
    hris_location: shared_hrislocation.HrisLocationTypedDict
    connection_id: str
    r"""ID of the connection"""
    id: str
    r"""ID of the Location"""
    fields: NotRequired[List[str]]
    r"""Comma-delimited fields to return"""


class PatchHrisLocationRequest(BaseModel):
    hris_location: Annotated[
        shared_hrislocation.HrisLocation,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    connection_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the connection"""

    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the Location"""

    fields: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Comma-delimited fields to return"""


class PatchHrisLocationResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    hris_location: NotRequired[shared_hrislocation.HrisLocationTypedDict]
    r"""Successful"""


class PatchHrisLocationResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    hris_location: Optional[shared_hrislocation.HrisLocation] = None
    r"""Successful"""
