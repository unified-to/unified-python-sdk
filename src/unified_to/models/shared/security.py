"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from typing import Optional


@dataclasses.dataclass
class Security:
    jwt: Optional[str] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'authorization' }})
    

