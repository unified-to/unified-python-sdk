"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class TaskTaskStatus(str, Enum):
    OPENED = "OPENED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"


class TaskTaskTypedDict(TypedDict):
    assigned_user_ids: NotRequired[List[str]]
    attachment_ids: NotRequired[List[str]]
    r"""Array of attachment IDs retrieved from StorageFile.Get endpoint"""
    completed_at: NotRequired[datetime]
    created_at: NotRequired[datetime]
    creator_user_id: NotRequired[str]
    due_at: NotRequired[datetime]
    follower_user_ids: NotRequired[List[str]]
    group_ids: NotRequired[List[str]]
    id: NotRequired[str]
    name: NotRequired[str]
    notes: NotRequired[str]
    parent_id: NotRequired[str]
    priority: NotRequired[str]
    project_id: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    status: NotRequired[TaskTaskStatus]
    tags: NotRequired[List[str]]
    updated_at: NotRequired[datetime]
    url: NotRequired[str]


class TaskTask(BaseModel):
    assigned_user_ids: Optional[List[str]] = None

    attachment_ids: Optional[List[str]] = None
    r"""Array of attachment IDs retrieved from StorageFile.Get endpoint"""

    completed_at: Optional[datetime] = None

    created_at: Optional[datetime] = None

    creator_user_id: Optional[str] = None

    due_at: Optional[datetime] = None

    follower_user_ids: Optional[List[str]] = None

    group_ids: Optional[List[str]] = None

    id: Optional[str] = None

    name: Optional[str] = None

    notes: Optional[str] = None

    parent_id: Optional[str] = None

    priority: Optional[str] = None

    project_id: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None

    status: Optional[TaskTaskStatus] = None

    tags: Optional[List[str]] = None

    updated_at: Optional[datetime] = None

    url: Optional[str] = None
