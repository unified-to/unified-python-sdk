# Earning

## Overview

### Available Operations

* [create_hris_earning](#create_hris_earning) - Create an earning
* [get_hris_earning](#get_hris_earning) - Retrieve an earning
* [list_hris_earnings](#list_hris_earnings) - List all earnings
* [patch_hris_earning](#patch_hris_earning) - Update an earning
* [remove_hris_earning](#remove_hris_earning) - Remove an earning
* [update_hris_earning](#update_hris_earning) - Update an earning

## create_hris_earning

Create an earning

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisEarning" method="post" path="/hris/{connection_id}/earning" example="hris_earning" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.earning.create_hris_earning(request={
        "hris_earning": {
            "amount": 4026.0,
            "created_at": parse_datetime("2019-01-26T12:44:52.326Z"),
            "currency": "PKR",
            "frequency": shared.HrisEarningFrequency.BIWEEKLY,
            "id": "b6e6a273-eb01-4360-a882-f99d50b59979",
            "notes": "Truculenter vinum beatae.",
            "start_at": parse_datetime("2022-07-23T04:12:47.832Z"),
            "status": shared.HrisEarningStatus.PROCESSED,
            "updated_at": parse_datetime("2020-02-08T04:03:44.335Z"),
        },
        "connection_id": "<id>",
    })

    assert res.hris_earning is not None

    # Handle response
    print(res.hris_earning)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateHrisEarningRequest](../../models/operations/createhrisearningrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateHrisEarningResponse](../../models/operations/createhrisearningresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_earning

Retrieve an earning

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisEarning" method="get" path="/hris/{connection_id}/earning/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.earning.get_hris_earning(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_earning is not None

    # Handle response
    print(res.hris_earning)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetHrisEarningRequest](../../models/operations/gethrisearningrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetHrisEarningResponse](../../models/operations/gethrisearningresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_earnings

List all earnings

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisEarnings" method="get" path="/hris/{connection_id}/earning" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.earning.list_hris_earnings(request={
        "connection_id": "<id>",
    })

    assert res.hris_earnings is not None

    # Handle response
    print(res.hris_earnings)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListHrisEarningsRequest](../../models/operations/listhrisearningsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListHrisEarningsResponse](../../models/operations/listhrisearningsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_earning

Update an earning

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisEarning" method="patch" path="/hris/{connection_id}/earning/{id}" example="hris_earning" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.earning.patch_hris_earning(request={
        "hris_earning": {
            "amount": 4026.0,
            "created_at": parse_datetime("2019-01-26T12:44:52.326Z"),
            "currency": "PKR",
            "frequency": shared.HrisEarningFrequency.BIWEEKLY,
            "id": "d9d8cf9f-340c-47fb-b9eb-8ea51e4a8f93",
            "notes": "Truculenter vinum beatae.",
            "start_at": parse_datetime("2022-07-23T04:12:47.836Z"),
            "status": shared.HrisEarningStatus.PROCESSED,
            "updated_at": parse_datetime("2020-02-08T04:03:44.337Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_earning is not None

    # Handle response
    print(res.hris_earning)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchHrisEarningRequest](../../models/operations/patchhrisearningrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchHrisEarningResponse](../../models/operations/patchhrisearningresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_earning

Remove an earning

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisEarning" method="delete" path="/hris/{connection_id}/earning/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.earning.remove_hris_earning(request={
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
| `request`                                                                                  | [operations.RemoveHrisEarningRequest](../../models/operations/removehrisearningrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveHrisEarningResponse](../../models/operations/removehrisearningresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_earning

Update an earning

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisEarning" method="put" path="/hris/{connection_id}/earning/{id}" example="hris_earning" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.earning.update_hris_earning(request={
        "hris_earning": {
            "amount": 4026.0,
            "created_at": parse_datetime("2019-01-26T12:44:52.326Z"),
            "currency": "PKR",
            "frequency": shared.HrisEarningFrequency.BIWEEKLY,
            "id": "d9d8cf9f-340c-47fb-b9eb-8ea51e4a8f93",
            "notes": "Truculenter vinum beatae.",
            "start_at": parse_datetime("2022-07-23T04:12:47.836Z"),
            "status": shared.HrisEarningStatus.PROCESSED,
            "updated_at": parse_datetime("2020-02-08T04:03:44.337Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_earning is not None

    # Handle response
    print(res.hris_earning)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateHrisEarningRequest](../../models/operations/updatehrisearningrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateHrisEarningResponse](../../models/operations/updatehrisearningresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |