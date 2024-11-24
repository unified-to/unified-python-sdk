"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class KmsPageType(str, Enum):
    HTML = "HTML"
    MARKDOWN = "MARKDOWN"
    TEXT = "TEXT"


class KmsPageTypedDict(TypedDict):
    download_url: str
    space_id: str
    title: str
    type: KmsPageType
    created_at: NotRequired[datetime]
    id: NotRequired[str]
    is_active: NotRequired[bool]
    parent_page_id: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    updated_at: NotRequired[datetime]
    user_id: NotRequired[str]


class KmsPage(BaseModel):
    download_url: str

    space_id: str

    title: str

    type: KmsPageType

    created_at: Optional[datetime] = None

    id: Optional[str] = None

    is_active: Optional[bool] = None

    parent_page_id: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None

    updated_at: Optional[datetime] = None

    user_id: Optional[str] = None
