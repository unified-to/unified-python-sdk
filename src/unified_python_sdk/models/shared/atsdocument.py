"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class AtsDocumentType(str, Enum):
    RESUME = "RESUME"
    COVER_LETTER = "COVER_LETTER"
    OFFER_PACKET = "OFFER_PACKET"
    OFFER_LETTER = "OFFER_LETTER"
    TAKE_HOME_TEST = "TAKE_HOME_TEST"
    OTHER = "OTHER"


class AtsDocumentTypedDict(TypedDict):
    application_id: NotRequired[str]
    candidate_id: NotRequired[str]
    created_at: NotRequired[datetime]
    document_data: NotRequired[str]
    document_url: NotRequired[str]
    filename: NotRequired[str]
    id: NotRequired[str]
    job_id: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    type: NotRequired[AtsDocumentType]
    updated_at: NotRequired[datetime]
    user_id: NotRequired[str]


class AtsDocument(BaseModel):
    application_id: Optional[str] = None

    candidate_id: Optional[str] = None

    created_at: Optional[datetime] = None

    document_data: Optional[str] = None

    document_url: Optional[str] = None

    filename: Optional[str] = None

    id: Optional[str] = None

    job_id: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None

    type: Optional[AtsDocumentType] = None

    updated_at: Optional[datetime] = None

    user_id: Optional[str] = None
