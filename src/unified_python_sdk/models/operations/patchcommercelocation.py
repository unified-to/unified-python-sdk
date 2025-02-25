"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.models.shared import commercelocation as shared_commercelocation
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)


class PatchCommerceLocationRequestTypedDict(TypedDict):
    commerce_location: shared_commercelocation.CommerceLocationTypedDict
    connection_id: str
    r"""ID of the connection"""
    id: str
    r"""ID of the Location"""
    fields: NotRequired[List[str]]
    r"""Comma-delimited fields to return"""


class PatchCommerceLocationRequest(BaseModel):
    commerce_location: Annotated[
        shared_commercelocation.CommerceLocation,
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


class PatchCommerceLocationResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    commerce_location: NotRequired[shared_commercelocation.CommerceLocationTypedDict]
    r"""Successful"""


class PatchCommerceLocationResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    commerce_location: Optional[shared_commercelocation.CommerceLocation] = None
    r"""Successful"""
