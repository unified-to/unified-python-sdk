"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .property_webhook_events import PropertyWebhookEvents
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import List, Optional
from unified_to import utils

class ObjectType(str, Enum):
    ACCOUNTING_ACCOUNT = 'accounting_account'
    ACCOUNTING_TRANSACTION = 'accounting_transaction'
    ACCOUNTING_CUSTOMER = 'accounting_customer'
    ACCOUNTING_INVOICE = 'accounting_invoice'
    ACCOUNTING_PAYMENT = 'accounting_payment'
    ATS_APPLICATION = 'ats_application'
    ATS_CANDIDATE = 'ats_candidate'
    ATS_DOCUMENT = 'ats_document'
    ATS_INTERVIEW = 'ats_interview'
    ATS_JOB = 'ats_job'
    ATS_SCORECARD = 'ats_scorecard'
    CRM_COMPANY = 'crm_company'
    CRM_CONTACT = 'crm_contact'
    CRM_DEAL = 'crm_deal'
    CRM_EVENT = 'crm_event'
    CRM_FILE = 'crm_file'
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


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Webhook:
    r"""A webhook is used to POST new/updated information to your server."""
    connection_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connection_id') }})
    events: List[PropertyWebhookEvents] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('events') }})
    hook_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hook_url') }})
    integration_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integration_type') }})
    interval: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('interval') }})
    object_type: ObjectType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_type') }})
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspace_id') }})
    checked_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('checked_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    environment: Optional[str] = dataclasses.field(default='Production', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    include_raw: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_raw'), 'exclude': lambda f: f is None }})
    subscriptions: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subscriptions'), 'exclude': lambda f: f is None }})
    r"""integration-specific subscriptions IDs"""
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    

