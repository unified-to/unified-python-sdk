"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import List, Optional
from unified_to import utils


class IssueStatus(str, Enum):
    COMPLETED = 'COMPLETED'
    NEW = 'NEW'
    ROADMAP = 'ROADMAP'
    IN_PROGRESS = 'IN_PROGRESS'
    ON_HOLD = 'ON_HOLD'
    VALIDATING = 'VALIDATING'
    REJECTED = 'REJECTED'
    UP_NEXT = 'UP_NEXT'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Issue:
    status: IssueStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    ticket_ref: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ticket_ref') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspace_id') }})
    created_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    importance: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('importance'), 'exclude': lambda f: f is None }})
    resolution_time: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resolution_time'), 'exclude': lambda f: f is None }})
    size: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('size'), 'exclude': lambda f: f is None }})
    type: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    updated_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'exclude': lambda f: f is None }})
    url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is None }})
    

