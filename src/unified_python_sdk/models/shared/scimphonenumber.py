"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class ScimPhoneNumberType(str, Enum):
    WORK = "work"
    HOME = "home"
    OTHER = "other"
    MOBILE = "mobile"
    FAX = "fax"
    PAGER = "pager"


class ScimPhoneNumberTypedDict(TypedDict):
    display: NotRequired[str]
    primary: NotRequired[bool]
    type: NotRequired[ScimPhoneNumberType]
    value: NotRequired[str]


class ScimPhoneNumber(BaseModel):
    display: Optional[str] = None

    primary: Optional[bool] = None

    type: Optional[ScimPhoneNumberType] = None

    value: Optional[str] = None
