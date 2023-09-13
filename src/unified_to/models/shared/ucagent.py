"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import property_ucagent_raw as shared_property_ucagent_raw
from ..shared import ucemail as shared_ucemail
from ..shared import uctelephone as shared_uctelephone
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from typing import Optional
from unified_to import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UcAgent:
    r"""Represents an agent"""
    raw: shared_property_ucagent_raw.PropertyUcAgentRaw = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw') }})
    r"""The raw data returned by the integration for this agent"""
    created_at: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    emails: Optional[list[shared_ucemail.UcEmail]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emails'), 'exclude': lambda f: f is None }})
    r"""An array of email addresses for this agent"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    telephones: Optional[list[shared_uctelephone.UcTelephone]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('telephones'), 'exclude': lambda f: f is None }})
    updated_at: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    

