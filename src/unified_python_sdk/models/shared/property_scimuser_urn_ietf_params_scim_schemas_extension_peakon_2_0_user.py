"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class PropertyScimUserUrnIetfParamsScimSchemasExtensionPeakon20UserGender(str, Enum):
    FEMALE = "Female"
    MALE = "Male"


class PropertyScimUserUrnIetfParamsScimSchemasExtensionPeakon20UserTypedDict(TypedDict):
    date_of_birth: NotRequired[datetime]
    gender: NotRequired[
        PropertyScimUserUrnIetfParamsScimSchemasExtensionPeakon20UserGender
    ]
    manager: NotRequired[str]
    team: NotRequired[str]


class PropertyScimUserUrnIetfParamsScimSchemasExtensionPeakon20User(BaseModel):
    date_of_birth: Annotated[
        Optional[datetime], pydantic.Field(alias="Date of Birth")
    ] = None

    gender: Annotated[
        Optional[PropertyScimUserUrnIetfParamsScimSchemasExtensionPeakon20UserGender],
        pydantic.Field(alias="Gender"),
    ] = None

    manager: Annotated[Optional[str], pydantic.Field(alias="Manager")] = None

    team: Annotated[Optional[str], pydantic.Field(alias="Team")] = None
