"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.models.shared import (
    accountinginvoice as shared_accountinginvoice,
)
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)


class CreateAccountingInvoiceRequestTypedDict(TypedDict):
    accounting_invoice: shared_accountinginvoice.AccountingInvoiceTypedDict
    connection_id: str
    r"""ID of the connection"""
    fields: NotRequired[List[str]]
    r"""Comma-delimited fields to return"""


class CreateAccountingInvoiceRequest(BaseModel):
    accounting_invoice: Annotated[
        shared_accountinginvoice.AccountingInvoice,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    connection_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the connection"""

    fields: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Comma-delimited fields to return"""


class CreateAccountingInvoiceResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    accounting_invoice: NotRequired[shared_accountinginvoice.AccountingInvoiceTypedDict]
    r"""Successful"""


class CreateAccountingInvoiceResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    accounting_invoice: Optional[shared_accountinginvoice.AccountingInvoice] = None
    r"""Successful"""
