"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import httpx
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)


class Scopes(str, Enum):
    AUTH_LOGIN = "auth_login"
    ACCOUNTING_ACCOUNT_READ = "accounting_account_read"
    ACCOUNTING_ACCOUNT_WRITE = "accounting_account_write"
    ACCOUNTING_TRANSACTION_READ = "accounting_transaction_read"
    ACCOUNTING_TRANSACTION_WRITE = "accounting_transaction_write"
    ACCOUNTING_JOURNAL_READ = "accounting_journal_read"
    ACCOUNTING_JOURNAL_WRITE = "accounting_journal_write"
    ACCOUNTING_INVOICE_READ = "accounting_invoice_read"
    ACCOUNTING_INVOICE_WRITE = "accounting_invoice_write"
    ACCOUNTING_CONTACT_READ = "accounting_contact_read"
    ACCOUNTING_CONTACT_WRITE = "accounting_contact_write"
    ACCOUNTING_TAXRATE_READ = "accounting_taxrate_read"
    ACCOUNTING_TAXRATE_WRITE = "accounting_taxrate_write"
    ACCOUNTING_ORGANIZATION_READ = "accounting_organization_read"
    ACCOUNTING_ORDER_READ = "accounting_order_read"
    ACCOUNTING_ORDER_WRITE = "accounting_order_write"
    PAYMENT_PAYMENT_READ = "payment_payment_read"
    PAYMENT_PAYMENT_WRITE = "payment_payment_write"
    PAYMENT_PAYOUT_READ = "payment_payout_read"
    PAYMENT_REFUND_READ = "payment_refund_read"
    PAYMENT_LINK_READ = "payment_link_read"
    PAYMENT_LINK_WRITE = "payment_link_write"
    COMMERCE_ITEM_READ = "commerce_item_read"
    COMMERCE_ITEM_WRITE = "commerce_item_write"
    COMMERCE_COLLECTION_READ = "commerce_collection_read"
    COMMERCE_COLLECTION_WRITE = "commerce_collection_write"
    COMMERCE_INVENTORY_READ = "commerce_inventory_read"
    COMMERCE_INVENTORY_WRITE = "commerce_inventory_write"
    COMMERCE_LOCATION_READ = "commerce_location_read"
    COMMERCE_LOCATION_WRITE = "commerce_location_write"
    COMMERCE_METADATA_READ = "commerce_metadata_read"
    COMMERCE_METADATA_WRITE = "commerce_metadata_write"
    ATS_ACTIVITY_READ = "ats_activity_read"
    ATS_ACTIVITY_WRITE = "ats_activity_write"
    ATS_APPLICATION_READ = "ats_application_read"
    ATS_APPLICATION_WRITE = "ats_application_write"
    ATS_APPLICATIONSTATUS_READ = "ats_applicationstatus_read"
    ATS_CANDIDATE_READ = "ats_candidate_read"
    ATS_CANDIDATE_WRITE = "ats_candidate_write"
    ATS_INTERVIEW_READ = "ats_interview_read"
    ATS_INTERVIEW_WRITE = "ats_interview_write"
    ATS_JOB_READ = "ats_job_read"
    ATS_JOB_WRITE = "ats_job_write"
    ATS_COMPANY_READ = "ats_company_read"
    ATS_DOCUMENT_READ = "ats_document_read"
    ATS_DOCUMENT_WRITE = "ats_document_write"
    ATS_SCORECARD_READ = "ats_scorecard_read"
    ATS_SCORECARD_WRITE = "ats_scorecard_write"
    CRM_COMPANY_READ = "crm_company_read"
    CRM_COMPANY_WRITE = "crm_company_write"
    CRM_CONTACT_READ = "crm_contact_read"
    CRM_CONTACT_WRITE = "crm_contact_write"
    CRM_DEAL_READ = "crm_deal_read"
    CRM_DEAL_WRITE = "crm_deal_write"
    CRM_EVENT_READ = "crm_event_read"
    CRM_EVENT_WRITE = "crm_event_write"
    CRM_LEAD_READ = "crm_lead_read"
    CRM_LEAD_WRITE = "crm_lead_write"
    CRM_PIPELINE_READ = "crm_pipeline_read"
    CRM_PIPELINE_WRITE = "crm_pipeline_write"
    MARTECH_LIST_READ = "martech_list_read"
    MARTECH_LIST_WRITE = "martech_list_write"
    MARTECH_MEMBER_READ = "martech_member_read"
    MARTECH_MEMBER_WRITE = "martech_member_write"
    TICKETING_CUSTOMER_READ = "ticketing_customer_read"
    TICKETING_CUSTOMER_WRITE = "ticketing_customer_write"
    TICKETING_TICKET_READ = "ticketing_ticket_read"
    TICKETING_TICKET_WRITE = "ticketing_ticket_write"
    TICKETING_NOTE_READ = "ticketing_note_read"
    TICKETING_NOTE_WRITE = "ticketing_note_write"
    HRIS_EMPLOYEE_READ = "hris_employee_read"
    HRIS_EMPLOYEE_WRITE = "hris_employee_write"
    HRIS_GROUP_READ = "hris_group_read"
    HRIS_GROUP_WRITE = "hris_group_write"
    HRIS_PAYSLIP_READ = "hris_payslip_read"
    HRIS_PAYSLIP_WRITE = "hris_payslip_write"
    HRIS_TIMEOFF_READ = "hris_timeoff_read"
    HRIS_TIMEOFF_WRITE = "hris_timeoff_write"
    HRIS_COMPANY_READ = "hris_company_read"
    HRIS_COMPANY_WRITE = "hris_company_write"
    HRIS_LOCATION_READ = "hris_location_read"
    HRIS_LOCATION_WRITE = "hris_location_write"
    UC_CALL_READ = "uc_call_read"
    STORAGE_FILE_READ = "storage_file_read"
    STORAGE_FILE_WRITE = "storage_file_write"
    WEBHOOK = "webhook"
    GENAI_MODEL_READ = "genai_model_read"
    GENAI_PROMPT_READ = "genai_prompt_read"
    GENAI_PROMPT_WRITE = "genai_prompt_write"
    MESSAGING_MESSAGE_READ = "messaging_message_read"
    MESSAGING_MESSAGE_WRITE = "messaging_message_write"
    MESSAGING_CHANNEL_READ = "messaging_channel_read"
    KMS_SPACE_READ = "kms_space_read"
    KMS_SPACE_WRITE = "kms_space_write"
    KMS_PAGE_READ = "kms_page_read"
    KMS_PAGE_WRITE = "kms_page_write"
    KMS_COMMENT_READ = "kms_comment_read"
    KMS_COMMENT_WRITE = "kms_comment_write"
    TASK_PROJECT_READ = "task_project_read"
    TASK_PROJECT_WRITE = "task_project_write"
    TASK_TASK_READ = "task_task_read"
    TASK_TASK_WRITE = "task_task_write"
    SCIM_USERS_READ = "scim_users_read"
    SCIM_USERS_WRITE = "scim_users_write"
    SCIM_GROUPS_READ = "scim_groups_read"
    SCIM_GROUPS_WRITE = "scim_groups_write"
    LMS_COURSE_READ = "lms_course_read"
    LMS_COURSE_WRITE = "lms_course_write"
    LMS_CLASS_READ = "lms_class_read"
    LMS_CLASS_WRITE = "lms_class_write"
    LMS_STUDENT_READ = "lms_student_read"
    LMS_STUDENT_WRITE = "lms_student_write"
    LMS_INSTRUCTOR_READ = "lms_instructor_read"
    LMS_INSTRUCTOR_WRITE = "lms_instructor_write"
    REPO_ORGANIZATION_READ = "repo_organization_read"
    REPO_ORGANIZATION_WRITE = "repo_organization_write"
    REPO_REPOSITORY_READ = "repo_repository_read"
    REPO_REPOSITORY_WRITE = "repo_repository_write"
    REPO_BRANCH_READ = "repo_branch_read"
    REPO_BRANCH_WRITE = "repo_branch_write"
    REPO_COMMIT_READ = "repo_commit_read"
    REPO_COMMIT_WRITE = "repo_commit_write"
    REPO_PULLREQUEST_READ = "repo_pullrequest_read"
    REPO_PULLREQUEST_WRITE = "repo_pullrequest_write"


