"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import integration as shared_integration
from enum import Enum
from typing import List, Optional

class ListUnifiedIntegrationWorkspacesCategories(str, Enum):
    PASSTHROUGH = 'passthrough'
    HRIS = 'hris'
    ATS = 'ats'
    AUTH = 'auth'
    CRM = 'crm'
    ENRICH = 'enrich'
    MARTECH = 'martech'
    TICKETING = 'ticketing'
    UC = 'uc'


@dataclasses.dataclass
class ListUnifiedIntegrationWorkspacesRequest:
    workspace_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspace_id', 'style': 'simple', 'explode': False }})
    r"""The ID of the workspace"""
    active: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'active', 'style': 'form', 'explode': True }})
    r"""Filter the results for only the workspace's active integrations"""
    categories: Optional[List[ListUnifiedIntegrationWorkspacesCategories]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'categories', 'style': 'form', 'explode': True }})
    r"""Filter the results on these categories"""
    env: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'env', 'style': 'form', 'explode': True }})
    limit: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    summary: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'summary', 'style': 'form', 'explode': True }})
    updated_gte: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'updated_gte', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class ListUnifiedIntegrationWorkspacesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    integrations: Optional[List[shared_integration.Integration]] = dataclasses.field(default=None)
    r"""Successful"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

