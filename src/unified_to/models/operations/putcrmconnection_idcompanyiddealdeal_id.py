"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import crmcompany as shared_crmcompany
from typing import Optional



@dataclasses.dataclass
class PutCrmConnectionIDCompanyIDDealDealIDSecurity:
    jwt: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'authorization' }})
    




@dataclasses.dataclass
class PutCrmConnectionIDCompanyIDDealDealIDRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    deal_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'deal_id', 'style': 'simple', 'explode': False }})
    r"""ID of the deal"""
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the Company"""
    




@dataclasses.dataclass
class PutCrmConnectionIDCompanyIDDealDealIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    crm_company: Optional[shared_crmcompany.CrmCompany] = dataclasses.field(default=None)
    r"""Successful"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

