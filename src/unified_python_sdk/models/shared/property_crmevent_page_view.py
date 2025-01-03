"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class PropertyCrmEventPageViewTypedDict(TypedDict):
    average: NotRequired[float]
    count: NotRequired[float]
    url: NotRequired[str]


class PropertyCrmEventPageView(BaseModel):
    average: Optional[float] = None

    count: Optional[float] = None

    url: Optional[str] = None