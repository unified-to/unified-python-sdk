"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from unified_to import utils


class CrmTelephoneType(str, Enum):
    WORK = 'WORK'
    HOME = 'HOME'
    OTHER = 'OTHER'
    FAX = 'FAX'
    MOBILE = 'MOBILE'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CrmTelephone:
    telephone: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('telephone') }})
    type: Optional[CrmTelephoneType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    

