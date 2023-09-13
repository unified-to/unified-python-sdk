"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import marketingmember as shared_marketingmember
from typing import Optional



@dataclasses.dataclass
class PostMartechConnectionIDListIDMemberSecurity:
    jwt: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'authorization' }})
    




@dataclasses.dataclass
class PostMartechConnectionIDListIDMemberRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    list_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'list_id', 'style': 'simple', 'explode': False }})
    r"""ID of the list"""
    marketing_member: Optional[shared_marketingmember.MarketingMember] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""A member represents a person"""
    




@dataclasses.dataclass
class PostMartechConnectionIDListIDMemberResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    marketing_member: Optional[shared_marketingmember.MarketingMember] = dataclasses.field(default=None)
    r"""Successful"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

