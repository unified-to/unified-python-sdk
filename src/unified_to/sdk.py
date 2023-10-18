"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .apicall import Apicall
from .application import Application
from .ats import Ats
from .auth import Auth
from .call import Call
from .candidate import Candidate
from .company import Company
from .connection import Connection
from .contact import Contact
from .crm import Crm
from .customer import Customer
from .deal import Deal
from .document import Document
from .employee import Employee
from .enrich import Enrich
from .event import Event
from .file import File
from .group import Group
from .hris import Hris
from .integration import Integration
from .interview import Interview
from .job import Job
from .lead import Lead
from .list import ListT
from .login import Login
from .martech import Martech
from .member import Member
from .note import Note
from .passthrough import Passthrough
from .person import Person
from .pipeline import Pipeline
from .sdkconfiguration import SDKConfiguration
from .ticket import Ticket
from .ticketing import Ticketing
from .uc import Uc
from .unified import Unified
from .webhook import Webhook
from typing import Dict
from unified_to import utils
from unified_to.models import shared

class UnifiedTo:
    r"""Unified.to API: One API to Rule Them All"""
    apicall: Apicall
    application: Application
    ats: Ats
    auth: Auth
    call: Call
    candidate: Candidate
    company: Company
    connection: Connection
    contact: Contact
    crm: Crm
    customer: Customer
    deal: Deal
    document: Document
    employee: Employee
    enrich: Enrich
    event: Event
    file: File
    group: Group
    hris: Hris
    integration: Integration
    interview: Interview
    job: Job
    lead: Lead
    list: ListT
    login: Login
    martech: Martech
    member: Member
    note: Note
    passthrough: Passthrough
    person: Person
    pipeline: Pipeline
    ticket: Ticket
    ticketing: Ticketing
    uc: Uc
    unified: Unified
    webhook: Webhook

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 security: shared.Security = None,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: shared.Security
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        
        security_client = utils.configure_security_client(client, security)
        
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security_client, server_url, server_idx, retry_config=retry_config)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.apicall = Apicall(self.sdk_configuration)
        self.application = Application(self.sdk_configuration)
        self.ats = Ats(self.sdk_configuration)
        self.auth = Auth(self.sdk_configuration)
        self.call = Call(self.sdk_configuration)
        self.candidate = Candidate(self.sdk_configuration)
        self.company = Company(self.sdk_configuration)
        self.connection = Connection(self.sdk_configuration)
        self.contact = Contact(self.sdk_configuration)
        self.crm = Crm(self.sdk_configuration)
        self.customer = Customer(self.sdk_configuration)
        self.deal = Deal(self.sdk_configuration)
        self.document = Document(self.sdk_configuration)
        self.employee = Employee(self.sdk_configuration)
        self.enrich = Enrich(self.sdk_configuration)
        self.event = Event(self.sdk_configuration)
        self.file = File(self.sdk_configuration)
        self.group = Group(self.sdk_configuration)
        self.hris = Hris(self.sdk_configuration)
        self.integration = Integration(self.sdk_configuration)
        self.interview = Interview(self.sdk_configuration)
        self.job = Job(self.sdk_configuration)
        self.lead = Lead(self.sdk_configuration)
        self.list = ListT(self.sdk_configuration)
        self.login = Login(self.sdk_configuration)
        self.martech = Martech(self.sdk_configuration)
        self.member = Member(self.sdk_configuration)
        self.note = Note(self.sdk_configuration)
        self.passthrough = Passthrough(self.sdk_configuration)
        self.person = Person(self.sdk_configuration)
        self.pipeline = Pipeline(self.sdk_configuration)
        self.ticket = Ticket(self.sdk_configuration)
        self.ticketing = Ticketing(self.sdk_configuration)
        self.uc = Uc(self.sdk_configuration)
        self.unified = Unified(self.sdk_configuration)
        self.webhook = Webhook(self.sdk_configuration)
    