"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.models.shared import crmdeal as shared_crmdeal
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)


class CreateCrmDealRequestTypedDict(TypedDict):
    connection_id: str
    r"""ID of the connection"""
    crm_deal: NotRequired[shared_crmdeal.CrmDealTypedDict]
    r"""A deal represents an opportunity with companies and/or contacts"""
    fields: NotRequired[List[str]]
    r"""Comma-delimited fields to return"""


class CreateCrmDealRequest(BaseModel):
    connection_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the connection"""

    crm_deal: Annotated[
        Optional[shared_crmdeal.CrmDeal],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
    r"""A deal represents an opportunity with companies and/or contacts"""

    fields: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Comma-delimited fields to return"""


class CreateCrmDealResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    crm_deal: NotRequired[shared_crmdeal.CrmDealTypedDict]
    r"""Successful"""


class CreateCrmDealResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    crm_deal: Optional[shared_crmdeal.CrmDeal] = None
    r"""Successful"""
