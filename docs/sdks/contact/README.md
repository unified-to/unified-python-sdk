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

Creates a AccountingContact. Provide the unified AccountingContact fields in the request body; they are mapped to the provider's API. Returns the created AccountingContact.

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
                "address1": "9171 Parisian Gateway",
                "city": "Lake Keltonboro",
                "country_code": "US",
                "postal_code": "70131-2908",
                "region": "Illinois",
                "region_code": "CO",
            },
            "company_name": "Rice LLC",
            "created_at": parse_datetime("2021-08-15T14:56:50.258Z"),
            "currency": "AUD",
            "emails": [
                {
                    "email": "michele.breitenberg@ricellc.com",
                    "type": shared.AccountingEmailType.WORK,
                },
                {
                    "email": "accounts@ricellc.com",
                    "type": shared.AccountingEmailType.OTHER,
                },
            ],
            "first_name": "Michele",
            "id": "6ffdfe98-c45a-42be-8eac-998457211a68",
            "identification": "508720595",
            "is_active": True,
            "is_customer": True,
            "last_name": "Breitenberg",
            "metadata": [],
            "name": "Rice LLC",
            "notes": "Tabella reprehenderit sono corrupti approbo crastinus sopor ultra.",
            "payment_methods": [
                {
                    "default": True,
                    "id": "43c7beab-abc7-4d66-ad33-b212013439d3",
                    "name": "Visa 5318",
                    "type": shared.AccountingContactPaymentMethodType.CARD,
                },
            ],
            "portal_url": "https://ricellc.com/billing",
            "shipping_address": {
                "address1": "786 Dare Meadows",
                "city": "Phoenix",
                "country_code": "US",
                "postal_code": "68675",
                "region": "Tennessee",
                "region_code": "NE",
            },
            "tax_exemption": shared.TaxExemption.FOREIGN,
            "tax_number": "564107844",
            "telephones": [
                {
                    "telephone": "(217) 260-4409",
                    "type": shared.AccountingTelephoneType.FAX,
                },
            ],
            "updated_at": parse_datetime("2024-01-05T03:13:26.378Z"),
            "website": "https://ricellc.com",
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

Creates a CrmContact. Provide the unified CrmContact fields in the request body; they are mapped to the provider's API. Returns the created CrmContact.

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
                "address1": "489 Eula Park",
                "address2": "Apt. 900",
                "city": "Archfield",
                "country_code": "US",
                "postal_code": "60941-8210",
                "region": "Texas",
                "region_code": "NH",
            },
            "created_at": parse_datetime("2021-01-02T00:41:38.885Z"),
            "department": "Health",
            "emails": [
                {
                    "email": "alexandro.kuphal@hotmail.com",
                    "type": shared.CrmEmailType.HOME,
                },
            ],
            "first_name": "Alexandro",
            "id": "0cb9e92a-f41d-4c8d-8e65-b3925244f5ff",
            "image_url": "https://avatars.githubusercontent.com/u/26594214",
            "last_name": "Kuphal",
            "link_urls": [
                "https://www.linkedin.com/in/alexandro-kuphal",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "37cef42c-e539-4916-b606-cdacb8c627e8",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "amplus",
                },
            ],
            "name": "Alexandro Kuphal",
            "telephones": [
                {
                    "telephone": "(404) 452-9269",
                    "type": shared.CrmTelephoneType.OTHER,
                },
                {
                    "telephone": "(989) 758-8616",
                    "type": shared.CrmTelephoneType.WORK,
                },
            ],
            "title": "Direct Infrastructure Administrator",
            "updated_at": parse_datetime("2021-02-25T02:46:23.329Z"),
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

Creates a UcContact. Provide the unified UcContact fields in the request body; they are mapped to the provider's API. Returns the created UcContact.

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
            "company": "Olson - Stanton",
            "created_at": parse_datetime("2019-10-28T11:06:56.460Z"),
            "emails": [
                {
                    "email": "Norval_Brekke@gmail.com",
                    "type": shared.UcEmailType.WORK,
                },
            ],
            "first_name": "Norval",
            "id": "2c39d126-e669-4218-8db5-e84c7d941baf",
            "last_name": "Brekke",
            "metadata": [],
            "name": "Norval Brekke",
            "telephones": [
                {
                    "telephone": "(992) 368-1868",
                    "type": shared.UcTelephoneType.FAX,
                },
                {
                    "telephone": "(238) 374-6019",
                    "type": shared.UcTelephoneType.HOME,
                },
                {
                    "telephone": "(736) 235-7480",
                    "type": shared.UcTelephoneType.MOBILE,
                },
            ],
            "title": "Internal Creative Director",
            "updated_at": parse_datetime("2023-12-29T13:20:51.045Z"),
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

