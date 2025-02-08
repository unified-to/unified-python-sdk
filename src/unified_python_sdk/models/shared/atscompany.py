"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .property_atscompany_address import (
    PropertyAtsCompanyAddress,
    PropertyAtsCompanyAddressTypedDict,
)
from datetime import datetime
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class AtsCompanyRawTypedDict(TypedDict):
    pass


class AtsCompanyRaw(BaseModel):
    pass


class AtsCompanyTypedDict(TypedDict):
    name: str
    address: NotRequired[PropertyAtsCompanyAddressTypedDict]
    created_at: NotRequired[datetime]
    id: NotRequired[str]
    parent_id: NotRequired[str]
    phone: NotRequired[str]
    raw: NotRequired[AtsCompanyRawTypedDict]
    recruiter_ids: NotRequired[List[str]]
    updated_at: NotRequired[datetime]
    website_url: NotRequired[str]


class AtsCompany(BaseModel):
    name: str

    address: Optional[PropertyAtsCompanyAddress] = None

    created_at: Optional[datetime] = None

    id: Optional[str] = None

    parent_id: Optional[str] = None

    phone: Optional[str] = None

    raw: Optional[AtsCompanyRaw] = None

    recruiter_ids: Optional[List[str]] = None

    updated_at: Optional[datetime] = None

    website_url: Optional[str] = None
