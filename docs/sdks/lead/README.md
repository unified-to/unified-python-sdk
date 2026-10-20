# Lead

## Overview

### Available Operations

* [create_crm_lead](#create_crm_lead) - Create a lead
* [get_crm_lead](#get_crm_lead) - Retrieve a lead
* [list_crm_leads](#list_crm_leads) - List all leads
* [patch_crm_lead](#patch_crm_lead) - Update a lead
* [remove_crm_lead](#remove_crm_lead) - Remove a lead
* [update_crm_lead](#update_crm_lead) - Update a lead

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

    res = unified_to.lead.create_crm_lead(request={
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
            "id": "bc734cd7-4fb1-4229-b749-5290de676a5d",
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
                    "id": "b6d672ca-9cb9-4139-bbab-3832d4944b72",
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
            "updated_at": parse_datetime("2020-05-17T19:05:56.705Z"),
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

    res = unified_to.lead.get_crm_lead(request={
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

    res = unified_to.lead.list_crm_leads(request={
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

    res = unified_to.lead.patch_crm_lead(request={
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
            "id": "36006639-6365-413e-af58-c659d5d80ba6",
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
                    "id": "33e648ce-3383-44f1-9872-d159a6f05c46",
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
            "updated_at": parse_datetime("2020-05-17T19:05:56.706Z"),
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

    res = unified_to.lead.remove_crm_lead(request={
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

    res = unified_to.lead.update_crm_lead(request={
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
            "id": "36006639-6365-413e-af58-c659d5d80ba6",
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
                    "id": "33e648ce-3383-44f1-9872-d159a6f05c46",
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
            "updated_at": parse_datetime("2020-05-17T19:05:56.706Z"),
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