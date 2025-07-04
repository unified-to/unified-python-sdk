"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from pydantic.functional_validators import PlainValidator
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk import utils
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import validate_open_enum


class APICallType(str, Enum, metaclass=utils.OpenEnumMeta):
    LOGIN = "login"
    WEBHOOK = "webhook"
    INBOUND = "inbound"


class APICallTypedDict(TypedDict):
    integration_type: str
    method: str
    name: str
    path: str
    status: str
    type: APICallType
    connection_id: NotRequired[str]
    created_at: NotRequired[datetime]
    environment: NotRequired[str]
    error: NotRequired[str]
    external_xref: NotRequired[str]
    id: NotRequired[str]
    ip_address: NotRequired[str]
    is_billable: NotRequired[bool]
    size: NotRequired[float]
    webhook_id: NotRequired[str]
    workspace_id: NotRequired[str]


class APICall(BaseModel):
    integration_type: str

    method: str

    name: str

    path: str

    status: str

    type: Annotated[APICallType, PlainValidator(validate_open_enum(False))]

    connection_id: Optional[str] = None

    created_at: Optional[datetime] = None

    environment: Optional[str] = "Production"

    error: Optional[str] = None

    external_xref: Optional[str] = None

    id: Optional[str] = None

    ip_address: Optional[str] = None

    is_billable: Optional[bool] = None

    size: Optional[float] = None

    webhook_id: Optional[str] = None

    workspace_id: Optional[str] = None
