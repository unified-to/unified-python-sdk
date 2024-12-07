"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .messagingattachment import MessagingAttachment, MessagingAttachmentTypedDict
from .messagingmember import MessagingMember, MessagingMemberTypedDict
from .property_messagingmessage_author_member import (
    PropertyMessagingMessageAuthorMember,
    PropertyMessagingMessageAuthorMemberTypedDict,
)
from datetime import datetime
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class MessagingMessageTypedDict(TypedDict):
    attachments: NotRequired[List[MessagingAttachmentTypedDict]]
    author_member: NotRequired[PropertyMessagingMessageAuthorMemberTypedDict]
    channel_id: NotRequired[str]
    created_at: NotRequired[datetime]
    destination_members: NotRequired[List[MessagingMemberTypedDict]]
    hidden_members: NotRequired[List[MessagingMemberTypedDict]]
    id: NotRequired[str]
    mentioned_members: NotRequired[List[MessagingMemberTypedDict]]
    message: NotRequired[str]
    message_html: NotRequired[str]
    parent_message_id: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    reference: NotRequired[str]
    root_message_id: NotRequired[str]
    subject: NotRequired[str]
    updated_at: NotRequired[datetime]
    web_url: NotRequired[str]


class MessagingMessage(BaseModel):
    attachments: Optional[List[MessagingAttachment]] = None

    author_member: Optional[PropertyMessagingMessageAuthorMember] = None

    channel_id: Optional[str] = None

    created_at: Optional[datetime] = None

    destination_members: Optional[List[MessagingMember]] = None

    hidden_members: Optional[List[MessagingMember]] = None

    id: Optional[str] = None

    mentioned_members: Optional[List[MessagingMember]] = None

    message: Optional[str] = None

    message_html: Optional[str] = None

    parent_message_id: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None

    reference: Optional[str] = None

    root_message_id: Optional[str] = None

    subject: Optional[str] = None

    updated_at: Optional[datetime] = None

    web_url: Optional[str] = None
