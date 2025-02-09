"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .crmemail import CrmEmail, CrmEmailTypedDict
from .crmtelephone import CrmTelephone, CrmTelephoneTypedDict
from .property_crmlead_address import (
    PropertyCrmLeadAddress,
    PropertyCrmLeadAddressTypedDict,
)
from datetime import datetime
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class CrmLeadRawTypedDict(TypedDict):
    pass


class CrmLeadRaw(BaseModel):
    pass


class CrmLeadTypedDict(TypedDict):
    address: NotRequired[PropertyCrmLeadAddressTypedDict]
    company_id: NotRequired[str]
    company_name: NotRequired[str]
    contact_id: NotRequired[str]
    created_at: NotRequired[datetime]
    creator_user_id: NotRequired[str]
    emails: NotRequired[List[CrmEmailTypedDict]]
    id: NotRequired[str]
    is_active: NotRequired[bool]
    link_urls: NotRequired[List[str]]
    name: NotRequired[str]
    raw: NotRequired[CrmLeadRawTypedDict]
    source: NotRequired[str]
    status: NotRequired[str]
    telephones: NotRequired[List[CrmTelephoneTypedDict]]
    updated_at: NotRequired[datetime]
    user_id: NotRequired[str]


class CrmLead(BaseModel):
    address: Optional[PropertyCrmLeadAddress] = None

    company_id: Optional[str] = None

    company_name: Optional[str] = None

    contact_id: Optional[str] = None

    created_at: Optional[datetime] = None

    creator_user_id: Optional[str] = None

    emails: Optional[List[CrmEmail]] = None

    id: Optional[str] = None

    is_active: Optional[bool] = None

    link_urls: Optional[List[str]] = None

    name: Optional[str] = None

    raw: Optional[CrmLeadRaw] = None

    source: Optional[str] = None

    status: Optional[str] = None

    telephones: Optional[List[CrmTelephone]] = None

    updated_at: Optional[datetime] = None

    user_id: Optional[str] = None
