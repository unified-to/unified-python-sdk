"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import property_integrationsupport_inbound_fields as shared_property_integrationsupport_inbound_fields
from ..shared import property_integrationsupport_outbound_fields as shared_property_integrationsupport_outbound_fields
from ..shared import property_integrationsupport_webhook_events as shared_property_integrationsupport_webhook_events
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Dict, List, Optional
from unified_to import utils

class IntegrationSupportWebhookType(str, Enum):
    VIRTUAL = 'virtual'
    NONE = 'none'
    NATIVE = 'native'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class IntegrationSupport:
    inbound_fields: Optional[shared_property_integrationsupport_inbound_fields.PropertyIntegrationSupportInboundFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('inbound_fields'), 'exclude': lambda f: f is None }})
    list_agent_id: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_agent_id'), 'exclude': lambda f: f is None }})
    list_application_id: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_application_id'), 'exclude': lambda f: f is None }})
    list_candidate_id: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_candidate_id'), 'exclude': lambda f: f is None }})
    list_company_id: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_company_id'), 'exclude': lambda f: f is None }})
    list_contact_id: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_contact_id'), 'exclude': lambda f: f is None }})
    list_customer_id: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_customer_id'), 'exclude': lambda f: f is None }})
    list_deal_id: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_deal_id'), 'exclude': lambda f: f is None }})
    list_invoice_id: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_invoice_id'), 'exclude': lambda f: f is None }})
    list_job_id: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_job_id'), 'exclude': lambda f: f is None }})
    list_limit: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_limit'), 'exclude': lambda f: f is None }})
    list_offset: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_offset'), 'exclude': lambda f: f is None }})
    list_order: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_order'), 'exclude': lambda f: f is None }})
    list_query: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_query'), 'exclude': lambda f: f is None }})
    list_sort_by_created_at: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_sort_by_created_at'), 'exclude': lambda f: f is None }})
    list_sort_by_name: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_sort_by_name'), 'exclude': lambda f: f is None }})
    list_sort_by_updated_at: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_sort_by_updated_at'), 'exclude': lambda f: f is None }})
    list_updated_gte: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_updated_gte'), 'exclude': lambda f: f is None }})
    methods: Optional[Dict[str, bool]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('methods'), 'exclude': lambda f: f is None }})
    outbound_fields: Optional[shared_property_integrationsupport_outbound_fields.PropertyIntegrationSupportOutboundFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('outbound_fields'), 'exclude': lambda f: f is None }})
    search_domain: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_domain'), 'exclude': lambda f: f is None }})
    search_email: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_email'), 'exclude': lambda f: f is None }})
    search_linkedin_url: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_linkedin_url'), 'exclude': lambda f: f is None }})
    search_name: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_name'), 'exclude': lambda f: f is None }})
    search_twitter: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_twitter'), 'exclude': lambda f: f is None }})
    webhook_events: Optional[List[shared_property_integrationsupport_webhook_events.PropertyIntegrationSupportWebhookEvents]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhook_events'), 'exclude': lambda f: f is None }})
    webhook_type: Optional[IntegrationSupportWebhookType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhook_type'), 'exclude': lambda f: f is None }})
    

