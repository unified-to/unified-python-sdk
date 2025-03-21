"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.models.shared import connection as shared_connection
from unified_python_sdk.types import BaseModel


class CreateUnifiedConnectionResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    connection: NotRequired[shared_connection.ConnectionTypedDict]
    r"""Successful"""


class CreateUnifiedConnectionResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    connection: Optional[shared_connection.Connection] = None
    r"""Successful"""
