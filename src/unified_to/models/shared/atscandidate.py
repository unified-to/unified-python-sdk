"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import atsemail as shared_atsemail
from ..shared import atstelephone as shared_atstelephone
from ..shared import property_atscandidate_address as shared_property_atscandidate_address
from ..shared import property_atscandidate_raw as shared_property_atscandidate_raw
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from typing import Optional
from unified_to import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AtsCandidate:
    r"""A candidate looking for work"""
    address: Optional[shared_property_atscandidate_address.PropertyAtsCandidateAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address'), 'exclude': lambda f: f is None }})
    r"""Unified address object"""
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company_name'), 'exclude': lambda f: f is None }})
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    emails: Optional[list[shared_atsemail.AtsEmail]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emails'), 'exclude': lambda f: f is None }})
    external_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_id'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    image_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('image_url'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    raw: Optional[shared_property_atscandidate_raw.PropertyAtsCandidateRaw] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw'), 'exclude': lambda f: f is None }})
    tags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags'), 'exclude': lambda f: f is None }})
    telephones: Optional[list[shared_atstelephone.AtsTelephone]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('telephones'), 'exclude': lambda f: f is None }})
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    

