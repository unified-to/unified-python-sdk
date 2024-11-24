"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from typing import Dict, List
from typing_extensions import Annotated, TypedDict
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import FieldMetadata, PathParamMetadata


class PatchUnifiedWebhookTriggerRequestTypedDict(TypedDict):
    id: str
    r"""ID of the Webhook"""


class PatchUnifiedWebhookTriggerRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the Webhook"""


class PatchUnifiedWebhookTriggerResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    headers: Dict[str, List[str]]
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""


class PatchUnifiedWebhookTriggerResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    headers: Dict[str, List[str]]

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""