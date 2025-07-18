"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from pydantic.functional_validators import PlainValidator
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk import utils
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import validate_open_enum


class DbType(str, Enum, metaclass=utils.OpenEnumMeta):
    MONGODB = "mongodb"
    MYSQL = "mysql"
    POSTGRES = "postgres"
    MSSQL = "mssql"
    MARIADB = "mariadb"


class Event(str, Enum, metaclass=utils.OpenEnumMeta):
    UPDATED = "updated"
    CREATED = "created"
    DELETED = "deleted"


class ObjectType(str, Enum, metaclass=utils.OpenEnumMeta):
    ACCOUNTING_ACCOUNT = "accounting_account"
    ACCOUNTING_TRANSACTION = "accounting_transaction"
    ACCOUNTING_JOURNAL = "accounting_journal"
    ACCOUNTING_CONTACT = "accounting_contact"
    ACCOUNTING_INVOICE = "accounting_invoice"
    ACCOUNTING_BILL = "accounting_bill"
    ACCOUNTING_CREDITMEMO = "accounting_creditmemo"
    ACCOUNTING_TAXRATE = "accounting_taxrate"
    ACCOUNTING_ORGANIZATION = "accounting_organization"
    ACCOUNTING_ORDER = "accounting_order"
    ACCOUNTING_SALESORDER = "accounting_salesorder"
    ACCOUNTING_PURCHASEORDER = "accounting_purchaseorder"
    ACCOUNTING_REPORT = "accounting_report"
    ACCOUNTING_BALANCESHEET = "accounting_balancesheet"
    ACCOUNTING_PROFITLOSS = "accounting_profitloss"
    ACCOUNTING_TRIALBALANCE = "accounting_trialbalance"
    PAYMENT_PAYMENT = "payment_payment"
    PAYMENT_LINK = "payment_link"
    PAYMENT_PAYOUT = "payment_payout"
    PAYMENT_REFUND = "payment_refund"
    PAYMENT_SUBSCRIPTION = "payment_subscription"
    COMMERCE_ITEM = "commerce_item"
    COMMERCE_COLLECTION = "commerce_collection"
    COMMERCE_INVENTORY = "commerce_inventory"
    COMMERCE_LOCATION = "commerce_location"
    COMMERCE_REVIEW = "commerce_review"
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
    HRIS_DEVICE = "hris_device"
    HRIS_TIMESHIFT = "hris_timeshift"
    MARTECH_LIST = "martech_list"
    MARTECH_MEMBER = "martech_member"
    PASSTHROUGH = "passthrough"
    TICKETING_NOTE = "ticketing_note"
    TICKETING_TICKET = "ticketing_ticket"
    TICKETING_CUSTOMER = "ticketing_customer"
    UC_CONTACT = "uc_contact"
    UC_CALL = "uc_call"
    UC_COMMENT = "uc_comment"
    UC_RECORDING = "uc_recording"
    ENRICH_PERSON = "enrich_person"
    ENRICH_COMPANY = "enrich_company"
    STORAGE_FILE = "storage_file"
    GENAI_MODEL = "genai_model"
    GENAI_PROMPT = "genai_prompt"
    MESSAGING_MESSAGE = "messaging_message"
    MESSAGING_CHANNEL = "messaging_channel"
    KMS_SPACE = "kms_space"
    KMS_PAGE = "kms_page"
    KMS_COMMENT = "kms_comment"
    TASK_PROJECT = "task_project"
    TASK_TASK = "task_task"
    TASK_COMMENT = "task_comment"
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
    METADATA_METADATA = "metadata_metadata"
    CALENDAR_CALENDAR = "calendar_calendar"
    CALENDAR_EVENT = "calendar_event"
    CALENDAR_BUSY = "calendar_busy"
    CALENDAR_LINK = "calendar_link"
    CALENDAR_RECORDING = "calendar_recording"


class WebhookType(str, Enum, metaclass=utils.OpenEnumMeta):
    VIRTUAL = "virtual"
    NATIVE = "native"


class WebhookTypedDict(TypedDict):
    r"""A webhook is used to POST new/updated information to your server."""

    connection_id: str
    event: Event
    object_type: ObjectType
    checked_at: NotRequired[datetime]
    created_at: NotRequired[datetime]
    db_name_prefix: NotRequired[str]
    db_type: NotRequired[DbType]
    db_url: NotRequired[str]
    environment: NotRequired[str]
    fields: NotRequired[str]
    filters: NotRequired[Dict[str, Any]]
    hook_url: NotRequired[str]
    id: NotRequired[str]
    integration_type: NotRequired[str]
    interval: NotRequired[float]
    is_healthy: NotRequired[bool]
    is_paused: NotRequired[bool]
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

    event: Annotated[Event, PlainValidator(validate_open_enum(False))]

    object_type: Annotated[ObjectType, PlainValidator(validate_open_enum(False))]

    checked_at: Optional[datetime] = None

    created_at: Optional[datetime] = None

    db_name_prefix: Optional[str] = None

    db_type: Annotated[Optional[DbType], PlainValidator(validate_open_enum(False))] = (
        None
    )

    db_url: Optional[str] = None

    environment: Optional[str] = "Production"

    fields: Optional[str] = None

    filters: Optional[Dict[str, Any]] = None

    hook_url: Optional[str] = None

    id: Optional[str] = None

    integration_type: Optional[str] = None

    interval: Optional[float] = None

    is_healthy: Optional[bool] = None

    is_paused: Optional[bool] = None

    meta: Optional[Dict[str, Any]] = None

    page_max_limit: Optional[float] = None

    runs: Optional[List[str]] = None
    r"""An array of the most revent virtual webhook runs"""

    updated_at: Optional[datetime] = None

    webhook_type: Annotated[
        Optional[WebhookType], PlainValidator(validate_open_enum(False))
    ] = None

    workspace_id: Optional[str] = None
