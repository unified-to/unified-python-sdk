"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from unified_to import utils

class AccountingContactPaymentMethodType(str, Enum):
    ACH = 'ACH'
    ALIPAY = 'ALIPAY'
    CARD = 'CARD'
    GIROPAY = 'GIROPAY'
    IDEAL = 'IDEAL'
    OTHER = 'OTHER'
    PAYPAL = 'PAYPAL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountingContactPaymentMethod:
    type: AccountingContactPaymentMethodType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    

