"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .crmmetadata import CrmMetadata, CrmMetadataTypedDict
from datetime import datetime
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class CrmDealTypedDict(TypedDict):
    r"""A deal represents an opportunity with companies and/or contacts"""

    amount: NotRequired[float]
    closed_at: NotRequired[datetime]
    company_ids: NotRequired[List[str]]
    contact_ids: NotRequired[List[str]]
    created_at: NotRequired[datetime]
    currency: NotRequired[str]
    id: NotRequired[str]
    lost_reason: NotRequired[str]
    metadata: NotRequired[List[CrmMetadataTypedDict]]
    name: NotRequired[str]
    pipeline: NotRequired[str]
    pipeline_id: NotRequired[str]
    probability: NotRequired[float]
    raw: NotRequired[Dict[str, Any]]
    source: NotRequired[str]
    stage: NotRequired[str]
    stage_id: NotRequired[str]
    tags: NotRequired[List[str]]
    updated_at: NotRequired[datetime]
    user_id: NotRequired[str]
    won_reason: NotRequired[str]


class CrmDeal(BaseModel):
    r"""A deal represents an opportunity with companies and/or contacts"""

    amount: Optional[float] = None

    closed_at: Optional[datetime] = None

    company_ids: Optional[List[str]] = None

    contact_ids: Optional[List[str]] = None

    created_at: Optional[datetime] = None

    currency: Optional[str] = None

    id: Optional[str] = None

    lost_reason: Optional[str] = None

    metadata: Optional[List[CrmMetadata]] = None

    name: Optional[str] = None

    pipeline: Optional[str] = None

    pipeline_id: Optional[str] = None

    probability: Optional[float] = None

    raw: Optional[Dict[str, Any]] = None

    source: Optional[str] = None

    stage: Optional[str] = None

    stage_id: Optional[str] = None

    tags: Optional[List[str]] = None

    updated_at: Optional[datetime] = None

    user_id: Optional[str] = None

    won_reason: Optional[str] = None
