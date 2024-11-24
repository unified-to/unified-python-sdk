"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .ucemail import UcEmail, UcEmailTypedDict
from .uctelephone import UcTelephone, UcTelephoneTypedDict
from datetime import datetime
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class UcContactTypedDict(TypedDict):
    r"""A contact represents a person that optionally is associated with a call"""

    company: NotRequired[str]
    created_at: NotRequired[datetime]
    emails: NotRequired[List[UcEmailTypedDict]]
    r"""An array of email addresses for this contact"""
    id: NotRequired[str]
    name: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    r"""The raw data returned by the integration for this contact"""
    telephones: NotRequired[List[UcTelephoneTypedDict]]
    r"""An array of telephones for this contact"""
    title: NotRequired[str]
    updated_at: NotRequired[datetime]


class UcContact(BaseModel):
    r"""A contact represents a person that optionally is associated with a call"""

    company: Optional[str] = None

    created_at: Optional[datetime] = None

    emails: Optional[List[UcEmail]] = None
    r"""An array of email addresses for this contact"""

    id: Optional[str] = None

    name: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None
    r"""The raw data returned by the integration for this contact"""

    telephones: Optional[List[UcTelephone]] = None
    r"""An array of telephones for this contact"""

    title: Optional[str] = None

    updated_at: Optional[datetime] = None