"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.models.shared import atsactivity as shared_atsactivity
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)


class UpdateAtsActivityRequestTypedDict(TypedDict):
    ats_activity: shared_atsactivity.AtsActivityTypedDict
    connection_id: str
    r"""ID of the connection"""
    id: str
    r"""ID of the Activity"""
    fields: NotRequired[List[str]]
    r"""Comma-delimited fields to return"""


class UpdateAtsActivityRequest(BaseModel):
    ats_activity: Annotated[
        shared_atsactivity.AtsActivity,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    connection_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the connection"""

    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the Activity"""

    fields: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Comma-delimited fields to return"""


class UpdateAtsActivityResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    ats_activity: NotRequired[shared_atsactivity.AtsActivityTypedDict]
    r"""Successful"""


class UpdateAtsActivityResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    ats_activity: Optional[shared_atsactivity.AtsActivity] = None
    r"""Successful"""
