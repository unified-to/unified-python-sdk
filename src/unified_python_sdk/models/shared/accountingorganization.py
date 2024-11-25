"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .property_accountingorganization_address import (
    PropertyAccountingOrganizationAddress,
    PropertyAccountingOrganizationAddressTypedDict,
)
from datetime import datetime
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class AccountingOrganizationTypedDict(TypedDict):
    name: str
    address: NotRequired[PropertyAccountingOrganizationAddressTypedDict]
    created_at: NotRequired[datetime]
    currency: NotRequired[str]
    fiscal_year_end_month: NotRequired[float]
    id: NotRequired[str]
    legal_name: NotRequired[str]
    organization_code: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    tax_number: NotRequired[str]
    timezone: NotRequired[str]
    updated_at: NotRequired[datetime]
    website: NotRequired[str]


class AccountingOrganization(BaseModel):
    name: str

    address: Optional[PropertyAccountingOrganizationAddress] = None

    created_at: Optional[datetime] = None

    currency: Optional[str] = None

    fiscal_year_end_month: Optional[float] = None

    id: Optional[str] = None

    legal_name: Optional[str] = None

    organization_code: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None

    tax_number: Optional[str] = None

    timezone: Optional[str] = None

    updated_at: Optional[datetime] = None

    website: Optional[str] = None
