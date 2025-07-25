"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from unified_python_sdk import utils


class PropertyConnectionCategories(str, Enum, metaclass=utils.OpenEnumMeta):
    PASSTHROUGH = "passthrough"
    HRIS = "hris"
    ATS = "ats"
    AUTH = "auth"
    CRM = "crm"
    ENRICH = "enrich"
    MARTECH = "martech"
    TICKETING = "ticketing"
    UC = "uc"
    ACCOUNTING = "accounting"
    STORAGE = "storage"
    COMMERCE = "commerce"
    PAYMENT = "payment"
    GENAI = "genai"
    MESSAGING = "messaging"
    KMS = "kms"
    TASK = "task"
    SCIM = "scim"
    LMS = "lms"
    REPO = "repo"
    METADATA = "metadata"
    CALENDAR = "calendar"
