"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.models.shared import paymentlink as shared_paymentlink
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)


class UpdatePaymentLinkRequestTypedDict(TypedDict):
    connection_id: str
    r"""ID of the connection"""
    id: str
    r"""ID of the Link"""
    payment_link: NotRequired[shared_paymentlink.PaymentLinkTypedDict]
    fields: NotRequired[List[str]]
    r"""Comma-delimited fields to return"""


class UpdatePaymentLinkRequest(BaseModel):
    connection_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the connection"""

    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the Link"""

    payment_link: Annotated[
        Optional[shared_paymentlink.PaymentLink],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None

    fields: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Comma-delimited fields to return"""


class UpdatePaymentLinkResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    payment_link: NotRequired[shared_paymentlink.PaymentLinkTypedDict]
    r"""Successful"""


class UpdatePaymentLinkResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    payment_link: Optional[shared_paymentlink.PaymentLink] = None
    r"""Successful"""