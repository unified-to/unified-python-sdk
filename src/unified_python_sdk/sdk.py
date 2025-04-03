"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, ClientOwner, HttpClient, close_clients
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
import httpx
from typing import Callable, Dict, Optional, Union, cast
from unified_python_sdk import utils
from unified_python_sdk._hooks import SDKHooks
from unified_python_sdk.account import Account
from unified_python_sdk.accounting import Accounting
from unified_python_sdk.activity import Activity
from unified_python_sdk.apicall import Apicall
from unified_python_sdk.application import Application
from unified_python_sdk.applicationstatus import Applicationstatus
from unified_python_sdk.ats import Ats
from unified_python_sdk.auth import Auth
from unified_python_sdk.branch import Branch
from unified_python_sdk.busy import Busy
from unified_python_sdk.calendar import Calendar
from unified_python_sdk.call import Call
from unified_python_sdk.candidate import Candidate
from unified_python_sdk.channel import Channel
from unified_python_sdk.class_ import Class
from unified_python_sdk.collection import Collection
from unified_python_sdk.comment import Comment
from unified_python_sdk.commerce import Commerce
from unified_python_sdk.commit import Commit
from unified_python_sdk.company import Company
from unified_python_sdk.connection import Connection
from unified_python_sdk.contact import Contact
from unified_python_sdk.course import Course
from unified_python_sdk.crm import Crm
from unified_python_sdk.customer import Customer
from unified_python_sdk.deal import Deal
from unified_python_sdk.document import Document
from unified_python_sdk.employee import Employee
from unified_python_sdk.enrich import Enrich
from unified_python_sdk.event import Event
from unified_python_sdk.file import File
from unified_python_sdk.genai import Genai
from unified_python_sdk.group import Group
from unified_python_sdk.hris import Hris
from unified_python_sdk.instructor import Instructor
from unified_python_sdk.integration import Integration
from unified_python_sdk.interview import Interview
from unified_python_sdk.inventory import Inventory
from unified_python_sdk.invoice import Invoice
from unified_python_sdk.issue import Issue
from unified_python_sdk.item import Item
from unified_python_sdk.job import Job
from unified_python_sdk.journal import Journal
from unified_python_sdk.kms import Kms
from unified_python_sdk.lead import Lead
from unified_python_sdk.link import Link
from unified_python_sdk.list import ListT
from unified_python_sdk.lms import Lms
from unified_python_sdk.location import Location
from unified_python_sdk.login import Login
from unified_python_sdk.martech import Martech
from unified_python_sdk.member import Member
from unified_python_sdk.message import Message
from unified_python_sdk.messaging import Messaging
from unified_python_sdk.metadata import Metadata
from unified_python_sdk.model import Model
from unified_python_sdk.models import shared
from unified_python_sdk.note import Note
from unified_python_sdk.order import Order
from unified_python_sdk.organization import Organization
from unified_python_sdk.page import Page
from unified_python_sdk.passthrough import Passthrough
from unified_python_sdk.payment import Payment
from unified_python_sdk.payout import Payout
from unified_python_sdk.payslip import Payslip
from unified_python_sdk.person import Person
from unified_python_sdk.pipeline import Pipeline
from unified_python_sdk.project import Project
from unified_python_sdk.prompt import Prompt
from unified_python_sdk.pullrequest import Pullrequest
from unified_python_sdk.recording import Recording
from unified_python_sdk.refund import Refund
from unified_python_sdk.repo import Repo
from unified_python_sdk.report import Report
from unified_python_sdk.repository import Repository
from unified_python_sdk.scim import Scim
from unified_python_sdk.scorecard import Scorecard
from unified_python_sdk.space import Space
from unified_python_sdk.storage import Storage
from unified_python_sdk.student import Student
from unified_python_sdk.subscription import Subscription
from unified_python_sdk.task import Task
from unified_python_sdk.taxrate import Taxrate
from unified_python_sdk.ticket import Ticket
from unified_python_sdk.ticketing import Ticketing
from unified_python_sdk.timeoff import Timeoff
from unified_python_sdk.transaction import Transaction
from unified_python_sdk.types import OptionalNullable, UNSET
from unified_python_sdk.uc import Uc
from unified_python_sdk.unified import Unified
from unified_python_sdk.user import User
from unified_python_sdk.webhook import Webhook
import weakref


