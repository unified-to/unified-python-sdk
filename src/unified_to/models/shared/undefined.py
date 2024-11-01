"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from unified_to import utils


class Operation(str, Enum):
    ADD = 'add'
    DELETE = 'delete'


class UndefinedType(str, Enum):
    USER = 'User'
    GROUP = 'Group'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UndefinedT:
    dollar_ref: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('$ref'), 'exclude': lambda f: f is None }})
    display: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display'), 'exclude': lambda f: f is None }})
    operation: Optional[Operation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operation'), 'exclude': lambda f: f is None }})
    type: Optional[UndefinedType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    
