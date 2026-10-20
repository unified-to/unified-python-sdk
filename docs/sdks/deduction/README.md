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

Create a deduction

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
            "id": "cb97a615-8c09-430a-8a47-b1121b34fa69",
            "is_active": True,
            "max_amount": 21794.0,
            "metadata": [],
            "notes": "Carmen desidero.",
            "start_at": parse_datetime("2025-03-14T09:29:19.282Z"),
            "type": shared.HrisDeductionType.FIXED,
            "updated_at": parse_datetime("2024-03-21T13:03:39.226Z"),
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

Retrieve a deduction

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

List all deductions

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

Update a deduction

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
            "id": "fea2c387-613b-4f99-86a4-e6262a909d11",
            "is_active": True,
            "max_amount": 21794.0,
            "metadata": [],
            "notes": "Carmen desidero.",
            "start_at": parse_datetime("2025-03-14T09:29:19.298Z"),
            "type": shared.HrisDeductionType.FIXED,
            "updated_at": parse_datetime("2024-03-21T13:03:39.239Z"),
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

Remove a deduction

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

Update a deduction

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
            "id": "fea2c387-613b-4f99-86a4-e6262a909d11",
            "is_active": True,
            "max_amount": 21794.0,
            "metadata": [],
            "notes": "Carmen desidero.",
            "start_at": parse_datetime("2025-03-14T09:29:19.298Z"),
            "type": shared.HrisDeductionType.FIXED,
            "updated_at": parse_datetime("2024-03-21T13:03:39.239Z"),
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