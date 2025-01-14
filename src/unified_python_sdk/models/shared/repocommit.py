"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class RepoCommitTypedDict(TypedDict):
    repo_id: str
    user_id: str
    branch_id: NotRequired[str]
    created_at: NotRequired[datetime]
    id: NotRequired[str]
    message: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    updated_at: NotRequired[datetime]


class RepoCommit(BaseModel):
    repo_id: str

    user_id: str

    branch_id: Optional[str] = None

    created_at: Optional[datetime] = None

    id: Optional[str] = None

    message: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None

    updated_at: Optional[datetime] = None
