# Taxwithholding

## Overview

### Available Operations

* [create_hris_taxwithholding](#create_hris_taxwithholding) - Create a taxwithholding
* [get_hris_taxwithholding](#get_hris_taxwithholding) - Retrieve a taxwithholding
* [list_hris_taxwithholdings](#list_hris_taxwithholdings) - List all taxwithholdings
* [patch_hris_taxwithholding](#patch_hris_taxwithholding) - Update a taxwithholding
* [remove_hris_taxwithholding](#remove_hris_taxwithholding) - Remove a taxwithholding
* [update_hris_taxwithholding](#update_hris_taxwithholding) - Update a taxwithholding

## create_hris_taxwithholding

Creates a HrisTaxwithholding. Provide the unified HrisTaxwithholding fields in the request body; they are mapped to the provider's API. Returns the created HrisTaxwithholding.

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisTaxwithholding" method="post" path="/hris/{connection_id}/taxwithholding" example="hris_taxwithholding" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.taxwithholding.create_hris_taxwithholding(request={
        "hris_taxwithholding": {
            "allowances": 1.0,
            "country": "US",
            "created_at": parse_datetime("2022-08-14T05:49:35.141Z"),
            "effective_at": parse_datetime("2022-08-14T05:49:35.141Z"),
            "extra_withholding_amount": 10.0,
            "filing_status": shared.FilingStatus.QUALIFYING_SURVIVOR,
            "form": shared.Form.STATE_FORM,
            "id": "0753c1a7-975a-47be-a9bb-14529f2d5ec2",
            "is_exempt": False,
            "is_resident": True,
            "jurisdiction": "OH",
            "jurisdiction_type": shared.JurisdictionType.STATE,
            "metadata": [],
            "override_amount": 19.0,
            "override_type": shared.OverrideType.FIXED_AMOUNT,
            "updated_at": parse_datetime("2026-09-28T07:48:30.232Z"),
        },
        "connection_id": "<id>",
    })

    assert res.hris_taxwithholding is not None

    # Handle response
    print(res.hris_taxwithholding)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateHrisTaxwithholdingRequest](../../models/operations/createhristaxwithholdingrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.CreateHrisTaxwithholdingResponse](../../models/operations/createhristaxwithholdingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_taxwithholding

Retrieves a single HrisTaxwithholding by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisTaxwithholding" method="get" path="/hris/{connection_id}/taxwithholding/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.taxwithholding.get_hris_taxwithholding(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_taxwithholding is not None

    # Handle response
    print(res.hris_taxwithholding)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetHrisTaxwithholdingRequest](../../models/operations/gethristaxwithholdingrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.GetHrisTaxwithholdingResponse](../../models/operations/gethristaxwithholdingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_taxwithholdings

Returns a list of HrisTaxwithholdings. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisTaxwithholdings" method="get" path="/hris/{connection_id}/taxwithholding" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.taxwithholding.list_hris_taxwithholdings(request={
        "connection_id": "<id>",
    })

    assert res.hris_taxwithholdings is not None

    # Handle response
    print(res.hris_taxwithholdings)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListHrisTaxwithholdingsRequest](../../models/operations/listhristaxwithholdingsrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.ListHrisTaxwithholdingsResponse](../../models/operations/listhristaxwithholdingsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_taxwithholding

Updates the HrisTaxwithholding identified by `id`. Provide the unified HrisTaxwithholding fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisTaxwithholding" method="patch" path="/hris/{connection_id}/taxwithholding/{id}" example="hris_taxwithholding" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.taxwithholding.patch_hris_taxwithholding(request={
        "hris_taxwithholding": {
            "allowances": 1.0,
            "country": "US",
            "created_at": parse_datetime("2022-08-14T05:49:35.141Z"),
            "effective_at": parse_datetime("2022-08-14T05:49:35.141Z"),
            "extra_withholding_amount": 10.0,
            "filing_status": shared.FilingStatus.QUALIFYING_SURVIVOR,
            "form": shared.Form.STATE_FORM,
            "id": "75d164df-d876-417d-a386-0fc50fa3903d",
            "is_exempt": False,
            "is_resident": True,
            "jurisdiction": "OH",
            "jurisdiction_type": shared.JurisdictionType.STATE,
            "metadata": [],
            "override_amount": 19.0,
            "override_type": shared.OverrideType.FIXED_AMOUNT,
            "updated_at": parse_datetime("2026-09-28T07:48:30.248Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_taxwithholding is not None

    # Handle response
    print(res.hris_taxwithholding)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PatchHrisTaxwithholdingRequest](../../models/operations/patchhristaxwithholdingrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.PatchHrisTaxwithholdingResponse](../../models/operations/patchhristaxwithholdingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_taxwithholding

Deletes the HrisTaxwithholding identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisTaxwithholding" method="delete" path="/hris/{connection_id}/taxwithholding/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.taxwithholding.remove_hris_taxwithholding(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RemoveHrisTaxwithholdingRequest](../../models/operations/removehristaxwithholdingrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.RemoveHrisTaxwithholdingResponse](../../models/operations/removehristaxwithholdingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_taxwithholding

Updates the HrisTaxwithholding identified by `id`. Provide the unified HrisTaxwithholding fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisTaxwithholding" method="put" path="/hris/{connection_id}/taxwithholding/{id}" example="hris_taxwithholding" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.taxwithholding.update_hris_taxwithholding(request={
        "hris_taxwithholding": {
            "allowances": 1.0,
            "country": "US",
            "created_at": parse_datetime("2022-08-14T05:49:35.141Z"),
            "effective_at": parse_datetime("2022-08-14T05:49:35.141Z"),
            "extra_withholding_amount": 10.0,
            "filing_status": shared.FilingStatus.QUALIFYING_SURVIVOR,
            "form": shared.Form.STATE_FORM,
            "id": "75d164df-d876-417d-a386-0fc50fa3903d",
            "is_exempt": False,
            "is_resident": True,
            "jurisdiction": "OH",
            "jurisdiction_type": shared.JurisdictionType.STATE,
            "metadata": [],
            "override_amount": 19.0,
            "override_type": shared.OverrideType.FIXED_AMOUNT,
            "updated_at": parse_datetime("2026-09-28T07:48:30.248Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_taxwithholding is not None

    # Handle response
    print(res.hris_taxwithholding)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateHrisTaxwithholdingRequest](../../models/operations/updatehristaxwithholdingrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.UpdateHrisTaxwithholdingResponse](../../models/operations/updatehristaxwithholdingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |