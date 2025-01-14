"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class Priority(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class PropertyCrmEventTaskStatus(str, Enum):
    COMPLETED = "COMPLETED"
    NOT_STARTED = "NOT_STARTED"
    WORK_IN_PROGRESS = "WORK_IN_PROGRESS"
    DEFERRED = "DEFERRED"


class PropertyCrmEventTaskTypedDict(TypedDict):
    r"""The task object, when type = task"""

    description: NotRequired[str]
    due_at: NotRequired[datetime]
    name: NotRequired[str]
    priority: NotRequired[Priority]
    status: NotRequired[PropertyCrmEventTaskStatus]


class PropertyCrmEventTask(BaseModel):
    r"""The task object, when type = task"""

    description: Optional[str] = None

    due_at: Optional[datetime] = None

    name: Optional[str] = None

    priority: Optional[Priority] = None

    status: Optional[PropertyCrmEventTaskStatus] = None
