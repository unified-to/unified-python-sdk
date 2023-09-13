"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import atsscorecard as shared_atsscorecard
from typing import Optional



@dataclasses.dataclass
class PutAtsConnectionIDScorecardIDSecurity:
    jwt: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'authorization' }})
    




@dataclasses.dataclass
class PutAtsConnectionIDScorecardIDRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the Document"""
    ats_scorecard: Optional[shared_atsscorecard.AtsScorecard] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class PutAtsConnectionIDScorecardIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    ats_scorecard: Optional[shared_atsscorecard.AtsScorecard] = dataclasses.field(default=None)
    r"""Successful"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

