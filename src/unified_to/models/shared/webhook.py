"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .property_webhook_meta import PropertyWebhookMeta
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import List, Optional
from unified_to import utils

class Event(str, Enum):
    UPDATED = 'updated'
    CREATED = 'created'

class ObjectType(str, Enum):
    ACCOUNTING_ACCOUNT = 'accounting_account'
    ACCOUNTING_TRANSACTION = 'accounting_transaction'
    ACCOUNTING_CONTACT = 'accounting_contact'
    ACCOUNTING_INVOICE = 'accounting_invoice'
    ACCOUNTING_PAYMENT = 'accounting_payment'
    ACCOUNTING_TAXRATE = 'accounting_taxrate'
    ACCOUNTING_ORGANIZATION = 'accounting_organization'
    ACCOUNTING_ITEM = 'accounting_item'
    ATS_APPLICATION = 'ats_application'
    ATS_APPLICATIONSTATUS = 'ats_applicationstatus'
    ATS_CANDIDATE = 'ats_candidate'
    ATS_DOCUMENT = 'ats_document'
    ATS_INTERVIEW = 'ats_interview'
    ATS_JOB = 'ats_job'
    ATS_SCORECARD = 'ats_scorecard'
    CRM_COMPANY = 'crm_company'
    CRM_CONTACT = 'crm_contact'
    CRM_DEAL = 'crm_deal'
    CRM_EVENT = 'crm_event'
    CRM_LEAD = 'crm_lead'
    CRM_PIPELINE = 'crm_pipeline'
    HRIS_EMPLOYEE = 'hris_employee'
    HRIS_GROUP = 'hris_group'
    MARTECH_LIST = 'martech_list'
    MARTECH_MEMBER = 'martech_member'
    PASSTHROUGH = 'passthrough'
    TICKETING_NOTE = 'ticketing_note'
    TICKETING_TICKET = 'ticketing_ticket'
    TICKETING_CUSTOMER = 'ticketing_customer'
    UC_CONTACT = 'uc_contact'
    UC_CALL = 'uc_call'
    ENRICH_PERSON = 'enrich_person'
    ENRICH_COMPANY = 'enrich_company'
    STORAGE_FILE = 'storage_file'

class WebhookWebhookType(str, Enum):
    VIRTUAL = 'virtual'
    NONE = 'none'
    NATIVE = 'native'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Webhook:
    r"""A webhook is used to POST new/updated information to your server."""
    connection_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connection_id') }})
    event: Event = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event') }})
    hook_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hook_url') }})
    interval: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('interval') }})
    object_type: ObjectType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_type') }})
    checked_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('checked_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    environment: Optional[str] = dataclasses.field(default='Production', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment'), 'exclude': lambda f: f is None }})
    fields: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fields'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    integration_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integration_type'), 'exclude': lambda f: f is None }})
    is_healthy: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_healthy'), 'exclude': lambda f: f is None }})
    meta: Optional[PropertyWebhookMeta] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('meta'), 'exclude': lambda f: f is None }})
    runs: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('runs'), 'exclude': lambda f: f is None }})
    r"""An array of the most revent virtual webhook runs"""
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    webhook_type: Optional[WebhookWebhookType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhook_type'), 'exclude': lambda f: f is None }})
    workspace_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspace_id'), 'exclude': lambda f: f is None }})
    

