"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import crmcompany as shared_crmcompany
from datetime import datetime
from typing import Optional



@dataclasses.dataclass
class GetCrmConnectionIDCompanyRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    contact_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'contact_id', 'style': 'form', 'explode': True }})
    r"""The contact ID to filter results"""
    deal_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'deal_id', 'style': 'form', 'explode': True }})
    r"""The deal ID to filter results"""
    limit: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    order: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'order', 'style': 'form', 'explode': True }})
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    r"""Query string to search. eg. email address or name"""
    sort: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sort', 'style': 'form', 'explode': True }})
    updated_gte: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'updated_gte', 'style': 'form', 'explode': True }})
    r"""Return only results whose updated date is equal or greater to this value"""
    




@dataclasses.dataclass
class GetCrmConnectionIDCompanyResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    crm_companies: Optional[list[shared_crmcompany.CrmCompany]] = dataclasses.field(default=None)
    r"""Successful"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