Retrieves a single AccountingContact by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Retrieves a single CrmContact by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Retrieves a single UcContact by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Returns a list of AccountingContacts. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Returns a list of CrmContacts. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Returns a list of UcContacts. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Updates the AccountingContact identified by `id`. Provide the unified AccountingContact fields to change in the request body.

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
                "address1": "9171 Parisian Gateway",
                "city": "Lake Keltonboro",
                "country_code": "US",
                "postal_code": "70131-2908",
                "region": "Illinois",
                "region_code": "CO",
            },
            "company_name": "Rice LLC",
            "created_at": parse_datetime("2021-08-15T14:56:50.258Z"),
            "currency": "AUD",
            "emails": [
                {
                    "email": "michele.breitenberg@ricellc.com",
                    "type": shared.AccountingEmailType.WORK,
                },
                {
                    "email": "accounts@ricellc.com",
                    "type": shared.AccountingEmailType.OTHER,
                },
            ],
            "first_name": "Michele",
            "id": "b3cd5556-0414-4043-a19a-55642194b29c",
            "identification": "508720595",
            "is_active": True,
            "is_customer": True,
            "last_name": "Breitenberg",
            "metadata": [],
            "name": "Rice LLC",
            "notes": "Tabella reprehenderit sono corrupti approbo crastinus sopor ultra.",
            "payment_methods": [
                {
                    "default": True,
                    "id": "e6fbdbad-13fd-424a-9552-2928b73efd2c",
                    "name": "Visa 5318",
                    "type": shared.AccountingContactPaymentMethodType.CARD,
                },
            ],
            "portal_url": "https://ricellc.com/billing",
            "shipping_address": {
                "address1": "786 Dare Meadows",
                "city": "Phoenix",
                "country_code": "US",
                "postal_code": "68675",
                "region": "Tennessee",
                "region_code": "NE",
            },
            "tax_exemption": shared.TaxExemption.FOREIGN,
            "tax_number": "564107844",
            "telephones": [
                {
                    "telephone": "(217) 260-4409",
                    "type": shared.AccountingTelephoneType.FAX,
                },
            ],
            "updated_at": parse_datetime("2024-01-05T03:13:26.393Z"),
            "website": "https://ricellc.com",
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

Updates the CrmContact identified by `id`. Provide the unified CrmContact fields to change in the request body.

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
                "address1": "489 Eula Park",
                "address2": "Apt. 900",
                "city": "Archfield",
                "country_code": "US",
                "postal_code": "60941-8210",
                "region": "Texas",
                "region_code": "NH",
            },
            "created_at": parse_datetime("2021-01-02T00:41:38.885Z"),
            "department": "Health",
            "emails": [
                {
                    "email": "alexandro.kuphal@hotmail.com",
                    "type": shared.CrmEmailType.HOME,
                },
            ],
            "first_name": "Alexandro",
            "id": "0f0cb0d9-601f-4bb8-808f-e234cc0fd51e",
            "image_url": "https://avatars.githubusercontent.com/u/26594214",
            "last_name": "Kuphal",
            "link_urls": [
                "https://www.linkedin.com/in/alexandro-kuphal",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "1feda212-b228-449d-bcf3-e4a0b60b1689",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "amplus",
                },
            ],
            "name": "Alexandro Kuphal",
            "telephones": [
                {
                    "telephone": "(404) 452-9269",
                    "type": shared.CrmTelephoneType.OTHER,
                },
                {
                    "telephone": "(989) 758-8616",
                    "type": shared.CrmTelephoneType.WORK,
                },
            ],
            "title": "Direct Infrastructure Administrator",
            "updated_at": parse_datetime("2021-02-25T02:46:23.330Z"),
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

Updates the UcContact identified by `id`. Provide the unified UcContact fields to change in the request body.

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
            "company": "Olson - Stanton",
            "created_at": parse_datetime("2019-10-28T11:06:56.460Z"),
            "emails": [
                {
                    "email": "Norval_Brekke@gmail.com",
                    "type": shared.UcEmailType.WORK,
                },
            ],
            "first_name": "Norval",
            "id": "ee028c4e-42f3-448f-b77e-fc5a6aa90ee3",
            "last_name": "Brekke",
            "metadata": [],
            "name": "Norval Brekke",
            "telephones": [
                {
                    "telephone": "(992) 368-1868",
                    "type": shared.UcTelephoneType.FAX,
                },
                {
                    "telephone": "(238) 374-6019",
                    "type": shared.UcTelephoneType.HOME,
                },
                {
                    "telephone": "(736) 235-7480",
                    "type": shared.UcTelephoneType.MOBILE,
                },
            ],
            "title": "Internal Creative Director",
            "updated_at": parse_datetime("2023-12-29T13:20:51.053Z"),
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

