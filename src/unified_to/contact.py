"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from typing import Optional
from unified_to import utils
from unified_to.models import errors, operations, shared

class Contact:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def delete_crm_connection_id_contact_id(self, request: operations.DeleteCrmConnectionIDContactIDRequest) -> operations.DeleteCrmConnectionIDContactIDResponse:
        r"""Remove a contact"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteCrmConnectionIDContactIDRequest, base_url, '/crm/{connection_id}/contact/{id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteCrmConnectionIDContactIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            if utils.match_content_type(content_type, 'application/json'):
                res.delete_crm_connection_id_contact_id_default_application_json_string = http_res.content
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def delete_uc_connection_id_contact_id(self, request: operations.DeleteUcConnectionIDContactIDRequest) -> operations.DeleteUcConnectionIDContactIDResponse:
        r"""Remove a contact"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteUcConnectionIDContactIDRequest, base_url, '/uc/{connection_id}/contact/{id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteUcConnectionIDContactIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            if utils.match_content_type(content_type, 'application/json'):
                res.delete_uc_connection_id_contact_id_default_application_json_string = http_res.content
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_crm_connection_id_contact(self, request: operations.GetCrmConnectionIDContactRequest) -> operations.GetCrmConnectionIDContactResponse:
        r"""List all contacts"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetCrmConnectionIDContactRequest, base_url, '/crm/{connection_id}/contact', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetCrmConnectionIDContactRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCrmConnectionIDContactResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.CrmContact]])
                res.crm_contacts = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_crm_connection_id_contact_id(self, request: operations.GetCrmConnectionIDContactIDRequest) -> operations.GetCrmConnectionIDContactIDResponse:
        r"""Retrieve a contact"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetCrmConnectionIDContactIDRequest, base_url, '/crm/{connection_id}/contact/{id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCrmConnectionIDContactIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CrmContact])
                res.crm_contact = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_uc_connection_id_contact(self, request: operations.GetUcConnectionIDContactRequest) -> operations.GetUcConnectionIDContactResponse:
        r"""List all contacts"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetUcConnectionIDContactRequest, base_url, '/uc/{connection_id}/contact', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetUcConnectionIDContactRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetUcConnectionIDContactResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.UcContact]])
                res.uc_contacts = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_uc_connection_id_contact_id(self, request: operations.GetUcConnectionIDContactIDRequest) -> operations.GetUcConnectionIDContactIDResponse:
        r"""Retrieve a contact"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetUcConnectionIDContactIDRequest, base_url, '/uc/{connection_id}/contact/{id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetUcConnectionIDContactIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.UcContact])
                res.uc_contact = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def patch_crm_connection_id_contact_id(self, request: operations.PatchCrmConnectionIDContactIDRequest) -> operations.PatchCrmConnectionIDContactIDResponse:
        r"""Update a contact"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PatchCrmConnectionIDContactIDRequest, base_url, '/crm/{connection_id}/contact/{id}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "crm_contact", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PatchCrmConnectionIDContactIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CrmContact])
                res.crm_contact = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def patch_uc_connection_id_contact_id(self, request: operations.PatchUcConnectionIDContactIDRequest) -> operations.PatchUcConnectionIDContactIDResponse:
        r"""Update a contact"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PatchUcConnectionIDContactIDRequest, base_url, '/uc/{connection_id}/contact/{id}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "uc_contact", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PatchUcConnectionIDContactIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.UcContact])
                res.uc_contact = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def post_crm_connection_id_contact(self, request: operations.PostCrmConnectionIDContactRequest) -> operations.PostCrmConnectionIDContactResponse:
        r"""Create a contact"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PostCrmConnectionIDContactRequest, base_url, '/crm/{connection_id}/contact', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "crm_contact", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostCrmConnectionIDContactResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CrmContact])
                res.crm_contact = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def post_uc_connection_id_contact(self, request: operations.PostUcConnectionIDContactRequest) -> operations.PostUcConnectionIDContactResponse:
        r"""Create a contact"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PostUcConnectionIDContactRequest, base_url, '/uc/{connection_id}/contact', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "uc_contact", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostUcConnectionIDContactResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.UcContact])
                res.uc_contact = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def put_crm_connection_id_contact_id(self, request: operations.PutCrmConnectionIDContactIDRequest) -> operations.PutCrmConnectionIDContactIDResponse:
        r"""Update a contact"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PutCrmConnectionIDContactIDRequest, base_url, '/crm/{connection_id}/contact/{id}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "crm_contact", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutCrmConnectionIDContactIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CrmContact])
                res.crm_contact = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def put_uc_connection_id_contact_id(self, request: operations.PutUcConnectionIDContactIDRequest) -> operations.PutUcConnectionIDContactIDResponse:
        r"""Update a contact"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PutUcConnectionIDContactIDRequest, base_url, '/uc/{connection_id}/contact/{id}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "uc_contact", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutUcConnectionIDContactIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.UcContact])
                res.uc_contact = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    