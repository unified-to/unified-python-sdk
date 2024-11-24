"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class Event(str, Enum):
    UPDATED = "updated"
    CREATED = "created"
    DELETED = "deleted"


class ObjectType(str, Enum):
    ACCOUNTING_ACCOUNT = "accounting_account"
    ACCOUNTING_TRANSACTION = "accounting_transaction"
    ACCOUNTING_JOURNAL = "accounting_journal"
    ACCOUNTING_CONTACT = "accounting_contact"
    ACCOUNTING_INVOICE = "accounting_invoice"
    ACCOUNTING_TAXRATE = "accounting_taxrate"
    ACCOUNTING_ORGANIZATION = "accounting_organization"
    ACCOUNTING_ORDER = "accounting_order"
    PAYMENT_PAYMENT = "payment_payment"
    PAYMENT_LINK = "payment_link"
    PAYMENT_PAYOUT = "payment_payout"
    PAYMENT_REFUND = "payment_refund"
    COMMERCE_ITEM = "commerce_item"
    COMMERCE_COLLECTION = "commerce_collection"
    COMMERCE_INVENTORY = "commerce_inventory"
    COMMERCE_LOCATION = "commerce_location"
    COMMERCE_METADATA = "commerce_metadata"
    ATS_ACTIVITY = "ats_activity"
    ATS_APPLICATION = "ats_application"
    ATS_APPLICATIONSTATUS = "ats_applicationstatus"
    ATS_CANDIDATE = "ats_candidate"
    ATS_DOCUMENT = "ats_document"
    ATS_INTERVIEW = "ats_interview"
    ATS_JOB = "ats_job"
    ATS_SCORECARD = "ats_scorecard"
    ATS_COMPANY = "ats_company"
    CRM_COMPANY = "crm_company"
    CRM_CONTACT = "crm_contact"
    CRM_DEAL = "crm_deal"
    CRM_EVENT = "crm_event"
    CRM_LEAD = "crm_lead"
    CRM_PIPELINE = "crm_pipeline"
    HRIS_EMPLOYEE = "hris_employee"
    HRIS_GROUP = "hris_group"
    HRIS_PAYSLIP = "hris_payslip"
    HRIS_TIMEOFF = "hris_timeoff"
    HRIS_COMPANY = "hris_company"
    HRIS_LOCATION = "hris_location"
    MARTECH_LIST = "martech_list"
    MARTECH_MEMBER = "martech_member"
    PASSTHROUGH = "passthrough"
    TICKETING_NOTE = "ticketing_note"
    TICKETING_TICKET = "ticketing_ticket"
    TICKETING_CUSTOMER = "ticketing_customer"
    UC_CONTACT = "uc_contact"
    UC_CALL = "uc_call"
    ENRICH_PERSON = "enrich_person"
    ENRICH_COMPANY = "enrich_company"
    STORAGE_FILE = "storage_file"
    GENAI_MODEL = "genai_model"
    GENAI_PROMPT = "genai_prompt"
    MESSAGING_MESSAGE = "messaging_message"
    MESSAGING_CHANNEL = "messaging_channel"
    KMS_SPACE = "kms_space"
    KMS_PAGE = "kms_page"
    TASK_PROJECT = "task_project"
    TASK_TASK = "task_task"
    SCIM_USERS = "scim_users"
    SCIM_GROUPS = "scim_groups"
    LMS_COURSE = "lms_course"
    LMS_CLASS = "lms_class"
    LMS_STUDENT = "lms_student"
    LMS_INSTRUCTOR = "lms_instructor"
    REPO_ORGANIZATION = "repo_organization"
    REPO_REPOSITORY = "repo_repository"
    REPO_BRANCH = "repo_branch"
    REPO_COMMIT = "repo_commit"
    REPO_PULLREQUEST = "repo_pullrequest"


class WebhookType(str, Enum):
    VIRTUAL = "virtual"
    NATIVE = "native"


class WebhookTypedDict(TypedDict):
    r"""A webhook is used to POST new/updated information to your server."""

    connection_id: str
    event: Event
    hook_url: str
    object_type: ObjectType
    checked_at: NotRequired[datetime]
    created_at: NotRequired[datetime]
    environment: NotRequired[str]
    fields: NotRequired[str]
    filters: NotRequired[Dict[str, str]]
    id: NotRequired[str]
    integration_type: NotRequired[str]
    interval: NotRequired[float]
    is_healthy: NotRequired[bool]
    meta: NotRequired[Dict[str, Any]]
    page_max_limit: NotRequired[float]
    runs: NotRequired[List[str]]
    r"""An array of the most revent virtual webhook runs"""
    updated_at: NotRequired[datetime]
    webhook_type: NotRequired[WebhookType]
    workspace_id: NotRequired[str]


class Webhook(BaseModel):
    r"""A webhook is used to POST new/updated information to your server."""

    connection_id: str

    event: Event

    hook_url: str

    object_type: ObjectType

    checked_at: Optional[datetime] = None

    created_at: Optional[datetime] = None

    environment: Optional[str] = "Production"

    fields: Optional[str] = None

    filters: Optional[Dict[str, str]] = None

    id: Optional[str] = None

    integration_type: Optional[str] = None

    interval: Optional[float] = None

    is_healthy: Optional[bool] = None

    meta: Optional[Dict[str, Any]] = None

    page_max_limit: Optional[float] = None

    runs: Optional[List[str]] = None
    r"""An array of the most revent virtual webhook runs"""

    updated_at: Optional[datetime] = None

    webhook_type: Optional[WebhookType] = None

    workspace_id: Optional[str] = None