"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from pydantic.functional_validators import PlainValidator
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk import utils
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import validate_open_enum


class ScimPhoneNumberType(str, Enum, metaclass=utils.OpenEnumMeta):
    WORK = "work"
    HOME = "home"
    OTHER = "other"
    MOBILE = "mobile"
    FAX = "fax"
    PAGER = "pager"


class ScimPhoneNumberTypedDict(TypedDict):
    display: NotRequired[str]
    primary: NotRequired[bool]
    type: NotRequired[ScimPhoneNumberType]
    value: NotRequired[str]


class ScimPhoneNumber(BaseModel):
    display: Optional[str] = None

    primary: Optional[bool] = None

    type: Annotated[
        Optional[ScimPhoneNumberType], PlainValidator(validate_open_enum(False))
    ] = None

    value: Optional[str] = None
