"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import crmcompany as shared_crmcompany
from typing import Optional


@dataclasses.dataclass
class PatchCrmCompanySecurity:
    jwt: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'authorization' }})
    



@dataclasses.dataclass
class PatchCrmCompanyRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the Company"""
    crm_company: Optional[shared_crmcompany.CrmCompany] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""A company represents an organization that optionally is associated with a deal and/or contacts"""
    



@dataclasses.dataclass
class PatchCrmCompanyResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    crm_company: Optional[shared_crmcompany.CrmCompany] = dataclasses.field(default=None)
    r"""Successful"""
    

