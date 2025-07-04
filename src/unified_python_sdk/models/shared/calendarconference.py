"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class CalendarConferenceTypedDict(TypedDict):
    conference_identifier: NotRequired[str]
    country_code: NotRequired[str]
    host_access_code: NotRequired[str]
    label: NotRequired[str]
    notes: NotRequired[str]
    participant_access_code: NotRequired[str]
    region_code: NotRequired[str]
    telephone: NotRequired[str]
    url: NotRequired[str]


class CalendarConference(BaseModel):
    conference_identifier: Optional[str] = None

    country_code: Optional[str] = None

    host_access_code: Optional[str] = None

    label: Optional[str] = None

    notes: Optional[str] = None

    participant_access_code: Optional[str] = None

    region_code: Optional[str] = None

    telephone: Optional[str] = None

    url: Optional[str] = None
