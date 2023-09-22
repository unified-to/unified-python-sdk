"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import crmfile as shared_crmfile
from typing import Optional



@dataclasses.dataclass
class GetCrmConnectionIDFileIDRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the File"""
    




@dataclasses.dataclass
class GetCrmConnectionIDFileIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    crm_file: Optional[shared_crmfile.CrmFile] = dataclasses.field(default=None)
    r"""Successful"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

