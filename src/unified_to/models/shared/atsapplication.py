"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import property_atsapplication_raw as shared_property_atsapplication_raw
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Optional
from unified_to import utils

class AtsApplicationStatus(str, Enum):
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


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AtsApplication:
    applied_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('applied_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    candidate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('candidate_id'), 'exclude': lambda f: f is None }})
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    job_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('job_id'), 'exclude': lambda f: f is None }})
    raw: Optional[shared_property_atsapplication_raw.PropertyAtsApplicationRaw] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw'), 'exclude': lambda f: f is None }})
    rejected_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rejected_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    rejected_reason: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rejected_reason'), 'exclude': lambda f: f is None }})
    source: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source'), 'exclude': lambda f: f is None }})
    status: Optional[AtsApplicationStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    

