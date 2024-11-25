"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .commerceitemmedia import CommerceItemMedia, CommerceItemMediaTypedDict
from .commerceitemmetadata import CommerceItemMetadata, CommerceItemMetadataTypedDict
from .commerceitemoption import CommerceItemOption, CommerceItemOptionTypedDict
from .commerceitemprice import CommerceItemPrice, CommerceItemPriceTypedDict
from datetime import datetime
from enum import Enum
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class SizeUnit(str, Enum):
    CM = "cm"
    INCH = "inch"


class WeightUnit(str, Enum):
    G = "g"
    KG = "kg"
    OZ = "oz"
    LB = "lb"


class CommerceItemVariantTypedDict(TypedDict):
    available_at: NotRequired[datetime]
    description: NotRequired[str]
    height: NotRequired[float]
    id: NotRequired[str]
    inventory_id: NotRequired[str]
    is_active: NotRequired[bool]
    is_featured: NotRequired[bool]
    is_visible: NotRequired[bool]
    length: NotRequired[float]
    media: NotRequired[List[CommerceItemMediaTypedDict]]
    metadata: NotRequired[List[CommerceItemMetadataTypedDict]]
    name: NotRequired[str]
    options: NotRequired[List[CommerceItemOptionTypedDict]]
    prices: NotRequired[List[CommerceItemPriceTypedDict]]
    public_description: NotRequired[str]
    public_name: NotRequired[str]
    requires_shipping: NotRequired[bool]
    size_unit: NotRequired[SizeUnit]
    sku: NotRequired[str]
    tags: NotRequired[List[str]]
    total_stock: NotRequired[float]
    weight: NotRequired[float]
    weight_unit: NotRequired[WeightUnit]
    width: NotRequired[float]


class CommerceItemVariant(BaseModel):
    available_at: Optional[datetime] = None

    description: Optional[str] = None

    height: Optional[float] = None

    id: Optional[str] = None

    inventory_id: Optional[str] = None

    is_active: Optional[bool] = None

    is_featured: Optional[bool] = None

    is_visible: Optional[bool] = None

    length: Optional[float] = None

    media: Optional[List[CommerceItemMedia]] = None

    metadata: Optional[List[CommerceItemMetadata]] = None

    name: Optional[str] = None

    options: Optional[List[CommerceItemOption]] = None

    prices: Optional[List[CommerceItemPrice]] = None

    public_description: Optional[str] = None

    public_name: Optional[str] = None

    requires_shipping: Optional[bool] = None

    size_unit: Optional[SizeUnit] = None

    sku: Optional[str] = None

    tags: Optional[List[str]] = None

    total_stock: Optional[float] = None

    weight: Optional[float] = None

    weight_unit: Optional[WeightUnit] = None

    width: Optional[float] = None
