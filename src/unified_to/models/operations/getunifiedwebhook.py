"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import webhook as shared_webhook
from typing import Optional



@dataclasses.dataclass
class GetUnifiedWebhookRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the Webhook"""
    




@dataclasses.dataclass
class GetUnifiedWebhookResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    webhook: Optional[shared_webhook.Webhook] = dataclasses.field(default=None)
    r"""Successful"""
    

