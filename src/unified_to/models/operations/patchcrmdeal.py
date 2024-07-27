"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import crmdeal as shared_crmdeal
from typing import Optional


@dataclasses.dataclass
class PatchCrmDealRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the Deal"""
    crm_deal: Optional[shared_crmdeal.CrmDeal] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""A deal represents an opportunity with companies and/or contacts"""
    



@dataclasses.dataclass
class PatchCrmDealResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    crm_deal: Optional[shared_crmdeal.CrmDeal] = dataclasses.field(default=None)
    r"""Successful"""
    

