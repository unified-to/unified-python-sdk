"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import crmcontact as shared_crmcontact
from typing import Optional



@dataclasses.dataclass
class PutCrmConnectionIDContactIDDealDealIDRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    deal_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'deal_id', 'style': 'simple', 'explode': False }})
    r"""ID of the deal"""
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the Contact"""
    




@dataclasses.dataclass
class PutCrmConnectionIDContactIDDealDealIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    crm_contact: Optional[shared_crmcontact.CrmContact] = dataclasses.field(default=None)
    r"""Successful"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

