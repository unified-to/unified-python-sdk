"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .property_property_user_urn_ietf_params_scim_schemas_extension_enterprise_2_0_user_manager import PropertyPropertyUserUrnIetfParamsScimSchemasExtensionEnterprise20UserManager
from .undefined import UndefinedT
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import List, Optional
from unified_to import utils


class PropertyUserUrnIetfParamsScimSchemasExtensionEnterprise20UserGender(str, Enum):
    FEMALE = 'female'
    MALE = 'male'


class Level(str, Enum):
    JUNIOR_ENGINEER = 'Junior Engineer'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PropertyUserUrnIetfParamsScimSchemasExtensionEnterprise20User:
    additional_managers: Optional[List[UndefinedT]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additionalManagers'), 'exclude': lambda f: f is None }})
    birthday: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('birthday'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    cost_center: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('costCenter'), 'exclude': lambda f: f is None }})
    department: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('department'), 'exclude': lambda f: f is None }})
    division: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('division'), 'exclude': lambda f: f is None }})
    employee_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('employeeNumber'), 'exclude': lambda f: f is None }})
    end_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('endDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    gender: Optional[PropertyUserUrnIetfParamsScimSchemasExtensionEnterprise20UserGender] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gender'), 'exclude': lambda f: f is None }})
    level: Optional[Level] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('level'), 'exclude': lambda f: f is None }})
    location: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location'), 'exclude': lambda f: f is None }})
    manager: Optional[PropertyPropertyUserUrnIetfParamsScimSchemasExtensionEnterprise20UserManager] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('manager'), 'exclude': lambda f: f is None }})
    organization: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization'), 'exclude': lambda f: f is None }})
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('startDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    
