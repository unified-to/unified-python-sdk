"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import property_ticketingagent_raw as shared_property_ticketingagent_raw
from ..shared import ticketingemail as shared_ticketingemail
from ..shared import ticketingtelephone as shared_ticketingtelephone
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from typing import Optional
from unified_to import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TicketingAgent:
    raw: shared_property_ticketingagent_raw.PropertyTicketingAgentRaw = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw') }})
    created_at: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    emails: Optional[list[shared_ticketingemail.TicketingEmail]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emails'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    telephones: Optional[list[shared_ticketingtelephone.TicketingTelephone]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('telephones'), 'exclude': lambda f: f is None }})
    updated_at: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    

