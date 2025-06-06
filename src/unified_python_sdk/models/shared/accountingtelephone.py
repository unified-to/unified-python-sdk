"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class AccountingTelephoneType(str, Enum):
    WORK = "WORK"
    HOME = "HOME"
    OTHER = "OTHER"
    FAX = "FAX"
    MOBILE = "MOBILE"


class AccountingTelephoneTypedDict(TypedDict):
    telephone: NotRequired[str]
    type: NotRequired[AccountingTelephoneType]


class AccountingTelephone(BaseModel):
    telephone: Optional[str] = None

    type: Optional[AccountingTelephoneType] = None
