"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import httpx
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.models.shared import integration as shared_integration
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import FieldMetadata, QueryParamMetadata


class ListUnifiedIntegrationsQueryParamCategories(str, Enum):
    PASSTHROUGH = "passthrough"
    HRIS = "hris"
    ATS = "ats"
    AUTH = "auth"
    CRM = "crm"
    ENRICH = "enrich"
    MARTECH = "martech"
    TICKETING = "ticketing"
    UC = "uc"
    ACCOUNTING = "accounting"
    STORAGE = "storage"
    COMMERCE = "commerce"
    PAYMENT = "payment"
    GENAI = "genai"
    MESSAGING = "messaging"
    KMS = "kms"
    TASK = "task"
    SCIM = "scim"
    LMS = "lms"
    REPO = "repo"
    METADATA = "metadata"
    CALENDAR = "calendar"


class ListUnifiedIntegrationsRequestTypedDict(TypedDict):
    active: NotRequired[bool]
    r"""Filter the results for only the workspace's active integrations"""
    categories: NotRequired[List[ListUnifiedIntegrationsQueryParamCategories]]
    r"""Filter the results on these categories"""
    env: NotRequired[str]
    limit: NotRequired[float]
    offset: NotRequired[float]
    summary: NotRequired[bool]
    type: NotRequired[str]
    r"""Filter the results for only this integration type"""
    updated_gte: NotRequired[str]


class ListUnifiedIntegrationsRequest(BaseModel):
    active: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter the results for only the workspace's active integrations"""

    categories: Annotated[
        Optional[List[ListUnifiedIntegrationsQueryParamCategories]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter the results on these categories"""

    env: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    limit: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    offset: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    summary: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    type: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter the results for only this integration type"""

    updated_gte: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None


class ListUnifiedIntegrationsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    integrations: NotRequired[List[shared_integration.IntegrationTypedDict]]
    r"""Successful"""


class ListUnifiedIntegrationsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    integrations: Optional[List[shared_integration.Integration]] = None
    r"""Successful"""
