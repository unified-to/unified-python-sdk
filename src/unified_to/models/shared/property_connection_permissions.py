"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class PropertyConnectionPermissions(str, Enum):
    AUTH_LOGIN = 'auth_login'
    ACCOUNTING_ACCOUNT_READ = 'accounting_account_read'
    ACCOUNTING_ACCOUNT_WRITE = 'accounting_account_write'
    ACCOUNTING_TRANSACTION_READ = 'accounting_transaction_read'
    ACCOUNTING_TRANSACTION_WRITE = 'accounting_transaction_write'
    ACCOUNTING_INVOICE_READ = 'accounting_invoice_read'
    ACCOUNTING_INVOICE_WRITE = 'accounting_invoice_write'
    ACCOUNTING_CUSTOMER_READ = 'accounting_customer_read'
    ACCOUNTING_CUSTOMER_WRITE = 'accounting_customer_write'
    ACCOUNTING_PAYMENT_READ = 'accounting_payment_read'
    ACCOUNTING_PAYMENT_WRITE = 'accounting_payment_write'
    ACCOUNTING_TAXRATE_READ = 'accounting_taxrate_read'
    ACCOUNTING_TAXRATE_WRITE = 'accounting_taxrate_write'
    ACCOUNTING_ORGANIZATION_READ = 'accounting_organization_read'
    ACCOUNTING_ITEM_READ = 'accounting_item_read'
    ATS_SCORECARD_READ = 'ats_scorecard_read'
    ATS_SCORECARD_WRITE = 'ats_scorecard_write'
    ATS_APPLICATION_READ = 'ats_application_read'
    ATS_APPLICATION_WRITE = 'ats_application_write'
    ATS_APPLICATIONSTATUS_READ = 'ats_applicationstatus_read'
    ATS_CANDIDATE_READ = 'ats_candidate_read'
    ATS_CANDIDATE_WRITE = 'ats_candidate_write'
    ATS_INTERVIEW_READ = 'ats_interview_read'
    ATS_INTERVIEW_WRITE = 'ats_interview_write'
    ATS_JOB_READ = 'ats_job_read'
    ATS_JOB_WRITE = 'ats_job_write'
    ATS_DOCUMENT_READ = 'ats_document_read'
    ATS_DOCUMENT_WRITE = 'ats_document_write'
    CRM_COMPANY_READ = 'crm_company_read'
    CRM_COMPANY_WRITE = 'crm_company_write'
    CRM_CONTACT_READ = 'crm_contact_read'
    CRM_CONTACT_WRITE = 'crm_contact_write'
    CRM_DEAL_READ = 'crm_deal_read'
    CRM_DEAL_WRITE = 'crm_deal_write'
    CRM_EVENT_READ = 'crm_event_read'
    CRM_EVENT_WRITE = 'crm_event_write'
    CRM_LEAD_READ = 'crm_lead_read'
    CRM_LEAD_WRITE = 'crm_lead_write'
    CRM_FILE_READ = 'crm_file_read'
    CRM_FILE_WRITE = 'crm_file_write'
    CRM_PIPELINE_READ = 'crm_pipeline_read'
    CRM_PIPELINE_WRITE = 'crm_pipeline_write'
    MARTECH_LIST_READ = 'martech_list_read'
    MARTECH_LIST_WRITE = 'martech_list_write'
    MARTECH_MEMBER_READ = 'martech_member_read'
    MARTECH_MEMBER_WRITE = 'martech_member_write'
    TICKETING_CUSTOMER_READ = 'ticketing_customer_read'
    TICKETING_CUSTOMER_WRITE = 'ticketing_customer_write'
    TICKETING_TICKET_READ = 'ticketing_ticket_read'
    TICKETING_TICKET_WRITE = 'ticketing_ticket_write'
    TICKETING_NOTE_READ = 'ticketing_note_read'
    TICKETING_NOTE_WRITE = 'ticketing_note_write'
    HRIS_EMPLOYEE_READ = 'hris_employee_read'
    HRIS_EMPLOYEE_WRITE = 'hris_employee_write'
    HRIS_GROUP_READ = 'hris_group_read'
    HRIS_GROUP_WRITE = 'hris_group_write'
    UC_CALL_READ = 'uc_call_read'
    STORAGE_FILE_READ = 'storage_file_read'
    STORAGE_FILE_WRITE = 'storage_file_write'
    WEBHOOK = 'webhook'
