# Benefit

## Overview

### Available Operations

* [create_hris_benefit](#create_hris_benefit) - Create a benefit
* [get_hris_benefit](#get_hris_benefit) - Retrieve a benefit
* [list_hris_benefits](#list_hris_benefits) - List all benefits
* [patch_hris_benefit](#patch_hris_benefit) - Update a benefit
* [remove_hris_benefit](#remove_hris_benefit) - Remove a benefit
* [update_hris_benefit](#update_hris_benefit) - Update a benefit

## create_hris_benefit

Creates a HrisBenefit. Provide the unified HrisBenefit fields in the request body; they are mapped to the provider's API. Returns the created HrisBenefit.

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisBenefit" method="post" path="/hris/{connection_id}/benefit" example="hris_benefit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.benefit.create_hris_benefit(request={
        "hris_benefit": {
            "coverage_level": shared.CoverageLevel.EMPLOYEE_SPOUSE,
            "created_at": parse_datetime("2020-06-11T01:24:05.654Z"),
            "currency": "GBP",
            "description": "Vomito voluptas dolor sed.",
            "employer_contribution_amount": 185006.0,
            "employer_contribution_max_amount": 179093.0,
            "employer_contribution_type": shared.EmployerContributionType.PERCENTAGE,
            "frequency": shared.HrisBenefitFrequency.MONTH,
            "id": "495cb30e-e666-430b-9ad2-4dbf6844001d",
            "is_active": False,
            "metadata": [],
            "name": "Frozen Wooden Ball",
            "tax": shared.Tax.PRE_TAX,
            "type": shared.HrisBenefitType.OTHER,
            "updated_at": parse_datetime("2023-03-24T18:54:29.596Z"),
        },
        "connection_id": "<id>",
    })

    assert res.hris_benefit is not None

    # Handle response
    print(res.hris_benefit)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateHrisBenefitRequest](../../models/operations/createhrisbenefitrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateHrisBenefitResponse](../../models/operations/createhrisbenefitresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_benefit

Retrieves a single HrisBenefit by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisBenefit" method="get" path="/hris/{connection_id}/benefit/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.benefit.get_hris_benefit(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_benefit is not None

    # Handle response
    print(res.hris_benefit)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetHrisBenefitRequest](../../models/operations/gethrisbenefitrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetHrisBenefitResponse](../../models/operations/gethrisbenefitresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_benefits

Returns a list of HrisBenefits. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisBenefits" method="get" path="/hris/{connection_id}/benefit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.benefit.list_hris_benefits(request={
        "connection_id": "<id>",
    })

    assert res.hris_benefits is not None

    # Handle response
    print(res.hris_benefits)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListHrisBenefitsRequest](../../models/operations/listhrisbenefitsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListHrisBenefitsResponse](../../models/operations/listhrisbenefitsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_benefit

Updates the HrisBenefit identified by `id`. Provide the unified HrisBenefit fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisBenefit" method="patch" path="/hris/{connection_id}/benefit/{id}" example="hris_benefit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.benefit.patch_hris_benefit(request={
        "hris_benefit": {
            "coverage_level": shared.CoverageLevel.EMPLOYEE_SPOUSE,
            "created_at": parse_datetime("2020-06-11T01:24:05.654Z"),
            "currency": "GBP",
            "description": "Vomito voluptas dolor sed.",
            "employer_contribution_amount": 185006.0,
            "employer_contribution_max_amount": 179093.0,
            "employer_contribution_type": shared.EmployerContributionType.PERCENTAGE,
            "frequency": shared.HrisBenefitFrequency.MONTH,
            "id": "207e10f2-9942-49c1-91be-d9ffac38c4cc",
            "is_active": False,
            "metadata": [],
            "name": "Frozen Wooden Ball",
            "tax": shared.Tax.PRE_TAX,
            "type": shared.HrisBenefitType.OTHER,
            "updated_at": parse_datetime("2023-03-24T18:54:29.608Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_benefit is not None

    # Handle response
    print(res.hris_benefit)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchHrisBenefitRequest](../../models/operations/patchhrisbenefitrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchHrisBenefitResponse](../../models/operations/patchhrisbenefitresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_benefit

Deletes the HrisBenefit identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisBenefit" method="delete" path="/hris/{connection_id}/benefit/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.benefit.remove_hris_benefit(request={
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
| `request`                                                                                  | [operations.RemoveHrisBenefitRequest](../../models/operations/removehrisbenefitrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveHrisBenefitResponse](../../models/operations/removehrisbenefitresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_benefit

Updates the HrisBenefit identified by `id`. Provide the unified HrisBenefit fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisBenefit" method="put" path="/hris/{connection_id}/benefit/{id}" example="hris_benefit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.benefit.update_hris_benefit(request={
        "hris_benefit": {
            "coverage_level": shared.CoverageLevel.EMPLOYEE_SPOUSE,
            "created_at": parse_datetime("2020-06-11T01:24:05.654Z"),
            "currency": "GBP",
            "description": "Vomito voluptas dolor sed.",
            "employer_contribution_amount": 185006.0,
            "employer_contribution_max_amount": 179093.0,
            "employer_contribution_type": shared.EmployerContributionType.PERCENTAGE,
            "frequency": shared.HrisBenefitFrequency.MONTH,
            "id": "207e10f2-9942-49c1-91be-d9ffac38c4cc",
            "is_active": False,
            "metadata": [],
            "name": "Frozen Wooden Ball",
            "tax": shared.Tax.PRE_TAX,
            "type": shared.HrisBenefitType.OTHER,
            "updated_at": parse_datetime("2023-03-24T18:54:29.608Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_benefit is not None

    # Handle response
    print(res.hris_benefit)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateHrisBenefitRequest](../../models/operations/updatehrisbenefitrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateHrisBenefitResponse](../../models/operations/updatehrisbenefitresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |