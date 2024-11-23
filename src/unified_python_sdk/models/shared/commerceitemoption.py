"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class CommerceItemOptionTypedDict(TypedDict):
    name: str
    values: List[str]
    id: NotRequired[str]
    position: NotRequired[float]


class CommerceItemOption(BaseModel):
    name: str

    values: List[str]

    id: Optional[str] = None

    position: Optional[float] = None
