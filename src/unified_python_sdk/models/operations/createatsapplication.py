"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.models.shared import atsapplication as shared_atsapplication
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)


class CreateAtsApplicationRequestTypedDict(TypedDict):
    ats_application: shared_atsapplication.AtsApplicationTypedDict
    connection_id: str
    r"""ID of the connection"""
    fields: NotRequired[List[str]]
    r"""Comma-delimited fields to return"""


class CreateAtsApplicationRequest(BaseModel):
    ats_application: Annotated[
        shared_atsapplication.AtsApplication,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    connection_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the connection"""

    fields: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Comma-delimited fields to return"""


class CreateAtsApplicationResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    ats_application: NotRequired[shared_atsapplication.AtsApplicationTypedDict]
    r"""Successful"""


class CreateAtsApplicationResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    ats_application: Optional[shared_atsapplication.AtsApplication] = None
    r"""Successful"""
