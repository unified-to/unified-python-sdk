"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class AccountingReportType(str, Enum):
    TRIAL_BALANCE = "TRIAL_BALANCE"
    BALANCE_SHEET = "BALANCE_SHEET"
    PROFIT_AND_LOSS = "PROFIT_AND_LOSS"


class AccountingReportTypedDict(TypedDict):
    account_id: NotRequired[str]
    amount: NotRequired[float]
    contact_id: NotRequired[str]
    created_at: NotRequired[datetime]
    group: NotRequired[str]
    id: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    subgroup: NotRequired[str]
    type: NotRequired[AccountingReportType]
    updated_at: NotRequired[datetime]


class AccountingReport(BaseModel):
    account_id: Optional[str] = None

    amount: Optional[float] = None

    contact_id: Optional[str] = None

    created_at: Optional[datetime] = None

    group: Optional[str] = None

    id: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None

    subgroup: Optional[str] = None

    type: Optional[AccountingReportType] = None

    updated_at: Optional[datetime] = None
