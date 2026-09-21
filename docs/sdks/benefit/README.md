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

Create a benefit

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
            "currency": "JOD",
            "description": "Vomito voluptas dolor sed.",
            "employer_contribution_amount": 185006.0,
            "employer_contribution_max_amount": 179093.0,
            "employer_contribution_type": shared.EmployerContributionType.PERCENTAGE,
            "frequency": shared.HrisBenefitFrequency.HOUR,
            "id": "b395db38-c261-454e-9bfe-9466e617f2ee",
            "is_active": False,
            "name": "Frozen Wooden Ball",
            "tax": shared.Tax.PRE_TAX,
            "type": shared.HrisBenefitType.GARNISHMENT,
            "updated_at": parse_datetime("2023-03-07T16:17:00.575Z"),
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

Retrieve a benefit

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

List all benefits

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

Update a benefit

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
            "currency": "JOD",
            "description": "Vomito voluptas dolor sed.",
            "employer_contribution_amount": 185006.0,
            "employer_contribution_max_amount": 179093.0,
            "employer_contribution_type": shared.EmployerContributionType.PERCENTAGE,
            "frequency": shared.HrisBenefitFrequency.HOUR,
            "id": "03fe3c3a-0a32-4f47-af0e-f9e4092754de",
            "is_active": False,
            "name": "Frozen Wooden Ball",
            "tax": shared.Tax.PRE_TAX,
            "type": shared.HrisBenefitType.GARNISHMENT,
            "updated_at": parse_datetime("2023-03-07T16:17:00.582Z"),
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

Remove a benefit

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

Update a benefit

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
            "currency": "JOD",
            "description": "Vomito voluptas dolor sed.",
            "employer_contribution_amount": 185006.0,
            "employer_contribution_max_amount": 179093.0,
            "employer_contribution_type": shared.EmployerContributionType.PERCENTAGE,
            "frequency": shared.HrisBenefitFrequency.HOUR,
            "id": "03fe3c3a-0a32-4f47-af0e-f9e4092754de",
            "is_active": False,
            "name": "Frozen Wooden Ball",
            "tax": shared.Tax.PRE_TAX,
            "type": shared.HrisBenefitType.GARNISHMENT,
            "updated_at": parse_datetime("2023-03-07T16:17:00.582Z"),
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