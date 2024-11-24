"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .lmsemail import LmsEmail, LmsEmailTypedDict
from .lmstelephone import LmsTelephone, LmsTelephoneTypedDict
from .property_lmsstudent_address import (
    PropertyLmsStudentAddress,
    PropertyLmsStudentAddressTypedDict,
)
from datetime import datetime
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class LmsStudentTypedDict(TypedDict):
    address: NotRequired[PropertyLmsStudentAddressTypedDict]
    created_at: NotRequired[datetime]
    emails: NotRequired[List[LmsEmailTypedDict]]
    id: NotRequired[str]
    image_url: NotRequired[str]
    name: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    telephones: NotRequired[List[LmsTelephoneTypedDict]]
    updated_at: NotRequired[datetime]


class LmsStudent(BaseModel):
    address: Optional[PropertyLmsStudentAddress] = None

    created_at: Optional[datetime] = None

    emails: Optional[List[LmsEmail]] = None

    id: Optional[str] = None

    image_url: Optional[str] = None

    name: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None

    telephones: Optional[List[LmsTelephone]] = None

    updated_at: Optional[datetime] = None