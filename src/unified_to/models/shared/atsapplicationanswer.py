"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import List
from unified_to import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AtsApplicationAnswer:
    answers: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('answers') }})
    question_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('question_id') }})
    
