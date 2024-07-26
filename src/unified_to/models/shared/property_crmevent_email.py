"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional
from unified_to import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PropertyCrmEventEmail:
    r"""The email object, when type = email"""
    attachment_file_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attachment_file_ids'), 'exclude': lambda f: f is None }})
    body: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('body'), 'exclude': lambda f: f is None }})
    cc: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cc'), 'exclude': lambda f: f is None }})
    r"""The event email's cc name & email (name <test@test.com>)"""
    from_: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from'), 'exclude': lambda f: f is None }})
    subject: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subject'), 'exclude': lambda f: f is None }})
    to: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('to'), 'exclude': lambda f: f is None }})
    r"""The event email's \\"to\\" name & email (name <test@test.com>)"""
    

