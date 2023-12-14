"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .accountingemail import AccountingEmail
from .accountingtelephone import AccountingTelephone
from .property_accountingcustomer_billing_address import PropertyAccountingCustomerBillingAddress
from .property_accountingcustomer_raw import PropertyAccountingCustomerRaw
from .property_accountingcustomer_shipping_address import PropertyAccountingCustomerShippingAddress
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import List, Optional
from unified_to import utils

class TaxExemption(str, Enum):
    FEDERAL_GOV = 'FEDERAL_GOV'
    REGION_GOV = 'REGION_GOV'
    LOCAL_GOV = 'LOCAL_GOV'
    TRIBAL_GOV = 'TRIBAL_GOV'
    CHARITABLE_ORG = 'CHARITABLE_ORG'
    RELIGIOUS_ORG = 'RELIGIOUS_ORG'
    EDUCATIONAL_ORG = 'EDUCATIONAL_ORG'
    MEDICAL_ORG = 'MEDICAL_ORG'
    RESALE = 'RESALE'
    FOREIGN = 'FOREIGN'
    OTHER = 'OTHER'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountingCustomer:
    billing_address: Optional[PropertyAccountingCustomerBillingAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address'), 'exclude': lambda f: f is None }})
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default='USD', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    emails: Optional[List[AccountingEmail]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emails'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    is_active: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_active'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    raw: Optional[PropertyAccountingCustomerRaw] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw'), 'exclude': lambda f: f is None }})
    shipping_address: Optional[PropertyAccountingCustomerShippingAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipping_address'), 'exclude': lambda f: f is None }})
    tax_exemption: Optional[TaxExemption] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tax_exemption'), 'exclude': lambda f: f is None }})
    tax_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tax_number'), 'exclude': lambda f: f is None }})
    telephones: Optional[List[AccountingTelephone]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('telephones'), 'exclude': lambda f: f is None }})
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    

