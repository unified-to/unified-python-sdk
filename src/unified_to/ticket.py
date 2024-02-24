"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from typing import List, Optional
from unified_to import utils
from unified_to.models import errors, operations, shared

class Ticket:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def create_ticketing_ticket(self, request: operations.CreateTicketingTicketRequest, security: operations.CreateTicketingTicketSecurity) -> operations.CreateTicketingTicketResponse:
        r"""Create a ticket"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.CreateTicketingTicketRequest, base_url, '/ticketing/{connection_id}/ticket', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, operations.CreateTicketingTicketRequest, "ticketing_ticket", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.CreateTicketingTicketResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TicketingTicket])
                res.ticketing_ticket = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_ticketing_ticket(self, request: operations.GetTicketingTicketRequest, security: operations.GetTicketingTicketSecurity) -> operations.GetTicketingTicketResponse:
        r"""Retrieve a ticket"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetTicketingTicketRequest, base_url, '/ticketing/{connection_id}/ticket/{id}', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetTicketingTicketRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.GetTicketingTicketResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TicketingTicket])
                res.ticketing_ticket = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def list_ticketing_tickets(self, request: operations.ListTicketingTicketsRequest, security: operations.ListTicketingTicketsSecurity) -> operations.ListTicketingTicketsResponse:
        r"""List all tickets"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ListTicketingTicketsRequest, base_url, '/ticketing/{connection_id}/ticket', request)
        headers = {}
        query_params = utils.get_query_params(operations.ListTicketingTicketsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.ListTicketingTicketsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[List[shared.TicketingTicket]])
                res.ticketing_tickets = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def patch_ticketing_ticket(self, request: operations.PatchTicketingTicketRequest, security: operations.PatchTicketingTicketSecurity) -> operations.PatchTicketingTicketResponse:
        r"""Update a ticket"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PatchTicketingTicketRequest, base_url, '/ticketing/{connection_id}/ticket/{id}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, operations.PatchTicketingTicketRequest, "ticketing_ticket", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.PatchTicketingTicketResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TicketingTicket])
                res.ticketing_ticket = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def remove_ticketing_ticket(self, request: operations.RemoveTicketingTicketRequest, security: operations.RemoveTicketingTicketSecurity) -> operations.RemoveTicketingTicketResponse:
        r"""Remove a ticket"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.RemoveTicketingTicketRequest, base_url, '/ticketing/{connection_id}/ticket/{id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.RemoveTicketingTicketResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            if utils.match_content_type(content_type, 'application/json'):
                res.res = http_res.content
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def update_ticketing_ticket(self, request: operations.UpdateTicketingTicketRequest, security: operations.UpdateTicketingTicketSecurity) -> operations.UpdateTicketingTicketResponse:
        r"""Update a ticket"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UpdateTicketingTicketRequest, base_url, '/ticketing/{connection_id}/ticket/{id}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, operations.UpdateTicketingTicketRequest, "ticketing_ticket", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.UpdateTicketingTicketResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TicketingTicket])
                res.ticketing_ticket = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    