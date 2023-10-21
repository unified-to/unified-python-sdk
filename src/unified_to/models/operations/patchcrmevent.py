"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import crmevent as shared_crmevent
from typing import Optional


@dataclasses.dataclass
class PatchCrmEventRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the Event"""
    crm_event: Optional[shared_crmevent.CrmEvent] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""An event represents an event, activity, or engagement and is always associated with a deal, contact, or company"""
    



@dataclasses.dataclass
class PatchCrmEventResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    crm_event: Optional[shared_crmevent.CrmEvent] = dataclasses.field(default=None)
    r"""Successful"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
