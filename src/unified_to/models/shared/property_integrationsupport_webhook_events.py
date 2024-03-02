"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .property_property_integrationsupport_webhook_events_created import PropertyPropertyIntegrationSupportWebhookEventsCreated
from .property_property_integrationsupport_webhook_events_deleted import PropertyPropertyIntegrationSupportWebhookEventsDeleted
from .property_property_integrationsupport_webhook_events_updated import PropertyPropertyIntegrationSupportWebhookEventsUpdated
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional
from unified_to import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PropertyIntegrationSupportWebhookEvents:
    created: Optional[List[PropertyPropertyIntegrationSupportWebhookEventsCreated]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created'), 'exclude': lambda f: f is None }})
    deleted: Optional[List[PropertyPropertyIntegrationSupportWebhookEventsDeleted]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deleted'), 'exclude': lambda f: f is None }})
    updated: Optional[List[PropertyPropertyIntegrationSupportWebhookEventsUpdated]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated'), 'exclude': lambda f: f is None }})
    

