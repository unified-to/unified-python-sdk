"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class GenaiModelTypedDict(TypedDict):
    description: NotRequired[str]
    has_temperature: NotRequired[bool]
    id: NotRequired[str]
    max_tokens: NotRequired[float]
    name: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    web_url: NotRequired[str]


class GenaiModel(BaseModel):
    description: Optional[str] = None

    has_temperature: Optional[bool] = None

    id: Optional[str] = None

    max_tokens: Optional[float] = None

    name: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None

    web_url: Optional[str] = None
