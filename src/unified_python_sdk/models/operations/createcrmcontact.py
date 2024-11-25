"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.models.shared import crmcontact as shared_crmcontact
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)


class CreateCrmContactRequestTypedDict(TypedDict):
    connection_id: str
    r"""ID of the connection"""
    crm_contact: NotRequired[shared_crmcontact.CrmContactTypedDict]
    r"""A contact represents a person that optionally is associated with a deal and/or a company"""
    fields: NotRequired[List[str]]
    r"""Comma-delimited fields to return"""


class CreateCrmContactRequest(BaseModel):
    connection_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the connection"""

    crm_contact: Annotated[
        Optional[shared_crmcontact.CrmContact],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
    r"""A contact represents a person that optionally is associated with a deal and/or a company"""

    fields: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Comma-delimited fields to return"""


class CreateCrmContactResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    crm_contact: NotRequired[shared_crmcontact.CrmContactTypedDict]
    r"""Successful"""


class CreateCrmContactResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    crm_contact: Optional[shared_crmcontact.CrmContact] = None
    r"""Successful"""
