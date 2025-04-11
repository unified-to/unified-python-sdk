"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .atsscorecardquestion import AtsScorecardQuestion, AtsScorecardQuestionTypedDict
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class Recommendation(str, Enum):
    DEFINITELY_NO = "DEFINITELY_NO"
    NO = "NO"
    YES = "YES"
    STRONG_YES = "STRONG_YES"


class AtsScorecardTypedDict(TypedDict):
    application_id: NotRequired[str]
    candidate_id: NotRequired[str]
    comment: NotRequired[str]
    created_at: NotRequired[datetime]
    id: NotRequired[str]
    interview_id: NotRequired[str]
    interviewer_id: NotRequired[str]
    job_id: NotRequired[str]
    questions: NotRequired[List[AtsScorecardQuestionTypedDict]]
    raw: NotRequired[Dict[str, Any]]
    recommendation: NotRequired[Recommendation]
    updated_at: NotRequired[datetime]


class AtsScorecard(BaseModel):
    application_id: Optional[str] = None

    candidate_id: Optional[str] = None

    comment: Optional[str] = None

    created_at: Optional[datetime] = None

    id: Optional[str] = None

    interview_id: Optional[str] = None

    interviewer_id: Optional[str] = None

    job_id: Optional[str] = None

    questions: Optional[List[AtsScorecardQuestion]] = None

    raw: Optional[Dict[str, Any]] = None

    recommendation: Optional[Recommendation] = None

    updated_at: Optional[datetime] = None
