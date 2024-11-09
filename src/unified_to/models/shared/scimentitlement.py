"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from unified_to import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ScimEntitlement:
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    display: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display'), 'exclude': lambda f: f is None }})
    primary: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primary'), 'exclude': lambda f: f is None }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    

