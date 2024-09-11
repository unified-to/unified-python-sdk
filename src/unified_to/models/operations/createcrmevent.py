"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import crmevent as shared_crmevent
from typing import List, Optional


@dataclasses.dataclass
class CreateCrmEventRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    crm_event: Optional[shared_crmevent.CrmEvent] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""An event represents an event, activity, or engagement and is always associated with a deal, contact, or company"""
    fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'fields', 'style': 'form', 'explode': True }})
    r"""Comma-delimited fields to return"""
    



@dataclasses.dataclass
class CreateCrmEventResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    crm_event: Optional[shared_crmevent.CrmEvent] = dataclasses.field(default=None)
    r"""Successful"""
    

