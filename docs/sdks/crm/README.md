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
            "id": "054b6b81-da14-4da6-9512-0290a7448cd0",
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
                    "id": "d8ad53c2-62e5-4d81-9cbb-fd4cd00ee2a2",
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
            "updated_at": parse_datetime("2025-02-28T20:59:16.261Z"),
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
            "id": "1ca9e006-7a9b-4a1a-866f-b255a908afe7",
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
                    "id": "52e29caf-41c1-4d5a-b965-58d2a38777b5",
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
            "updated_at": parse_datetime("2021-02-24T03:16:00.728Z"),
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
            "closed_at": parse_datetime("2024-03-09T18:53:25.631Z"),
            "closing_at": parse_datetime("2025-08-29T12:34:39.752Z"),
            "created_at": parse_datetime("2023-07-04T12:48:48.470Z"),
            "currency": "IQD",
            "description": "Tabula cicuta sophismata comis tepidus sit cavus.",
            "id": "aa95bafb-d207-4e33-9a57-ec15e964f39c",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "02d268d4-b535-45b3-8e61-53d1ee6b46fa",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "conatus",
                },
            ],
            "name": "Frozen Silk Chicken",
            "pipelines": [
                {
                    "id": "af5d98e5-2523-476d-b15f-8289cea0caba",
                    "name": "trans",
                },
            ],
            "probability": 65.0,
            "source": "cubo",
            "stages": [
                {
                    "id": "ac80d9a0-d774-4ec3-948a-7b37fa056574",
                    "name": "tubineus",
                },
                {
                    "id": "e26bbeb6-ad9e-4321-831e-8a7cc43e281e",
                    "name": "adfectus",
                },
            ],
            "tags": [
                "causa",
                "suus",
            ],
            "updated_at": parse_datetime("2024-10-10T16:52:26.088Z"),
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
                "start_at": parse_datetime("2024-12-08T21:11:58.242Z"),
            },
            "created_at": parse_datetime("2020-07-14T04:53:23.784Z"),
            "id": "be7f0919-1ab7-4e18-b1bd-d7aa3d30f759",
            "type": shared.CrmEventType.CALL,
            "updated_at": parse_datetime("2026-10-08T11:52:26.112Z"),
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
            "id": "b8932295-8f59-4e55-9a32-9f9df58afb3f",
            "is_active": True,
            "last_name": "Sporer",
            "link_urls": [
                "https://ruddy-unblinking.info/",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "74bcf488-5e6a-4364-b123-b2dca3539fd7",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "vitiosus",
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
            "title": "Direct Research Assistant",
            "updated_at": parse_datetime("2020-05-17T15:20:06.235Z"),
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
            "id": "3c7e75a7-6ea6-4fbf-aa5d-1ec7ac75d393",
            "is_active": True,
            "name": "Small Steel Bacon",
            "stages": [
                {
                    "active": False,
                    "created_at": parse_datetime("2022-12-28T13:45:38.446Z"),
                    "deal_probability": 84.0,
                    "display_order": 72.0,
                    "id": "3a407a12-5779-4b41-8b89-2071415468f1",
                    "is_closed": True,
                    "name": "Veniam.",
                    "updated_at": parse_datetime("2025-10-08T06:53:56.080Z"),
                },
            ],
            "updated_at": parse_datetime("2025-10-29T23:11:35.001Z"),
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
            "id": "774c7974-966e-4d98-b956-252cb19aecc2",
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
                    "id": "c1082a7d-37eb-4636-bc80-0e3a84c8d851",
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
            "updated_at": parse_datetime("2025-02-28T20:59:16.279Z"),
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
            "id": "bb18fa30-a3cd-4ed8-a598-a6efc7f970b6",
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
                    "id": "5ed3cfbd-9f59-47f9-8ae1-6424fabe11c2",
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
            "updated_at": parse_datetime("2021-02-24T03:16:00.729Z"),
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
            "closed_at": parse_datetime("2024-03-09T18:53:25.634Z"),
            "closing_at": parse_datetime("2025-08-29T12:34:39.763Z"),
            "created_at": parse_datetime("2023-07-04T12:48:48.470Z"),
            "currency": "IQD",
            "description": "Tabula cicuta sophismata comis tepidus sit cavus.",
            "id": "1081b832-ba28-4007-b398-20b237ceb6c2",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "b33e82e8-3a34-4554-9ad9-0cd39c039032",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "conatus",
                },
            ],
            "name": "Frozen Silk Chicken",
            "pipelines": [
                {
                    "id": "8552803a-a795-4523-af93-d88be97d5bc4",
                    "name": "trans",
                },
            ],
            "probability": 65.0,
            "source": "cubo",
            "stages": [
                {
                    "id": "3da6dba3-5510-44aa-ab46-f95cc69bcf8b",
                    "name": "tubineus",
                },
                {
                    "id": "41e5f005-b9b8-4ad2-86af-2cefcc22a27f",
                    "name": "adfectus",
                },
            ],
            "tags": [
                "causa",
                "suus",
            ],
            "updated_at": parse_datetime("2024-10-10T16:52:26.095Z"),
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
                "start_at": parse_datetime("2024-12-08T21:11:58.273Z"),
            },
            "created_at": parse_datetime("2020-07-14T04:53:23.784Z"),
            "id": "9e53471f-35b7-4f52-957c-fb88720c7cde",
            "type": shared.CrmEventType.CALL,
            "updated_at": parse_datetime("2026-10-08T11:52:26.156Z"),
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
            "id": "30a9d2ae-d575-4013-91a0-8296c7786a5b",
            "is_active": True,
            "last_name": "Sporer",
            "link_urls": [
                "https://ruddy-unblinking.info/",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "56292293-a6a8-4423-bb0b-b39f29db0dcc",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "vitiosus",
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
            "title": "Direct Research Assistant",
            "updated_at": parse_datetime("2020-05-17T15:20:06.238Z"),
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
            "id": "5f36173f-6345-4bdf-83fe-7ce6189b0a23",
            "is_active": True,
            "name": "Small Steel Bacon",
            "stages": [
                {
                    "active": False,
                    "created_at": parse_datetime("2022-12-28T13:45:38.446Z"),
                    "deal_probability": 84.0,
                    "display_order": 72.0,
                    "id": "8a1f7744-f62c-4116-95c1-a32a7cc7b081",
                    "is_closed": True,
                    "name": "Veniam.",
                    "updated_at": parse_datetime("2025-10-08T06:53:56.086Z"),
                },
            ],
            "updated_at": parse_datetime("2025-10-29T23:11:35.007Z"),
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
            "id": "774c7974-966e-4d98-b956-252cb19aecc2",
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
                    "id": "c1082a7d-37eb-4636-bc80-0e3a84c8d851",
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
            "updated_at": parse_datetime("2025-02-28T20:59:16.279Z"),
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
            "id": "bb18fa30-a3cd-4ed8-a598-a6efc7f970b6",
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
                    "id": "5ed3cfbd-9f59-47f9-8ae1-6424fabe11c2",
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
            "updated_at": parse_datetime("2021-02-24T03:16:00.729Z"),
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
            "closed_at": parse_datetime("2024-03-09T18:53:25.634Z"),
            "closing_at": parse_datetime("2025-08-29T12:34:39.763Z"),
            "created_at": parse_datetime("2023-07-04T12:48:48.470Z"),
            "currency": "IQD",
            "description": "Tabula cicuta sophismata comis tepidus sit cavus.",
            "id": "1081b832-ba28-4007-b398-20b237ceb6c2",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "b33e82e8-3a34-4554-9ad9-0cd39c039032",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "conatus",
                },
            ],
            "name": "Frozen Silk Chicken",
            "pipelines": [
                {
                    "id": "8552803a-a795-4523-af93-d88be97d5bc4",
                    "name": "trans",
                },
            ],
            "probability": 65.0,
            "source": "cubo",
            "stages": [
                {
                    "id": "3da6dba3-5510-44aa-ab46-f95cc69bcf8b",
                    "name": "tubineus",
                },
                {
                    "id": "41e5f005-b9b8-4ad2-86af-2cefcc22a27f",
                    "name": "adfectus",
                },
            ],
            "tags": [
                "causa",
                "suus",
            ],
            "updated_at": parse_datetime("2024-10-10T16:52:26.095Z"),
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
                "start_at": parse_datetime("2024-12-08T21:11:58.273Z"),
            },
            "created_at": parse_datetime("2020-07-14T04:53:23.784Z"),
            "id": "9e53471f-35b7-4f52-957c-fb88720c7cde",
            "type": shared.CrmEventType.CALL,
            "updated_at": parse_datetime("2026-10-08T11:52:26.156Z"),
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
            "id": "30a9d2ae-d575-4013-91a0-8296c7786a5b",
            "is_active": True,
            "last_name": "Sporer",
            "link_urls": [
                "https://ruddy-unblinking.info/",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "56292293-a6a8-4423-bb0b-b39f29db0dcc",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "vitiosus",
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
            "title": "Direct Research Assistant",
            "updated_at": parse_datetime("2020-05-17T15:20:06.238Z"),
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
            "id": "5f36173f-6345-4bdf-83fe-7ce6189b0a23",
            "is_active": True,
            "name": "Small Steel Bacon",
            "stages": [
                {
                    "active": False,
                    "created_at": parse_datetime("2022-12-28T13:45:38.446Z"),
                    "deal_probability": 84.0,
                    "display_order": 72.0,
                    "id": "8a1f7744-f62c-4116-95c1-a32a7cc7b081",
                    "is_closed": True,
                    "name": "Veniam.",
                    "updated_at": parse_datetime("2025-10-08T06:53:56.086Z"),
                },
            ],
            "updated_at": parse_datetime("2025-10-29T23:11:35.007Z"),
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