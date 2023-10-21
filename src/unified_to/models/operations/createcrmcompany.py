"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import crmcompany as shared_crmcompany
from typing import Optional


@dataclasses.dataclass
class CreateCrmCompanyRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    crm_company: Optional[shared_crmcompany.CrmCompany] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""A company represents an organization that optionally is associated with a deal and/or contacts"""
    



@dataclasses.dataclass
class CreateCrmCompanyResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    crm_company: Optional[shared_crmcompany.CrmCompany] = dataclasses.field(default=None)
    r"""Successful"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
