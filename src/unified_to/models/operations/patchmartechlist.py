"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import marketinglist as shared_marketinglist
from typing import Optional


@dataclasses.dataclass
class PatchMartechListRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the List"""
    marketing_list: Optional[shared_marketinglist.MarketingList] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Mailing List"""
    



@dataclasses.dataclass
class PatchMartechListResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    marketing_list: Optional[shared_marketinglist.MarketingList] = dataclasses.field(default=None)
    r"""Successful"""
    

