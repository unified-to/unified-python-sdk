"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .property_atsstatus_raw import PropertyAtsStatusRaw
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from unified_to import utils

class AtsStatusStatus(str, Enum):
    NEW = 'NEW'
    REVIEWING = 'REVIEWING'
    SCREENING = 'SCREENING'
    SUBMITTED = 'SUBMITTED'
    FIRST_INTERVIEW = 'FIRST_INTERVIEW'
    SECOND_INTERVIEW = 'SECOND_INTERVIEW'
    THIRD_INTERVIEW = 'THIRD_INTERVIEW'
    BACKGROUND_CHECK = 'BACKGROUND_CHECK'
    OFFERED = 'OFFERED'
    ACCEPTED = 'ACCEPTED'
    HIRED = 'HIRED'
    REJECTED = 'REJECTED'
    WITHDRAWN = 'WITHDRAWN'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AtsStatus:
    original_status: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('original_status') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    raw: Optional[PropertyAtsStatusRaw] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw'), 'exclude': lambda f: f is None }})
    status: Optional[AtsStatusStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    

