"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import connection as shared_connection
from typing import Optional


@dataclasses.dataclass
class UpdateUnifiedConnectionRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the Connection"""
    connection: Optional[shared_connection.Connection] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""A connection represents a specific authentication of an integration."""
    



@dataclasses.dataclass
class UpdateUnifiedConnectionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    connection: Optional[shared_connection.Connection] = dataclasses.field(default=None)
    r"""Successful"""
    