class UnifiedTo(BaseSDK):
    r"""Unified.to API: One API to Rule Them All"""

    accounting: Accounting
    account: Account
    contact: Contact
    invoice: Invoice
    journal: Journal
    order: Order
    organization: Organization
    report: Report
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
    calendar: Calendar
    busy: Busy
    event: Event
    link: Link
    recording: Recording
    commerce: Commerce
    collection: Collection
    inventory: Inventory
    item: Item
    location: Location
    crm: Crm
    deal: Deal
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
    comment: Comment
    page: Page
    space: Space
    lms: Lms
    class_: Class
    course: Course
    instructor: Instructor
    student: Student
    martech: Martech
    list: ListT
    member: Member
    messaging: Messaging
    channel: Channel
    message: Message
    metadata: Metadata
    passthrough: Passthrough
    payment: Payment
    payout: Payout
    refund: Refund
    subscription: Subscription
    repo: Repo
    branch: Branch
    commit: Commit
    pullrequest: Pullrequest
    repository: Repository
    scim: Scim
    user: User
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

    def __init__(
        self,
        security: Union[shared.Security, Callable[[], shared.Security]],
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param security: The security details required for authentication
        :param server_idx: The index of the server to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        client_supplied = True
        if client is None:
            client = httpx.Client()
            client_supplied = False

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        async_client_supplied = True
        if async_client is None:
            async_client = httpx.AsyncClient()
            async_client_supplied = False

        if debug_logger is None:
            debug_logger = get_default_logger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        BaseSDK.__init__(
            self,
            SDKConfiguration(
                client=client,
                client_supplied=client_supplied,
                async_client=async_client,
                async_client_supplied=async_client_supplied,
                security=security,
                server_url=server_url,
                server_idx=server_idx,
                retry_config=retry_config,
                timeout_ms=timeout_ms,
                debug_logger=debug_logger,
            ),
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(
            current_server_url, client
        )
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        weakref.finalize(
            self,
            close_clients,
            cast(ClientOwner, self.sdk_configuration),
            self.sdk_configuration.client,
            self.sdk_configuration.client_supplied,
            self.sdk_configuration.async_client,
            self.sdk_configuration.async_client_supplied,
        )

        self._init_sdks()

    def _init_sdks(self):
        self.accounting = Accounting(self.sdk_configuration)
        self.account = Account(self.sdk_configuration)
        self.contact = Contact(self.sdk_configuration)
        self.invoice = Invoice(self.sdk_configuration)
        self.journal = Journal(self.sdk_configuration)
        self.order = Order(self.sdk_configuration)
        self.organization = Organization(self.sdk_configuration)
        self.report = Report(self.sdk_configuration)
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
        self.calendar = Calendar(self.sdk_configuration)
        self.busy = Busy(self.sdk_configuration)
        self.event = Event(self.sdk_configuration)
        self.link = Link(self.sdk_configuration)
        self.recording = Recording(self.sdk_configuration)
        self.commerce = Commerce(self.sdk_configuration)
        self.collection = Collection(self.sdk_configuration)
        self.inventory = Inventory(self.sdk_configuration)
        self.item = Item(self.sdk_configuration)
        self.location = Location(self.sdk_configuration)
        self.crm = Crm(self.sdk_configuration)
        self.deal = Deal(self.sdk_configuration)
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
        self.comment = Comment(self.sdk_configuration)
        self.page = Page(self.sdk_configuration)
        self.space = Space(self.sdk_configuration)
        self.lms = Lms(self.sdk_configuration)
        self.class_ = Class(self.sdk_configuration)
        self.course = Course(self.sdk_configuration)
        self.instructor = Instructor(self.sdk_configuration)
        self.student = Student(self.sdk_configuration)
        self.martech = Martech(self.sdk_configuration)
        self.list = ListT(self.sdk_configuration)
        self.member = Member(self.sdk_configuration)
        self.messaging = Messaging(self.sdk_configuration)
        self.channel = Channel(self.sdk_configuration)
        self.message = Message(self.sdk_configuration)
        self.metadata = Metadata(self.sdk_configuration)
        self.passthrough = Passthrough(self.sdk_configuration)
        self.payment = Payment(self.sdk_configuration)
        self.payout = Payout(self.sdk_configuration)
        self.refund = Refund(self.sdk_configuration)
        self.subscription = Subscription(self.sdk_configuration)
        self.repo = Repo(self.sdk_configuration)
        self.branch = Branch(self.sdk_configuration)
        self.commit = Commit(self.sdk_configuration)
        self.pullrequest = Pullrequest(self.sdk_configuration)
        self.repository = Repository(self.sdk_configuration)
        self.scim = Scim(self.sdk_configuration)
        self.user = User(self.sdk_configuration)
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

    def __enter__(self):
        return self

    async def __aenter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if (
            self.sdk_configuration.client is not None
            and not self.sdk_configuration.client_supplied
        ):
            self.sdk_configuration.client.close()
        self.sdk_configuration.client = None

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if (
            self.sdk_configuration.async_client is not None
            and not self.sdk_configuration.async_client_supplied
        ):
            await self.sdk_configuration.async_client.aclose()
        self.sdk_configuration.async_client = None
