"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class CommerceItemMetadataTypedDict(TypedDict):
    key: str
    extra_data: NotRequired[Dict[str, Any]]
    id: NotRequired[str]
    namespace: NotRequired[str]
    type: NotRequired[str]
    value: NotRequired[Dict[str, Any]]


class CommerceItemMetadata(BaseModel):
    key: str

    extra_data: Optional[Dict[str, Any]] = None

    id: Optional[str] = None

    namespace: Optional[str] = None

    type: Optional[str] = None

    value: Optional[Dict[str, Any]] = None
