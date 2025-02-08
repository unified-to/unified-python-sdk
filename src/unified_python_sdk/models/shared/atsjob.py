"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .atsaddress import AtsAddress, AtsAddressTypedDict
from .atscompensation import AtsCompensation, AtsCompensationTypedDict
from .atsjobposting import AtsJobPosting, AtsJobPostingTypedDict
from .atsjobquestion import AtsJobQuestion, AtsJobQuestionTypedDict
from datetime import datetime
from enum import Enum
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class EmploymentType(str, Enum):
    FULL_TIME = "FULL_TIME"
    PART_TIME = "PART_TIME"
    CONTRACTOR = "CONTRACTOR"
    INTERN = "INTERN"
    CONSULTANT = "CONSULTANT"
    VOLUNTEER = "VOLUNTEER"
    CASUAL = "CASUAL"
    SEASONAL = "SEASONAL"
    FREELANCE = "FREELANCE"
    OTHER = "OTHER"


class AtsJobRawTypedDict(TypedDict):
    pass


class AtsJobRaw(BaseModel):
    pass


class AtsJobStatus(str, Enum):
    ARCHIVED = "ARCHIVED"
    PENDING = "PENDING"
    DRAFT = "DRAFT"
    OPEN = "OPEN"
    CLOSED = "CLOSED"


class AtsJobTypedDict(TypedDict):
    addresses: NotRequired[List[AtsAddressTypedDict]]
    closed_at: NotRequired[datetime]
    company_id: NotRequired[str]
    compensation: NotRequired[List[AtsCompensationTypedDict]]
    created_at: NotRequired[datetime]
    departments: NotRequired[List[str]]
    r"""The names of the departments/divisions that this job belongs to"""
    description: NotRequired[str]
    employment_type: NotRequired[EmploymentType]
    hiring_manager_ids: NotRequired[List[str]]
    id: NotRequired[str]
    language_locale: NotRequired[str]
    name: NotRequired[str]
    number_of_openings: NotRequired[float]
    postings: NotRequired[List[AtsJobPostingTypedDict]]
    r"""Public job postings"""
    public_job_urls: NotRequired[List[str]]
    r"""URLs for pages containing public listings for the job"""
    questions: NotRequired[List[AtsJobQuestionTypedDict]]
    raw: NotRequired[AtsJobRawTypedDict]
    recruiter_ids: NotRequired[List[str]]
    remote: NotRequired[bool]
    status: NotRequired[AtsJobStatus]
    updated_at: NotRequired[datetime]


class AtsJob(BaseModel):
    addresses: Optional[List[AtsAddress]] = None

    closed_at: Optional[datetime] = None

    company_id: Optional[str] = None

    compensation: Optional[List[AtsCompensation]] = None

    created_at: Optional[datetime] = None

    departments: Optional[List[str]] = None
    r"""The names of the departments/divisions that this job belongs to"""

    description: Optional[str] = None

    employment_type: Optional[EmploymentType] = None

    hiring_manager_ids: Optional[List[str]] = None

    id: Optional[str] = None

    language_locale: Optional[str] = None

    name: Optional[str] = None

    number_of_openings: Optional[float] = None

    postings: Optional[List[AtsJobPosting]] = None
    r"""Public job postings"""

    public_job_urls: Optional[List[str]] = None
    r"""URLs for pages containing public listings for the job"""

    questions: Optional[List[AtsJobQuestion]] = None

    raw: Optional[AtsJobRaw] = None

    recruiter_ids: Optional[List[str]] = None

    remote: Optional[bool] = None

    status: Optional[AtsJobStatus] = None

    updated_at: Optional[datetime] = None
