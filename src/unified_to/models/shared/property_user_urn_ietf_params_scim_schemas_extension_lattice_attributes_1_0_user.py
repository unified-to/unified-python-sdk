"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Optional
from unified_to import utils


class Ethnicity(str, Enum):
    CAUCASIAN = 'Caucasian'
    EAST_ASIAN = 'East Asian'
    MIDDLE_EASTERN = 'Middle Eastern'
    WHITE_MIXED = 'White'
    BLACK = 'Black'
    BIRACIAL_SOUTH_ASIAN_AND_CAUCASIAN_ = 'Biracial (South Asian & Caucasian)'
    FILIPINO = 'Filipino'
    SOUTH_ASIAN = 'South Asian'
    INDIAN = 'Indian'
    WHITE_LOWER = 'white'
    ASIAN = 'Asian'


class PropertyUserUrnIetfParamsScimSchemasExtensionLatticeAttributes10UserGender(str, Enum):
    FEMALE = 'female'
    MALE = 'male'


class SexualOrientation(str, Enum):
    QUEER = 'Queer'
    HETEROSEXUAL = 'Heterosexual'
    STRAIGHT_MIXED = 'Straight'
    STRAIGHT_LOWER = 'straight'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PropertyUserUrnIetfParamsScimSchemasExtensionLatticeAttributes10User:
    job_level: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Job Level'), 'exclude': lambda f: f is None }})
    people_manager_reviews: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('People Manager (Reviews)'), 'exclude': lambda f: f is None }})
    remote_work_location: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Remote Work - Location'), 'exclude': lambda f: f is None }})
    salary_information: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Salary Information'), 'exclude': lambda f: f is None }})
    sub_departments: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Sub Departments '), 'exclude': lambda f: f is None }})
    birth_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('birthDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    ethnicity: Optional[Ethnicity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ethnicity'), 'exclude': lambda f: f is None }})
    gender: Optional[PropertyUserUrnIetfParamsScimSchemasExtensionLatticeAttributes10UserGender] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gender'), 'exclude': lambda f: f is None }})
    sexual_orientation: Optional[SexualOrientation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sexualOrientation'), 'exclude': lambda f: f is None }})
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('startDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    
