"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .property_atsjobposting_address import (
    PropertyAtsJobPostingAddress,
    PropertyAtsJobPostingAddressTypedDict,
)
from datetime import datetime
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class AtsJobPostingTypedDict(TypedDict):
    address: NotRequired[PropertyAtsJobPostingAddressTypedDict]
    r"""job-post-specific address"""
    created_at: NotRequired[datetime]
    description: NotRequired[str]
    id: NotRequired[str]
    is_active: NotRequired[bool]
    location: NotRequired[str]
    name: NotRequired[str]
    posting_url: NotRequired[str]
    updated_at: NotRequired[datetime]


class AtsJobPosting(BaseModel):
    address: Optional[PropertyAtsJobPostingAddress] = None
    r"""job-post-specific address"""

    created_at: Optional[datetime] = None

    description: Optional[str] = None

    id: Optional[str] = None

    is_active: Optional[bool] = None

    location: Optional[str] = None

    name: Optional[str] = None

    posting_url: Optional[str] = None

    updated_at: Optional[datetime] = None
