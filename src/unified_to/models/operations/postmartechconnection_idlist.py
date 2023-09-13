"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import marketinglist as shared_marketinglist
from typing import Optional



@dataclasses.dataclass
class PostMartechConnectionIDListSecurity:
    jwt: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'authorization' }})
    




@dataclasses.dataclass
class PostMartechConnectionIDListRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    marketing_list: Optional[shared_marketinglist.MarketingList] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Mailing List"""
    




@dataclasses.dataclass
class PostMartechConnectionIDListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    marketing_list: Optional[shared_marketinglist.MarketingList] = dataclasses.field(default=None)
    r"""Successful"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

