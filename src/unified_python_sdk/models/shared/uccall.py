"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .property_uccall_telephone import (
    PropertyUcCallTelephone,
    PropertyUcCallTelephoneTypedDict,
)
from datetime import datetime
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class UcCallTypedDict(TypedDict):
    contact_id: NotRequired[str]
    created_at: NotRequired[datetime]
    end_at: NotRequired[datetime]
    id: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    r"""The raw data returned by the integration for this call"""
    start_at: NotRequired[datetime]
    telephone: NotRequired[PropertyUcCallTelephoneTypedDict]
    r"""The telephone number called"""
    updated_at: NotRequired[datetime]
    user_id: NotRequired[str]


class UcCall(BaseModel):
    contact_id: Optional[str] = None

    created_at: Optional[datetime] = None

    end_at: Optional[datetime] = None

    id: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None
    r"""The raw data returned by the integration for this call"""

    start_at: Optional[datetime] = None

    telephone: Optional[PropertyUcCallTelephone] = None
    r"""The telephone number called"""

    updated_at: Optional[datetime] = None

    user_id: Optional[str] = None
