"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import webhook as shared_webhook
from enum import Enum
from typing import Optional

class PostUnifiedWebhookConnectionIDObjectEvents(str, Enum):
    UPDATED = 'updated'
    CREATED = 'created'



@dataclasses.dataclass
class PostUnifiedWebhookConnectionIDObjectRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    object: str = dataclasses.field(metadata={'path_param': { 'field_name': 'object', 'style': 'simple', 'explode': False }})
    r"""The object to subscribe to"""
    events: Optional[list[PostUnifiedWebhookConnectionIDObjectEvents]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'events', 'style': 'form', 'explode': True }})
    r"""Which events to subscribe to."""
    webhook: Optional[shared_webhook.Webhook] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""A webhook is used to POST new/updated information to your server."""
    




@dataclasses.dataclass
class PostUnifiedWebhookConnectionIDObjectResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    webhook: Optional[shared_webhook.Webhook] = dataclasses.field(default=None)
    r"""Successful"""
    

