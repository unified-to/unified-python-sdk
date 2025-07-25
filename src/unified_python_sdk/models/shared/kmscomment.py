"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from pydantic.functional_validators import PlainValidator
from typing import Any, Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk import utils
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import validate_open_enum


class ContentType(str, Enum, metaclass=utils.OpenEnumMeta):
    HTML = "HTML"
    MARKDOWN = "MARKDOWN"
    TEXT = "TEXT"
    OTHER = "OTHER"


class KmsCommentType(str, Enum, metaclass=utils.OpenEnumMeta):
    PAGE_INLINE = "PAGE_INLINE"
    PAGE = "PAGE"


class KmsCommentTypedDict(TypedDict):
    content: str
    content_type: NotRequired[ContentType]
    created_at: NotRequired[datetime]
    id: NotRequired[str]
    page_id: NotRequired[str]
    parent_id: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    type: NotRequired[KmsCommentType]
    updated_at: NotRequired[datetime]
    user_id: NotRequired[str]


class KmsComment(BaseModel):
    content: str

    content_type: Annotated[
        Optional[ContentType], PlainValidator(validate_open_enum(False))
    ] = None

    created_at: Optional[datetime] = None

    id: Optional[str] = None

    page_id: Optional[str] = None

    parent_id: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None

    type: Annotated[
        Optional[KmsCommentType], PlainValidator(validate_open_enum(False))
    ] = None

    updated_at: Optional[datetime] = None

    user_id: Optional[str] = None
