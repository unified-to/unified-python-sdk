"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .property_connection_auth import (
    PropertyConnectionAuth,
    PropertyConnectionAuthTypedDict,
)
from .property_connection_categories import PropertyConnectionCategories
from .property_connection_permissions import PropertyConnectionPermissions
from datetime import datetime
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class ConnectionTypedDict(TypedDict):
    r"""A connection represents a specific authentication of an integration."""

    categories: List[PropertyConnectionCategories]
    r"""The Integration categories that this connection supports"""
    integration_type: str
    permissions: List[PropertyConnectionPermissions]
    auth: NotRequired[PropertyConnectionAuthTypedDict]
    r"""An authentication object that represents a specific authorized user's connection to an integration."""
    auth_aws_arn: NotRequired[str]
    created_at: NotRequired[datetime]
    environment: NotRequired[str]
    external_xref: NotRequired[str]
    id: NotRequired[str]
    is_paused: NotRequired[bool]
    last_healthy_at: NotRequired[datetime]
    last_unhealthy_at: NotRequired[datetime]
    updated_at: NotRequired[datetime]
    workspace_id: NotRequired[str]


class Connection(BaseModel):
    r"""A connection represents a specific authentication of an integration."""

    categories: List[PropertyConnectionCategories]
    r"""The Integration categories that this connection supports"""

    integration_type: str

    permissions: List[PropertyConnectionPermissions]

    auth: Optional[PropertyConnectionAuth] = None
    r"""An authentication object that represents a specific authorized user's connection to an integration."""

    auth_aws_arn: Optional[str] = None

    created_at: Optional[datetime] = None

    environment: Optional[str] = "Production"

    external_xref: Optional[str] = None

    id: Optional[str] = None

    is_paused: Optional[bool] = None

    last_healthy_at: Optional[datetime] = None

    last_unhealthy_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None

    workspace_id: Optional[str] = None