"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class GetUnifiedIntegrationLoginRequest:
    integration_type: str = dataclasses.field(metadata={'path_param': { 'field_name': 'integration_type', 'style': 'simple', 'explode': False }})
    r"""Type of the supported integration"""
    workspace_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspace_id', 'style': 'simple', 'explode': False }})
    r"""The ID of the workspace"""
    env: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'env', 'style': 'form', 'explode': True }})
    failure_redirect: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'failure_redirect', 'style': 'form', 'explode': True }})
    r"""The URL where you want the user to be redirect to after an unsuccessful authentication. An \\"error\\" variable will be appended."""
    redirect: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'redirect', 'style': 'form', 'explode': True }})
    state: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'state', 'style': 'form', 'explode': True }})
    r"""Extra state to send back to your success URL"""
    success_redirect: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'success_redirect', 'style': 'form', 'explode': True }})
    r"""The URL where you want the user to be redirect to after a successful authentication.  The connection ID will be appended with (id=<connectionId>) to this URL, as will the state that was provided."""
    



@dataclasses.dataclass
class GetUnifiedIntegrationLoginResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    res: Optional[str] = dataclasses.field(default=None)
    r"""Successful"""
    

