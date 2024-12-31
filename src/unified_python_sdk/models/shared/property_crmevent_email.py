"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class PropertyCrmEventEmailTypedDict(TypedDict):
    r"""The email object, when type = email"""

    attachment_file_ids: NotRequired[List[str]]
    body: NotRequired[str]
    cc: NotRequired[List[str]]
    r"""The event email's cc name & email (name )"""
    from_: NotRequired[str]
    subject: NotRequired[str]
    to: NotRequired[List[str]]
    r"""The event email's \"to\" name & email (name )"""


class PropertyCrmEventEmail(BaseModel):
    r"""The email object, when type = email"""

    attachment_file_ids: Optional[List[str]] = None

    body: Optional[str] = None

    cc: Optional[List[str]] = None
    r"""The event email's cc name & email (name )"""

    from_: Annotated[Optional[str], pydantic.Field(alias="from")] = None

    subject: Optional[str] = None

    to: Optional[List[str]] = None
    r"""The event email's \"to\" name & email (name )"""
