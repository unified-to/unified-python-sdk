"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import crmfile as shared_crmfile
from datetime import datetime
from typing import List, Optional


@dataclasses.dataclass
class ListCrmFilesRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    company_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'company_id', 'style': 'form', 'explode': True }})
    r"""The company ID to filter results"""
    contact_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'contact_id', 'style': 'form', 'explode': True }})
    r"""The contact ID to filter results"""
    deal_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'deal_id', 'style': 'form', 'explode': True }})
    r"""The deal ID to filter results"""
    fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'fields', 'style': 'form', 'explode': True }})
    r"""Comma-delimited fields to return"""
    limit: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    order: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'order', 'style': 'form', 'explode': True }})
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    r"""Query string to search. eg. email address or name"""
    sort: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sort', 'style': 'form', 'explode': True }})
    updated_gte: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'updated_gte', 'style': 'form', 'explode': True }})
    r"""Return only results whose updated date is equal or greater to this value"""
    



@dataclasses.dataclass
class ListCrmFilesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    crm_files: Optional[List[shared_crmfile.CrmFile]] = dataclasses.field(default=None)
    r"""Successful"""
    

