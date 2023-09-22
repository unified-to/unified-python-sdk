"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional



@dataclasses.dataclass
class DeleteMartechConnectionIDListIDMemberIDRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the Member"""
    list_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'list_id', 'style': 'simple', 'explode': False }})
    r"""ID of the list"""
    




@dataclasses.dataclass
class DeleteMartechConnectionIDListIDMemberIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_martech_connection_id_list_id_member_id_default_application_json_string: Optional[str] = dataclasses.field(default=None)
    r"""Successful"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

