"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.models.shared import uccontact as shared_uccontact
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)


class UpdateUcContactRequestTypedDict(TypedDict):
    uc_contact: shared_uccontact.UcContactTypedDict
    r"""A contact represents a person that optionally is associated with a call"""
    connection_id: str
    r"""ID of the connection"""
    id: str
    r"""ID of the Contact"""
    fields: NotRequired[List[str]]
    r"""Comma-delimited fields to return"""


class UpdateUcContactRequest(BaseModel):
    uc_contact: Annotated[
        shared_uccontact.UcContact,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
    r"""A contact represents a person that optionally is associated with a call"""

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


class UpdateUcContactResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    uc_contact: NotRequired[shared_uccontact.UcContactTypedDict]
    r"""Successful"""


class UpdateUcContactResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    uc_contact: Optional[shared_uccontact.UcContact] = None
    r"""Successful"""
