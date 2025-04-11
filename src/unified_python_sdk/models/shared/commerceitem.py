"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .commerceitemmedia import CommerceItemMedia, CommerceItemMediaTypedDict
from .commerceitemvariant import CommerceItemVariant, CommerceItemVariantTypedDict
from .commercemetadata import CommerceMetadata, CommerceMetadataTypedDict
from datetime import datetime
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class CommerceItemTypedDict(TypedDict):
    account_id: NotRequired[str]
    collection_ids: NotRequired[List[str]]
    created_at: NotRequired[datetime]
    description: NotRequired[str]
    id: NotRequired[str]
    is_active: NotRequired[bool]
    is_taxable: NotRequired[bool]
    media: NotRequired[List[CommerceItemMediaTypedDict]]
    metadata: NotRequired[List[CommerceMetadataTypedDict]]
    name: NotRequired[str]
    public_description: NotRequired[str]
    public_name: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    slug: NotRequired[str]
    tags: NotRequired[List[str]]
    type: NotRequired[str]
    updated_at: NotRequired[datetime]
    variants: NotRequired[List[CommerceItemVariantTypedDict]]
    r"""first variant is the default variant"""
    vendor_name: NotRequired[str]


class CommerceItem(BaseModel):
    account_id: Optional[str] = None

    collection_ids: Optional[List[str]] = None

    created_at: Optional[datetime] = None

    description: Optional[str] = None

    id: Optional[str] = None

    is_active: Optional[bool] = None

    is_taxable: Optional[bool] = None

    media: Optional[List[CommerceItemMedia]] = None

    metadata: Optional[List[CommerceMetadata]] = None

    name: Optional[str] = None

    public_description: Optional[str] = None

    public_name: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None

    slug: Optional[str] = None

    tags: Optional[List[str]] = None

    type: Optional[str] = None

    updated_at: Optional[datetime] = None

    variants: Optional[List[CommerceItemVariant]] = None
    r"""first variant is the default variant"""

    vendor_name: Optional[str] = None
