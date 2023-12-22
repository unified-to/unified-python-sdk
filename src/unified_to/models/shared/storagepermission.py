"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .property_storagepermission_roles import PropertyStoragePermissionRoles
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional
from unified_to import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class StoragePermission:
    roles: List[PropertyStoragePermissionRoles] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('roles') }})
    group_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group_id'), 'exclude': lambda f: f is None }})
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id'), 'exclude': lambda f: f is None }})
    

