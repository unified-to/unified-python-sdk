"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Dict, List, Optional


@dataclasses.dataclass
class UpdatePassthroughJSONRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    path: str = dataclasses.field(metadata={'path_param': { 'field_name': 'path', 'style': 'simple', 'explode': False }})
    request_body: Optional[Any] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""integration-specific payload"""
    



@dataclasses.dataclass
class UpdatePassthroughJSONResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    headers: Dict[str, List[str]] = dataclasses.field()
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    two_xx_application_json_any: Optional[Any] = dataclasses.field(default=None)
    r"""Successful"""
    two_xx_text_plain_res: Optional[str] = dataclasses.field(default=None)
    r"""Successful"""
    body: Optional[bytes] = dataclasses.field(default=None)
    

