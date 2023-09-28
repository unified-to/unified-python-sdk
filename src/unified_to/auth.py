"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from unified_to import utils
from unified_to.models import errors, operations

class Auth:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def get_unified_integration_auth_workspace_id_integration_type(self, request: operations.GetUnifiedIntegrationAuthWorkspaceIDIntegrationTypeRequest) -> operations.GetUnifiedIntegrationAuthWorkspaceIDIntegrationTypeResponse:
        r"""Create connection indirectly
        Returns an authorization URL for the specified integration.  Once a successful authorization occurs, a new connection is created.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetUnifiedIntegrationAuthWorkspaceIDIntegrationTypeRequest, base_url, '/unified/integration/auth/{workspace_id}/{integration_type}', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetUnifiedIntegrationAuthWorkspaceIDIntegrationTypeRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetUnifiedIntegrationAuthWorkspaceIDIntegrationTypeResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                res.get_unified_integration_auth_workspace_id_integration_type_200_application_json_string = http_res.content
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_unified_integration_login_workspace_id_integration_type(self, request: operations.GetUnifiedIntegrationLoginWorkspaceIDIntegrationTypeRequest) -> operations.GetUnifiedIntegrationLoginWorkspaceIDIntegrationTypeResponse:
        r"""Sign in a user
        Returns an authentication URL for the specified integration.  Once a successful authentication occurs, the name and emails are returned.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetUnifiedIntegrationLoginWorkspaceIDIntegrationTypeRequest, base_url, '/unified/integration/login/{workspace_id}/{integration_type}', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetUnifiedIntegrationLoginWorkspaceIDIntegrationTypeRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetUnifiedIntegrationLoginWorkspaceIDIntegrationTypeResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                res.get_unified_integration_login_workspace_id_integration_type_200_application_json_string = http_res.content
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    