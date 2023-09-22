"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import hrisgroup as shared_hrisgroup
from typing import Optional



@dataclasses.dataclass
class PatchHrisConnectionIDGroupIDRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the Group"""
    hris_group: Optional[shared_hrisgroup.HrisGroup] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class PatchHrisConnectionIDGroupIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    hris_group: Optional[shared_hrisgroup.HrisGroup] = dataclasses.field(default=None)
    r"""Successful"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

