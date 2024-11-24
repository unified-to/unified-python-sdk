"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import FieldMetadata, SecurityMetadata


class SecurityTypedDict(TypedDict):
    jwt: NotRequired[str]


class Security(BaseModel):
    jwt: Annotated[
        Optional[str],
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True,
                scheme_type="apiKey",
                sub_type="header",
                field_name="authorization",
            )
        ),
    ] = None