"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Dict, Optional


@dataclasses.dataclass
class RemovePassthroughRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    path: str = dataclasses.field(metadata={'path_param': { 'field_name': 'path', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class RemovePassthroughResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    undefined: Optional[Dict[str, Any]] = dataclasses.field(default=None)
    r"""Successful"""
    

