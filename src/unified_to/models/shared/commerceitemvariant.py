"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .commerceitemmedia import CommerceItemMedia
from .commerceitemoption import CommerceItemOption
from .commerceitemprice import CommerceItemPrice
from .commercemetadata import CommerceMetadata
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import List, Optional
from unified_to import utils


class SizeUnit(str, Enum):
    CM = 'cm'
    INCH = 'inch'


class WeightUnit(str, Enum):
    G = 'g'
    KG = 'kg'
    OZ = 'oz'
    LB = 'lb'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CommerceItemVariant:
    available_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('available_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    height: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('height'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    inventory_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('inventory_id'), 'exclude': lambda f: f is None }})
    is_active: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_active'), 'exclude': lambda f: f is None }})
    is_featured: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_featured'), 'exclude': lambda f: f is None }})
    is_visible: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_visible'), 'exclude': lambda f: f is None }})
    length: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('length'), 'exclude': lambda f: f is None }})
    media: Optional[List[CommerceItemMedia]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('media'), 'exclude': lambda f: f is None }})
    metadata: Optional[List[CommerceMetadata]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    options: Optional[List[CommerceItemOption]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    prices: Optional[List[CommerceItemPrice]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prices'), 'exclude': lambda f: f is None }})
    public_description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('public_description'), 'exclude': lambda f: f is None }})
    public_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('public_name'), 'exclude': lambda f: f is None }})
    requires_shipping: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requires_shipping'), 'exclude': lambda f: f is None }})
    size_unit: Optional[SizeUnit] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('size_unit'), 'exclude': lambda f: f is None }})
    sku: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sku'), 'exclude': lambda f: f is None }})
    tags: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags'), 'exclude': lambda f: f is None }})
    total_stock: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_stock'), 'exclude': lambda f: f is None }})
    weight: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weight'), 'exclude': lambda f: f is None }})
    weight_unit: Optional[WeightUnit] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weight_unit'), 'exclude': lambda f: f is None }})
    width: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('width'), 'exclude': lambda f: f is None }})
    

