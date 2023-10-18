"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from unified_to import utils

class AtsCompensationFrequency(str, Enum):
    ONE_TIME = 'ONE_TIME'
    DAY = 'DAY'
    QUARTER = 'QUARTER'
    YEAR = 'YEAR'
    HOUR = 'HOUR'
    MONTH = 'MONTH'
    WEEK = 'WEEK'

class AtsCompensationType(str, Enum):
    SALARY = 'SALARY'
    BONUS = 'BONUS'
    STOCK_OPTIONS = 'STOCK_OPTIONS'
    EQUITY = 'EQUITY'
    OTHER = 'OTHER'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AtsCompensation:
    type: AtsCompensationType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    frequency: Optional[AtsCompensationFrequency] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('frequency'), 'exclude': lambda f: f is None }})
    max: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max'), 'exclude': lambda f: f is None }})
    min: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('min'), 'exclude': lambda f: f is None }})
    

