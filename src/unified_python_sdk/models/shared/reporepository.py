"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class RepoRepositoryTypedDict(TypedDict):
    name: str
    created_at: NotRequired[datetime]
    description: NotRequired[str]
    id: NotRequired[str]
    is_private: NotRequired[bool]
    org_id: NotRequired[str]
    owner: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    updated_at: NotRequired[datetime]
    web_url: NotRequired[str]


class RepoRepository(BaseModel):
    name: str

    created_at: Optional[datetime] = None

    description: Optional[str] = None

    id: Optional[str] = None

    is_private: Optional[bool] = None

    org_id: Optional[str] = None

    owner: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None

    updated_at: Optional[datetime] = None

    web_url: Optional[str] = None