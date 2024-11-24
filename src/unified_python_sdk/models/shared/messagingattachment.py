"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class MessagingAttachmentTypedDict(TypedDict):
    content_type: NotRequired[str]
    download_url: NotRequired[str]
    filename: NotRequired[str]
    message_id: NotRequired[str]
    size: NotRequired[float]


class MessagingAttachment(BaseModel):
    content_type: Optional[str] = None

    download_url: Optional[str] = None

    filename: Optional[str] = None

    message_id: Optional[str] = None

    size: Optional[float] = None