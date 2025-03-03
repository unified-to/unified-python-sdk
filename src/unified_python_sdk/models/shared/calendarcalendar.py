"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class CalendarCalendarRawTypedDict(TypedDict):
    pass


class CalendarCalendarRaw(BaseModel):
    pass


class CalendarCalendarTypedDict(TypedDict):
    name: str
    created_at: NotRequired[datetime]
    description: NotRequired[str]
    id: NotRequired[str]
    raw: NotRequired[CalendarCalendarRawTypedDict]
    timezone: NotRequired[str]
    updated_at: NotRequired[datetime]


class CalendarCalendar(BaseModel):
    name: str

    created_at: Optional[datetime] = None

    description: Optional[str] = None

    id: Optional[str] = None

    raw: Optional[CalendarCalendarRaw] = None

    timezone: Optional[str] = None

    updated_at: Optional[datetime] = None
