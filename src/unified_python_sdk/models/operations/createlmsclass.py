"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.models.shared import lmsclass as shared_lmsclass
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)


class CreateLmsClassRequestTypedDict(TypedDict):
    connection_id: str
    r"""ID of the connection"""
    lms_class: NotRequired[shared_lmsclass.LmsClassTypedDict]
    fields: NotRequired[List[str]]
    r"""Comma-delimited fields to return"""


class CreateLmsClassRequest(BaseModel):
    connection_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the connection"""

    lms_class: Annotated[
        Optional[shared_lmsclass.LmsClass],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None

    fields: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Comma-delimited fields to return"""


class CreateLmsClassResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    lms_class: NotRequired[shared_lmsclass.LmsClassTypedDict]
    r"""Successful"""


class CreateLmsClassResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    lms_class: Optional[shared_lmsclass.LmsClass] = None
    r"""Successful"""
