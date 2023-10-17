"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import connection as shared_connection
from typing import Optional


@dataclasses.dataclass
class PatchUnifiedConnectionRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the Connection"""
    connection: Optional[shared_connection.Connection] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""A connection represents a specific authentication of an integration."""
    



@dataclasses.dataclass
class PatchUnifiedConnectionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    connection: Optional[shared_connection.Connection] = dataclasses.field(default=None)
    r"""Successful"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

