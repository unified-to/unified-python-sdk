"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import atsapplication as shared_atsapplication
from datetime import datetime
from typing import Optional



@dataclasses.dataclass
class ListAtsApplicationsRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    candidate_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'candidate_id', 'style': 'form', 'explode': True }})
    r"""The candidate ID to filter results"""
    fields_: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'fields', 'style': 'form', 'explode': True }})
    r"""Comma-delimited fields to return"""
    job_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'job_id', 'style': 'form', 'explode': True }})
    r"""The job ID to filter results"""
    limit: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    order: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'order', 'style': 'form', 'explode': True }})
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    r"""Query string to search. eg. email address or name"""
    sort: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sort', 'style': 'form', 'explode': True }})
    updated_gte: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'updated_gte', 'style': 'form', 'explode': True }})
    r"""Return only results whose updated date is equal or greater to this value"""
    




@dataclasses.dataclass
class ListAtsApplicationsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    ats_applications: Optional[list[shared_atsapplication.AtsApplication]] = dataclasses.field(default=None)
    r"""Successful"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

