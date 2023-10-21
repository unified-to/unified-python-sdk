"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import undefined as shared_undefined
from typing import Optional


@dataclasses.dataclass
class CreatePassthroughRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    path: str = dataclasses.field(metadata={'path_param': { 'field_name': 'path', 'style': 'simple', 'explode': False }})
    undefined: Optional[shared_undefined.Undefined] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""integration-specific payload"""
    



@dataclasses.dataclass
class CreatePassthroughResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    undefined: Optional[shared_undefined.Undefined] = dataclasses.field(default=None)
    r"""Successful"""
    
