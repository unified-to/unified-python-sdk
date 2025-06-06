"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.models.shared import webhook as shared_webhook
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import FieldMetadata, QueryParamMetadata


class ListUnifiedWebhooksRequestTypedDict(TypedDict):
    connection_id: NotRequired[str]
    r"""Filter the results to just this integration"""
    created_lte: NotRequired[str]
    r"""Return only results whose created date is equal or less to this value"""
    env: NotRequired[str]
    integration_type: NotRequired[str]
    r"""Filter the results to just this integration"""
    limit: NotRequired[float]
    object: NotRequired[str]
    r"""Filter the results for webhooks for only this object"""
    offset: NotRequired[float]
    order: NotRequired[str]
    sort: NotRequired[str]
    updated_gte: NotRequired[str]
    r"""Return only results whose updated date is equal or greater to this value"""


class ListUnifiedWebhooksRequest(BaseModel):
    connection_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter the results to just this integration"""

    created_lte: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Return only results whose created date is equal or less to this value"""

    env: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    integration_type: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter the results to just this integration"""

    limit: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    object: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter the results for webhooks for only this object"""

    offset: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    order: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    sort: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    updated_gte: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Return only results whose updated date is equal or greater to this value"""


class ListUnifiedWebhooksResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    webhooks: NotRequired[List[shared_webhook.WebhookTypedDict]]
    r"""Successful"""


class ListUnifiedWebhooksResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    webhooks: Optional[List[shared_webhook.Webhook]] = None
    r"""Successful"""
