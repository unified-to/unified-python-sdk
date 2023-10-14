"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import crmdeal as shared_crmdeal
from typing import Optional



@dataclasses.dataclass
class CreateCrmDealRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    crm_deal: Optional[shared_crmdeal.CrmDeal] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""A deal represents an opportunity with companies and/or contacts"""
    fields_: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'fields', 'style': 'form', 'explode': True }})
    r"""Comma-delimited fields to return"""
    




@dataclasses.dataclass
class CreateCrmDealResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    crm_deal: Optional[shared_crmdeal.CrmDeal] = dataclasses.field(default=None)
    r"""Successful"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

