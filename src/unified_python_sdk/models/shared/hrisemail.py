"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class HrisEmailType(str, Enum):
    WORK = "WORK"
    HOME = "HOME"
    OTHER = "OTHER"


class HrisEmailTypedDict(TypedDict):
    email: str
    type: NotRequired[HrisEmailType]


class HrisEmail(BaseModel):
    email: str

    type: Optional[HrisEmailType] = None