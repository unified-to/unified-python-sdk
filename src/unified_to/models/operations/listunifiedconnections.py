"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import connection as shared_connection
from datetime import datetime
from enum import Enum
from typing import List, Optional

class Categories(str, Enum):
    PASSTHROUGH = 'passthrough'
    HRIS = 'hris'
    ATS = 'ats'
    AUTH = 'auth'
    CRM = 'crm'
    ENRICH = 'enrich'
    MARTECH = 'martech'
    TICKETING = 'ticketing'
    UC = 'uc'
    ACCOUNTING = 'accounting'


@dataclasses.dataclass
class ListUnifiedConnectionsRequest:
    categories: Optional[List[Categories]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'categories', 'style': 'form', 'explode': True }})
    r"""Filter the results on these categories"""
    env: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'env', 'style': 'form', 'explode': True }})
    external_xref: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'external_xref', 'style': 'form', 'explode': True }})
    r"""Filter the results to only those integrations for your user referenced by this value"""
    limit: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    order: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'order', 'style': 'form', 'explode': True }})
    sort: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sort', 'style': 'form', 'explode': True }})
    updated_gte: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'updated_gte', 'style': 'form', 'explode': True }})
    r"""Return only results whose updated date is equal or greater to this value"""
    



@dataclasses.dataclass
class ListUnifiedConnectionsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    connections: Optional[List[shared_connection.Connection]] = dataclasses.field(default=None)
    r"""Successful"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

