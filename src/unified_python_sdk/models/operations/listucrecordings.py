"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.models.shared import ucrecording as shared_ucrecording
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)


class ListUcRecordingsRequestTypedDict(TypedDict):
    connection_id: str
    r"""ID of the connection"""
    call_id: NotRequired[str]
    r"""The call ID to filter by"""
    contact_id: NotRequired[str]
    r"""The contact ID to filter by"""
    end_le: NotRequired[str]
    r"""The end date to filter by"""
    fields: NotRequired[List[str]]
    r"""Comma-delimited fields to return"""
    limit: NotRequired[float]
    offset: NotRequired[float]
    order: NotRequired[str]
    query: NotRequired[str]
    r"""Query string to search. eg. email address or name"""
    raw: NotRequired[str]
    r"""Raw parameters to include in the 3rd-party request. Encoded as a URL component. eg. raw parameters: foo=bar&zoo=bar -> raw=foo%3Dbar%26zoo%3Dbar"""
    sort: NotRequired[str]
    start_gte: NotRequired[str]
    r"""The start date to filter by"""
    updated_gte: NotRequired[str]
    r"""Return only results whose updated date is equal or greater to this value"""
    user_id: NotRequired[str]
    r"""The user/employee ID to filter by"""


class ListUcRecordingsRequest(BaseModel):
    connection_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the connection"""

    call_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The call ID to filter by"""

    contact_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The contact ID to filter by"""

    end_le: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The end date to filter by"""

    fields: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Comma-delimited fields to return"""

    limit: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    offset: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    order: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    query: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Query string to search. eg. email address or name"""

    raw: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Raw parameters to include in the 3rd-party request. Encoded as a URL component. eg. raw parameters: foo=bar&zoo=bar -> raw=foo%3Dbar%26zoo%3Dbar"""

    sort: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    start_gte: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The start date to filter by"""

    updated_gte: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Return only results whose updated date is equal or greater to this value"""

    user_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The user/employee ID to filter by"""


class ListUcRecordingsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    uc_recordings: NotRequired[List[shared_ucrecording.UcRecordingTypedDict]]
    r"""Successful"""


class ListUcRecordingsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    uc_recordings: Optional[List[shared_ucrecording.UcRecording]] = None
    r"""Successful"""
