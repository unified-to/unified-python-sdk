"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import commerceinventory as shared_commerceinventory
from typing import Optional


@dataclasses.dataclass
class CreateCommerceInventoryRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    commerce_inventory: Optional[shared_commerceinventory.CommerceInventory] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class CreateCommerceInventoryResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    commerce_inventory: Optional[shared_commerceinventory.CommerceInventory] = dataclasses.field(default=None)
    r"""Successful"""
    

