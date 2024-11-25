"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class PropertyCrmCompanyAddressTypedDict(TypedDict):
    address1: NotRequired[str]
    address2: NotRequired[str]
    city: NotRequired[str]
    country: NotRequired[str]
    country_code: NotRequired[str]
    postal_code: NotRequired[str]
    region: NotRequired[str]
    region_code: NotRequired[str]


class PropertyCrmCompanyAddress(BaseModel):
    address1: Optional[str] = None

    address2: Optional[str] = None

    city: Optional[str] = None

    country: Optional[str] = None

    country_code: Optional[str] = None

    postal_code: Optional[str] = None

    region: Optional[str] = None

    region_code: Optional[str] = None
