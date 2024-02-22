"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""


import requests as requests_http
from .utils import utils
from .utils.retries import RetryConfig
from dataclasses import dataclass
from typing import Callable, Dict, Tuple, Union
from unified_to.models import shared


SERVERS = [
    'https://api.unified.to',
    # North American data region
    'https://api-eu.unified.to',
    # European data region
]
"""Contains the list of servers available to the SDK"""

@dataclass
class SDKConfiguration:
    client: requests_http.Session
    security: Union[shared.Security,Callable[[], shared.Security]] = None
    server_url: str = ''
    server_idx: int = 0
    language: str = 'python'
    openapi_doc_version: str = '1.0'
    sdk_version: str = '0.16.9'
    gen_version: str = '2.263.3'
    user_agent: str = 'speakeasy-sdk/python 0.16.9 2.263.3 1.0 Unified-python-sdk'
    retry_config: RetryConfig = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url:
            return utils.remove_suffix(self.server_url, '/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}
