"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.models.shared import webhook as shared_webhook
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata


class UpdateUnifiedWebhookRequestTypedDict(TypedDict):
    id: str
    r"""ID of the Webhook"""
    webhook: NotRequired[shared_webhook.WebhookTypedDict]
    r"""A webhook is used to POST new/updated information to your server."""


class UpdateUnifiedWebhookRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the Webhook"""

    webhook: Annotated[
        Optional[shared_webhook.Webhook],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
    r"""A webhook is used to POST new/updated information to your server."""


class UpdateUnifiedWebhookResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    webhook: NotRequired[shared_webhook.WebhookTypedDict]
    r"""Successful"""


class UpdateUnifiedWebhookResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    webhook: Optional[shared_webhook.Webhook] = None
    r"""Successful"""
