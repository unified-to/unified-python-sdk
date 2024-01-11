"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .accountingaccount import *
from .accountingcustomer import *
from .accountingemail import *
from .accountinginvoice import *
from .accountingitem import *
from .accountinglineitem import *
from .accountingorganization import *
from .accountingpayment import *
from .accountingtaxrate import *
from .accountingtelephone import *
from .accountingtransaction import *
from .accountingtransactionlineitem import *
from .apicall import *
from .atsaddress import *
from .atsapplication import *
from .atscandidate import *
from .atscompensation import *
from .atsdocument import *
from .atsemail import *
from .atsinterview import *
from .atsjob import *
from .atsscorecard import *
from .atsstatus import *
from .atstelephone import *
from .connection import *
from .crmcompany import *
from .crmcontact import *
from .crmdeal import *
from .crmemail import *
from .crmevent import *
from .crmfile import *
from .crmlead import *
from .crmpipeline import *
from .crmtelephone import *
from .enrichcompany import *
from .enrichemail import *
from .enrichperson import *
from .enrichpersonworkhistory import *
from .enrichtelephone import *
from .hrisemail import *
from .hrisemployee import *
from .hrisgroup import *
from .hristelephone import *
from .integration import *
from .integrationsupport import *
from .marketingemail import *
from .marketinglist import *
from .marketingmember import *
from .property_accountingaccount_raw import *
from .property_accountingcustomer_billing_address import *
from .property_accountingcustomer_raw import *
from .property_accountingcustomer_shipping_address import *
from .property_accountinginvoice_raw import *
from .property_accountingitem_raw import *
from .property_accountinglineitem_raw import *
from .property_accountingorganization_address import *
from .property_accountingorganization_raw import *
from .property_accountingpayment_raw import *
from .property_accountingtaxrate_raw import *
from .property_accountingtransaction_raw import *
from .property_atsapplication_raw import *
from .property_atscandidate_address import *
from .property_atscandidate_raw import *
from .property_atsdocument_raw import *
from .property_atsinterview_raw import *
from .property_atsjob_raw import *
from .property_atsscorecard_raw import *
from .property_atsstatus_raw import *
from .property_connection_auth import *
from .property_connection_categories import *
from .property_connection_permissions import *
from .property_crmcompany_address import *
from .property_crmcompany_raw import *
from .property_crmcontact_address import *
from .property_crmcontact_raw import *
from .property_crmdeal_raw import *
from .property_crmevent_call import *
from .property_crmevent_email import *
from .property_crmevent_meeting import *
from .property_crmevent_note import *
from .property_crmevent_raw import *
from .property_crmevent_task import *
from .property_crmfile_raw import *
from .property_crmlead_address import *
from .property_crmlead_raw import *
from .property_crmpipeline_raw import *
from .property_enrichcompany_address import *
from .property_enrichcompany_raw import *
from .property_enrichperson_address import *
from .property_enrichperson_raw import *
from .property_hrisemployee_address import *
from .property_hrisemployee_raw import *
from .property_hrisgroup_raw import *
from .property_integration_categories import *
from .property_integrationsupport_inbound_fields import *
from .property_integrationsupport_outbound_fields import *
from .property_integrationsupport_webhook_events import *
from .property_marketinglist_raw import *
from .property_marketingmember_raw import *
from .property_property_connection_auth_meta import *
from .property_storagefile_raw import *
from .property_storagepermission_roles import *
from .property_ticketingcustomer_raw import *
from .property_ticketingnote_raw import *
from .property_ticketingticket_raw import *
from .property_uccall_raw import *
from .property_uccall_telephone import *
from .property_uccontact_raw import *
from .property_webhook_meta import *
from .security import *
from .storagefile import *
from .storagepermission import *
from .ticketingcustomer import *
from .ticketingemail import *
from .ticketingnote import *
from .ticketingtelephone import *
from .ticketingticket import *
from .uccall import *
from .uccontact import *
from .ucemail import *
from .uctelephone import *
from .undefined import *
from .webhook import *

__all__ = ["APICall","APICallType","AccountingAccount","AccountingCustomer","AccountingEmail","AccountingEmailType","AccountingInvoice","AccountingInvoiceStatus","AccountingItem","AccountingLineitem","AccountingOrganization","AccountingPayment","AccountingTaxrate","AccountingTelephone","AccountingTelephoneType","AccountingTransaction","AccountingTransactionLineitem","AccountingTransactionType","AtsAddress","AtsApplication","AtsApplicationStatus","AtsCandidate","AtsCompensation","AtsCompensationType","AtsDocument","AtsDocumentType","AtsEmail","AtsEmailType","AtsInterview","AtsInterviewStatus","AtsJob","AtsJobStatus","AtsScorecard","AtsStatus","AtsStatusStatus","AtsTelephone","AtsTelephoneType","Connection","CrmCompany","CrmContact","CrmDeal","CrmEmail","CrmEmailType","CrmEvent","CrmEventType","CrmFile","CrmLead","CrmPipeline","CrmTelephone","CrmTelephoneType","EmploymentStatus","EmploymentType","EnrichCompany","EnrichEmail","EnrichEmailType","EnrichPerson","EnrichPersonWorkHistory","EnrichTelephone","EnrichTelephoneType","Event","Frequency","Gender","HrisEmail","HrisEmailType","HrisEmployee","HrisEmployeeEmploymentType","HrisEmployeeGender","HrisGroup","HrisGroupType","HrisTelephone","HrisTelephoneType","Integration","IntegrationSupport","MaritalStatus","MarketingEmail","MarketingEmailType","MarketingList","MarketingMember","ObjectType","PropertyAccountingAccountRaw","PropertyAccountingCustomerBillingAddress","PropertyAccountingCustomerRaw","PropertyAccountingCustomerShippingAddress","PropertyAccountingInvoiceRaw","PropertyAccountingItemRaw","PropertyAccountingLineitemRaw","PropertyAccountingOrganizationAddress","PropertyAccountingOrganizationRaw","PropertyAccountingPaymentRaw","PropertyAccountingTaxrateRaw","PropertyAccountingTransactionRaw","PropertyAtsApplicationRaw","PropertyAtsCandidateAddress","PropertyAtsCandidateRaw","PropertyAtsDocumentRaw","PropertyAtsInterviewRaw","PropertyAtsJobRaw","PropertyAtsScorecardRaw","PropertyAtsStatusRaw","PropertyConnectionAuth","PropertyConnectionCategories","PropertyConnectionPermissions","PropertyCrmCompanyAddress","PropertyCrmCompanyRaw","PropertyCrmContactAddress","PropertyCrmContactRaw","PropertyCrmDealRaw","PropertyCrmEventCall","PropertyCrmEventEmail","PropertyCrmEventMeeting","PropertyCrmEventNote","PropertyCrmEventRaw","PropertyCrmEventTask","PropertyCrmEventTaskStatus","PropertyCrmFileRaw","PropertyCrmLeadAddress","PropertyCrmLeadRaw","PropertyCrmPipelineRaw","PropertyEnrichCompanyAddress","PropertyEnrichCompanyRaw","PropertyEnrichPersonAddress","PropertyEnrichPersonRaw","PropertyHrisEmployeeAddress","PropertyHrisEmployeeRaw","PropertyHrisGroupRaw","PropertyIntegrationCategories","PropertyIntegrationSupportInboundFields","PropertyIntegrationSupportOutboundFields","PropertyIntegrationSupportWebhookEvents","PropertyMarketingListRaw","PropertyMarketingMemberRaw","PropertyPropertyConnectionAuthMeta","PropertyStorageFileRaw","PropertyStoragePermissionRoles","PropertyTicketingCustomerRaw","PropertyTicketingNoteRaw","PropertyTicketingTicketRaw","PropertyUcCallRaw","PropertyUcCallTelephone","PropertyUcCallTelephoneType","PropertyUcContactRaw","PropertyWebhookMeta","Recommendation","Security","Status","StorageFile","StorageFileType","StoragePermission","TaxExemption","TicketingCustomer","TicketingEmail","TicketingEmailType","TicketingNote","TicketingTelephone","TicketingTelephoneType","TicketingTicket","TicketingTicketStatus","Type","UcCall","UcContact","UcEmail","UcEmailType","UcTelephone","UcTelephoneType","Undefined","Webhook","WebhookType","WebhookWebhookType"]
