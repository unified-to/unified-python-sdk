"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class PropertyCalendarEventOrganizerStatus(str, Enum):
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    TENTATIVE = "TENTATIVE"


class PropertyCalendarEventOrganizerTypedDict(TypedDict):
    email: NotRequired[str]
    name: NotRequired[str]
    required: NotRequired[bool]
    status: NotRequired[PropertyCalendarEventOrganizerStatus]
    user_id: NotRequired[str]


class PropertyCalendarEventOrganizer(BaseModel):
    email: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    status: Optional[PropertyCalendarEventOrganizerStatus] = None

    user_id: Optional[str] = None
