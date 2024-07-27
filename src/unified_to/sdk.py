"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

import requests as requests_http
from .account import Account
from .accounting import Accounting
from .activity import Activity
from .apicall import Apicall
from .application import Application
from .applicationstatus import Applicationstatus
from .ats import Ats
from .auth import Auth
from .call import Call
from .candidate import Candidate
from .channel import Channel
from .collection import Collection
from .commerce import Commerce
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
from .genai import Genai
from .group import Group
from .hris import Hris
from .integration import Integration
from .interview import Interview
from .inventory import Inventory
from .invoice import Invoice
from .issue import Issue
from .item import Item
from .job import Job
from .journal import Journal
from .kms import Kms
from .lead import Lead
from .link import Link
from .list import ListT
from .location import Location
from .login import Login
from .martech import Martech
from .member import Member
from .message import Message
from .messaging import Messaging
from .model import Model
from .note import Note
from .organization import Organization
from .page import Page
from .passthrough import Passthrough
from .payment import Payment
from .payout import Payout
from .payslip import Payslip
from .person import Person
from .pipeline import Pipeline
from .project import Project
from .prompt import Prompt
from .refund import Refund
from .scorecard import Scorecard
from .sdkconfiguration import SDKConfiguration
from .space import Space
from .storage import Storage
from .task import Task
from .taxrate import Taxrate
from .ticket import Ticket
from .ticketing import Ticketing
from .timeoff import Timeoff
from .transaction import Transaction
from .uc import Uc
from .unified import Unified
from .utils.retries import RetryConfig
from .webhook import Webhook
from typing import Callable, Dict, Optional, Union
from unified_to import utils
from unified_to._hooks import SDKHooks
from unified_to.models import shared

