"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import marketingmember as shared_marketingmember
from typing import Optional



@dataclasses.dataclass
class UpdateMartechMemberRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the Member"""
    list_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'list_id', 'style': 'simple', 'explode': False }})
    r"""ID of the list"""
    marketing_member: Optional[shared_marketingmember.MarketingMember] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""A member represents a person"""
    




@dataclasses.dataclass
class UpdateMartechMemberResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    marketing_member: Optional[shared_marketingmember.MarketingMember] = dataclasses.field(default=None)
    r"""Successful"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

