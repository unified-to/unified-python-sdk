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
            "associated_contacts": [],
            "balance_amount": 55574.0,
            "billing_address": {
                "address1": "4091 Tromp Coves",
                "city": "Lake Emmybury",
                "country_code": "US",
                "postal_code": "50764-5226",
                "region": "Washington",
                "region_code": "CA",
            },
            "company_name": "Kertzmann Group",
            "created_at": parse_datetime("2021-08-15T14:56:50.258Z"),
            "currency": "AUD",
            "emails": [
                {
                    "email": "delores.reynolds@kertzmanngroup.com",
                    "type": shared.AccountingEmailType.WORK,
                },
                {
                    "email": "accounts@kertzmanngroup.com",
                    "type": shared.AccountingEmailType.OTHER,
                },
            ],
            "first_name": "Delores",
            "id": "4b985b9a-65ff-4d96-bbf2-afb487afe6e6",
            "identification": "531850872",
            "is_active": True,
            "is_customer": True,
            "last_name": "Reynolds",
            "metadata": [],
            "name": "Kertzmann Group",
            "notes": "Et videlicet pauci.",
            "payment_methods": [
                {
                    "default": True,
                    "id": "888a5045-1b70-4854-ae2d-221aceaac24a",
                    "name": "Visa 7844",
                    "type": shared.AccountingContactPaymentMethodType.CARD,
                },
            ],
            "portal_url": "https://kertzmanngroup.com/billing",
            "shipping_address": {
                "address1": "23129 Rebekah Mews",
                "city": "Mortimerhaven",
                "country_code": "US",
                "postal_code": "55878-6806",
                "region": "Florida",
                "region_code": "OK",
            },
            "tax_exemption": shared.TaxExemption.FOREIGN,
            "tax_number": "867556410",
            "telephones": [
                {
                    "telephone": "(432) 760-1716",
                    "type": shared.AccountingTelephoneType.FAX,
                },
            ],
            "updated_at": parse_datetime("2023-12-19T07:40:07.518Z"),
            "website": "https://kertzmanngroup.com",
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
                "address1": "65838 College Avenue",
                "address2": "Apt. 335",
                "city": "Fort Alexandratown",
                "country_code": "US",
                "postal_code": "80888-6094",
                "region": "Montana",
                "region_code": "NM",
            },
            "created_at": parse_datetime("2021-01-02T00:41:38.885Z"),
            "department": "Beauty",
            "emails": [
                {
                    "email": "mohammad.bartell@hotmail.com",
                    "type": shared.CrmEmailType.HOME,
                },
            ],
            "first_name": "Mohammad",
            "id": "bbcb70c6-5e6a-49ca-a8eb-cf27c0ddb292",
            "image_url": "https://avatars.githubusercontent.com/u/26803724",
            "last_name": "Bartell",
            "link_urls": [
                "https://www.linkedin.com/in/mohammad-bartell",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "283434f1-33c2-4ca0-9698-8f777afd037c",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "antiquus",
                },
            ],
            "name": "Mohammad Bartell",
            "telephones": [
                {
                    "telephone": "(254) 404-3529",
                    "type": shared.CrmTelephoneType.OTHER,
                },
                {
                    "telephone": "(469) 989-7588",
                    "type": shared.CrmTelephoneType.WORK,
                },
            ],
            "title": "National Tactics Analyst",
            "updated_at": parse_datetime("2021-02-24T04:22:37.378Z"),
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
            "id": "3ced7f4f-7bf5-42ec-88c9-6e47316705e7",
            "last_name": "Rogahn",
            "metadata": [],
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
            "updated_at": parse_datetime("2023-12-07T15:56:26.134Z"),
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
            "associated_contacts": [],
            "balance_amount": 55574.0,
            "billing_address": {
                "address1": "4091 Tromp Coves",
                "city": "Lake Emmybury",
                "country_code": "US",
                "postal_code": "50764-5226",
                "region": "Washington",
                "region_code": "CA",
            },
            "company_name": "Kertzmann Group",
            "created_at": parse_datetime("2021-08-15T14:56:50.258Z"),
            "currency": "AUD",
            "emails": [
                {
                    "email": "delores.reynolds@kertzmanngroup.com",
                    "type": shared.AccountingEmailType.WORK,
                },
                {
                    "email": "accounts@kertzmanngroup.com",
                    "type": shared.AccountingEmailType.OTHER,
                },
            ],
            "first_name": "Delores",
            "id": "c68927a3-7321-4c55-9a75-c9e203870e52",
            "identification": "531850872",
            "is_active": True,
            "is_customer": True,
            "last_name": "Reynolds",
            "metadata": [],
            "name": "Kertzmann Group",
            "notes": "Et videlicet pauci.",
            "payment_methods": [
                {
                    "default": True,
                    "id": "57d6ffc5-f8d4-40da-8c97-5568f8253ff7",
                    "name": "Visa 7844",
                    "type": shared.AccountingContactPaymentMethodType.CARD,
                },
            ],
            "portal_url": "https://kertzmanngroup.com/billing",
            "shipping_address": {
                "address1": "23129 Rebekah Mews",
                "city": "Mortimerhaven",
                "country_code": "US",
                "postal_code": "55878-6806",
                "region": "Florida",
                "region_code": "OK",
            },
            "tax_exemption": shared.TaxExemption.FOREIGN,
            "tax_number": "867556410",
            "telephones": [
                {
                    "telephone": "(432) 760-1716",
                    "type": shared.AccountingTelephoneType.FAX,
                },
            ],
            "updated_at": parse_datetime("2023-12-19T07:40:07.543Z"),
            "website": "https://kertzmanngroup.com",
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
                "address1": "65838 College Avenue",
                "address2": "Apt. 335",
                "city": "Fort Alexandratown",
                "country_code": "US",
                "postal_code": "80888-6094",
                "region": "Montana",
                "region_code": "NM",
            },
            "created_at": parse_datetime("2021-01-02T00:41:38.885Z"),
            "department": "Beauty",
            "emails": [
                {
                    "email": "mohammad.bartell@hotmail.com",
                    "type": shared.CrmEmailType.HOME,
                },
            ],
            "first_name": "Mohammad",
            "id": "7c0eb65f-ece5-4b77-afda-c8f2b0641a85",
            "image_url": "https://avatars.githubusercontent.com/u/26803724",
            "last_name": "Bartell",
            "link_urls": [
                "https://www.linkedin.com/in/mohammad-bartell",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "bc473062-bddc-4261-a510-183ff8082bd9",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "antiquus",
                },
            ],
            "name": "Mohammad Bartell",
            "telephones": [
                {
                    "telephone": "(254) 404-3529",
                    "type": shared.CrmTelephoneType.OTHER,
                },
                {
                    "telephone": "(469) 989-7588",
                    "type": shared.CrmTelephoneType.WORK,
                },
            ],
            "title": "National Tactics Analyst",
            "updated_at": parse_datetime("2021-02-24T04:22:37.378Z"),
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
            "id": "5fed26b9-5419-4e72-a1a9-52672864c4d1",
            "last_name": "Rogahn",
            "metadata": [],
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
            "updated_at": parse_datetime("2023-12-07T15:56:26.141Z"),
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
            "associated_contacts": [],
            "balance_amount": 55574.0,
            "billing_address": {
                "address1": "4091 Tromp Coves",
                "city": "Lake Emmybury",
                "country_code": "US",
                "postal_code": "50764-5226",
                "region": "Washington",
                "region_code": "CA",
            },
            "company_name": "Kertzmann Group",
            "created_at": parse_datetime("2021-08-15T14:56:50.258Z"),
            "currency": "AUD",
            "emails": [
                {
                    "email": "delores.reynolds@kertzmanngroup.com",
                    "type": shared.AccountingEmailType.WORK,
                },
                {
                    "email": "accounts@kertzmanngroup.com",
                    "type": shared.AccountingEmailType.OTHER,
                },
            ],
            "first_name": "Delores",
            "id": "c68927a3-7321-4c55-9a75-c9e203870e52",
            "identification": "531850872",
            "is_active": True,
            "is_customer": True,
            "last_name": "Reynolds",
            "metadata": [],
            "name": "Kertzmann Group",
            "notes": "Et videlicet pauci.",
            "payment_methods": [
                {
                    "default": True,
                    "id": "57d6ffc5-f8d4-40da-8c97-5568f8253ff7",
                    "name": "Visa 7844",
                    "type": shared.AccountingContactPaymentMethodType.CARD,
                },
            ],
            "portal_url": "https://kertzmanngroup.com/billing",
            "shipping_address": {
                "address1": "23129 Rebekah Mews",
                "city": "Mortimerhaven",
                "country_code": "US",
                "postal_code": "55878-6806",
                "region": "Florida",
                "region_code": "OK",
            },
            "tax_exemption": shared.TaxExemption.FOREIGN,
            "tax_number": "867556410",
            "telephones": [
                {
                    "telephone": "(432) 760-1716",
                    "type": shared.AccountingTelephoneType.FAX,
                },
            ],
            "updated_at": parse_datetime("2023-12-19T07:40:07.543Z"),
            "website": "https://kertzmanngroup.com",
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
                "address1": "65838 College Avenue",
                "address2": "Apt. 335",
                "city": "Fort Alexandratown",
                "country_code": "US",
                "postal_code": "80888-6094",
                "region": "Montana",
                "region_code": "NM",
            },
            "created_at": parse_datetime("2021-01-02T00:41:38.885Z"),
            "department": "Beauty",
            "emails": [
                {
                    "email": "mohammad.bartell@hotmail.com",
                    "type": shared.CrmEmailType.HOME,
                },
            ],
            "first_name": "Mohammad",
            "id": "7c0eb65f-ece5-4b77-afda-c8f2b0641a85",
            "image_url": "https://avatars.githubusercontent.com/u/26803724",
            "last_name": "Bartell",
            "link_urls": [
                "https://www.linkedin.com/in/mohammad-bartell",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "bc473062-bddc-4261-a510-183ff8082bd9",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "antiquus",
                },
            ],
            "name": "Mohammad Bartell",
            "telephones": [
                {
                    "telephone": "(254) 404-3529",
                    "type": shared.CrmTelephoneType.OTHER,
                },
                {
                    "telephone": "(469) 989-7588",
                    "type": shared.CrmTelephoneType.WORK,
                },
            ],
            "title": "National Tactics Analyst",
            "updated_at": parse_datetime("2021-02-24T04:22:37.378Z"),
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
            "id": "5fed26b9-5419-4e72-a1a9-52672864c4d1",
            "last_name": "Rogahn",
            "metadata": [],
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
            "updated_at": parse_datetime("2023-12-07T15:56:26.141Z"),
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