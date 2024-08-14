"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import atsactivity as shared_atsactivity
from datetime import datetime
from typing import List, Optional


@dataclasses.dataclass
class ListAtsActivitiesRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    application_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'application_id', 'style': 'form', 'explode': True }})
    candidate_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'candidate_id', 'style': 'form', 'explode': True }})
    document_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'document_id', 'style': 'form', 'explode': True }})
    fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'fields', 'style': 'form', 'explode': True }})
    r"""Comma-delimited fields to return"""
    interview_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'interview_id', 'style': 'form', 'explode': True }})
    job_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'job_id', 'style': 'form', 'explode': True }})
    limit: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    order: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'order', 'style': 'form', 'explode': True }})
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    r"""Query string to search. eg. email address or name"""
    sort: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sort', 'style': 'form', 'explode': True }})
    updated_gte: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'updated_gte', 'style': 'form', 'explode': True }})
    r"""Return only results whose updated date is equal or greater to this value"""
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'user_id', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class ListAtsActivitiesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    ats_activities: Optional[List[shared_atsactivity.AtsActivity]] = dataclasses.field(default=None)
    r"""Successful"""
    

