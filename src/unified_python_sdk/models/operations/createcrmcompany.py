"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.models.shared import crmcompany as shared_crmcompany
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)


class CreateCrmCompanyRequestTypedDict(TypedDict):
    connection_id: str
    r"""ID of the connection"""
    crm_company: NotRequired[shared_crmcompany.CrmCompanyTypedDict]
    r"""A company represents an organization that optionally is associated with a deal and/or contacts"""
    fields: NotRequired[List[str]]
    r"""Comma-delimited fields to return"""


class CreateCrmCompanyRequest(BaseModel):
    connection_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the connection"""

    crm_company: Annotated[
        Optional[shared_crmcompany.CrmCompany],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
    r"""A company represents an organization that optionally is associated with a deal and/or contacts"""

    fields: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Comma-delimited fields to return"""


class CreateCrmCompanyResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    crm_company: NotRequired[shared_crmcompany.CrmCompanyTypedDict]
    r"""Successful"""


class CreateCrmCompanyResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    crm_company: Optional[shared_crmcompany.CrmCompany] = None
    r"""Successful"""
