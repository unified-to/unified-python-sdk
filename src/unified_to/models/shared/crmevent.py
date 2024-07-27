"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .property_crmevent_call import PropertyCrmEventCall
from .property_crmevent_email import PropertyCrmEventEmail
from .property_crmevent_meeting import PropertyCrmEventMeeting
from .property_crmevent_note import PropertyCrmEventNote
from .property_crmevent_task import PropertyCrmEventTask
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from unified_to import utils


class CrmEventType(str, Enum):
    NOTE = 'NOTE'
    EMAIL = 'EMAIL'
    TASK = 'TASK'
    MEETING = 'MEETING'
    CALL = 'CALL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CrmEvent:
    r"""An event represents an event, activity, or engagement and is always associated with a deal, contact, or company"""
    call: Optional[PropertyCrmEventCall] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('call'), 'exclude': lambda f: f is None }})
    r"""The call object, when type = call"""
    company_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company_ids'), 'exclude': lambda f: f is None }})
    r"""An array of company IDs associated with this event"""
    contact_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contact_ids'), 'exclude': lambda f: f is None }})
    r"""An array of contact IDs associated with this event"""
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    deal_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deal_ids'), 'exclude': lambda f: f is None }})
    r"""An array of deal IDs associated with this event"""
    email: Optional[PropertyCrmEventEmail] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    r"""The email object, when type = email"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    lead_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lead_ids'), 'exclude': lambda f: f is None }})
    meeting: Optional[PropertyCrmEventMeeting] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('meeting'), 'exclude': lambda f: f is None }})
    r"""The meeting object, when type = meeting"""
    note: Optional[PropertyCrmEventNote] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('note'), 'exclude': lambda f: f is None }})
    r"""The note object, when type = note"""
    raw: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw'), 'exclude': lambda f: f is None }})
    r"""The raw data returned by the integration for this event."""
    task: Optional[PropertyCrmEventTask] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('task'), 'exclude': lambda f: f is None }})
    r"""The task object, when type = task"""
    type: Optional[CrmEventType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id'), 'exclude': lambda f: f is None }})
    

