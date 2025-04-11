"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .atscandidateeducation import AtsCandidateEducation, AtsCandidateEducationTypedDict
from .atscandidateexperience import (
    AtsCandidateExperience,
    AtsCandidateExperienceTypedDict,
)
from .atsemail import AtsEmail, AtsEmailTypedDict
from .atsmetadata import AtsMetadata, AtsMetadataTypedDict
from .atstelephone import AtsTelephone, AtsTelephoneTypedDict
from .property_atscandidate_address import (
    PropertyAtsCandidateAddress,
    PropertyAtsCandidateAddressTypedDict,
)
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class Origin(str, Enum):
    AGENCY = "AGENCY"
    APPLIED = "APPLIED"
    INTERNAL = "INTERNAL"
    REFERRED = "REFERRED"
    SOURCED = "SOURCED"
    UNIVERSITY = "UNIVERSITY"


class AtsCandidateTypedDict(TypedDict):
    address: NotRequired[PropertyAtsCandidateAddressTypedDict]
    company_id: NotRequired[str]
    company_name: NotRequired[str]
    created_at: NotRequired[datetime]
    date_of_birth: NotRequired[datetime]
    education: NotRequired[List[AtsCandidateEducationTypedDict]]
    emails: NotRequired[List[AtsEmailTypedDict]]
    experiences: NotRequired[List[AtsCandidateExperienceTypedDict]]
    external_identifier: NotRequired[str]
    id: NotRequired[str]
    image_url: NotRequired[str]
    link_urls: NotRequired[List[str]]
    r"""URLs for web pages containing additional material about the candidate (LinkedIn, other social media, articles, etc.)"""
    metadata: NotRequired[List[AtsMetadataTypedDict]]
    name: NotRequired[str]
    origin: NotRequired[Origin]
    raw: NotRequired[Dict[str, Any]]
    skills: NotRequired[List[str]]
    sources: NotRequired[List[str]]
    tags: NotRequired[List[str]]
    telephones: NotRequired[List[AtsTelephoneTypedDict]]
    title: NotRequired[str]
    updated_at: NotRequired[datetime]
    user_id: NotRequired[str]
    web_url: NotRequired[str]


class AtsCandidate(BaseModel):
    address: Optional[PropertyAtsCandidateAddress] = None

    company_id: Optional[str] = None

    company_name: Optional[str] = None

    created_at: Optional[datetime] = None

    date_of_birth: Optional[datetime] = None

    education: Optional[List[AtsCandidateEducation]] = None

    emails: Optional[List[AtsEmail]] = None

    experiences: Optional[List[AtsCandidateExperience]] = None

    external_identifier: Optional[str] = None

    id: Optional[str] = None

    image_url: Optional[str] = None

    link_urls: Optional[List[str]] = None
    r"""URLs for web pages containing additional material about the candidate (LinkedIn, other social media, articles, etc.)"""

    metadata: Optional[List[AtsMetadata]] = None

    name: Optional[str] = None

    origin: Optional[Origin] = None

    raw: Optional[Dict[str, Any]] = None

    skills: Optional[List[str]] = None

    sources: Optional[List[str]] = None

    tags: Optional[List[str]] = None

    telephones: Optional[List[AtsTelephone]] = None

    title: Optional[str] = None

    updated_at: Optional[datetime] = None

    user_id: Optional[str] = None

    web_url: Optional[str] = None
