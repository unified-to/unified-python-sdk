"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import atscandidate as shared_atscandidate
from typing import Optional



@dataclasses.dataclass
class CreateAtsCandidateRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    ats_candidate: Optional[shared_atscandidate.AtsCandidate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""A candidate looking for work"""
    




@dataclasses.dataclass
class CreateAtsCandidateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    ats_candidate: Optional[shared_atscandidate.AtsCandidate] = dataclasses.field(default=None)
    r"""Successful"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

