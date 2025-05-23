"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .property_atsapplicationanswer_answers import PropertyAtsApplicationAnswerAnswers
from typing import List
from typing_extensions import TypedDict
from unified_python_sdk.types import BaseModel


class AtsApplicationAnswerTypedDict(TypedDict):
    answers: List[PropertyAtsApplicationAnswerAnswers]
    question_id: str


class AtsApplicationAnswer(BaseModel):
    answers: List[PropertyAtsApplicationAnswerAnswers]

    question_id: str
