"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import ticketingnote as shared_ticketingnote
from typing import List, Optional


@dataclasses.dataclass
class GetTicketingNoteRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the Note"""
    ticket_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ticket_id', 'style': 'simple', 'explode': False }})
    r"""ID of the ticket"""
    fields_: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'fields', 'style': 'form', 'explode': True }})
    r"""Comma-delimited fields to return"""
    



@dataclasses.dataclass
class GetTicketingNoteResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    ticketing_note: Optional[shared_ticketingnote.TicketingNote] = dataclasses.field(default=None)
    r"""Successful"""
    