class GetUnifiedIntegrationAuthRequestTypedDict(TypedDict):
    integration_type: str
    r"""Type of the supported integration"""
    workspace_id: str
    r"""The ID of the workspace"""
    env: NotRequired[str]
    external_xref: NotRequired[str]
    r"""Your user identifier to associate with the new Integration"""
    failure_redirect: NotRequired[str]
    r"""The URL where you want the user to be redirect to after an unsuccessful authentication. An \"error\" variable will be appended."""
    lang: NotRequired[str]
    r"""Language: en, fr, es, it, pt, zh, hi"""
    redirect: NotRequired[bool]
    scopes: NotRequired[List[Scopes]]
    state: NotRequired[str]
    r"""Extra state to send back to your success URL"""
    subdomain: NotRequired[str]
    success_redirect: NotRequired[str]
    r"""The URL where you want the user to be redirect to after a successful authorization.  The connection ID will be appended with (id=<connectionId>) to this URL, as will the state that was provided."""


class GetUnifiedIntegrationAuthRequest(BaseModel):
    integration_type: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Type of the supported integration"""

    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the workspace"""

    env: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    external_xref: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Your user identifier to associate with the new Integration"""

    failure_redirect: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The URL where you want the user to be redirect to after an unsuccessful authentication. An \"error\" variable will be appended."""

    lang: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Language: en, fr, es, it, pt, zh, hi"""

    redirect: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    scopes: Annotated[
        Optional[List[Scopes]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    state: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Extra state to send back to your success URL"""

    subdomain: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    success_redirect: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The URL where you want the user to be redirect to after a successful authorization.  The connection ID will be appended with (id=<connectionId>) to this URL, as will the state that was provided."""


class GetUnifiedIntegrationAuthResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    res: NotRequired[str]
    r"""Successful"""


class GetUnifiedIntegrationAuthResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    res: Optional[str] = None
    r"""Successful"""
