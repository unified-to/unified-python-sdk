"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import crmevent as shared_crmevent
from typing import Optional


@dataclasses.dataclass
class UpdateCrmEventSecurity:
    jwt: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'authorization' }})
    



@dataclasses.dataclass
class UpdateCrmEventRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the Event"""
    crm_event: Optional[shared_crmevent.CrmEvent] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""An event represents an event, activity, or engagement and is always associated with a deal, contact, or company"""
    



@dataclasses.dataclass
class UpdateCrmEventResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    crm_event: Optional[shared_crmevent.CrmEvent] = dataclasses.field(default=None)
    r"""Successful"""
    

