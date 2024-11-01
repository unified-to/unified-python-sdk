"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Optional
from unified_to import utils


class PropertyUserUrnIetfParamsScimSchemasExtensionPeakon20UserGender(str, Enum):
    FEMALE = 'Female'
    MALE = 'Male'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PropertyUserUrnIetfParamsScimSchemasExtensionPeakon20User:
    date_of_birth: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Date of Birth'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    gender: Optional[PropertyUserUrnIetfParamsScimSchemasExtensionPeakon20UserGender] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Gender'), 'exclude': lambda f: f is None }})
    manager: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Manager'), 'exclude': lambda f: f is None }})
    team: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Team'), 'exclude': lambda f: f is None }})
    
