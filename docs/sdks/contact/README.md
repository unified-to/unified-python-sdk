# Contact

## Overview

### Available Operations

* [create_accounting_contact](#create_accounting_contact) - Create a contact
* [create_crm_contact](#create_crm_contact) - Create a contact
* [create_uc_contact](#create_uc_contact) - Create a contact
* [get_accounting_contact](#get_accounting_contact) - Retrieve a contact
* [get_crm_contact](#get_crm_contact) - Retrieve a contact
* [get_uc_contact](#get_uc_contact) - Retrieve a contact
* [list_accounting_contacts](#list_accounting_contacts) - List all contacts
* [list_crm_contacts](#list_crm_contacts) - List all contacts
* [list_uc_contacts](#list_uc_contacts) - List all contacts
* [patch_accounting_contact](#patch_accounting_contact) - Update a contact
* [patch_crm_contact](#patch_crm_contact) - Update a contact
* [patch_uc_contact](#patch_uc_contact) - Update a contact
* [remove_accounting_contact](#remove_accounting_contact) - Remove a contact
* [remove_crm_contact](#remove_crm_contact) - Remove a contact
* [remove_uc_contact](#remove_uc_contact) - Remove a contact
* [update_accounting_contact](#update_accounting_contact) - Update a contact
* [update_crm_contact](#update_crm_contact) - Update a contact
* [update_uc_contact](#update_uc_contact) - Update a contact

## create_accounting_contact

Create a contact

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingContact" method="post" path="/accounting/{connection_id}/contact" example="accounting_contact" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.contact.create_accounting_contact(request={
        "accounting_contact": {
            "associated_contacts": [
                {
                    "id": "58f146b9-e071-4991-8f11-069bd6bf5c64",
                    "name": "Delores Reynolds",
                },
                {
                    "id": "a796429a-599c-4ca1-ad43-30e50e39f50a",
                    "name": "Delores Reynolds",
                },
            ],
            "billing_address": {
                "address1": "2633 Stoney Lane",
                "address2": "Suite 176",
                "city": "Ladariusboro",
                "country_code": "US",
                "postal_code": "70131-2908",
                "region": "Illinois",
                "region_code": "NV",
            },
            "company_name": "Marquardt Inc",
            "created_at": parse_datetime("2021-08-15T14:56:50.258Z"),
            "currency": "ISK",
            "emails": [
                {
                    "email": "Delores.Reynolds10@hotmail.com",
                    "type": shared.AccountingEmailType.HOME,
                },
            ],
            "first_name": "Delores",
            "id": "59a5541c-67a2-49bf-b35b-5f6cc6eba698",
            "identification": "amicitia",
            "is_active": True,
            "is_customer": True,
            "last_name": "Reynolds",
            "name": "Delores Reynolds",
            "notes": "Caput accusamus et videlicet.",
            "payment_methods": [
                {
                    "default": True,
                    "id": "500ff164-5aaf-4cd1-89c6-2086921dbe22",
                    "name": "Visa 1234",
                    "type": shared.AccountingContactPaymentMethodType.CARD,
                },
            ],
            "portal_url": "https://scented-t-shirt.info/",
            "shipping_address": {
                "address1": "786 Renner Stream",
                "address2": "Apt. 555",
                "city": "Roanoke",
                "country_code": "US",
                "postal_code": "80686-7556",
                "region": "Vermont",
                "region_code": "NE",
            },
            "tax_exemption": shared.TaxExemption.RESALE,
            "tax_number": "amplexus",
            "telephones": [
                {
                    "telephone": "(427) 701-7160",
                    "type": shared.AccountingTelephoneType.HOME,
                },
                {
                    "telephone": "(540) 913-9171",
                    "type": shared.AccountingTelephoneType.FAX,
                },
            ],
            "updated_at": parse_datetime("2023-12-17T13:10:05.795Z"),
            "website": "https://noxious-advertisement.org",
        },
        "connection_id": "<id>",
    })

    assert res.accounting_contact is not None

    # Handle response
    print(res.accounting_contact)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAccountingContactRequest](../../models/operations/createaccountingcontactrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateAccountingContactResponse](../../models/operations/createaccountingcontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_crm_contact

Create a contact

### Example Usage

<!-- UsageSnippet language="python" operationID="createCrmContact" method="post" path="/crm/{connection_id}/contact" example="crm_contact" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.contact.create_crm_contact(request={
        "crm_contact": {
            "address": {
                "address1": "518 Brannon Burg",
                "city": "East Helenebury",
                "country_code": "US",
                "postal_code": "92622-2406",
                "region": "Vermont",
                "region_code": "AZ",
            },
            "company": "Lowe - Jakubowski",
            "created_at": parse_datetime("2021-01-02T00:41:38.885Z"),
            "department": "systematic",
            "emails": [
                {
                    "email": "Mohammad.Bartell45@hotmail.com",
                    "type": shared.CrmEmailType.HOME,
                },
                {
                    "email": "Mohammad.Bartell90@hotmail.com",
                    "type": shared.CrmEmailType.HOME,
                },
                {
                    "email": "Mohammad_Bartell@hotmail.com",
                    "type": shared.CrmEmailType.WORK,
                },
            ],
            "first_name": "Mohammad",
            "id": "dab52f0e-1def-4204-a117-5ac3fd948347",
            "image_url": "https://picsum.photos/seed/zmbPeg/2905/378",
            "last_name": "Bartell",
            "link_urls": [
                "https://limited-parade.info",
                "https://faint-papa.com/",
                "https://windy-accountability.name",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "7c8ea297-4c8e-4c75-a6bf-383a57257554",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "autem",
                },
            ],
            "name": "Mohammad Bartell",
            "telephones": [
                {
                    "telephone": "(975) 986-1658",
                    "type": shared.CrmTelephoneType.WORK,
                },
                {
                    "telephone": "(489) 332-3509",
                    "type": shared.CrmTelephoneType.HOME,
                },
                {
                    "telephone": "(205) 880-8886",
                    "type": shared.CrmTelephoneType.HOME,
                },
            ],
            "title": "National Tactics Analyst",
            "updated_at": parse_datetime("2021-02-24T02:01:06.262Z"),
        },
        "connection_id": "<id>",
    })

    assert res.crm_contact is not None

    # Handle response
    print(res.crm_contact)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateCrmContactRequest](../../models/operations/createcrmcontactrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreateCrmContactResponse](../../models/operations/createcrmcontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_uc_contact

Create a contact

### Example Usage

<!-- UsageSnippet language="python" operationID="createUcContact" method="post" path="/uc/{connection_id}/contact" example="uc_contact" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.contact.create_uc_contact(request={
        "uc_contact": {
            "company": "Tillman Group",
            "created_at": parse_datetime("2019-10-28T11:06:56.460Z"),
            "emails": [
                {
                    "email": "Luther_Rogahn32@yahoo.com",
                    "type": shared.UcEmailType.WORK,
                },
            ],
            "first_name": "Luther",
            "id": "de1b1bd4-cc69-45d1-aab7-91864b846c8a",
            "last_name": "Rogahn",
            "name": "Luther Rogahn",
            "telephones": [
                {
                    "telephone": "(809) 992-1681",
                    "type": shared.UcTelephoneType.FAX,
                },
                {
                    "telephone": "(868) 238-2746",
                    "type": shared.UcTelephoneType.HOME,
                },
                {
                    "telephone": "(219) 736-0357",
                    "type": shared.UcTelephoneType.MOBILE,
                },
            ],
            "title": "Chief Optimization Executive",
            "updated_at": parse_datetime("2023-12-05T08:36:26.614Z"),
        },
        "connection_id": "<id>",
    })

    assert res.uc_contact is not None

    # Handle response
    print(res.uc_contact)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateUcContactRequest](../../models/operations/createuccontactrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.CreateUcContactResponse](../../models/operations/createuccontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_contact

Retrieve a contact

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingContact" method="get" path="/accounting/{connection_id}/contact/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.contact.get_accounting_contact(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_contact is not None

    # Handle response
    print(res.accounting_contact)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingContactRequest](../../models/operations/getaccountingcontactrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetAccountingContactResponse](../../models/operations/getaccountingcontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_crm_contact

Retrieve a contact

### Example Usage

<!-- UsageSnippet language="python" operationID="getCrmContact" method="get" path="/crm/{connection_id}/contact/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.contact.get_crm_contact(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_contact is not None

    # Handle response
    print(res.crm_contact)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetCrmContactRequest](../../models/operations/getcrmcontactrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetCrmContactResponse](../../models/operations/getcrmcontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_uc_contact

Retrieve a contact

### Example Usage

<!-- UsageSnippet language="python" operationID="getUcContact" method="get" path="/uc/{connection_id}/contact/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.contact.get_uc_contact(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_contact is not None

    # Handle response
    print(res.uc_contact)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetUcContactRequest](../../models/operations/getuccontactrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GetUcContactResponse](../../models/operations/getuccontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_contacts

List all contacts

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingContacts" method="get" path="/accounting/{connection_id}/contact" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.contact.list_accounting_contacts(request={
        "connection_id": "<id>",
    })

    assert res.accounting_contacts is not None

    # Handle response
    print(res.accounting_contacts)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountingContactsRequest](../../models/operations/listaccountingcontactsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListAccountingContactsResponse](../../models/operations/listaccountingcontactsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_crm_contacts

List all contacts

### Example Usage

<!-- UsageSnippet language="python" operationID="listCrmContacts" method="get" path="/crm/{connection_id}/contact" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.contact.list_crm_contacts(request={
        "connection_id": "<id>",
    })

    assert res.crm_contacts is not None

    # Handle response
    print(res.crm_contacts)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListCrmContactsRequest](../../models/operations/listcrmcontactsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListCrmContactsResponse](../../models/operations/listcrmcontactsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_uc_contacts

List all contacts

### Example Usage

<!-- UsageSnippet language="python" operationID="listUcContacts" method="get" path="/uc/{connection_id}/contact" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.contact.list_uc_contacts(request={
        "connection_id": "<id>",
    })

    assert res.uc_contacts is not None

    # Handle response
    print(res.uc_contacts)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListUcContactsRequest](../../models/operations/listuccontactsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListUcContactsResponse](../../models/operations/listuccontactsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_contact

Update a contact

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingContact" method="patch" path="/accounting/{connection_id}/contact/{id}" example="accounting_contact" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.contact.patch_accounting_contact(request={
        "accounting_contact": {
            "associated_contacts": [
                {
                    "id": "b31a900c-87d4-4f03-a7a1-c5a03882cfab",
                    "name": "Delores Reynolds",
                },
                {
                    "id": "efc216ad-c193-4556-ace1-4ee83af4e484",
                    "name": "Delores Reynolds",
                },
            ],
            "billing_address": {
                "address1": "2633 Stoney Lane",
                "address2": "Suite 176",
                "city": "Ladariusboro",
                "country_code": "US",
                "postal_code": "70131-2908",
                "region": "Illinois",
                "region_code": "NV",
            },
            "company_name": "Marquardt Inc",
            "created_at": parse_datetime("2021-08-15T14:56:50.258Z"),
            "currency": "ISK",
            "emails": [
                {
                    "email": "Delores.Reynolds10@hotmail.com",
                    "type": shared.AccountingEmailType.HOME,
                },
            ],
            "first_name": "Delores",
            "id": "e615b98f-39db-496d-a866-1f3e55dee199",
            "identification": "amicitia",
            "is_active": True,
            "is_customer": True,
            "last_name": "Reynolds",
            "name": "Delores Reynolds",
            "notes": "Caput accusamus et videlicet.",
            "payment_methods": [
                {
                    "default": True,
                    "id": "d01c28f5-1076-4ea0-a40c-22221ba86846",
                    "name": "Visa 1234",
                    "type": shared.AccountingContactPaymentMethodType.CARD,
                },
            ],
            "portal_url": "https://scented-t-shirt.info/",
            "shipping_address": {
                "address1": "786 Renner Stream",
                "address2": "Apt. 555",
                "city": "Roanoke",
                "country_code": "US",
                "postal_code": "80686-7556",
                "region": "Vermont",
                "region_code": "NE",
            },
            "tax_exemption": shared.TaxExemption.RESALE,
            "tax_number": "amplexus",
            "telephones": [
                {
                    "telephone": "(427) 701-7160",
                    "type": shared.AccountingTelephoneType.HOME,
                },
                {
                    "telephone": "(540) 913-9171",
                    "type": shared.AccountingTelephoneType.FAX,
                },
            ],
            "updated_at": parse_datetime("2023-12-17T13:10:05.808Z"),
            "website": "https://noxious-advertisement.org",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_contact is not None

    # Handle response
    print(res.accounting_contact)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchAccountingContactRequest](../../models/operations/patchaccountingcontactrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchAccountingContactResponse](../../models/operations/patchaccountingcontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_crm_contact

Update a contact

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCrmContact" method="patch" path="/crm/{connection_id}/contact/{id}" example="crm_contact" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.contact.patch_crm_contact(request={
        "crm_contact": {
            "address": {
                "address1": "518 Brannon Burg",
                "city": "East Helenebury",
                "country_code": "US",
                "postal_code": "92622-2406",
                "region": "Vermont",
                "region_code": "AZ",
            },
            "company": "Lowe - Jakubowski",
            "created_at": parse_datetime("2021-01-02T00:41:38.885Z"),
            "department": "systematic",
            "emails": [
                {
                    "email": "Mohammad.Bartell45@hotmail.com",
                    "type": shared.CrmEmailType.HOME,
                },
                {
                    "email": "Mohammad.Bartell90@hotmail.com",
                    "type": shared.CrmEmailType.HOME,
                },
                {
                    "email": "Mohammad_Bartell@hotmail.com",
                    "type": shared.CrmEmailType.WORK,
                },
            ],
            "first_name": "Mohammad",
            "id": "c20cb19e-95ab-4b71-b88e-53674e888910",
            "image_url": "https://picsum.photos/seed/zmbPeg/2905/378",
            "last_name": "Bartell",
            "link_urls": [
                "https://limited-parade.info",
                "https://faint-papa.com/",
                "https://windy-accountability.name",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "a34b11e4-3163-43ea-a49d-98fc85959577",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "autem",
                },
            ],
            "name": "Mohammad Bartell",
            "telephones": [
                {
                    "telephone": "(975) 986-1658",
                    "type": shared.CrmTelephoneType.WORK,
                },
                {
                    "telephone": "(489) 332-3509",
                    "type": shared.CrmTelephoneType.HOME,
                },
                {
                    "telephone": "(205) 880-8886",
                    "type": shared.CrmTelephoneType.HOME,
                },
            ],
            "title": "National Tactics Analyst",
            "updated_at": parse_datetime("2021-02-24T02:01:06.262Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_contact is not None

    # Handle response
    print(res.crm_contact)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchCrmContactRequest](../../models/operations/patchcrmcontactrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchCrmContactResponse](../../models/operations/patchcrmcontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_uc_contact

Update a contact

### Example Usage

<!-- UsageSnippet language="python" operationID="patchUcContact" method="patch" path="/uc/{connection_id}/contact/{id}" example="uc_contact" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.contact.patch_uc_contact(request={
        "uc_contact": {
            "company": "Tillman Group",
            "created_at": parse_datetime("2019-10-28T11:06:56.460Z"),
            "emails": [
                {
                    "email": "Luther_Rogahn32@yahoo.com",
                    "type": shared.UcEmailType.WORK,
                },
            ],
            "first_name": "Luther",
            "id": "a68a0d0b-75b8-43ca-94cf-630cbc976888",
            "last_name": "Rogahn",
            "name": "Luther Rogahn",
            "telephones": [
                {
                    "telephone": "(809) 992-1681",
                    "type": shared.UcTelephoneType.FAX,
                },
                {
                    "telephone": "(868) 238-2746",
                    "type": shared.UcTelephoneType.HOME,
                },
                {
                    "telephone": "(219) 736-0357",
                    "type": shared.UcTelephoneType.MOBILE,
                },
            ],
            "title": "Chief Optimization Executive",
            "updated_at": parse_datetime("2023-12-05T08:36:26.618Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_contact is not None

    # Handle response
    print(res.uc_contact)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchUcContactRequest](../../models/operations/patchuccontactrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.PatchUcContactResponse](../../models/operations/patchuccontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_contact

Remove a contact

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingContact" method="delete" path="/accounting/{connection_id}/contact/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.contact.remove_accounting_contact(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveAccountingContactRequest](../../models/operations/removeaccountingcontactrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveAccountingContactResponse](../../models/operations/removeaccountingcontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_crm_contact

Remove a contact

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCrmContact" method="delete" path="/crm/{connection_id}/contact/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.contact.remove_crm_contact(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.RemoveCrmContactRequest](../../models/operations/removecrmcontactrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemoveCrmContactResponse](../../models/operations/removecrmcontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_uc_contact

Remove a contact

### Example Usage

<!-- UsageSnippet language="python" operationID="removeUcContact" method="delete" path="/uc/{connection_id}/contact/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.contact.remove_uc_contact(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.RemoveUcContactRequest](../../models/operations/removeuccontactrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.RemoveUcContactResponse](../../models/operations/removeuccontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_contact

Update a contact

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingContact" method="put" path="/accounting/{connection_id}/contact/{id}" example="accounting_contact" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.contact.update_accounting_contact(request={
        "accounting_contact": {
            "associated_contacts": [
                {
                    "id": "b31a900c-87d4-4f03-a7a1-c5a03882cfab",
                    "name": "Delores Reynolds",
                },
                {
                    "id": "efc216ad-c193-4556-ace1-4ee83af4e484",
                    "name": "Delores Reynolds",
                },
            ],
            "billing_address": {
                "address1": "2633 Stoney Lane",
                "address2": "Suite 176",
                "city": "Ladariusboro",
                "country_code": "US",
                "postal_code": "70131-2908",
                "region": "Illinois",
                "region_code": "NV",
            },
            "company_name": "Marquardt Inc",
            "created_at": parse_datetime("2021-08-15T14:56:50.258Z"),
            "currency": "ISK",
            "emails": [
                {
                    "email": "Delores.Reynolds10@hotmail.com",
                    "type": shared.AccountingEmailType.HOME,
                },
            ],
            "first_name": "Delores",
            "id": "e615b98f-39db-496d-a866-1f3e55dee199",
            "identification": "amicitia",
            "is_active": True,
            "is_customer": True,
            "last_name": "Reynolds",
            "name": "Delores Reynolds",
            "notes": "Caput accusamus et videlicet.",
            "payment_methods": [
                {
                    "default": True,
                    "id": "d01c28f5-1076-4ea0-a40c-22221ba86846",
                    "name": "Visa 1234",
                    "type": shared.AccountingContactPaymentMethodType.CARD,
                },
            ],
            "portal_url": "https://scented-t-shirt.info/",
            "shipping_address": {
                "address1": "786 Renner Stream",
                "address2": "Apt. 555",
                "city": "Roanoke",
                "country_code": "US",
                "postal_code": "80686-7556",
                "region": "Vermont",
                "region_code": "NE",
            },
            "tax_exemption": shared.TaxExemption.RESALE,
            "tax_number": "amplexus",
            "telephones": [
                {
                    "telephone": "(427) 701-7160",
                    "type": shared.AccountingTelephoneType.HOME,
                },
                {
                    "telephone": "(540) 913-9171",
                    "type": shared.AccountingTelephoneType.FAX,
                },
            ],
            "updated_at": parse_datetime("2023-12-17T13:10:05.808Z"),
            "website": "https://noxious-advertisement.org",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_contact is not None

    # Handle response
    print(res.accounting_contact)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateAccountingContactRequest](../../models/operations/updateaccountingcontactrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateAccountingContactResponse](../../models/operations/updateaccountingcontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_crm_contact

Update a contact

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCrmContact" method="put" path="/crm/{connection_id}/contact/{id}" example="crm_contact" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.contact.update_crm_contact(request={
        "crm_contact": {
            "address": {
                "address1": "518 Brannon Burg",
                "city": "East Helenebury",
                "country_code": "US",
                "postal_code": "92622-2406",
                "region": "Vermont",
                "region_code": "AZ",
            },
            "company": "Lowe - Jakubowski",
            "created_at": parse_datetime("2021-01-02T00:41:38.885Z"),
            "department": "systematic",
            "emails": [
                {
                    "email": "Mohammad.Bartell45@hotmail.com",
                    "type": shared.CrmEmailType.HOME,
                },
                {
                    "email": "Mohammad.Bartell90@hotmail.com",
                    "type": shared.CrmEmailType.HOME,
                },
                {
                    "email": "Mohammad_Bartell@hotmail.com",
                    "type": shared.CrmEmailType.WORK,
                },
            ],
            "first_name": "Mohammad",
            "id": "c20cb19e-95ab-4b71-b88e-53674e888910",
            "image_url": "https://picsum.photos/seed/zmbPeg/2905/378",
            "last_name": "Bartell",
            "link_urls": [
                "https://limited-parade.info",
                "https://faint-papa.com/",
                "https://windy-accountability.name",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "a34b11e4-3163-43ea-a49d-98fc85959577",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "autem",
                },
            ],
            "name": "Mohammad Bartell",
            "telephones": [
                {
                    "telephone": "(975) 986-1658",
                    "type": shared.CrmTelephoneType.WORK,
                },
                {
                    "telephone": "(489) 332-3509",
                    "type": shared.CrmTelephoneType.HOME,
                },
                {
                    "telephone": "(205) 880-8886",
                    "type": shared.CrmTelephoneType.HOME,
                },
            ],
            "title": "National Tactics Analyst",
            "updated_at": parse_datetime("2021-02-24T02:01:06.262Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_contact is not None

    # Handle response
    print(res.crm_contact)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateCrmContactRequest](../../models/operations/updatecrmcontactrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdateCrmContactResponse](../../models/operations/updatecrmcontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_uc_contact

Update a contact

### Example Usage

<!-- UsageSnippet language="python" operationID="updateUcContact" method="put" path="/uc/{connection_id}/contact/{id}" example="uc_contact" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.contact.update_uc_contact(request={
        "uc_contact": {
            "company": "Tillman Group",
            "created_at": parse_datetime("2019-10-28T11:06:56.460Z"),
            "emails": [
                {
                    "email": "Luther_Rogahn32@yahoo.com",
                    "type": shared.UcEmailType.WORK,
                },
            ],
            "first_name": "Luther",
            "id": "a68a0d0b-75b8-43ca-94cf-630cbc976888",
            "last_name": "Rogahn",
            "name": "Luther Rogahn",
            "telephones": [
                {
                    "telephone": "(809) 992-1681",
                    "type": shared.UcTelephoneType.FAX,
                },
                {
                    "telephone": "(868) 238-2746",
                    "type": shared.UcTelephoneType.HOME,
                },
                {
                    "telephone": "(219) 736-0357",
                    "type": shared.UcTelephoneType.MOBILE,
                },
            ],
            "title": "Chief Optimization Executive",
            "updated_at": parse_datetime("2023-12-05T08:36:26.618Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_contact is not None

    # Handle response
    print(res.uc_contact)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateUcContactRequest](../../models/operations/updateuccontactrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.UpdateUcContactResponse](../../models/operations/updateuccontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |