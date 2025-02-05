"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .accountingaccount import (
    AccountingAccount,
    AccountingAccountTypedDict,
    Status,
    Type,
)
from .accountingcontact import (
    AccountingContact,
    AccountingContactTypedDict,
    TaxExemption,
)
from .accountingcontactpaymentmethod import (
    AccountingContactPaymentMethod,
    AccountingContactPaymentMethodType,
    AccountingContactPaymentMethodTypedDict,
)
from .accountingemail import (
    AccountingEmail,
    AccountingEmailType,
    AccountingEmailTypedDict,
)
from .accountinginvoice import (
    AccountingInvoice,
    AccountingInvoiceStatus,
    AccountingInvoiceType,
    AccountingInvoiceTypedDict,
    PaymentCollectionMethod,
)
from .accountingjournal import AccountingJournal, AccountingJournalTypedDict
from .accountingjournallineitem import (
    AccountingJournalLineitem,
    AccountingJournalLineitemTypedDict,
)
from .accountinglineitem import AccountingLineitem, AccountingLineitemTypedDict
from .accountingorder import (
    AccountingOrder,
    AccountingOrderStatus,
    AccountingOrderType,
    AccountingOrderTypedDict,
)
from .accountingorganization import (
    AccountingOrganization,
    AccountingOrganizationTypedDict,
)
from .accountingtaxrate import AccountingTaxrate, AccountingTaxrateTypedDict
from .accountingtelephone import (
    AccountingTelephone,
    AccountingTelephoneType,
    AccountingTelephoneTypedDict,
)
from .accountingtransaction import AccountingTransaction, AccountingTransactionTypedDict
from .accountingtransactioncontact import (
    AccountingTransactionContact,
    AccountingTransactionContactTypedDict,
)
from .accountingtransactionlineitem import (
    AccountingTransactionLineItem,
    AccountingTransactionLineItemTypedDict,
)
from .apicall import APICall, APICallType, APICallTypedDict
from .atsactivity import AtsActivity, AtsActivityType, AtsActivityTypedDict
from .atsaddress import AtsAddress, AtsAddressTypedDict
from .atsapplication import (
    AtsApplication,
    AtsApplicationStatus,
    AtsApplicationTypedDict,
)
from .atsapplicationanswer import AtsApplicationAnswer, AtsApplicationAnswerTypedDict
from .atscandidate import AtsCandidate, AtsCandidateTypedDict, Origin
from .atscompany import AtsCompany, AtsCompanyTypedDict
from .atscompensation import (
    AtsCompensation,
    AtsCompensationType,
    AtsCompensationTypedDict,
    Frequency,
)
from .atsdocument import AtsDocument, AtsDocumentType, AtsDocumentTypedDict
from .atsemail import AtsEmail, AtsEmailType, AtsEmailTypedDict
from .atsinterview import AtsInterview, AtsInterviewStatus, AtsInterviewTypedDict
from .atsjob import AtsJob, AtsJobStatus, AtsJobTypedDict, EmploymentType
from .atsjobquestion import AtsJobQuestion, AtsJobQuestionType, AtsJobQuestionTypedDict
from .atsoffer import AtsOffer, AtsOfferTypedDict
from .atsscorecard import AtsScorecard, AtsScorecardTypedDict, Recommendation
from .atsscorecardquestion import AtsScorecardQuestion, AtsScorecardQuestionTypedDict
from .atsstatus import AtsStatus, AtsStatusStatus, AtsStatusTypedDict
from .atstelephone import AtsTelephone, AtsTelephoneType, AtsTelephoneTypedDict
from .commercecollection import (
    CommerceCollection,
    CommerceCollectionType,
    CommerceCollectionTypedDict,
    Raw,
    RawTypedDict,
)
from .commerceinventory import (
    CommerceInventory,
    CommerceInventoryRaw,
    CommerceInventoryRawTypedDict,
    CommerceInventoryTypedDict,
)
from .commerceitem import (
    CommerceItem,
    CommerceItemRaw,
    CommerceItemRawTypedDict,
    CommerceItemTypedDict,
)
from .commerceitemmedia import (
    CommerceItemMedia,
    CommerceItemMediaType,
    CommerceItemMediaTypedDict,
)
from .commerceitemmetadata import (
    CommerceItemMetadata,
    CommerceItemMetadataTypedDict,
    ExtraData,
    ExtraDataTypedDict,
    Value,
    ValueTypedDict,
)
from .commerceitemoption import CommerceItemOption, CommerceItemOptionTypedDict
from .commerceitemprice import CommerceItemPrice, CommerceItemPriceTypedDict
from .commerceitemvariant import (
    CommerceItemVariant,
    CommerceItemVariantTypedDict,
    SizeUnit,
    WeightUnit,
)
from .commercelocation import (
    CommerceLocation,
    CommerceLocationRaw,
    CommerceLocationRawTypedDict,
    CommerceLocationTypedDict,
)
from .connection import Connection, ConnectionTypedDict
from .crmcompany import CrmCompany, CrmCompanyTypedDict
from .crmcontact import CrmContact, CrmContactTypedDict
from .crmdeal import CrmDeal, CrmDealTypedDict
from .crmemail import CrmEmail, CrmEmailType, CrmEmailTypedDict
from .crmevent import CrmEvent, CrmEventType, CrmEventTypedDict
from .crmeventformfield import (
    CrmEventFormField,
    CrmEventFormFieldType,
    CrmEventFormFieldTypedDict,
)
from .crmeventformoption import CrmEventFormOption, CrmEventFormOptionTypedDict
from .crmlead import CrmLead, CrmLeadTypedDict
from .crmpipeline import CrmPipeline, CrmPipelineTypedDict
from .crmstage import CrmStage, CrmStageTypedDict
from .crmtelephone import CrmTelephone, CrmTelephoneType, CrmTelephoneTypedDict
from .enrichcompany import EnrichCompany, EnrichCompanyTypedDict
from .enrichemail import EnrichEmail, EnrichEmailType, EnrichEmailTypedDict
from .enrichperson import EnrichPerson, EnrichPersonTypedDict, Gender
from .enrichpersonworkhistory import (
    EnrichPersonWorkHistory,
    EnrichPersonWorkHistoryTypedDict,
)
from .enrichtelephone import (
    EnrichTelephone,
    EnrichTelephoneType,
    EnrichTelephoneTypedDict,
)
from .genaicontent import GenaiContent, GenaiContentTypedDict, Role
from .genaimodel import GenaiModel, GenaiModelTypedDict
from .genaiprompt import GenaiPrompt, GenaiPromptTypedDict
from .hriscompany import HrisCompany, HrisCompanyTypedDict
from .hriscompensation import (
    HrisCompensation,
    HrisCompensationFrequency,
    HrisCompensationType,
    HrisCompensationTypedDict,
)
from .hrisemail import HrisEmail, HrisEmailType, HrisEmailTypedDict
from .hrisemployee import (
    EmploymentStatus,
    HrisEmployee,
    HrisEmployeeEmploymentType,
    HrisEmployeeGender,
    HrisEmployeeTypedDict,
    MaritalStatus,
)
from .hrisgroup import HrisGroup, HrisGroupType, HrisGroupTypedDict
from .hrislocation import HrisLocation, HrisLocationTypedDict
from .hrispayslip import HrisPayslip, HrisPayslipTypedDict, PaymentType
from .hrispayslipdetail import (
    HrisPayslipDetail,
    HrisPayslipDetailType,
    HrisPayslipDetailTypedDict,
)
from .hristelephone import HrisTelephone, HrisTelephoneType, HrisTelephoneTypedDict
from .hristimeoff import (
    HrisTimeoff,
    HrisTimeoffStatus,
    HrisTimeoffType,
    HrisTimeoffTypedDict,
)
from .integration import Integration, IntegrationTypedDict
from .integrationsupport import (
    FromWebhook,
    IntegrationSupport,
    IntegrationSupportTypedDict,
    ListAccountID,
    ListApplicationID,
    ListCandidateID,
    ListChannelID,
    ListClassID,
    ListCollectionID,
    ListCompanyID,
    ListContactID,
    ListCourseID,
    ListCustomerID,
    ListDealID,
    ListInstructorID,
    ListInterviewID,
    ListInvoiceID,
    ListItemID,
    ListItemVariantID,
    ListJobID,
    ListLimit,
    ListLinkID,
    ListListID,
    ListLocationID,
    ListOffset,
    ListOrder,
    ListOrgID,
    ListPageID,
    ListParentID,
    ListProjectID,
    ListQuery,
    ListRawFields,
    ListRepoID,
    ListRootID,
    ListSortByCreatedAt,
    ListSortByName,
    ListSortByUpdatedAt,
    ListSpaceID,
    ListStudentID,
    ListTaskID,
    ListTicketID,
    ListType,
    ListUpdatedGte,
    ListUserID,
    NativeWebhookParentID,
    NativeWebhookProjectID,
    SearchDomain,
    SearchEmail,
    SearchLinkedinurl,
    SearchName,
    SearchTwitter,
    VirtualWebhookChannelID,
    VirtualWebhookCompanyID,
    VirtualWebhookContactID,
    VirtualWebhookDealID,
    VirtualWebhookJobID,
    VirtualWebhookLimit,
    VirtualWebhookParentID,
    VirtualWebhookTicketID,
    VirtualWebhookType,
    VirtualWebhookUpdatedGte,
    VirtualWebhookUserID,
)
from .issue import Issue, IssueStatus, IssueTypedDict
from .kmscomment import ContentType, KmsComment, KmsCommentType, KmsCommentTypedDict
from .kmspage import KmsPage, KmsPageType, KmsPageTypedDict
from .kmspagemetadata import KmsPageMetadata, KmsPageMetadataTypedDict
from .kmsspace import KmsSpace, KmsSpaceTypedDict
from .lmsclass import LmsClass, LmsClassTypedDict
from .lmscourse import LmsCourse, LmsCourseTypedDict
from .lmsemail import LmsEmail, LmsEmailTypedDict
from .lmsinstructor import LmsInstructor, LmsInstructorTypedDict
from .lmsmedia import LmsMedia, LmsMediaType, LmsMediaTypedDict
from .lmsstudent import LmsStudent, LmsStudentTypedDict
from .lmstelephone import LmsTelephone, LmsTelephoneType, LmsTelephoneTypedDict
from .marketingemail import MarketingEmail, MarketingEmailType, MarketingEmailTypedDict
from .marketinglist import MarketingList, MarketingListTypedDict
from .marketingmember import MarketingMember, MarketingMemberTypedDict
from .messagingattachment import MessagingAttachment, MessagingAttachmentTypedDict
from .messagingchannel import MessagingChannel, MessagingChannelTypedDict
from .messagingmember import MessagingMember, MessagingMemberTypedDict
from .messagingmessage import MessagingMessage, MessagingMessageTypedDict
from .metadatametadata import MetadataMetadata, MetadataMetadataTypedDict
from .paymentlineitem import PaymentLineitem, PaymentLineitemTypedDict
from .paymentlink import PaymentLink, PaymentLinkTypedDict
from .paymentpayment import PaymentPayment, PaymentPaymentTypedDict
from .paymentpayout import PaymentPayout, PaymentPayoutStatus, PaymentPayoutTypedDict
from .paymentrefund import PaymentRefund, PaymentRefundStatus, PaymentRefundTypedDict
from .paymentsubscription import (
    IntervalUnit,
    PaymentSubscription,
    PaymentSubscriptionStatus,
    PaymentSubscriptionTypedDict,
)
from .property_accountingcontact_billing_address import (
    PropertyAccountingContactBillingAddress,
    PropertyAccountingContactBillingAddressTypedDict,
)
from .property_accountingcontact_shipping_address import (
    PropertyAccountingContactShippingAddress,
    PropertyAccountingContactShippingAddressTypedDict,
)
from .property_accountingorder_billing_address import (
    PropertyAccountingOrderBillingAddress,
    PropertyAccountingOrderBillingAddressTypedDict,
)
from .property_accountingorder_shipping_address import (
    PropertyAccountingOrderShippingAddress,
    PropertyAccountingOrderShippingAddressTypedDict,
)
from .property_accountingorganization_address import (
    PropertyAccountingOrganizationAddress,
    PropertyAccountingOrganizationAddressTypedDict,
)
from .property_atsactivity_from import (
    PropertyAtsActivityFrom,
    PropertyAtsActivityFromType,
    PropertyAtsActivityFromTypedDict,
)
from .property_atscandidate_address import (
    PropertyAtsCandidateAddress,
    PropertyAtsCandidateAddressTypedDict,
)
from .property_atscompany_address import (
    PropertyAtsCompanyAddress,
    PropertyAtsCompanyAddressTypedDict,
)
from .property_commercelocation_address import (
    PropertyCommerceLocationAddress,
    PropertyCommerceLocationAddressTypedDict,
)
from .property_connection_auth import (
    PropertyConnectionAuth,
    PropertyConnectionAuthMeta,
    PropertyConnectionAuthMetaTypedDict,
    PropertyConnectionAuthTypedDict,
)
from .property_connection_categories import PropertyConnectionCategories
from .property_connection_permissions import PropertyConnectionPermissions
from .property_crmcompany_address import (
    PropertyCrmCompanyAddress,
    PropertyCrmCompanyAddressTypedDict,
)
from .property_crmcontact_address import (
    PropertyCrmContactAddress,
    PropertyCrmContactAddressTypedDict,
)
from .property_crmevent_call import PropertyCrmEventCall, PropertyCrmEventCallTypedDict
from .property_crmevent_email import (
    PropertyCrmEventEmail,
    PropertyCrmEventEmailTypedDict,
)
from .property_crmevent_form import PropertyCrmEventForm, PropertyCrmEventFormTypedDict
from .property_crmevent_marketing_email import (
    PropertyCrmEventMarketingEmail,
    PropertyCrmEventMarketingEmailTypedDict,
)
from .property_crmevent_meeting import (
    PropertyCrmEventMeeting,
    PropertyCrmEventMeetingTypedDict,
)
from .property_crmevent_note import PropertyCrmEventNote, PropertyCrmEventNoteTypedDict
from .property_crmevent_page_view import (
    PropertyCrmEventPageView,
    PropertyCrmEventPageViewTypedDict,
)
from .property_crmevent_task import (
    Priority,
    PropertyCrmEventTask,
    PropertyCrmEventTaskStatus,
    PropertyCrmEventTaskTypedDict,
)
from .property_crmlead_address import (
    PropertyCrmLeadAddress,
    PropertyCrmLeadAddressTypedDict,
)
from .property_enrichcompany_address import (
    PropertyEnrichCompanyAddress,
    PropertyEnrichCompanyAddressTypedDict,
)
from .property_enrichperson_address import (
    PropertyEnrichPersonAddress,
    PropertyEnrichPersonAddressTypedDict,
)
from .property_hriscompany_address import (
    PropertyHrisCompanyAddress,
    PropertyHrisCompanyAddressTypedDict,
)
from .property_hrisemployee_address import (
    PropertyHrisEmployeeAddress,
    PropertyHrisEmployeeAddressTypedDict,
)
from .property_hrisemployee_employee_roles import PropertyHrisEmployeeEmployeeRoles
from .property_hrislocation_address import (
    PropertyHrisLocationAddress,
    PropertyHrisLocationAddressTypedDict,
)
from .property_integration_categories import PropertyIntegrationCategories
from .property_integrationsupport_webhook_events import (
    PropertyIntegrationSupportWebhookEvents,
    PropertyIntegrationSupportWebhookEventsTypedDict,
)
from .property_integrationsupport_webhook_events_created import (
    PropertyIntegrationSupportWebhookEventsCreated,
)
from .property_integrationsupport_webhook_events_deleted import (
    PropertyIntegrationSupportWebhookEventsDeleted,
)
from .property_integrationsupport_webhook_events_updated import (
    PropertyIntegrationSupportWebhookEventsUpdated,
)
from .property_lmsstudent_address import (
    PropertyLmsStudentAddress,
    PropertyLmsStudentAddressTypedDict,
)
from .property_messagingmessage_author_member import (
    PropertyMessagingMessageAuthorMember,
    PropertyMessagingMessageAuthorMemberTypedDict,
)
from .property_scimgroup_meta import (
    PropertyScimGroupMeta,
    PropertyScimGroupMetaTypedDict,
    ResourceType,
)
from .property_scimgroup_schemas import PropertyScimGroupSchemas
from .property_scimuser_meta import (
    PropertyScimUserMeta,
    PropertyScimUserMetaResourceType,
    PropertyScimUserMetaTypedDict,
)
from .property_scimuser_name import PropertyScimUserName, PropertyScimUserNameTypedDict
from .property_scimuser_schemas import PropertyScimUserSchemas
from .property_scimuser_urn_ietf_params_scim_schemas_extension_enterprise_2_0_user import (
    PropertyScimUserUrnIetfParamsScimSchemasExtensionEnterprise20User,
    PropertyScimUserUrnIetfParamsScimSchemasExtensionEnterprise20UserGender,
    PropertyScimUserUrnIetfParamsScimSchemasExtensionEnterprise20UserTypedDict,
)
from .property_scimuser_urn_ietf_params_scim_schemas_extension_enterprise_2_0_user_manager import (
    PropertyScimUserUrnIetfParamsScimSchemasExtensionEnterprise20UserManager,
    PropertyScimUserUrnIetfParamsScimSchemasExtensionEnterprise20UserManagerType,
    PropertyScimUserUrnIetfParamsScimSchemasExtensionEnterprise20UserManagerTypedDict,
)
from .property_scimuser_urn_ietf_params_scim_schemas_extension_lattice_attributes_1_0_user import (
    Ethnicity,
    PropertyScimUserUrnIetfParamsScimSchemasExtensionLatticeAttributes10User,
    PropertyScimUserUrnIetfParamsScimSchemasExtensionLatticeAttributes10UserGender,
    PropertyScimUserUrnIetfParamsScimSchemasExtensionLatticeAttributes10UserTypedDict,
    SexualOrientation,
)
from .property_scimuser_urn_ietf_params_scim_schemas_extension_peakon_2_0_user import (
    PropertyScimUserUrnIetfParamsScimSchemasExtensionPeakon20User,
    PropertyScimUserUrnIetfParamsScimSchemasExtensionPeakon20UserGender,
    PropertyScimUserUrnIetfParamsScimSchemasExtensionPeakon20UserTypedDict,
)
from .property_storagepermission_roles import PropertyStoragePermissionRoles
from .property_uccall_telephone import (
    PropertyUcCallTelephone,
    PropertyUcCallTelephoneType,
    PropertyUcCallTelephoneTypedDict,
)
from .repobranch import RepoBranch, RepoBranchTypedDict
from .repocommit import RepoCommit, RepoCommitTypedDict
from .repoorganization import RepoOrganization, RepoOrganizationTypedDict
from .repopullrequest import (
    RepoPullrequest,
    RepoPullrequestStatus,
    RepoPullrequestTypedDict,
)
from .reporepository import RepoRepository, RepoRepositoryTypedDict
from .scimaddress import ScimAddress, ScimAddressType, ScimAddressTypedDict
from .scimemail import ScimEmail, ScimEmailType, ScimEmailTypedDict
from .scimentitlement import ScimEntitlement, ScimEntitlementTypedDict
from .scimgroup import ScimGroup, ScimGroupTypedDict
from .scimgroupmember import (
    Operation,
    ScimGroupMember,
    ScimGroupMemberType,
    ScimGroupMemberTypedDict,
)
from .scimims import ScimIms, ScimImsType, ScimImsTypedDict
from .scimmanager import ScimManager, ScimManagerType, ScimManagerTypedDict
from .scimphonenumber import (
    ScimPhoneNumber,
    ScimPhoneNumberType,
    ScimPhoneNumberTypedDict,
)
from .scimphoto import ScimPhoto, ScimPhotoType, ScimPhotoTypedDict
from .scimrole import ScimRole, ScimRoleTypedDict
from .scimuser import ScimUser, ScimUserTypedDict
from .scimusergroups import ScimUserGroups, ScimUserGroupsType, ScimUserGroupsTypedDict
from .security import Security, SecurityTypedDict
from .storagefile import StorageFile, StorageFileType, StorageFileTypedDict
from .storagepermission import StoragePermission, StoragePermissionTypedDict
from .taskcomment import TaskComment, TaskCommentTypedDict
from .taskproject import TaskProject, TaskProjectTypedDict
from .tasktask import TaskTask, TaskTaskStatus, TaskTaskTypedDict
from .ticketingcustomer import TicketingCustomer, TicketingCustomerTypedDict
from .ticketingemail import TicketingEmail, TicketingEmailType, TicketingEmailTypedDict
from .ticketingnote import TicketingNote, TicketingNoteTypedDict
from .ticketingtelephone import (
    TicketingTelephone,
    TicketingTelephoneType,
    TicketingTelephoneTypedDict,
)
from .ticketingticket import (
    TicketingTicket,
    TicketingTicketStatus,
    TicketingTicketTypedDict,
)
from .uccall import UcCall, UcCallTypedDict
from .uccontact import UcContact, UcContactTypedDict
from .ucemail import UcEmail, UcEmailType, UcEmailTypedDict
from .uctelephone import UcTelephone, UcTelephoneType, UcTelephoneTypedDict
from .webhook import (
    Event,
    Meta,
    MetaTypedDict,
    ObjectType,
    Webhook,
    WebhookType,
    WebhookTypedDict,
)


__all__ = [
    "APICall",
    "APICallType",
    "APICallTypedDict",
    "AccountingAccount",
    "AccountingAccountTypedDict",
    "AccountingContact",
    "AccountingContactPaymentMethod",
    "AccountingContactPaymentMethodType",
    "AccountingContactPaymentMethodTypedDict",
    "AccountingContactTypedDict",
    "AccountingEmail",
    "AccountingEmailType",
    "AccountingEmailTypedDict",
    "AccountingInvoice",
    "AccountingInvoiceStatus",
    "AccountingInvoiceType",
    "AccountingInvoiceTypedDict",
    "AccountingJournal",
    "AccountingJournalLineitem",
    "AccountingJournalLineitemTypedDict",
    "AccountingJournalTypedDict",
    "AccountingLineitem",
    "AccountingLineitemTypedDict",
    "AccountingOrder",
    "AccountingOrderStatus",
    "AccountingOrderType",
    "AccountingOrderTypedDict",
    "AccountingOrganization",
    "AccountingOrganizationTypedDict",
    "AccountingTaxrate",
    "AccountingTaxrateTypedDict",
    "AccountingTelephone",
    "AccountingTelephoneType",
    "AccountingTelephoneTypedDict",
    "AccountingTransaction",
    "AccountingTransactionContact",
    "AccountingTransactionContactTypedDict",
    "AccountingTransactionLineItem",
    "AccountingTransactionLineItemTypedDict",
    "AccountingTransactionTypedDict",
    "AtsActivity",
    "AtsActivityType",
    "AtsActivityTypedDict",
    "AtsAddress",
    "AtsAddressTypedDict",
    "AtsApplication",
    "AtsApplicationAnswer",
    "AtsApplicationAnswerTypedDict",
    "AtsApplicationStatus",
    "AtsApplicationTypedDict",
    "AtsCandidate",
    "AtsCandidateTypedDict",
    "AtsCompany",
    "AtsCompanyTypedDict",
    "AtsCompensation",
    "AtsCompensationType",
    "AtsCompensationTypedDict",
    "AtsDocument",
    "AtsDocumentType",
    "AtsDocumentTypedDict",
    "AtsEmail",
    "AtsEmailType",
    "AtsEmailTypedDict",
    "AtsInterview",
    "AtsInterviewStatus",
    "AtsInterviewTypedDict",
    "AtsJob",
    "AtsJobQuestion",
    "AtsJobQuestionType",
    "AtsJobQuestionTypedDict",
    "AtsJobStatus",
    "AtsJobTypedDict",
    "AtsOffer",
    "AtsOfferTypedDict",
    "AtsScorecard",
    "AtsScorecardQuestion",
    "AtsScorecardQuestionTypedDict",
    "AtsScorecardTypedDict",
    "AtsStatus",
    "AtsStatusStatus",
    "AtsStatusTypedDict",
    "AtsTelephone",
    "AtsTelephoneType",
    "AtsTelephoneTypedDict",
    "CommerceCollection",
    "CommerceCollectionType",
    "CommerceCollectionTypedDict",
    "CommerceInventory",
    "CommerceInventoryRaw",
    "CommerceInventoryRawTypedDict",
    "CommerceInventoryTypedDict",
    "CommerceItem",
    "CommerceItemMedia",
    "CommerceItemMediaType",
    "CommerceItemMediaTypedDict",
    "CommerceItemMetadata",
    "CommerceItemMetadataTypedDict",
    "CommerceItemOption",
    "CommerceItemOptionTypedDict",
    "CommerceItemPrice",
    "CommerceItemPriceTypedDict",
    "CommerceItemRaw",
    "CommerceItemRawTypedDict",
    "CommerceItemTypedDict",
    "CommerceItemVariant",
    "CommerceItemVariantTypedDict",
    "CommerceLocation",
    "CommerceLocationRaw",
    "CommerceLocationRawTypedDict",
    "CommerceLocationTypedDict",
    "Connection",
    "ConnectionTypedDict",
    "ContentType",
    "CrmCompany",
    "CrmCompanyTypedDict",
    "CrmContact",
    "CrmContactTypedDict",
    "CrmDeal",
    "CrmDealTypedDict",
    "CrmEmail",
    "CrmEmailType",
    "CrmEmailTypedDict",
    "CrmEvent",
    "CrmEventFormField",
    "CrmEventFormFieldType",
    "CrmEventFormFieldTypedDict",
    "CrmEventFormOption",
    "CrmEventFormOptionTypedDict",
    "CrmEventType",
    "CrmEventTypedDict",
    "CrmLead",
    "CrmLeadTypedDict",
    "CrmPipeline",
    "CrmPipelineTypedDict",
    "CrmStage",
    "CrmStageTypedDict",
    "CrmTelephone",
    "CrmTelephoneType",
    "CrmTelephoneTypedDict",
    "EmploymentStatus",
    "EmploymentType",
    "EnrichCompany",
    "EnrichCompanyTypedDict",
    "EnrichEmail",
    "EnrichEmailType",
    "EnrichEmailTypedDict",
    "EnrichPerson",
    "EnrichPersonTypedDict",
    "EnrichPersonWorkHistory",
    "EnrichPersonWorkHistoryTypedDict",
    "EnrichTelephone",
    "EnrichTelephoneType",
    "EnrichTelephoneTypedDict",
    "Ethnicity",
    "Event",
    "ExtraData",
    "ExtraDataTypedDict",
    "Frequency",
    "FromWebhook",
    "GenaiContent",
    "GenaiContentTypedDict",
    "GenaiModel",
    "GenaiModelTypedDict",
    "GenaiPrompt",
    "GenaiPromptTypedDict",
    "Gender",
    "HrisCompany",
    "HrisCompanyTypedDict",
    "HrisCompensation",
    "HrisCompensationFrequency",
    "HrisCompensationType",
    "HrisCompensationTypedDict",
    "HrisEmail",
    "HrisEmailType",
    "HrisEmailTypedDict",
    "HrisEmployee",
    "HrisEmployeeEmploymentType",
    "HrisEmployeeGender",
    "HrisEmployeeTypedDict",
    "HrisGroup",
    "HrisGroupType",
    "HrisGroupTypedDict",
    "HrisLocation",
    "HrisLocationTypedDict",
    "HrisPayslip",
    "HrisPayslipDetail",
    "HrisPayslipDetailType",
    "HrisPayslipDetailTypedDict",
    "HrisPayslipTypedDict",
    "HrisTelephone",
    "HrisTelephoneType",
    "HrisTelephoneTypedDict",
    "HrisTimeoff",
    "HrisTimeoffStatus",
    "HrisTimeoffType",
    "HrisTimeoffTypedDict",
    "Integration",
    "IntegrationSupport",
    "IntegrationSupportTypedDict",
    "IntegrationTypedDict",
    "IntervalUnit",
    "Issue",
    "IssueStatus",
    "IssueTypedDict",
    "KmsComment",
    "KmsCommentType",
    "KmsCommentTypedDict",
    "KmsPage",
    "KmsPageMetadata",
    "KmsPageMetadataTypedDict",
    "KmsPageType",
    "KmsPageTypedDict",
    "KmsSpace",
    "KmsSpaceTypedDict",
    "ListAccountID",
    "ListApplicationID",
    "ListCandidateID",
    "ListChannelID",
    "ListClassID",
    "ListCollectionID",
    "ListCompanyID",
    "ListContactID",
    "ListCourseID",
    "ListCustomerID",
    "ListDealID",
    "ListInstructorID",
    "ListInterviewID",
    "ListInvoiceID",
    "ListItemID",
    "ListItemVariantID",
    "ListJobID",
    "ListLimit",
    "ListLinkID",
    "ListListID",
    "ListLocationID",
    "ListOffset",
    "ListOrder",
    "ListOrgID",
    "ListPageID",
    "ListParentID",
    "ListProjectID",
    "ListQuery",
    "ListRawFields",
    "ListRepoID",
    "ListRootID",
    "ListSortByCreatedAt",
    "ListSortByName",
    "ListSortByUpdatedAt",
    "ListSpaceID",
    "ListStudentID",
    "ListTaskID",
    "ListTicketID",
    "ListType",
    "ListUpdatedGte",
    "ListUserID",
    "LmsClass",
    "LmsClassTypedDict",
    "LmsCourse",
    "LmsCourseTypedDict",
    "LmsEmail",
    "LmsEmailTypedDict",
    "LmsInstructor",
    "LmsInstructorTypedDict",
    "LmsMedia",
    "LmsMediaType",
    "LmsMediaTypedDict",
    "LmsStudent",
    "LmsStudentTypedDict",
    "LmsTelephone",
    "LmsTelephoneType",
    "LmsTelephoneTypedDict",
    "MaritalStatus",
    "MarketingEmail",
    "MarketingEmailType",
    "MarketingEmailTypedDict",
    "MarketingList",
    "MarketingListTypedDict",
    "MarketingMember",
    "MarketingMemberTypedDict",
    "MessagingAttachment",
    "MessagingAttachmentTypedDict",
    "MessagingChannel",
    "MessagingChannelTypedDict",
    "MessagingMember",
    "MessagingMemberTypedDict",
    "MessagingMessage",
    "MessagingMessageTypedDict",
    "Meta",
    "MetaTypedDict",
    "MetadataMetadata",
    "MetadataMetadataTypedDict",
    "NativeWebhookParentID",
    "NativeWebhookProjectID",
    "ObjectType",
    "Operation",
    "Origin",
    "PaymentCollectionMethod",
    "PaymentLineitem",
    "PaymentLineitemTypedDict",
    "PaymentLink",
    "PaymentLinkTypedDict",
    "PaymentPayment",
    "PaymentPaymentTypedDict",
    "PaymentPayout",
    "PaymentPayoutStatus",
    "PaymentPayoutTypedDict",
    "PaymentRefund",
    "PaymentRefundStatus",
    "PaymentRefundTypedDict",
    "PaymentSubscription",
    "PaymentSubscriptionStatus",
    "PaymentSubscriptionTypedDict",
    "PaymentType",
    "Priority",
    "PropertyAccountingContactBillingAddress",
    "PropertyAccountingContactBillingAddressTypedDict",
    "PropertyAccountingContactShippingAddress",
    "PropertyAccountingContactShippingAddressTypedDict",
    "PropertyAccountingOrderBillingAddress",
    "PropertyAccountingOrderBillingAddressTypedDict",
    "PropertyAccountingOrderShippingAddress",
    "PropertyAccountingOrderShippingAddressTypedDict",
    "PropertyAccountingOrganizationAddress",
    "PropertyAccountingOrganizationAddressTypedDict",
    "PropertyAtsActivityFrom",
    "PropertyAtsActivityFromType",
    "PropertyAtsActivityFromTypedDict",
    "PropertyAtsCandidateAddress",
    "PropertyAtsCandidateAddressTypedDict",
    "PropertyAtsCompanyAddress",
    "PropertyAtsCompanyAddressTypedDict",
    "PropertyCommerceLocationAddress",
    "PropertyCommerceLocationAddressTypedDict",
    "PropertyConnectionAuth",
    "PropertyConnectionAuthMeta",
    "PropertyConnectionAuthMetaTypedDict",
    "PropertyConnectionAuthTypedDict",
    "PropertyConnectionCategories",
    "PropertyConnectionPermissions",
    "PropertyCrmCompanyAddress",
    "PropertyCrmCompanyAddressTypedDict",
    "PropertyCrmContactAddress",
    "PropertyCrmContactAddressTypedDict",
    "PropertyCrmEventCall",
    "PropertyCrmEventCallTypedDict",
    "PropertyCrmEventEmail",
    "PropertyCrmEventEmailTypedDict",
    "PropertyCrmEventForm",
    "PropertyCrmEventFormTypedDict",
    "PropertyCrmEventMarketingEmail",
    "PropertyCrmEventMarketingEmailTypedDict",
    "PropertyCrmEventMeeting",
    "PropertyCrmEventMeetingTypedDict",
    "PropertyCrmEventNote",
    "PropertyCrmEventNoteTypedDict",
    "PropertyCrmEventPageView",
    "PropertyCrmEventPageViewTypedDict",
    "PropertyCrmEventTask",
    "PropertyCrmEventTaskStatus",
    "PropertyCrmEventTaskTypedDict",
    "PropertyCrmLeadAddress",
    "PropertyCrmLeadAddressTypedDict",
    "PropertyEnrichCompanyAddress",
    "PropertyEnrichCompanyAddressTypedDict",
    "PropertyEnrichPersonAddress",
    "PropertyEnrichPersonAddressTypedDict",
    "PropertyHrisCompanyAddress",
    "PropertyHrisCompanyAddressTypedDict",
    "PropertyHrisEmployeeAddress",
    "PropertyHrisEmployeeAddressTypedDict",
    "PropertyHrisEmployeeEmployeeRoles",
    "PropertyHrisLocationAddress",
    "PropertyHrisLocationAddressTypedDict",
    "PropertyIntegrationCategories",
    "PropertyIntegrationSupportWebhookEvents",
    "PropertyIntegrationSupportWebhookEventsCreated",
    "PropertyIntegrationSupportWebhookEventsDeleted",
    "PropertyIntegrationSupportWebhookEventsTypedDict",
    "PropertyIntegrationSupportWebhookEventsUpdated",
    "PropertyLmsStudentAddress",
    "PropertyLmsStudentAddressTypedDict",
    "PropertyMessagingMessageAuthorMember",
    "PropertyMessagingMessageAuthorMemberTypedDict",
    "PropertyScimGroupMeta",
    "PropertyScimGroupMetaTypedDict",
    "PropertyScimGroupSchemas",
    "PropertyScimUserMeta",
    "PropertyScimUserMetaResourceType",
    "PropertyScimUserMetaTypedDict",
    "PropertyScimUserName",
    "PropertyScimUserNameTypedDict",
    "PropertyScimUserSchemas",
    "PropertyScimUserUrnIetfParamsScimSchemasExtensionEnterprise20User",
    "PropertyScimUserUrnIetfParamsScimSchemasExtensionEnterprise20UserGender",
    "PropertyScimUserUrnIetfParamsScimSchemasExtensionEnterprise20UserManager",
    "PropertyScimUserUrnIetfParamsScimSchemasExtensionEnterprise20UserManagerType",
    "PropertyScimUserUrnIetfParamsScimSchemasExtensionEnterprise20UserManagerTypedDict",
    "PropertyScimUserUrnIetfParamsScimSchemasExtensionEnterprise20UserTypedDict",
    "PropertyScimUserUrnIetfParamsScimSchemasExtensionLatticeAttributes10User",
    "PropertyScimUserUrnIetfParamsScimSchemasExtensionLatticeAttributes10UserGender",
    "PropertyScimUserUrnIetfParamsScimSchemasExtensionLatticeAttributes10UserTypedDict",
    "PropertyScimUserUrnIetfParamsScimSchemasExtensionPeakon20User",
    "PropertyScimUserUrnIetfParamsScimSchemasExtensionPeakon20UserGender",
    "PropertyScimUserUrnIetfParamsScimSchemasExtensionPeakon20UserTypedDict",
    "PropertyStoragePermissionRoles",
    "PropertyUcCallTelephone",
    "PropertyUcCallTelephoneType",
    "PropertyUcCallTelephoneTypedDict",
    "Raw",
    "RawTypedDict",
    "Recommendation",
    "RepoBranch",
    "RepoBranchTypedDict",
    "RepoCommit",
    "RepoCommitTypedDict",
    "RepoOrganization",
    "RepoOrganizationTypedDict",
    "RepoPullrequest",
    "RepoPullrequestStatus",
    "RepoPullrequestTypedDict",
    "RepoRepository",
    "RepoRepositoryTypedDict",
    "ResourceType",
    "Role",
    "ScimAddress",
    "ScimAddressType",
    "ScimAddressTypedDict",
    "ScimEmail",
    "ScimEmailType",
    "ScimEmailTypedDict",
    "ScimEntitlement",
    "ScimEntitlementTypedDict",
    "ScimGroup",
    "ScimGroupMember",
    "ScimGroupMemberType",
    "ScimGroupMemberTypedDict",
    "ScimGroupTypedDict",
    "ScimIms",
    "ScimImsType",
    "ScimImsTypedDict",
    "ScimManager",
    "ScimManagerType",
    "ScimManagerTypedDict",
    "ScimPhoneNumber",
    "ScimPhoneNumberType",
    "ScimPhoneNumberTypedDict",
    "ScimPhoto",
    "ScimPhotoType",
    "ScimPhotoTypedDict",
    "ScimRole",
    "ScimRoleTypedDict",
    "ScimUser",
    "ScimUserGroups",
    "ScimUserGroupsType",
    "ScimUserGroupsTypedDict",
    "ScimUserTypedDict",
    "SearchDomain",
    "SearchEmail",
    "SearchLinkedinurl",
    "SearchName",
    "SearchTwitter",
    "Security",
    "SecurityTypedDict",
    "SexualOrientation",
    "SizeUnit",
    "Status",
    "StorageFile",
    "StorageFileType",
    "StorageFileTypedDict",
    "StoragePermission",
    "StoragePermissionTypedDict",
    "TaskComment",
    "TaskCommentTypedDict",
    "TaskProject",
    "TaskProjectTypedDict",
    "TaskTask",
    "TaskTaskStatus",
    "TaskTaskTypedDict",
    "TaxExemption",
    "TicketingCustomer",
    "TicketingCustomerTypedDict",
    "TicketingEmail",
    "TicketingEmailType",
    "TicketingEmailTypedDict",
    "TicketingNote",
    "TicketingNoteTypedDict",
    "TicketingTelephone",
    "TicketingTelephoneType",
    "TicketingTelephoneTypedDict",
    "TicketingTicket",
    "TicketingTicketStatus",
    "TicketingTicketTypedDict",
    "Type",
    "UcCall",
    "UcCallTypedDict",
    "UcContact",
    "UcContactTypedDict",
    "UcEmail",
    "UcEmailType",
    "UcEmailTypedDict",
    "UcTelephone",
    "UcTelephoneType",
    "UcTelephoneTypedDict",
    "Value",
    "ValueTypedDict",
    "VirtualWebhookChannelID",
    "VirtualWebhookCompanyID",
    "VirtualWebhookContactID",
    "VirtualWebhookDealID",
    "VirtualWebhookJobID",
    "VirtualWebhookLimit",
    "VirtualWebhookParentID",
    "VirtualWebhookTicketID",
    "VirtualWebhookType",
    "VirtualWebhookUpdatedGte",
    "VirtualWebhookUserID",
    "Webhook",
    "WebhookType",
    "WebhookTypedDict",
    "WeightUnit",
]
