"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .property_integrationsupport_webhook_events import PropertyIntegrationSupportWebhookEvents
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Dict, List, Optional
from unified_to import utils


class FromWebhook(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListAccountID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListApplicationID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListCandidateID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListChannelID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListClassID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListCollectionID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListCompanyID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListContactID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListCourseID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListCustomerID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListDealID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListInstructorID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListInterviewID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListInvoiceID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListItemID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListItemVariantID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListJobID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListLimit(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListLinkID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListListID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListLocationID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListOffset(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListOrder(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListParentID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListProjectID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListQuery(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListRawFields(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListSortByCreatedAt(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListSortByName(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListSortByUpdatedAt(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListSpaceID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListStudentID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListTicketID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListType(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListUpdatedGte(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class ListUserID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class NativeWebhookParentID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class NativeWebhookProjectID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class SearchDomain(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class SearchEmail(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class SearchLinkedinurl(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class SearchName(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class SearchTwitter(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class VirtualWebhookChannelID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class VirtualWebhookCompanyID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class VirtualWebhookContactID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class VirtualWebhookDealID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class VirtualWebhookLimit(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class VirtualWebhookParentID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class VirtualWebhookTicketID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class VirtualWebhookType(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class VirtualWebhookUpdatedGte(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


class VirtualWebhookUserID(str, Enum):
    SUPPORTED_REQUIRED = 'supported-required'
    SUPPORTED = 'supported'
    NOT_SUPPORTED = 'not-supported'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class IntegrationSupport:
    from_webhook: Optional[FromWebhook] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from_webhook'), 'exclude': lambda f: f is None }})
    inbound_fields: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('inbound_fields'), 'exclude': lambda f: f is None }})
    list_account_id: Optional[ListAccountID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_account_id'), 'exclude': lambda f: f is None }})
    list_application_id: Optional[ListApplicationID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_application_id'), 'exclude': lambda f: f is None }})
    list_candidate_id: Optional[ListCandidateID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_candidate_id'), 'exclude': lambda f: f is None }})
    list_channel_id: Optional[ListChannelID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_channel_id'), 'exclude': lambda f: f is None }})
    list_class_id: Optional[ListClassID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_class_id'), 'exclude': lambda f: f is None }})
    list_collection_id: Optional[ListCollectionID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_collection_id'), 'exclude': lambda f: f is None }})
    list_company_id: Optional[ListCompanyID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_company_id'), 'exclude': lambda f: f is None }})
    list_contact_id: Optional[ListContactID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_contact_id'), 'exclude': lambda f: f is None }})
    list_course_id: Optional[ListCourseID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_course_id'), 'exclude': lambda f: f is None }})
    list_customer_id: Optional[ListCustomerID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_customer_id'), 'exclude': lambda f: f is None }})
    list_deal_id: Optional[ListDealID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_deal_id'), 'exclude': lambda f: f is None }})
    list_instructor_id: Optional[ListInstructorID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_instructor_id'), 'exclude': lambda f: f is None }})
    list_interview_id: Optional[ListInterviewID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_interview_id'), 'exclude': lambda f: f is None }})
    list_invoice_id: Optional[ListInvoiceID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_invoice_id'), 'exclude': lambda f: f is None }})
    list_item_id: Optional[ListItemID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_item_id'), 'exclude': lambda f: f is None }})
    list_item_variant_id: Optional[ListItemVariantID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_item_variant_id'), 'exclude': lambda f: f is None }})
    list_job_id: Optional[ListJobID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_job_id'), 'exclude': lambda f: f is None }})
    list_limit: Optional[ListLimit] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_limit'), 'exclude': lambda f: f is None }})
    list_link_id: Optional[ListLinkID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_link_id'), 'exclude': lambda f: f is None }})
    list_list_id: Optional[ListListID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_list_id'), 'exclude': lambda f: f is None }})
    list_location_id: Optional[ListLocationID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_location_id'), 'exclude': lambda f: f is None }})
    list_offset: Optional[ListOffset] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_offset'), 'exclude': lambda f: f is None }})
    list_order: Optional[ListOrder] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_order'), 'exclude': lambda f: f is None }})
    list_parent_id: Optional[ListParentID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_parent_id'), 'exclude': lambda f: f is None }})
    list_project_id: Optional[ListProjectID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_project_id'), 'exclude': lambda f: f is None }})
    list_query: Optional[ListQuery] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_query'), 'exclude': lambda f: f is None }})
    list_raw_fields: Optional[ListRawFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_raw_fields'), 'exclude': lambda f: f is None }})
    list_sort_by_created_at: Optional[ListSortByCreatedAt] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_sort_by_created_at'), 'exclude': lambda f: f is None }})
    list_sort_by_name: Optional[ListSortByName] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_sort_by_name'), 'exclude': lambda f: f is None }})
    list_sort_by_updated_at: Optional[ListSortByUpdatedAt] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_sort_by_updated_at'), 'exclude': lambda f: f is None }})
    list_space_id: Optional[ListSpaceID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_space_id'), 'exclude': lambda f: f is None }})
    list_student_id: Optional[ListStudentID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_student_id'), 'exclude': lambda f: f is None }})
    list_ticket_id: Optional[ListTicketID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_ticket_id'), 'exclude': lambda f: f is None }})
    list_type: Optional[ListType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_type'), 'exclude': lambda f: f is None }})
    list_updated_gte: Optional[ListUpdatedGte] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_updated_gte'), 'exclude': lambda f: f is None }})
    list_user_id: Optional[ListUserID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_user_id'), 'exclude': lambda f: f is None }})
    methods: Optional[Dict[str, bool]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('methods'), 'exclude': lambda f: f is None }})
    native_webhook_parent_id: Optional[NativeWebhookParentID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('native_webhook_parent_id'), 'exclude': lambda f: f is None }})
    native_webhook_project_id: Optional[NativeWebhookProjectID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('native_webhook_project_id'), 'exclude': lambda f: f is None }})
    outbound_fields: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('outbound_fields'), 'exclude': lambda f: f is None }})
    raw_objects: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw_objects'), 'exclude': lambda f: f is None }})
    r"""objects that we map from in the integration"""
    search_domain: Optional[SearchDomain] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_domain'), 'exclude': lambda f: f is None }})
    search_email: Optional[SearchEmail] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_email'), 'exclude': lambda f: f is None }})
    search_linkedinurl: Optional[SearchLinkedinurl] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_linkedinurl'), 'exclude': lambda f: f is None }})
    search_name: Optional[SearchName] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_name'), 'exclude': lambda f: f is None }})
    search_twitter: Optional[SearchTwitter] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_twitter'), 'exclude': lambda f: f is None }})
    virtual_webhook_channel_id: Optional[VirtualWebhookChannelID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('virtual_webhook_channel_id'), 'exclude': lambda f: f is None }})
    virtual_webhook_company_id: Optional[VirtualWebhookCompanyID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('virtual_webhook_company_id'), 'exclude': lambda f: f is None }})
    virtual_webhook_contact_id: Optional[VirtualWebhookContactID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('virtual_webhook_contact_id'), 'exclude': lambda f: f is None }})
    virtual_webhook_deal_id: Optional[VirtualWebhookDealID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('virtual_webhook_deal_id'), 'exclude': lambda f: f is None }})
    virtual_webhook_limit: Optional[VirtualWebhookLimit] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('virtual_webhook_limit'), 'exclude': lambda f: f is None }})
    virtual_webhook_parent_id: Optional[VirtualWebhookParentID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('virtual_webhook_parent_id'), 'exclude': lambda f: f is None }})
    virtual_webhook_ticket_id: Optional[VirtualWebhookTicketID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('virtual_webhook_ticket_id'), 'exclude': lambda f: f is None }})
    virtual_webhook_type: Optional[VirtualWebhookType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('virtual_webhook_type'), 'exclude': lambda f: f is None }})
    virtual_webhook_updated_gte: Optional[VirtualWebhookUpdatedGte] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('virtual_webhook_updated_gte'), 'exclude': lambda f: f is None }})
    virtual_webhook_user_id: Optional[VirtualWebhookUserID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('virtual_webhook_user_id'), 'exclude': lambda f: f is None }})
    webhook_events: Optional[PropertyIntegrationSupportWebhookEvents] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhook_events'), 'exclude': lambda f: f is None }})
    

