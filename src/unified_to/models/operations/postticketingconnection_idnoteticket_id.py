"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import ticketingnote as shared_ticketingnote
from typing import Optional



@dataclasses.dataclass
class PostTicketingConnectionIDNoteTicketIDRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    ticket_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ticket_id', 'style': 'simple', 'explode': False }})
    r"""ID of the ticket"""
    ticketing_note: Optional[shared_ticketingnote.TicketingNote] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class PostTicketingConnectionIDNoteTicketIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    ticketing_note: Optional[shared_ticketingnote.TicketingNote] = dataclasses.field(default=None)
    r"""Successful"""
    

