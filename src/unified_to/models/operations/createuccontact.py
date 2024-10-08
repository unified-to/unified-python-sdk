"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import uccontact as shared_uccontact
from typing import List, Optional


@dataclasses.dataclass
class CreateUcContactRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    uc_contact: Optional[shared_uccontact.UcContact] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""A contact represents a person that optionally is associated with a call"""
    fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'fields', 'style': 'form', 'explode': True }})
    r"""Comma-delimited fields to return"""
    



@dataclasses.dataclass
class CreateUcContactResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    uc_contact: Optional[shared_uccontact.UcContact] = dataclasses.field(default=None)
    r"""Successful"""
    

