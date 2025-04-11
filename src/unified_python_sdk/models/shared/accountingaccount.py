"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class Status(str, Enum):
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"


class Type(str, Enum):
    ACCOUNTS_PAYABLE = "ACCOUNTS_PAYABLE"
    ACCOUNTS_RECEIVABLE = "ACCOUNTS_RECEIVABLE"
    BANK = "BANK"
    CREDIT_CARD = "CREDIT_CARD"
    FIXED_ASSET = "FIXED_ASSET"
    LIABILITY = "LIABILITY"
    EQUITY = "EQUITY"
    EXPENSE = "EXPENSE"
    REVENUE = "REVENUE"
    OTHER = "OTHER"


class AccountingAccountTypedDict(TypedDict):
    r"""Chart of accounts"""

    balance: NotRequired[float]
    created_at: NotRequired[datetime]
    currency: NotRequired[str]
    customer_defined_code: NotRequired[str]
    description: NotRequired[str]
    group: NotRequired[str]
    id: NotRequired[str]
    is_payable: NotRequired[bool]
    name: NotRequired[str]
    parent_account_id: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    section: NotRequired[str]
    status: NotRequired[Status]
    subgroup: NotRequired[str]
    subsection: NotRequired[str]
    type: NotRequired[Type]
    updated_at: NotRequired[datetime]


class AccountingAccount(BaseModel):
    r"""Chart of accounts"""

    balance: Optional[float] = None

    created_at: Optional[datetime] = None

    currency: Optional[str] = None

    customer_defined_code: Optional[str] = None

    description: Optional[str] = None

    group: Optional[str] = None

    id: Optional[str] = None

    is_payable: Optional[bool] = None

    name: Optional[str] = None

    parent_account_id: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None

    section: Optional[str] = None

    status: Optional[Status] = None

    subgroup: Optional[str] = None

    subsection: Optional[str] = None

    type: Optional[Type] = None

    updated_at: Optional[datetime] = None
