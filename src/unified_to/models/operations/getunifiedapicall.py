"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apicall as shared_apicall
from datetime import datetime
from typing import Optional



@dataclasses.dataclass
class GetUnifiedApicallRequest:
    connection_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'connection_id', 'style': 'form', 'explode': True }})
    r"""Filter the results to just this integration's API calls"""
    created_lte: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'created_lte', 'style': 'form', 'explode': True }})
    r"""Return only results whose updated date is equal or less to this value"""
    env: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'env', 'style': 'form', 'explode': True }})
    error: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'error', 'style': 'form', 'explode': True }})
    r"""Filter the results for API Calls with errors"""
    external_xref: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'external_xref', 'style': 'form', 'explode': True }})
    r"""Filter the results to only those integrations for your user referenced by this value"""
    integration_type: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'integration_type', 'style': 'form', 'explode': True }})
    r"""Filter the results for connections with this integration"""
    limit: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    order: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'order', 'style': 'form', 'explode': True }})
    sort: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sort', 'style': 'form', 'explode': True }})
    updated_gte: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'updated_gte', 'style': 'form', 'explode': True }})
    r"""Return only results whose updated date is equal or greater to this value"""
    




@dataclasses.dataclass
class GetUnifiedApicallResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_calls: Optional[list[shared_apicall.APICall]] = dataclasses.field(default=None)
    r"""Successful"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

