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
                "address1": "7261 Salisbury Road",
                "address2": "Apt. 778",
                "city": "Harrisburg",
                "country_code": "US",
                "postal_code": "56293-3678",
                "region": "Pennsylvania",
                "region_code": "ID",
            },
            "created_at": parse_datetime("2020-05-11T18:26:32.925Z"),
            "description": "Balbus crapula spiculum.",
            "domains": [
                "fussy-nerve.info",
                "sturdy-lobster.org",
                "greedy-offset.name",
            ],
            "emails": [
                {
                    "email": "Sandrine_Jacobi@hotmail.com",
                    "type": shared.CrmEmailType.WORK,
                },
                {
                    "email": "Sandrine_Jacobi@gmail.com",
                    "type": shared.CrmEmailType.WORK,
                },
                {
                    "email": "Sandrine.Jacobi@yahoo.com",
                    "type": shared.CrmEmailType.OTHER,
                },
            ],
            "employees": 967.0,
            "id": "04c6bfbe-e86d-4892-8215-2d7b2293f78a",
            "industry": "Infrastructure",
            "is_active": True,
            "link_urls": [
                "https://blue-license.org",
                "https://minor-formation.com",
                "https://ecstatic-hammock.com",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "7b6e0be7-1408-4df6-a66c-bb7971ba25fd",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "esse",
                },
            ],
            "name": "Goodwin and Sons",
            "tags": [
                "quaerat",
                "valeo",
            ],
            "telephones": [
                {
                    "telephone": "(432) 849-2690",
                    "type": shared.CrmTelephoneType.MOBILE,
                },
                {
                    "telephone": "(606) 871-2046",
                    "type": shared.CrmTelephoneType.OTHER,
                },
                {
                    "telephone": "(842) 258-9395",
                    "type": shared.CrmTelephoneType.MOBILE,
                },
            ],
            "timezone": "Europe/San_Marino",
            "updated_at": parse_datetime("2025-02-07T12:07:08.669Z"),
            "websites": [
                "https://wise-possession.org",
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
            "id": "2abf3756-4209-4f90-bc21-d7c6e26147d7",
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
                    "id": "a5693a3f-5ba5-4e36-9b7a-bdc7b5c4390a",
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
            "updated_at": parse_datetime("2021-02-23T10:00:43.228Z"),
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
            "closed_at": parse_datetime("2024-03-03T20:19:43.644Z"),
            "closing_at": parse_datetime("2025-08-10T18:27:16.565Z"),
            "created_at": parse_datetime("2023-07-04T12:48:48.470Z"),
            "currency": "IQD",
            "description": "Tabula cicuta sophismata comis tepidus sit cavus.",
            "id": "65023b3b-6233-4971-a2a7-5279069c6fe0",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "1b85be14-5e6c-47c3-8de9-611a7204770f",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "conatus",
                },
            ],
            "name": "Frozen Silk Chicken",
            "pipelines": [
                {
                    "id": "6c1141b1-e956-4afa-b736-fe4d8e00405d",
                    "name": "trans",
                },
            ],
            "probability": 65.0,
            "source": "cubo",
            "stages": [
                {
                    "id": "9ac747ff-048d-454f-8110-f152c0f07dfa",
                    "name": "tubineus",
                },
                {
                    "id": "52fd8b58-9103-418d-aaa8-5aafda4342aa",
                    "name": "adfectus",
                },
            ],
            "tags": [
                "causa",
                "suus",
            ],
            "updated_at": parse_datetime("2024-09-29T15:23:23.799Z"),
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
                "start_at": parse_datetime("2024-11-18T17:48:10.858Z"),
            },
            "created_at": parse_datetime("2020-07-14T04:53:23.784Z"),
            "id": "d072f81b-fbf2-4bfd-8998-65ab67683716",
            "type": shared.CrmEventType.CALL,
            "updated_at": parse_datetime("2026-09-09T23:33:52.405Z"),
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
                "address1": "528 Forest Road",
                "address2": "Apt. 643",
                "city": "Palm Springs",
                "country_code": "US",
                "postal_code": "55624-6499",
                "region": "New Jersey",
                "region_code": "LA",
            },
            "company_name": "Tillman - Wiegand",
            "created_at": parse_datetime("2019-10-12T11:27:59.003Z"),
            "emails": [
                {
                    "email": "Velda.Sporer16@yahoo.com",
                    "type": shared.CrmEmailType.OTHER,
                },
                {
                    "email": "Velda.Sporer@yahoo.com",
                    "type": shared.CrmEmailType.HOME,
                },
            ],
            "first_name": "Velda",
            "id": "03997800-568a-4e2c-8ea6-3bd5b05bbb74",
            "is_active": True,
            "last_name": "Sporer",
            "link_urls": [
                "https://classic-sightseeing.com/",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "2262bb92-5609-48a9-8e4b-96f5a1035dda",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "sublime",
                },
            ],
            "name": "Velda Sporer",
            "source": "aetas",
            "status": "vesco",
            "telephones": [
                {
                    "telephone": "(955) 643-9849",
                    "type": shared.CrmTelephoneType.OTHER,
                },
                {
                    "telephone": "(621) 811-8800",
                    "type": shared.CrmTelephoneType.WORK,
                },
            ],
            "updated_at": parse_datetime("2020-05-15T04:49:59.456Z"),
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
            "id": "881c85ba-532a-42b3-b06e-718200358d0e",
            "is_active": True,
            "name": "Small Steel Bacon",
            "stages": [
                {
                    "active": False,
                    "created_at": parse_datetime("2022-12-28T13:45:38.446Z"),
                    "deal_probability": 84.0,
                    "display_order": 72.0,
                    "id": "d97cf8ae-acf7-4d13-82cb-ff1acd694385",
                    "is_closed": True,
                    "name": "Veniam.",
                    "updated_at": parse_datetime("2025-09-17T09:02:38.560Z"),
                },
            ],
            "updated_at": parse_datetime("2025-10-08T14:36:58.607Z"),
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
                "address1": "7261 Salisbury Road",
                "address2": "Apt. 778",
                "city": "Harrisburg",
                "country_code": "US",
                "postal_code": "56293-3678",
                "region": "Pennsylvania",
                "region_code": "ID",
            },
            "created_at": parse_datetime("2020-05-11T18:26:32.925Z"),
            "description": "Balbus crapula spiculum.",
            "domains": [
                "fussy-nerve.info",
                "sturdy-lobster.org",
                "greedy-offset.name",
            ],
            "emails": [
                {
                    "email": "Sandrine_Jacobi@hotmail.com",
                    "type": shared.CrmEmailType.WORK,
                },
                {
                    "email": "Sandrine_Jacobi@gmail.com",
                    "type": shared.CrmEmailType.WORK,
                },
                {
                    "email": "Sandrine.Jacobi@yahoo.com",
                    "type": shared.CrmEmailType.OTHER,
                },
            ],
            "employees": 967.0,
            "id": "8dbb7912-877f-4751-8d56-19f07e402bf6",
            "industry": "Infrastructure",
            "is_active": True,
            "link_urls": [
                "https://blue-license.org",
                "https://minor-formation.com",
                "https://ecstatic-hammock.com",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "1c0402ce-fea2-48af-ae85-f62a7f6c7cb6",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "esse",
                },
            ],
            "name": "Goodwin and Sons",
            "tags": [
                "quaerat",
                "valeo",
            ],
            "telephones": [
                {
                    "telephone": "(432) 849-2690",
                    "type": shared.CrmTelephoneType.MOBILE,
                },
                {
                    "telephone": "(606) 871-2046",
                    "type": shared.CrmTelephoneType.OTHER,
                },
                {
                    "telephone": "(842) 258-9395",
                    "type": shared.CrmTelephoneType.MOBILE,
                },
            ],
            "timezone": "Europe/San_Marino",
            "updated_at": parse_datetime("2025-02-07T12:07:08.692Z"),
            "websites": [
                "https://wise-possession.org",
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
            "id": "172494b8-00f3-4fd1-812c-ee2040175cb0",
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
                    "id": "00b9288b-80e7-487d-b827-b8ee96896579",
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
            "updated_at": parse_datetime("2021-02-23T10:00:43.229Z"),
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
            "closed_at": parse_datetime("2024-03-03T20:19:43.648Z"),
            "closing_at": parse_datetime("2025-08-10T18:27:16.580Z"),
            "created_at": parse_datetime("2023-07-04T12:48:48.470Z"),
            "currency": "IQD",
            "description": "Tabula cicuta sophismata comis tepidus sit cavus.",
            "id": "73108402-8c3a-41bb-8761-fabdd28d8a3e",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "61f40e19-9ed5-4f4e-bf1d-3021a39513a9",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "conatus",
                },
            ],
            "name": "Frozen Silk Chicken",
            "pipelines": [
                {
                    "id": "b6ecd991-cf05-45f3-9d38-337e7cbd488e",
                    "name": "trans",
                },
            ],
            "probability": 65.0,
            "source": "cubo",
            "stages": [
                {
                    "id": "a2bb3dd8-9944-429d-9e14-b5e0c203d2c4",
                    "name": "tubineus",
                },
                {
                    "id": "202e0e54-e4eb-4d99-b67b-328f0691f7ec",
                    "name": "adfectus",
                },
            ],
            "tags": [
                "causa",
                "suus",
            ],
            "updated_at": parse_datetime("2024-09-29T15:23:23.807Z"),
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
                "start_at": parse_datetime("2024-11-18T17:48:10.885Z"),
            },
            "created_at": parse_datetime("2020-07-14T04:53:23.784Z"),
            "id": "5d88b351-9a11-4132-a3be-20de85cf387f",
            "type": shared.CrmEventType.CALL,
            "updated_at": parse_datetime("2026-09-09T23:33:52.444Z"),
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
                "address1": "528 Forest Road",
                "address2": "Apt. 643",
                "city": "Palm Springs",
                "country_code": "US",
                "postal_code": "55624-6499",
                "region": "New Jersey",
                "region_code": "LA",
            },
            "company_name": "Tillman - Wiegand",
            "created_at": parse_datetime("2019-10-12T11:27:59.003Z"),
            "emails": [
                {
                    "email": "Velda.Sporer16@yahoo.com",
                    "type": shared.CrmEmailType.OTHER,
                },
                {
                    "email": "Velda.Sporer@yahoo.com",
                    "type": shared.CrmEmailType.HOME,
                },
            ],
            "first_name": "Velda",
            "id": "d0c31181-b804-46fb-bf61-ee2423d5d262",
            "is_active": True,
            "last_name": "Sporer",
            "link_urls": [
                "https://classic-sightseeing.com/",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "7ace4194-267c-48f6-8869-56e5735bb8ec",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "sublime",
                },
            ],
            "name": "Velda Sporer",
            "source": "aetas",
            "status": "vesco",
            "telephones": [
                {
                    "telephone": "(955) 643-9849",
                    "type": shared.CrmTelephoneType.OTHER,
                },
                {
                    "telephone": "(621) 811-8800",
                    "type": shared.CrmTelephoneType.WORK,
                },
            ],
            "updated_at": parse_datetime("2020-05-15T04:49:59.458Z"),
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
            "id": "4a46c383-5524-4834-bc87-cf811454d988",
            "is_active": True,
            "name": "Small Steel Bacon",
            "stages": [
                {
                    "active": False,
                    "created_at": parse_datetime("2022-12-28T13:45:38.446Z"),
                    "deal_probability": 84.0,
                    "display_order": 72.0,
                    "id": "4f8d46c1-b18f-4a7b-a225-51067d2034aa",
                    "is_closed": True,
                    "name": "Veniam.",
                    "updated_at": parse_datetime("2025-09-17T09:02:38.569Z"),
                },
            ],
            "updated_at": parse_datetime("2025-10-08T14:36:58.615Z"),
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
                "address1": "7261 Salisbury Road",
                "address2": "Apt. 778",
                "city": "Harrisburg",
                "country_code": "US",
                "postal_code": "56293-3678",
                "region": "Pennsylvania",
                "region_code": "ID",
            },
            "created_at": parse_datetime("2020-05-11T18:26:32.925Z"),
            "description": "Balbus crapula spiculum.",
            "domains": [
                "fussy-nerve.info",
                "sturdy-lobster.org",
                "greedy-offset.name",
            ],
            "emails": [
                {
                    "email": "Sandrine_Jacobi@hotmail.com",
                    "type": shared.CrmEmailType.WORK,
                },
                {
                    "email": "Sandrine_Jacobi@gmail.com",
                    "type": shared.CrmEmailType.WORK,
                },
                {
                    "email": "Sandrine.Jacobi@yahoo.com",
                    "type": shared.CrmEmailType.OTHER,
                },
            ],
            "employees": 967.0,
            "id": "8dbb7912-877f-4751-8d56-19f07e402bf6",
            "industry": "Infrastructure",
            "is_active": True,
            "link_urls": [
                "https://blue-license.org",
                "https://minor-formation.com",
                "https://ecstatic-hammock.com",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "1c0402ce-fea2-48af-ae85-f62a7f6c7cb6",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "esse",
                },
            ],
            "name": "Goodwin and Sons",
            "tags": [
                "quaerat",
                "valeo",
            ],
            "telephones": [
                {
                    "telephone": "(432) 849-2690",
                    "type": shared.CrmTelephoneType.MOBILE,
                },
                {
                    "telephone": "(606) 871-2046",
                    "type": shared.CrmTelephoneType.OTHER,
                },
                {
                    "telephone": "(842) 258-9395",
                    "type": shared.CrmTelephoneType.MOBILE,
                },
            ],
            "timezone": "Europe/San_Marino",
            "updated_at": parse_datetime("2025-02-07T12:07:08.692Z"),
            "websites": [
                "https://wise-possession.org",
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
            "id": "172494b8-00f3-4fd1-812c-ee2040175cb0",
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
                    "id": "00b9288b-80e7-487d-b827-b8ee96896579",
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
            "updated_at": parse_datetime("2021-02-23T10:00:43.229Z"),
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
            "closed_at": parse_datetime("2024-03-03T20:19:43.648Z"),
            "closing_at": parse_datetime("2025-08-10T18:27:16.580Z"),
            "created_at": parse_datetime("2023-07-04T12:48:48.470Z"),
            "currency": "IQD",
            "description": "Tabula cicuta sophismata comis tepidus sit cavus.",
            "id": "73108402-8c3a-41bb-8761-fabdd28d8a3e",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "61f40e19-9ed5-4f4e-bf1d-3021a39513a9",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "conatus",
                },
            ],
            "name": "Frozen Silk Chicken",
            "pipelines": [
                {
                    "id": "b6ecd991-cf05-45f3-9d38-337e7cbd488e",
                    "name": "trans",
                },
            ],
            "probability": 65.0,
            "source": "cubo",
            "stages": [
                {
                    "id": "a2bb3dd8-9944-429d-9e14-b5e0c203d2c4",
                    "name": "tubineus",
                },
                {
                    "id": "202e0e54-e4eb-4d99-b67b-328f0691f7ec",
                    "name": "adfectus",
                },
            ],
            "tags": [
                "causa",
                "suus",
            ],
            "updated_at": parse_datetime("2024-09-29T15:23:23.807Z"),
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
                "start_at": parse_datetime("2024-11-18T17:48:10.885Z"),
            },
            "created_at": parse_datetime("2020-07-14T04:53:23.784Z"),
            "id": "5d88b351-9a11-4132-a3be-20de85cf387f",
            "type": shared.CrmEventType.CALL,
            "updated_at": parse_datetime("2026-09-09T23:33:52.444Z"),
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
                "address1": "528 Forest Road",
                "address2": "Apt. 643",
                "city": "Palm Springs",
                "country_code": "US",
                "postal_code": "55624-6499",
                "region": "New Jersey",
                "region_code": "LA",
            },
            "company_name": "Tillman - Wiegand",
            "created_at": parse_datetime("2019-10-12T11:27:59.003Z"),
            "emails": [
                {
                    "email": "Velda.Sporer16@yahoo.com",
                    "type": shared.CrmEmailType.OTHER,
                },
                {
                    "email": "Velda.Sporer@yahoo.com",
                    "type": shared.CrmEmailType.HOME,
                },
            ],
            "first_name": "Velda",
            "id": "d0c31181-b804-46fb-bf61-ee2423d5d262",
            "is_active": True,
            "last_name": "Sporer",
            "link_urls": [
                "https://classic-sightseeing.com/",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "7ace4194-267c-48f6-8869-56e5735bb8ec",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "sublime",
                },
            ],
            "name": "Velda Sporer",
            "source": "aetas",
            "status": "vesco",
            "telephones": [
                {
                    "telephone": "(955) 643-9849",
                    "type": shared.CrmTelephoneType.OTHER,
                },
                {
                    "telephone": "(621) 811-8800",
                    "type": shared.CrmTelephoneType.WORK,
                },
            ],
            "updated_at": parse_datetime("2020-05-15T04:49:59.458Z"),
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
            "id": "4a46c383-5524-4834-bc87-cf811454d988",
            "is_active": True,
            "name": "Small Steel Bacon",
            "stages": [
                {
                    "active": False,
                    "created_at": parse_datetime("2022-12-28T13:45:38.446Z"),
                    "deal_probability": 84.0,
                    "display_order": 72.0,
                    "id": "4f8d46c1-b18f-4a7b-a225-51067d2034aa",
                    "is_closed": True,
                    "name": "Veniam.",
                    "updated_at": parse_datetime("2025-09-17T09:02:38.569Z"),
                },
            ],
            "updated_at": parse_datetime("2025-10-08T14:36:58.615Z"),
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