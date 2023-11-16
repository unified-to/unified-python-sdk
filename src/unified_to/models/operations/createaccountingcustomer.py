"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import accountingcustomer as shared_accountingcustomer
from typing import Optional


@dataclasses.dataclass
class CreateAccountingCustomerRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connection_id', 'style': 'simple', 'explode': False }})
    r"""ID of the connection"""
    accounting_customer: Optional[shared_accountingcustomer.AccountingCustomer] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class CreateAccountingCustomerResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    accounting_customer: Optional[shared_accountingcustomer.AccountingCustomer] = dataclasses.field(default=None)
    r"""Successful"""
    

