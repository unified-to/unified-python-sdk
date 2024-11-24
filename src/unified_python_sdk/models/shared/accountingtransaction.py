"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountingtransactioncontact import (
    AccountingTransactionContact,
    AccountingTransactionContactTypedDict,
)
from .accountingtransactionlineitem import (
    AccountingTransactionLineItem,
    AccountingTransactionLineItemTypedDict,
)
from datetime import datetime
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class AccountingTransactionTypedDict(TypedDict):
    account_id: NotRequired[str]
    contact_id: NotRequired[str]
    contacts: NotRequired[List[AccountingTransactionContactTypedDict]]
    created_at: NotRequired[datetime]
    currency: NotRequired[str]
    customer_message: NotRequired[str]
    id: NotRequired[str]
    lineitems: NotRequired[List[AccountingTransactionLineItemTypedDict]]
    memo: NotRequired[str]
    payment_method: NotRequired[str]
    payment_terms: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    reference: NotRequired[str]
    split_account_id: NotRequired[str]
    sub_total_amount: NotRequired[float]
    tax_amount: NotRequired[float]
    total_amount: NotRequired[float]
    type: NotRequired[str]
    updated_at: NotRequired[datetime]


class AccountingTransaction(BaseModel):
    account_id: Optional[str] = None

    contact_id: Optional[str] = None

    contacts: Optional[List[AccountingTransactionContact]] = None

    created_at: Optional[datetime] = None

    currency: Optional[str] = None

    customer_message: Optional[str] = None

    id: Optional[str] = None

    lineitems: Optional[List[AccountingTransactionLineItem]] = None

    memo: Optional[str] = None

    payment_method: Optional[str] = None

    payment_terms: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None

    reference: Optional[str] = None

    split_account_id: Optional[str] = None

    sub_total_amount: Optional[float] = None

    tax_amount: Optional[float] = None

    total_amount: Optional[float] = None

    type: Optional[str] = None

    updated_at: Optional[datetime] = None