class UnifiedTo:
    r"""Unified.to API: One API to Rule Them All"""
    accounting: Accounting
    account: Account
    contact: Contact
    invoice: Invoice
    journal: Journal
    organization: Organization
    taxrate: Taxrate
    transaction: Transaction
    ats: Ats
    activity: Activity
    application: Application
    applicationstatus: Applicationstatus
    candidate: Candidate
    company: Company
    document: Document
    interview: Interview
    job: Job
    scorecard: Scorecard
    commerce: Commerce
    collection: Collection
    inventory: Inventory
    item: Item
    location: Location
    crm: Crm
    deal: Deal
    event: Event
    lead: Lead
    pipeline: Pipeline
    enrich: Enrich
    person: Person
    genai: Genai
    model: Model
    prompt: Prompt
    hris: Hris
    employee: Employee
    group: Group
    payslip: Payslip
    timeoff: Timeoff
    kms: Kms
    page: Page
    space: Space
    martech: Martech
    list: ListT
    member: Member
    messaging: Messaging
    channel: Channel
    message: Message
    passthrough: Passthrough
    payment: Payment
    link: Link
    payout: Payout
    refund: Refund
    storage: Storage
    file: File
    task: Task
    project: Project
    ticketing: Ticketing
    customer: Customer
    note: Note
    ticket: Ticket
    uc: Uc
    call: Call
    unified: Unified
    apicall: Apicall
    connection: Connection
    integration: Integration
    auth: Auth
    login: Login
    issue: Issue
    webhook: Webhook

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 security: Union[shared.Security,Callable[[], shared.Security]] = None,
                 server_idx: Optional[int] = None,
                 server_url: Optional[str] = None,
                 url_params: Optional[Dict[str, str]] = None,
                 client: Optional[requests_http.Session] = None,
                 retry_config: Optional[RetryConfig] = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.

        :param security: The security details required for authentication
        :type security: Union[shared.Security,Callable[[], shared.Security]]
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: RetryConfig
        """
        if client is None:
            client = requests_http.Session()

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)
    

        self.sdk_configuration = SDKConfiguration(
            client,
            security,
            server_url,
            server_idx,
            retry_config=retry_config
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(current_server_url, self.sdk_configuration.client)
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__['_hooks'] = hooks

        self._init_sdks()


    def _init_sdks(self):
        self.accounting = Accounting(self.sdk_configuration)
        self.account = Account(self.sdk_configuration)
        self.contact = Contact(self.sdk_configuration)
        self.invoice = Invoice(self.sdk_configuration)
        self.journal = Journal(self.sdk_configuration)
        self.organization = Organization(self.sdk_configuration)
        self.taxrate = Taxrate(self.sdk_configuration)
        self.transaction = Transaction(self.sdk_configuration)
        self.ats = Ats(self.sdk_configuration)
        self.activity = Activity(self.sdk_configuration)
        self.application = Application(self.sdk_configuration)
        self.applicationstatus = Applicationstatus(self.sdk_configuration)
        self.candidate = Candidate(self.sdk_configuration)
        self.company = Company(self.sdk_configuration)
        self.document = Document(self.sdk_configuration)
        self.interview = Interview(self.sdk_configuration)
        self.job = Job(self.sdk_configuration)
        self.scorecard = Scorecard(self.sdk_configuration)
        self.commerce = Commerce(self.sdk_configuration)
        self.collection = Collection(self.sdk_configuration)
        self.inventory = Inventory(self.sdk_configuration)
        self.item = Item(self.sdk_configuration)
        self.location = Location(self.sdk_configuration)
        self.crm = Crm(self.sdk_configuration)
        self.deal = Deal(self.sdk_configuration)
        self.event = Event(self.sdk_configuration)
        self.lead = Lead(self.sdk_configuration)
        self.pipeline = Pipeline(self.sdk_configuration)
        self.enrich = Enrich(self.sdk_configuration)
        self.person = Person(self.sdk_configuration)
        self.genai = Genai(self.sdk_configuration)
        self.model = Model(self.sdk_configuration)
        self.prompt = Prompt(self.sdk_configuration)
        self.hris = Hris(self.sdk_configuration)
        self.employee = Employee(self.sdk_configuration)
        self.group = Group(self.sdk_configuration)
        self.payslip = Payslip(self.sdk_configuration)
        self.timeoff = Timeoff(self.sdk_configuration)
        self.kms = Kms(self.sdk_configuration)
        self.page = Page(self.sdk_configuration)
        self.space = Space(self.sdk_configuration)
        self.martech = Martech(self.sdk_configuration)
        self.list = ListT(self.sdk_configuration)
        self.member = Member(self.sdk_configuration)
        self.messaging = Messaging(self.sdk_configuration)
        self.channel = Channel(self.sdk_configuration)
        self.message = Message(self.sdk_configuration)
        self.passthrough = Passthrough(self.sdk_configuration)
        self.payment = Payment(self.sdk_configuration)
        self.link = Link(self.sdk_configuration)
        self.payout = Payout(self.sdk_configuration)
        self.refund = Refund(self.sdk_configuration)
        self.storage = Storage(self.sdk_configuration)
        self.file = File(self.sdk_configuration)
        self.task = Task(self.sdk_configuration)
        self.project = Project(self.sdk_configuration)
        self.ticketing = Ticketing(self.sdk_configuration)
        self.customer = Customer(self.sdk_configuration)
        self.note = Note(self.sdk_configuration)
        self.ticket = Ticket(self.sdk_configuration)
        self.uc = Uc(self.sdk_configuration)
        self.call = Call(self.sdk_configuration)
        self.unified = Unified(self.sdk_configuration)
        self.apicall = Apicall(self.sdk_configuration)
        self.connection = Connection(self.sdk_configuration)
        self.integration = Integration(self.sdk_configuration)
        self.auth = Auth(self.sdk_configuration)
        self.login = Login(self.sdk_configuration)
        self.issue = Issue(self.sdk_configuration)
        self.webhook = Webhook(self.sdk_configuration)
