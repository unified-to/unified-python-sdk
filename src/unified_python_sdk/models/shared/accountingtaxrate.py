"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class AccountingTaxrateRawTypedDict(TypedDict):
    pass


class AccountingTaxrateRaw(BaseModel):
    pass


class AccountingTaxrateTypedDict(TypedDict):
    created_at: NotRequired[datetime]
    description: NotRequired[str]
    id: NotRequired[str]
    is_active: NotRequired[bool]
    name: NotRequired[str]
    rate: NotRequired[float]
    raw: NotRequired[AccountingTaxrateRawTypedDict]
    updated_at: NotRequired[datetime]


class AccountingTaxrate(BaseModel):
    created_at: Optional[datetime] = None

    description: Optional[str] = None

    id: Optional[str] = None

    is_active: Optional[bool] = None

    name: Optional[str] = None

    rate: Optional[float] = None

    raw: Optional[AccountingTaxrateRaw] = None

    updated_at: Optional[datetime] = None
