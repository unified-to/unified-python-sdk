# Crm

## Overview

### Available Operations

* [create_crm_company](#create_crm_company) - Create a company
* [create_crm_contact](#create_crm_contact) - Create a contact
* [create_crm_deal](#create_crm_deal) - Create a deal
* [create_crm_event](#create_crm_event) - Create an event
* [create_crm_lead](#create_crm_lead) - Create a lead
* [create_crm_pipeline](#create_crm_pipeline) - Create a pipeline
* [get_crm_company](#get_crm_company) - Retrieve a company
* [get_crm_contact](#get_crm_contact) - Retrieve a contact
* [get_crm_deal](#get_crm_deal) - Retrieve a deal
* [get_crm_event](#get_crm_event) - Retrieve an event
* [get_crm_lead](#get_crm_lead) - Retrieve a lead
* [get_crm_pipeline](#get_crm_pipeline) - Retrieve a pipeline
* [list_crm_companies](#list_crm_companies) - List all companies
* [list_crm_contacts](#list_crm_contacts) - List all contacts
* [list_crm_deals](#list_crm_deals) - List all deals
* [list_crm_events](#list_crm_events) - List all events
* [list_crm_leads](#list_crm_leads) - List all leads
* [list_crm_pipelines](#list_crm_pipelines) - List all pipelines
* [list_crm_taxonomies](#list_crm_taxonomies) - List all taxonomies
* [patch_crm_company](#patch_crm_company) - Update a company
* [patch_crm_contact](#patch_crm_contact) - Update a contact
* [patch_crm_deal](#patch_crm_deal) - Update a deal
* [patch_crm_event](#patch_crm_event) - Update an event
* [patch_crm_lead](#patch_crm_lead) - Update a lead
* [patch_crm_pipeline](#patch_crm_pipeline) - Update a pipeline
* [remove_crm_company](#remove_crm_company) - Remove a company
* [remove_crm_contact](#remove_crm_contact) - Remove a contact
* [remove_crm_deal](#remove_crm_deal) - Remove a deal
* [remove_crm_event](#remove_crm_event) - Remove an event
* [remove_crm_lead](#remove_crm_lead) - Remove a lead
* [remove_crm_pipeline](#remove_crm_pipeline) - Remove a pipeline
* [update_crm_company](#update_crm_company) - Update a company
* [update_crm_contact](#update_crm_contact) - Update a contact
* [update_crm_deal](#update_crm_deal) - Update a deal
* [update_crm_event](#update_crm_event) - Update an event
* [update_crm_lead](#update_crm_lead) - Update a lead
* [update_crm_pipeline](#update_crm_pipeline) - Update a pipeline

## create_crm_company

Create a company

### Example Usage

<!-- UsageSnippet language="python" operationID="createCrmCompany" method="post" path="/crm/{connection_id}/company" example="crm_company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.create_crm_company(request={
        "crm_company": {
            "address": {
                "address1": "3328 Wunsch Flat",
                "address2": "Suite 905",
                "city": "New Ryderfort",
                "country_code": "US",
                "postal_code": "04674",
                "region": "Delaware",
                "region_code": "NY",
            },
            "created_at": parse_datetime("2020-05-11T18:26:32.925Z"),
            "description": "Venustas cruentus votum patruus terebro.",
            "domains": [
                "goodwinsons.com",
            ],
            "emails": [
                {
                    "email": "info@goodwinsons.com",
                    "type": shared.CrmEmailType.WORK,
                },
                {
                    "email": "sales@goodwinsons.com",
                    "type": shared.CrmEmailType.WORK,
                },
                {
                    "email": "support@goodwinsons.com",
                    "type": shared.CrmEmailType.WORK,
                },
            ],
            "employees": 4177.0,
            "id": "e59e2366-70e5-4e6e-a25a-5650778b39d9",
            "industry": "Metrics",
            "is_active": True,
            "link_urls": [
                "https://www.linkedin.com/company/goodwin-and-sons",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "e3cac440-3fea-4034-b28e-5a92904d60dd",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "unde",
                },
            ],
            "name": "Goodwin and Sons",
            "tags": [
                "censura",
                "abstergo",
                "ipsam",
            ],
            "telephones": [
                {
                    "telephone": "(667) 607-5872",
                    "type": shared.CrmTelephoneType.HOME,
                },
            ],
            "timezone": "Atlantic/Azores",
            "updated_at": parse_datetime("2025-03-03T03:40:38.960Z"),
            "websites": [
                "https://www.goodwinsons.com",
            ],
        },
        "connection_id": "<id>",
    })

    assert res.crm_company is not None

    # Handle response
    print(res.crm_company)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateCrmCompanyRequest](../../models/operations/createcrmcompanyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreateCrmCompanyResponse](../../models/operations/createcrmcompanyresponse.md)**

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

    res = unified_to.crm.create_crm_contact(request={
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
            "id": "739ce1b5-555e-43f0-8d48-ef496726adb2",
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
                    "id": "61bee087-b03b-416d-9a99-40e30b15d0bb",
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
            "updated_at": parse_datetime("2021-02-24T05:06:24.613Z"),
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

## create_crm_deal

Create a deal

### Example Usage

<!-- UsageSnippet language="python" operationID="createCrmDeal" method="post" path="/crm/{connection_id}/deal" example="crm_deal" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.create_crm_deal(request={
        "crm_deal": {
            "amount": 98162.0,
            "closed_at": parse_datetime("2024-03-10T10:05:32.936Z"),
            "closing_at": parse_datetime("2025-08-31T12:34:35.326Z"),
            "created_at": parse_datetime("2023-07-04T12:48:48.470Z"),
            "currency": "USD",
            "description": "Comis tepidus sit cavus crustulum trans tubineus adfectus.",
            "id": "d8a93100-6862-4009-a9e2-452e5976a617",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "02819c29-ddff-4a57-99fc-4264e853b2aa",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "conatus",
                },
            ],
            "name": "Stoltenberg - Funk - Luxurious Rubber Chicken",
            "probability": 42.0,
            "source": "cubo",
            "tags": [
                "causa",
                "suus",
            ],
            "updated_at": parse_datetime("2024-10-11T21:11:01.441Z"),
            "won_reason": "Usque libero soleo.",
        },
        "connection_id": "<id>",
    })

    assert res.crm_deal is not None

    # Handle response
    print(res.crm_deal)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateCrmDealRequest](../../models/operations/createcrmdealrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.CreateCrmDealResponse](../../models/operations/createcrmdealresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_crm_event

Create an event

### Example Usage

<!-- UsageSnippet language="python" operationID="createCrmEvent" method="post" path="/crm/{connection_id}/event" example="crm_event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.create_crm_event(request={
        "crm_event": {
            "call": {
                "description": "Arbitro aptus.",
                "duration": 64.0,
                "start_at": parse_datetime("2024-12-11T00:44:46.970Z"),
            },
            "created_at": parse_datetime("2020-07-14T04:53:23.784Z"),
            "id": "9398fe29-3988-44ce-b5dc-2b2767c9445f",
            "metadata": [],
            "type": shared.CrmEventType.CALL,
            "updated_at": parse_datetime("2026-10-11T12:50:42.303Z"),
        },
        "connection_id": "<id>",
    })

    assert res.crm_event is not None

    # Handle response
    print(res.crm_event)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateCrmEventRequest](../../models/operations/createcrmeventrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.CreateCrmEventResponse](../../models/operations/createcrmeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_crm_lead

Create a lead

### Example Usage

<!-- UsageSnippet language="python" operationID="createCrmLead" method="post" path="/crm/{connection_id}/lead" example="crm_lead" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.create_crm_lead(request={
        "crm_lead": {
            "address": {
                "address1": "87206 Hudson Street",
                "city": "Leslieboro",
                "country_code": "US",
                "postal_code": "49909-1183",
                "region": "Michigan",
                "region_code": "MO",
            },
            "company_name": "Tillman - Wiegand",
            "created_at": parse_datetime("2019-10-12T11:27:59.003Z"),
            "emails": [
                {
                    "email": "velda.sporer@icloud.com",
                    "type": shared.CrmEmailType.WORK,
                },
            ],
            "first_name": "Velda",
            "id": "5d292300-797b-4000-b1ca-2012860106d7",
            "is_active": True,
            "last_name": "Sporer",
            "link_urls": [
                "https://www.linkedin.com/in/velda-sporer",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "8192ee89-602e-4056-a9d3-f6bff42b1a8b",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "vitiosus",
                },
            ],
            "name": "Velda Sporer",
            "source": "Advertisement",
            "status": "New",
            "telephones": [
                {
                    "telephone": "(841) 271-0595",
                    "type": shared.CrmTelephoneType.FAX,
                },
                {
                    "telephone": "(664) 498-4952",
                    "type": shared.CrmTelephoneType.HOME,
                },
                {
                    "telephone": "(281) 288-0037",
                    "type": shared.CrmTelephoneType.OTHER,
                },
            ],
            "title": "International Factors Administrator",
            "updated_at": parse_datetime("2020-05-17T21:34:24.238Z"),
        },
        "connection_id": "<id>",
    })

    assert res.crm_lead is not None

    # Handle response
    print(res.crm_lead)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateCrmLeadRequest](../../models/operations/createcrmleadrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.CreateCrmLeadResponse](../../models/operations/createcrmleadresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_crm_pipeline

Create a pipeline

### Example Usage

<!-- UsageSnippet language="python" operationID="createCrmPipeline" method="post" path="/crm/{connection_id}/pipeline" example="crm_pipeline" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.create_crm_pipeline(request={
        "crm_pipeline": {
            "created_at": parse_datetime("2022-12-28T13:45:38.446Z"),
            "deal_probability": 99.0,
            "display_order": 8.0,
            "id": "d0123b5e-6e85-46b1-a76f-30daf7ed4d05",
            "is_active": True,
            "metadata": [],
            "name": "Small Steel Bacon",
            "stages": [
                {
                    "active": False,
                    "created_at": parse_datetime("2022-12-28T13:45:38.446Z"),
                    "deal_probability": 84.0,
                    "display_order": 72.0,
                    "id": "ee9654fd-afff-4826-a69d-fd916916542d",
                    "is_closed": True,
                    "name": "Veniam.",
                    "updated_at": parse_datetime("2025-10-10T12:24:50.707Z"),
                },
            ],
            "updated_at": parse_datetime("2025-11-01T05:51:05.610Z"),
        },
        "connection_id": "<id>",
    })

    assert res.crm_pipeline is not None

    # Handle response
    print(res.crm_pipeline)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateCrmPipelineRequest](../../models/operations/createcrmpipelinerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateCrmPipelineResponse](../../models/operations/createcrmpipelineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_crm_company

Retrieve a company

### Example Usage

<!-- UsageSnippet language="python" operationID="getCrmCompany" method="get" path="/crm/{connection_id}/company/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.get_crm_company(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_company is not None

    # Handle response
    print(res.crm_company)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetCrmCompanyRequest](../../models/operations/getcrmcompanyrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetCrmCompanyResponse](../../models/operations/getcrmcompanyresponse.md)**

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

    res = unified_to.crm.get_crm_contact(request={
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

## get_crm_deal

Retrieve a deal

### Example Usage

<!-- UsageSnippet language="python" operationID="getCrmDeal" method="get" path="/crm/{connection_id}/deal/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.get_crm_deal(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_deal is not None

    # Handle response
    print(res.crm_deal)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetCrmDealRequest](../../models/operations/getcrmdealrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.GetCrmDealResponse](../../models/operations/getcrmdealresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_crm_event

Retrieve an event

### Example Usage

<!-- UsageSnippet language="python" operationID="getCrmEvent" method="get" path="/crm/{connection_id}/event/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.get_crm_event(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_event is not None

    # Handle response
    print(res.crm_event)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetCrmEventRequest](../../models/operations/getcrmeventrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.GetCrmEventResponse](../../models/operations/getcrmeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_crm_lead

Retrieve a lead

### Example Usage

<!-- UsageSnippet language="python" operationID="getCrmLead" method="get" path="/crm/{connection_id}/lead/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.get_crm_lead(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_lead is not None

    # Handle response
    print(res.crm_lead)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetCrmLeadRequest](../../models/operations/getcrmleadrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.GetCrmLeadResponse](../../models/operations/getcrmleadresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_crm_pipeline

Retrieve a pipeline

### Example Usage

<!-- UsageSnippet language="python" operationID="getCrmPipeline" method="get" path="/crm/{connection_id}/pipeline/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.get_crm_pipeline(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_pipeline is not None

    # Handle response
    print(res.crm_pipeline)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetCrmPipelineRequest](../../models/operations/getcrmpipelinerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetCrmPipelineResponse](../../models/operations/getcrmpipelineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_crm_companies

List all companies

### Example Usage

<!-- UsageSnippet language="python" operationID="listCrmCompanies" method="get" path="/crm/{connection_id}/company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.list_crm_companies(request={
        "connection_id": "<id>",
    })

    assert res.crm_companies is not None

    # Handle response
    print(res.crm_companies)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListCrmCompaniesRequest](../../models/operations/listcrmcompaniesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListCrmCompaniesResponse](../../models/operations/listcrmcompaniesresponse.md)**

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

    res = unified_to.crm.list_crm_contacts(request={
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

## list_crm_deals

List all deals

### Example Usage

<!-- UsageSnippet language="python" operationID="listCrmDeals" method="get" path="/crm/{connection_id}/deal" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.list_crm_deals(request={
        "connection_id": "<id>",
    })

    assert res.crm_deals is not None

    # Handle response
    print(res.crm_deals)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListCrmDealsRequest](../../models/operations/listcrmdealsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.ListCrmDealsResponse](../../models/operations/listcrmdealsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_crm_events

List all events

### Example Usage

<!-- UsageSnippet language="python" operationID="listCrmEvents" method="get" path="/crm/{connection_id}/event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.list_crm_events(request={
        "connection_id": "<id>",
    })

    assert res.crm_events is not None

    # Handle response
    print(res.crm_events)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListCrmEventsRequest](../../models/operations/listcrmeventsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.ListCrmEventsResponse](../../models/operations/listcrmeventsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_crm_leads

List all leads

### Example Usage

<!-- UsageSnippet language="python" operationID="listCrmLeads" method="get" path="/crm/{connection_id}/lead" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.list_crm_leads(request={
        "connection_id": "<id>",
    })

    assert res.crm_leads is not None

    # Handle response
    print(res.crm_leads)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListCrmLeadsRequest](../../models/operations/listcrmleadsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.ListCrmLeadsResponse](../../models/operations/listcrmleadsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_crm_pipelines

List all pipelines

### Example Usage

<!-- UsageSnippet language="python" operationID="listCrmPipelines" method="get" path="/crm/{connection_id}/pipeline" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.list_crm_pipelines(request={
        "connection_id": "<id>",
    })

    assert res.crm_pipelines is not None

    # Handle response
    print(res.crm_pipelines)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListCrmPipelinesRequest](../../models/operations/listcrmpipelinesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListCrmPipelinesResponse](../../models/operations/listcrmpipelinesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_crm_taxonomies

List all taxonomies

### Example Usage

<!-- UsageSnippet language="python" operationID="listCrmTaxonomies" method="get" path="/crm/{connection_id}/taxonomy" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.list_crm_taxonomies(request={
        "connection_id": "<id>",
    })

    assert res.crm_taxonomies is not None

    # Handle response
    print(res.crm_taxonomies)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListCrmTaxonomiesRequest](../../models/operations/listcrmtaxonomiesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListCrmTaxonomiesResponse](../../models/operations/listcrmtaxonomiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_crm_company

Update a company

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCrmCompany" method="patch" path="/crm/{connection_id}/company/{id}" example="crm_company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.patch_crm_company(request={
        "crm_company": {
            "address": {
                "address1": "3328 Wunsch Flat",
                "address2": "Suite 905",
                "city": "New Ryderfort",
                "country_code": "US",
                "postal_code": "04674",
                "region": "Delaware",
                "region_code": "NY",
            },
            "created_at": parse_datetime("2020-05-11T18:26:32.925Z"),
            "description": "Venustas cruentus votum patruus terebro.",
            "domains": [
                "goodwinsons.com",
            ],
            "emails": [
                {
                    "email": "info@goodwinsons.com",
                    "type": shared.CrmEmailType.WORK,
                },
                {
                    "email": "sales@goodwinsons.com",
                    "type": shared.CrmEmailType.WORK,
                },
                {
                    "email": "support@goodwinsons.com",
                    "type": shared.CrmEmailType.WORK,
                },
            ],
            "employees": 4177.0,
            "id": "57af47d8-b577-4f38-ac58-5d8ef38cbef4",
            "industry": "Metrics",
            "is_active": True,
            "link_urls": [
                "https://www.linkedin.com/company/goodwin-and-sons",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "431bf807-6d6e-4bba-bf48-22307df458ed",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "unde",
                },
            ],
            "name": "Goodwin and Sons",
            "tags": [
                "censura",
                "abstergo",
                "ipsam",
            ],
            "telephones": [
                {
                    "telephone": "(667) 607-5872",
                    "type": shared.CrmTelephoneType.HOME,
                },
            ],
            "timezone": "Atlantic/Azores",
            "updated_at": parse_datetime("2025-03-03T03:40:38.979Z"),
            "websites": [
                "https://www.goodwinsons.com",
            ],
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_company is not None

    # Handle response
    print(res.crm_company)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchCrmCompanyRequest](../../models/operations/patchcrmcompanyrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchCrmCompanyResponse](../../models/operations/patchcrmcompanyresponse.md)**

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

    res = unified_to.crm.patch_crm_contact(request={
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
            "id": "5755d189-87e9-4fad-9745-135da57f80dc",
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
                    "id": "76fee8e1-4c33-4429-9dc6-3e428eb31ba6",
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
            "updated_at": parse_datetime("2021-02-24T05:06:24.614Z"),
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

## patch_crm_deal

Update a deal

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCrmDeal" method="patch" path="/crm/{connection_id}/deal/{id}" example="crm_deal" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.patch_crm_deal(request={
        "crm_deal": {
            "amount": 98162.0,
            "closed_at": parse_datetime("2024-03-10T10:05:32.939Z"),
            "closing_at": parse_datetime("2025-08-31T12:34:35.337Z"),
            "created_at": parse_datetime("2023-07-04T12:48:48.470Z"),
            "currency": "USD",
            "description": "Comis tepidus sit cavus crustulum trans tubineus adfectus.",
            "id": "2f87abfb-7cab-4105-8835-3504a8954792",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "83983b53-507a-41e7-aae2-dc4809f4474a",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "conatus",
                },
            ],
            "name": "Stoltenberg - Funk - Luxurious Rubber Chicken",
            "probability": 42.0,
            "source": "cubo",
            "tags": [
                "causa",
                "suus",
            ],
            "updated_at": parse_datetime("2024-10-11T21:11:01.447Z"),
            "won_reason": "Usque libero soleo.",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_deal is not None

    # Handle response
    print(res.crm_deal)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.PatchCrmDealRequest](../../models/operations/patchcrmdealrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.PatchCrmDealResponse](../../models/operations/patchcrmdealresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_crm_event

Update an event

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCrmEvent" method="patch" path="/crm/{connection_id}/event/{id}" example="crm_event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.patch_crm_event(request={
        "crm_event": {
            "call": {
                "description": "Arbitro aptus.",
                "duration": 64.0,
                "start_at": parse_datetime("2024-12-11T00:44:47.004Z"),
            },
            "created_at": parse_datetime("2020-07-14T04:53:23.784Z"),
            "id": "c0be1b9e-c952-494e-9e1e-9f7b757c2075",
            "metadata": [],
            "type": shared.CrmEventType.CALL,
            "updated_at": parse_datetime("2026-10-11T12:50:42.351Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_event is not None

    # Handle response
    print(res.crm_event)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.PatchCrmEventRequest](../../models/operations/patchcrmeventrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.PatchCrmEventResponse](../../models/operations/patchcrmeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_crm_lead

Update a lead

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCrmLead" method="patch" path="/crm/{connection_id}/lead/{id}" example="crm_lead" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.patch_crm_lead(request={
        "crm_lead": {
            "address": {
                "address1": "87206 Hudson Street",
                "city": "Leslieboro",
                "country_code": "US",
                "postal_code": "49909-1183",
                "region": "Michigan",
                "region_code": "MO",
            },
            "company_name": "Tillman - Wiegand",
            "created_at": parse_datetime("2019-10-12T11:27:59.003Z"),
            "emails": [
                {
                    "email": "velda.sporer@icloud.com",
                    "type": shared.CrmEmailType.WORK,
                },
            ],
            "first_name": "Velda",
            "id": "486acb6f-bf72-469b-83d6-d6d3bdce740f",
            "is_active": True,
            "last_name": "Sporer",
            "link_urls": [
                "https://www.linkedin.com/in/velda-sporer",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "03fe51ec-f800-4a12-885f-f1f6de8f1320",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "vitiosus",
                },
            ],
            "name": "Velda Sporer",
            "source": "Advertisement",
            "status": "New",
            "telephones": [
                {
                    "telephone": "(841) 271-0595",
                    "type": shared.CrmTelephoneType.FAX,
                },
                {
                    "telephone": "(664) 498-4952",
                    "type": shared.CrmTelephoneType.HOME,
                },
                {
                    "telephone": "(281) 288-0037",
                    "type": shared.CrmTelephoneType.OTHER,
                },
            ],
            "title": "International Factors Administrator",
            "updated_at": parse_datetime("2020-05-17T21:34:24.241Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_lead is not None

    # Handle response
    print(res.crm_lead)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.PatchCrmLeadRequest](../../models/operations/patchcrmleadrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.PatchCrmLeadResponse](../../models/operations/patchcrmleadresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_crm_pipeline

Update a pipeline

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCrmPipeline" method="patch" path="/crm/{connection_id}/pipeline/{id}" example="crm_pipeline" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.patch_crm_pipeline(request={
        "crm_pipeline": {
            "created_at": parse_datetime("2022-12-28T13:45:38.446Z"),
            "deal_probability": 99.0,
            "display_order": 8.0,
            "id": "ca408faa-6d21-4cac-b0c8-6d85e2e18aea",
            "is_active": True,
            "metadata": [],
            "name": "Small Steel Bacon",
            "stages": [
                {
                    "active": False,
                    "created_at": parse_datetime("2022-12-28T13:45:38.446Z"),
                    "deal_probability": 84.0,
                    "display_order": 72.0,
                    "id": "3a27a710-8f08-4c86-8b84-6126f2473c6f",
                    "is_closed": True,
                    "name": "Veniam.",
                    "updated_at": parse_datetime("2025-10-10T12:24:50.717Z"),
                },
            ],
            "updated_at": parse_datetime("2025-11-01T05:51:05.620Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_pipeline is not None

    # Handle response
    print(res.crm_pipeline)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchCrmPipelineRequest](../../models/operations/patchcrmpipelinerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchCrmPipelineResponse](../../models/operations/patchcrmpipelineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_crm_company

Remove a company

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCrmCompany" method="delete" path="/crm/{connection_id}/company/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.remove_crm_company(request={
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
| `request`                                                                                | [operations.RemoveCrmCompanyRequest](../../models/operations/removecrmcompanyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemoveCrmCompanyResponse](../../models/operations/removecrmcompanyresponse.md)**

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

    res = unified_to.crm.remove_crm_contact(request={
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

## remove_crm_deal

Remove a deal

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCrmDeal" method="delete" path="/crm/{connection_id}/deal/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.remove_crm_deal(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.RemoveCrmDealRequest](../../models/operations/removecrmdealrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.RemoveCrmDealResponse](../../models/operations/removecrmdealresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_crm_event

Remove an event

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCrmEvent" method="delete" path="/crm/{connection_id}/event/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.remove_crm_event(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.RemoveCrmEventRequest](../../models/operations/removecrmeventrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.RemoveCrmEventResponse](../../models/operations/removecrmeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_crm_lead

Remove a lead

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCrmLead" method="delete" path="/crm/{connection_id}/lead/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.remove_crm_lead(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.RemoveCrmLeadRequest](../../models/operations/removecrmleadrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.RemoveCrmLeadResponse](../../models/operations/removecrmleadresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_crm_pipeline

Remove a pipeline

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCrmPipeline" method="delete" path="/crm/{connection_id}/pipeline/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.remove_crm_pipeline(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveCrmPipelineRequest](../../models/operations/removecrmpipelinerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveCrmPipelineResponse](../../models/operations/removecrmpipelineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_crm_company

Update a company

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCrmCompany" method="put" path="/crm/{connection_id}/company/{id}" example="crm_company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.update_crm_company(request={
        "crm_company": {
            "address": {
                "address1": "3328 Wunsch Flat",
                "address2": "Suite 905",
                "city": "New Ryderfort",
                "country_code": "US",
                "postal_code": "04674",
                "region": "Delaware",
                "region_code": "NY",
            },
            "created_at": parse_datetime("2020-05-11T18:26:32.925Z"),
            "description": "Venustas cruentus votum patruus terebro.",
            "domains": [
                "goodwinsons.com",
            ],
            "emails": [
                {
                    "email": "info@goodwinsons.com",
                    "type": shared.CrmEmailType.WORK,
                },
                {
                    "email": "sales@goodwinsons.com",
                    "type": shared.CrmEmailType.WORK,
                },
                {
                    "email": "support@goodwinsons.com",
                    "type": shared.CrmEmailType.WORK,
                },
            ],
            "employees": 4177.0,
            "id": "57af47d8-b577-4f38-ac58-5d8ef38cbef4",
            "industry": "Metrics",
            "is_active": True,
            "link_urls": [
                "https://www.linkedin.com/company/goodwin-and-sons",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "431bf807-6d6e-4bba-bf48-22307df458ed",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "unde",
                },
            ],
            "name": "Goodwin and Sons",
            "tags": [
                "censura",
                "abstergo",
                "ipsam",
            ],
            "telephones": [
                {
                    "telephone": "(667) 607-5872",
                    "type": shared.CrmTelephoneType.HOME,
                },
            ],
            "timezone": "Atlantic/Azores",
            "updated_at": parse_datetime("2025-03-03T03:40:38.979Z"),
            "websites": [
                "https://www.goodwinsons.com",
            ],
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_company is not None

    # Handle response
    print(res.crm_company)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateCrmCompanyRequest](../../models/operations/updatecrmcompanyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdateCrmCompanyResponse](../../models/operations/updatecrmcompanyresponse.md)**

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

    res = unified_to.crm.update_crm_contact(request={
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
            "id": "5755d189-87e9-4fad-9745-135da57f80dc",
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
                    "id": "76fee8e1-4c33-4429-9dc6-3e428eb31ba6",
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
            "updated_at": parse_datetime("2021-02-24T05:06:24.614Z"),
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

## update_crm_deal

Update a deal

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCrmDeal" method="put" path="/crm/{connection_id}/deal/{id}" example="crm_deal" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.update_crm_deal(request={
        "crm_deal": {
            "amount": 98162.0,
            "closed_at": parse_datetime("2024-03-10T10:05:32.939Z"),
            "closing_at": parse_datetime("2025-08-31T12:34:35.337Z"),
            "created_at": parse_datetime("2023-07-04T12:48:48.470Z"),
            "currency": "USD",
            "description": "Comis tepidus sit cavus crustulum trans tubineus adfectus.",
            "id": "2f87abfb-7cab-4105-8835-3504a8954792",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "83983b53-507a-41e7-aae2-dc4809f4474a",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "conatus",
                },
            ],
            "name": "Stoltenberg - Funk - Luxurious Rubber Chicken",
            "probability": 42.0,
            "source": "cubo",
            "tags": [
                "causa",
                "suus",
            ],
            "updated_at": parse_datetime("2024-10-11T21:11:01.447Z"),
            "won_reason": "Usque libero soleo.",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_deal is not None

    # Handle response
    print(res.crm_deal)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateCrmDealRequest](../../models/operations/updatecrmdealrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.UpdateCrmDealResponse](../../models/operations/updatecrmdealresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_crm_event

Update an event

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCrmEvent" method="put" path="/crm/{connection_id}/event/{id}" example="crm_event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.update_crm_event(request={
        "crm_event": {
            "call": {
                "description": "Arbitro aptus.",
                "duration": 64.0,
                "start_at": parse_datetime("2024-12-11T00:44:47.004Z"),
            },
            "created_at": parse_datetime("2020-07-14T04:53:23.784Z"),
            "id": "c0be1b9e-c952-494e-9e1e-9f7b757c2075",
            "metadata": [],
            "type": shared.CrmEventType.CALL,
            "updated_at": parse_datetime("2026-10-11T12:50:42.351Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_event is not None

    # Handle response
    print(res.crm_event)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateCrmEventRequest](../../models/operations/updatecrmeventrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.UpdateCrmEventResponse](../../models/operations/updatecrmeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_crm_lead

Update a lead

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCrmLead" method="put" path="/crm/{connection_id}/lead/{id}" example="crm_lead" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.update_crm_lead(request={
        "crm_lead": {
            "address": {
                "address1": "87206 Hudson Street",
                "city": "Leslieboro",
                "country_code": "US",
                "postal_code": "49909-1183",
                "region": "Michigan",
                "region_code": "MO",
            },
            "company_name": "Tillman - Wiegand",
            "created_at": parse_datetime("2019-10-12T11:27:59.003Z"),
            "emails": [
                {
                    "email": "velda.sporer@icloud.com",
                    "type": shared.CrmEmailType.WORK,
                },
            ],
            "first_name": "Velda",
            "id": "486acb6f-bf72-469b-83d6-d6d3bdce740f",
            "is_active": True,
            "last_name": "Sporer",
            "link_urls": [
                "https://www.linkedin.com/in/velda-sporer",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "03fe51ec-f800-4a12-885f-f1f6de8f1320",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "vitiosus",
                },
            ],
            "name": "Velda Sporer",
            "source": "Advertisement",
            "status": "New",
            "telephones": [
                {
                    "telephone": "(841) 271-0595",
                    "type": shared.CrmTelephoneType.FAX,
                },
                {
                    "telephone": "(664) 498-4952",
                    "type": shared.CrmTelephoneType.HOME,
                },
                {
                    "telephone": "(281) 288-0037",
                    "type": shared.CrmTelephoneType.OTHER,
                },
            ],
            "title": "International Factors Administrator",
            "updated_at": parse_datetime("2020-05-17T21:34:24.241Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_lead is not None

    # Handle response
    print(res.crm_lead)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateCrmLeadRequest](../../models/operations/updatecrmleadrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.UpdateCrmLeadResponse](../../models/operations/updatecrmleadresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_crm_pipeline

Update a pipeline

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCrmPipeline" method="put" path="/crm/{connection_id}/pipeline/{id}" example="crm_pipeline" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.crm.update_crm_pipeline(request={
        "crm_pipeline": {
            "created_at": parse_datetime("2022-12-28T13:45:38.446Z"),
            "deal_probability": 99.0,
            "display_order": 8.0,
            "id": "ca408faa-6d21-4cac-b0c8-6d85e2e18aea",
            "is_active": True,
            "metadata": [],
            "name": "Small Steel Bacon",
            "stages": [
                {
                    "active": False,
                    "created_at": parse_datetime("2022-12-28T13:45:38.446Z"),
                    "deal_probability": 84.0,
                    "display_order": 72.0,
                    "id": "3a27a710-8f08-4c86-8b84-6126f2473c6f",
                    "is_closed": True,
                    "name": "Veniam.",
                    "updated_at": parse_datetime("2025-10-10T12:24:50.717Z"),
                },
            ],
            "updated_at": parse_datetime("2025-11-01T05:51:05.620Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_pipeline is not None

    # Handle response
    print(res.crm_pipeline)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateCrmPipelineRequest](../../models/operations/updatecrmpipelinerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateCrmPipelineResponse](../../models/operations/updatecrmpipelineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |