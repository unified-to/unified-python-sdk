"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import connection as shared_connection
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
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    connection: Optional[shared_connection.Connection] = dataclasses.field(default=None)
    r"""Successful"""
    

