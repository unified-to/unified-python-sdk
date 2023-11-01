"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import webhook as shared_webhook
from enum import Enum
from typing import List, Optional

class Events(str, Enum):
    UPDATED = 'updated'
    CREATED = 'created'


@dataclasses.dataclass
class CreateUnifiedWebhookRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    object: str = dataclasses.field(metadata={'path_param': { 'field_name': 'object', 'style': 'simple', 'explode': False }})
    r"""The object to subscribe to"""
    events: Optional[List[Events]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'events', 'style': 'form', 'explode': True }})
    r"""Which events to subscribe to."""
    webhook: Optional[shared_webhook.Webhook] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class CreateUnifiedWebhookResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    webhook: Optional[shared_webhook.Webhook] = dataclasses.field(default=None)
    r"""Successful"""
    