Deletes the AccountingContact identified by `id`.

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

Deletes the CrmContact identified by `id`.

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

Deletes the UcContact identified by `id`.

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

Updates the AccountingContact identified by `id`. Provide the unified AccountingContact fields to change in the request body.

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
                "address1": "9171 Parisian Gateway",
                "city": "Lake Keltonboro",
                "country_code": "US",
                "postal_code": "70131-2908",
                "region": "Illinois",
                "region_code": "CO",
            },
            "company_name": "Rice LLC",
            "created_at": parse_datetime("2021-08-15T14:56:50.258Z"),
            "currency": "AUD",
            "emails": [
                {
                    "email": "michele.breitenberg@ricellc.com",
                    "type": shared.AccountingEmailType.WORK,
                },
                {
                    "email": "accounts@ricellc.com",
                    "type": shared.AccountingEmailType.OTHER,
                },
            ],
            "first_name": "Michele",
            "id": "b3cd5556-0414-4043-a19a-55642194b29c",
            "identification": "508720595",
            "is_active": True,
            "is_customer": True,
            "last_name": "Breitenberg",
            "metadata": [],
            "name": "Rice LLC",
            "notes": "Tabella reprehenderit sono corrupti approbo crastinus sopor ultra.",
            "payment_methods": [
                {
                    "default": True,
                    "id": "e6fbdbad-13fd-424a-9552-2928b73efd2c",
                    "name": "Visa 5318",
                    "type": shared.AccountingContactPaymentMethodType.CARD,
                },
            ],
            "portal_url": "https://ricellc.com/billing",
            "shipping_address": {
                "address1": "786 Dare Meadows",
                "city": "Phoenix",
                "country_code": "US",
                "postal_code": "68675",
                "region": "Tennessee",
                "region_code": "NE",
            },
            "tax_exemption": shared.TaxExemption.FOREIGN,
            "tax_number": "564107844",
            "telephones": [
                {
                    "telephone": "(217) 260-4409",
                    "type": shared.AccountingTelephoneType.FAX,
                },
            ],
            "updated_at": parse_datetime("2024-01-05T03:13:26.393Z"),
            "website": "https://ricellc.com",
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

Updates the CrmContact identified by `id`. Provide the unified CrmContact fields to change in the request body.

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
                "address1": "489 Eula Park",
                "address2": "Apt. 900",
                "city": "Archfield",
                "country_code": "US",
                "postal_code": "60941-8210",
                "region": "Texas",
                "region_code": "NH",
            },
            "created_at": parse_datetime("2021-01-02T00:41:38.885Z"),
            "department": "Health",
            "emails": [
                {
                    "email": "alexandro.kuphal@hotmail.com",
                    "type": shared.CrmEmailType.HOME,
                },
            ],
            "first_name": "Alexandro",
            "id": "0f0cb0d9-601f-4bb8-808f-e234cc0fd51e",
            "image_url": "https://avatars.githubusercontent.com/u/26594214",
            "last_name": "Kuphal",
            "link_urls": [
                "https://www.linkedin.com/in/alexandro-kuphal",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "1feda212-b228-449d-bcf3-e4a0b60b1689",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "amplus",
                },
            ],
            "name": "Alexandro Kuphal",
            "telephones": [
                {
                    "telephone": "(404) 452-9269",
                    "type": shared.CrmTelephoneType.OTHER,
                },
                {
                    "telephone": "(989) 758-8616",
                    "type": shared.CrmTelephoneType.WORK,
                },
            ],
            "title": "Direct Infrastructure Administrator",
            "updated_at": parse_datetime("2021-02-25T02:46:23.330Z"),
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

Updates the UcContact identified by `id`. Provide the unified UcContact fields to change in the request body.

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
            "company": "Olson - Stanton",
            "created_at": parse_datetime("2019-10-28T11:06:56.460Z"),
            "emails": [
                {
                    "email": "Norval_Brekke@gmail.com",
                    "type": shared.UcEmailType.WORK,
                },
            ],
            "first_name": "Norval",
            "id": "ee028c4e-42f3-448f-b77e-fc5a6aa90ee3",
            "last_name": "Brekke",
            "metadata": [],
            "name": "Norval Brekke",
            "telephones": [
                {
                    "telephone": "(992) 368-1868",
                    "type": shared.UcTelephoneType.FAX,
                },
                {
                    "telephone": "(238) 374-6019",
                    "type": shared.UcTelephoneType.HOME,
                },
                {
                    "telephone": "(736) 235-7480",
                    "type": shared.UcTelephoneType.MOBILE,
                },
            ],
            "title": "Internal Creative Director",
            "updated_at": parse_datetime("2023-12-29T13:20:51.053Z"),
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