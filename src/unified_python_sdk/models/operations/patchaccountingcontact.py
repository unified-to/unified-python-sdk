"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.models.shared import (
    accountingcontact as shared_accountingcontact,
)
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)


class PatchAccountingContactRequestTypedDict(TypedDict):
    accounting_contact: shared_accountingcontact.AccountingContactTypedDict
    connection_id: str
    r"""ID of the connection"""
    id: str
    r"""ID of the Contact"""
    fields: NotRequired[List[str]]
    r"""Comma-delimited fields to return"""


class PatchAccountingContactRequest(BaseModel):
    accounting_contact: Annotated[
        shared_accountingcontact.AccountingContact,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    connection_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the connection"""

    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the Contact"""

    fields: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Comma-delimited fields to return"""


class PatchAccountingContactResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    accounting_contact: NotRequired[shared_accountingcontact.AccountingContactTypedDict]
    r"""Successful"""


class PatchAccountingContactResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    accounting_contact: Optional[shared_accountingcontact.AccountingContact] = None
    r"""Successful"""
