"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .property_integrationsupport_webhook_events_created import (
    PropertyIntegrationSupportWebhookEventsCreated,
)
from .property_integrationsupport_webhook_events_deleted import (
    PropertyIntegrationSupportWebhookEventsDeleted,
)
from .property_integrationsupport_webhook_events_updated import (
    PropertyIntegrationSupportWebhookEventsUpdated,
)
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class PropertyIntegrationSupportWebhookEventsTypedDict(TypedDict):
    created: NotRequired[List[PropertyIntegrationSupportWebhookEventsCreated]]
    deleted: NotRequired[List[PropertyIntegrationSupportWebhookEventsDeleted]]
    updated: NotRequired[List[PropertyIntegrationSupportWebhookEventsUpdated]]


class PropertyIntegrationSupportWebhookEvents(BaseModel):
    created: Optional[List[PropertyIntegrationSupportWebhookEventsCreated]] = None

    deleted: Optional[List[PropertyIntegrationSupportWebhookEventsDeleted]] = None

    updated: Optional[List[PropertyIntegrationSupportWebhookEventsUpdated]] = None
