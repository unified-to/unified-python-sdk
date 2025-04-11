"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class HrisTimeoffStatus(str, Enum):
    APPROVED = "APPROVED"
    PENDING = "PENDING"
    DENIED = "DENIED"


class HrisTimeoffType(str, Enum):
    PAID = "PAID"
    UNPAID = "UNPAID"


class HrisTimeoffTypedDict(TypedDict):
    start_at: datetime
    approved_at: NotRequired[datetime]
    approver_user_id: NotRequired[str]
    comments: NotRequired[str]
    company_id: NotRequired[str]
    created_at: NotRequired[datetime]
    end_at: NotRequired[datetime]
    id: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    status: NotRequired[HrisTimeoffStatus]
    type: NotRequired[HrisTimeoffType]
    updated_at: NotRequired[datetime]
    user_id: NotRequired[str]


class HrisTimeoff(BaseModel):
    start_at: datetime

    approved_at: Optional[datetime] = None

    approver_user_id: Optional[str] = None

    comments: Optional[str] = None

    company_id: Optional[str] = None

    created_at: Optional[datetime] = None

    end_at: Optional[datetime] = None

    id: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None

    status: Optional[HrisTimeoffStatus] = None

    type: Optional[HrisTimeoffType] = None

    updated_at: Optional[datetime] = None

    user_id: Optional[str] = None
