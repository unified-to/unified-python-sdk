"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import List, Optional
from unified_to import utils

class AtsJobQuestionType(str, Enum):
    TEXT = 'TEXT'
    NUMBER = 'NUMBER'
    DATE = 'DATE'
    BOOLEAN = 'BOOLEAN'
    MULTIPLE_CHOICE = 'MULTIPLE_CHOICE'
    FILE = 'FILE'
    TEXTAREA = 'TEXTAREA'
    MULTIPLE_SELECT = 'MULTIPLE_SELECT'
    UNIVERSITY = 'UNIVERSITY'
    YES_NO = 'YES_NO'
    CURRENCY = 'CURRENCY'
    URL = 'URL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AtsJobQuestion:
    question: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('question') }})
    type: AtsJobQuestionType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    options: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    prompt: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})
    

