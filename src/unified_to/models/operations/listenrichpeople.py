"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import enrichperson as shared_enrichperson
from typing import Optional


@dataclasses.dataclass
class ListEnrichPeopleRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'company_name', 'style': 'form', 'explode': True }})
    r"""The name of the company the person is associated with.  Not valid by itself."""
    email: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'email', 'style': 'form', 'explode': True }})
    r"""The email of the person to search"""
    linkedin_url: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'linkedin_url', 'style': 'form', 'explode': True }})
    r"""The LinkedIn URL of the person to search"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    r"""The name of the person to search"""
    twitter: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'twitter', 'style': 'form', 'explode': True }})
    r"""The twitter handle of the person to search"""
    



@dataclasses.dataclass
class ListEnrichPeopleResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    enrich_person: Optional[shared_enrichperson.EnrichPerson] = dataclasses.field(default=None)
    r"""Successful"""
    

