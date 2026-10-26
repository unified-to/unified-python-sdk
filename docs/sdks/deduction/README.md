# Deduction

## Overview

### Available Operations

* [create_hris_deduction](#create_hris_deduction) - Create a deduction
* [get_hris_deduction](#get_hris_deduction) - Retrieve a deduction
* [list_hris_deductions](#list_hris_deductions) - List all deductions
* [patch_hris_deduction](#patch_hris_deduction) - Update a deduction
* [remove_hris_deduction](#remove_hris_deduction) - Remove a deduction
* [update_hris_deduction](#update_hris_deduction) - Update a deduction

## create_hris_deduction

Creates a HrisDeduction. Provide the unified HrisDeduction fields in the request body; they are mapped to the provider's API. Returns the created HrisDeduction.

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisDeduction" method="post" path="/hris/{connection_id}/deduction" example="hris_deduction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.deduction.create_hris_deduction(request={
        "hris_deduction": {
            "amount": 564.0,
            "coverage_level": shared.HrisDeductionCoverageLevel.EMPLOYEE_CHILD,
            "created_at": parse_datetime("2020-02-05T01:46:31.384Z"),
            "employer_amount": 80510.0,
            "employer_type": shared.EmployerType.PERCENTAGE,
            "frequency": shared.HrisDeductionFrequency.ONE_TIME,
            "garnishment_type": shared.GarnishmentType.CHILD_SUPPORT,
            "id": "83127532-a422-4056-8133-940703303d56",
            "is_active": True,
            "max_amount": 21794.0,
            "metadata": [],
            "notes": "Carmen desidero.",
            "start_at": parse_datetime("2025-03-19T03:37:46.086Z"),
            "type": shared.HrisDeductionType.FIXED,
            "updated_at": parse_datetime("2024-03-25T09:17:33.644Z"),
        },
        "connection_id": "<id>",
    })

    assert res.hris_deduction is not None

    # Handle response
    print(res.hris_deduction)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateHrisDeductionRequest](../../models/operations/createhrisdeductionrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreateHrisDeductionResponse](../../models/operations/createhrisdeductionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_deduction

Retrieves a single HrisDeduction by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisDeduction" method="get" path="/hris/{connection_id}/deduction/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.deduction.get_hris_deduction(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_deduction is not None

    # Handle response
    print(res.hris_deduction)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetHrisDeductionRequest](../../models/operations/gethrisdeductionrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetHrisDeductionResponse](../../models/operations/gethrisdeductionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_deductions

Returns a list of HrisDeductions. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisDeductions" method="get" path="/hris/{connection_id}/deduction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.deduction.list_hris_deductions(request={
        "connection_id": "<id>",
    })

    assert res.hris_deductions is not None

    # Handle response
    print(res.hris_deductions)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListHrisDeductionsRequest](../../models/operations/listhrisdeductionsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListHrisDeductionsResponse](../../models/operations/listhrisdeductionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_deduction

Updates the HrisDeduction identified by `id`. Provide the unified HrisDeduction fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisDeduction" method="patch" path="/hris/{connection_id}/deduction/{id}" example="hris_deduction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.deduction.patch_hris_deduction(request={
        "hris_deduction": {
            "amount": 564.0,
            "coverage_level": shared.HrisDeductionCoverageLevel.EMPLOYEE_CHILD,
            "created_at": parse_datetime("2020-02-05T01:46:31.384Z"),
            "employer_amount": 80510.0,
            "employer_type": shared.EmployerType.PERCENTAGE,
            "frequency": shared.HrisDeductionFrequency.ONE_TIME,
            "garnishment_type": shared.GarnishmentType.CHILD_SUPPORT,
            "id": "511a551e-dcde-4924-8793-c41eb6c3c87e",
            "is_active": True,
            "max_amount": 21794.0,
            "metadata": [],
            "notes": "Carmen desidero.",
            "start_at": parse_datetime("2025-03-19T03:37:46.117Z"),
            "type": shared.HrisDeductionType.FIXED,
            "updated_at": parse_datetime("2024-03-25T09:17:33.669Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_deduction is not None

    # Handle response
    print(res.hris_deduction)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchHrisDeductionRequest](../../models/operations/patchhrisdeductionrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.PatchHrisDeductionResponse](../../models/operations/patchhrisdeductionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_deduction

Deletes the HrisDeduction identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisDeduction" method="delete" path="/hris/{connection_id}/deduction/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.deduction.remove_hris_deduction(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.RemoveHrisDeductionRequest](../../models/operations/removehrisdeductionrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.RemoveHrisDeductionResponse](../../models/operations/removehrisdeductionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_deduction

Updates the HrisDeduction identified by `id`. Provide the unified HrisDeduction fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisDeduction" method="put" path="/hris/{connection_id}/deduction/{id}" example="hris_deduction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.deduction.update_hris_deduction(request={
        "hris_deduction": {
            "amount": 564.0,
            "coverage_level": shared.HrisDeductionCoverageLevel.EMPLOYEE_CHILD,
            "created_at": parse_datetime("2020-02-05T01:46:31.384Z"),
            "employer_amount": 80510.0,
            "employer_type": shared.EmployerType.PERCENTAGE,
            "frequency": shared.HrisDeductionFrequency.ONE_TIME,
            "garnishment_type": shared.GarnishmentType.CHILD_SUPPORT,
            "id": "511a551e-dcde-4924-8793-c41eb6c3c87e",
            "is_active": True,
            "max_amount": 21794.0,
            "metadata": [],
            "notes": "Carmen desidero.",
            "start_at": parse_datetime("2025-03-19T03:37:46.117Z"),
            "type": shared.HrisDeductionType.FIXED,
            "updated_at": parse_datetime("2024-03-25T09:17:33.669Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_deduction is not None

    # Handle response
    print(res.hris_deduction)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateHrisDeductionRequest](../../models/operations/updatehrisdeductionrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.UpdateHrisDeductionResponse](../../models/operations/updatehrisdeductionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |