"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class CrmEventFormOptionTypedDict(TypedDict):
    label: NotRequired[str]
    value: NotRequired[str]


class CrmEventFormOption(BaseModel):
    label: Optional[str] = None

    value: Optional[str] = None
