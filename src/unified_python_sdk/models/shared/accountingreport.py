"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .property_accountingreport_balance_sheet import (
    PropertyAccountingReportBalanceSheet,
    PropertyAccountingReportBalanceSheetTypedDict,
)
from .property_accountingreport_profit_and_loss import (
    PropertyAccountingReportProfitAndLoss,
    PropertyAccountingReportProfitAndLossTypedDict,
)
from .property_accountingreport_trial_balance import (
    PropertyAccountingReportTrialBalance,
    PropertyAccountingReportTrialBalanceTypedDict,
)
from datetime import datetime
from enum import Enum
from pydantic.functional_validators import PlainValidator
from typing import Any, Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk import utils
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import validate_open_enum


class AccountingReportType(str, Enum, metaclass=utils.OpenEnumMeta):
    TRIAL_BALANCE = "TRIAL_BALANCE"
    BALANCE_SHEET = "BALANCE_SHEET"
    PROFIT_AND_LOSS = "PROFIT_AND_LOSS"


class AccountingReportTypedDict(TypedDict):
    balance_sheet: NotRequired[PropertyAccountingReportBalanceSheetTypedDict]
    created_at: NotRequired[datetime]
    currency: NotRequired[str]
    end_at: NotRequired[datetime]
    id: NotRequired[str]
    name: NotRequired[str]
    profit_and_loss: NotRequired[PropertyAccountingReportProfitAndLossTypedDict]
    raw: NotRequired[Dict[str, Any]]
    start_at: NotRequired[datetime]
    trial_balance: NotRequired[PropertyAccountingReportTrialBalanceTypedDict]
    type: NotRequired[AccountingReportType]
    updated_at: NotRequired[datetime]


class AccountingReport(BaseModel):
    balance_sheet: Optional[PropertyAccountingReportBalanceSheet] = None

    created_at: Optional[datetime] = None

    currency: Optional[str] = None

    end_at: Optional[datetime] = None

    id: Optional[str] = None

    name: Optional[str] = None

    profit_and_loss: Optional[PropertyAccountingReportProfitAndLoss] = None

    raw: Optional[Dict[str, Any]] = None

    start_at: Optional[datetime] = None

    trial_balance: Optional[PropertyAccountingReportTrialBalance] = None

    type: Annotated[
        Optional[AccountingReportType], PlainValidator(validate_open_enum(False))
    ] = None

    updated_at: Optional[datetime] = None
