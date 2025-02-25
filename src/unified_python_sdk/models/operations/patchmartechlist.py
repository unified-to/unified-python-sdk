"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.models.shared import marketinglist as shared_marketinglist
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)


class PatchMartechListRequestTypedDict(TypedDict):
    marketing_list: shared_marketinglist.MarketingListTypedDict
    r"""Mailing List"""
    connection_id: str
    r"""ID of the connection"""
    id: str
    r"""ID of the List"""
    fields: NotRequired[List[str]]
    r"""Comma-delimited fields to return"""


class PatchMartechListRequest(BaseModel):
    marketing_list: Annotated[
        shared_marketinglist.MarketingList,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
    r"""Mailing List"""

    connection_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the connection"""

    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the List"""

    fields: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Comma-delimited fields to return"""


class PatchMartechListResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    marketing_list: NotRequired[shared_marketinglist.MarketingListTypedDict]
    r"""Successful"""


class PatchMartechListResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    marketing_list: Optional[shared_marketinglist.MarketingList] = None
    r"""Successful"""
