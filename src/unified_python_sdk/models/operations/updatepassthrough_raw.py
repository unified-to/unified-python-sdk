"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
import io
from typing import Any, Dict, IO, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)


class UpdatePassthroughRawRequestTypedDict(TypedDict):
    connection_id: str
    r"""ID of the connection"""
    path: str
    request_body: NotRequired[Union[bytes, IO[bytes], io.BufferedReader]]
    r"""integration-specific payload"""
    query: NotRequired[Dict[str, Any]]


class UpdatePassthroughRawRequest(BaseModel):
    connection_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the connection"""

    path: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        Optional[Union[bytes, IO[bytes], io.BufferedReader]],
        FieldMetadata(request=RequestMetadata(media_type="text/plain")),
    ] = None
    r"""integration-specific payload"""

    query: Annotated[
        Optional[Dict[str, Any]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None


class UpdatePassthroughRawResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    headers: Dict[str, List[str]]
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    default_wildcard_wildcard_response_stream: NotRequired[httpx.Response]
    r"""Successful"""
    default_application_json_any: NotRequired[Any]
    r"""Successful"""
    default_application_xml_res: NotRequired[str]
    r"""Successful"""
    default_text_csv_res: NotRequired[str]
    r"""Successful"""
    default_text_plain_res: NotRequired[str]
    r"""Successful"""


class UpdatePassthroughRawResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    headers: Dict[str, List[str]]

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    default_wildcard_wildcard_response_stream: Optional[httpx.Response] = None
    r"""Successful"""

    default_application_json_any: Optional[Any] = None
    r"""Successful"""

    default_application_xml_res: Optional[str] = None
    r"""Successful"""

    default_text_csv_res: Optional[str] = None
    r"""Successful"""

    default_text_plain_res: Optional[str] = None
    r"""Successful"""
