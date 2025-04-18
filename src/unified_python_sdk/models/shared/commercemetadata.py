"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class CommerceMetadataExtraDataTypedDict(TypedDict):
    pass


class CommerceMetadataExtraData(BaseModel):
    pass


class CommerceMetadataValueTypedDict(TypedDict):
    pass


class CommerceMetadataValue(BaseModel):
    pass


class CommerceMetadataTypedDict(TypedDict):
    extra_data: NotRequired[CommerceMetadataExtraDataTypedDict]
    id: NotRequired[str]
    key: NotRequired[str]
    namespace: NotRequired[str]
    slug: NotRequired[str]
    type: NotRequired[str]
    value: NotRequired[CommerceMetadataValueTypedDict]


class CommerceMetadata(BaseModel):
    extra_data: Optional[CommerceMetadataExtraData] = None

    id: Optional[str] = None

    key: Optional[str] = None

    namespace: Optional[str] = None

    slug: Optional[str] = None

    type: Optional[str] = None

    value: Optional[CommerceMetadataValue] = None
