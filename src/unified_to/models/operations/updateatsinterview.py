"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import atsinterview as shared_atsinterview
from typing import Optional


@dataclasses.dataclass
class UpdateAtsInterviewRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the Interview"""
    ats_interview: Optional[shared_atsinterview.AtsInterview] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""An interview between a candidate for a specific job"""
    



@dataclasses.dataclass
class UpdateAtsInterviewResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    ats_interview: Optional[shared_atsinterview.AtsInterview] = dataclasses.field(default=None)
    r"""Successful"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

