"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import accountingitem as shared_accountingitem
from typing import Optional


@dataclasses.dataclass
class UpdateAccountingItemRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the Item"""
    accounting_item: Optional[shared_accountingitem.AccountingItem] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""An item or product"""
    



@dataclasses.dataclass
class UpdateAccountingItemResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    accounting_item: Optional[shared_accountingitem.AccountingItem] = dataclasses.field(default=None)
    r"""Successful"""
    

