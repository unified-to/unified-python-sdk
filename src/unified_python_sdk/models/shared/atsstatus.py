"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class AtsStatusStatus(str, Enum):
    NEW = "NEW"
    REVIEWING = "REVIEWING"
    SCREENING = "SCREENING"
    SUBMITTED = "SUBMITTED"
    FIRST_INTERVIEW = "FIRST_INTERVIEW"
    SECOND_INTERVIEW = "SECOND_INTERVIEW"
    THIRD_INTERVIEW = "THIRD_INTERVIEW"
    BACKGROUND_CHECK = "BACKGROUND_CHECK"
    OFFERED = "OFFERED"
    ACCEPTED = "ACCEPTED"
    HIRED = "HIRED"
    REJECTED = "REJECTED"
    DECLINED = "DECLINED"
    WITHDRAWN = "WITHDRAWN"


class AtsStatusTypedDict(TypedDict):
    description: NotRequired[str]
    id: NotRequired[str]
    original_status: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    status: NotRequired[AtsStatusStatus]


class AtsStatus(BaseModel):
    description: Optional[str] = None

    id: Optional[str] = None

    original_status: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None

    status: Optional[AtsStatusStatus] = None
