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

Creates a HrisEarning. Provide the unified HrisEarning fields in the request body; they are mapped to the provider's API. Returns the created HrisEarning.

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
            "currency": "USD",
            "frequency": shared.HrisEarningFrequency.SEMIMONTHLY,
            "id": "348483ee-63d9-4dfc-9e88-fd14175d3fa7",
            "metadata": [],
            "notes": "Deporto truculenter vinum beatae.",
            "start_at": parse_datetime("2022-07-26T18:43:09.755Z"),
            "status": shared.HrisEarningStatus.ENDED,
            "updated_at": parse_datetime("2020-02-09T05:42:41.557Z"),
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

Retrieves a single HrisEarning by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Returns a list of HrisEarnings. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Updates the HrisEarning identified by `id`. Provide the unified HrisEarning fields to change in the request body.

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
            "currency": "USD",
            "frequency": shared.HrisEarningFrequency.SEMIMONTHLY,
            "id": "36c2a2ce-5d66-48ee-8387-0812206e6d51",
            "metadata": [],
            "notes": "Deporto truculenter vinum beatae.",
            "start_at": parse_datetime("2022-07-26T18:43:09.764Z"),
            "status": shared.HrisEarningStatus.ENDED,
            "updated_at": parse_datetime("2020-02-09T05:42:41.559Z"),
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

Deletes the HrisEarning identified by `id`.

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

Updates the HrisEarning identified by `id`. Provide the unified HrisEarning fields to change in the request body.

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
            "currency": "USD",
            "frequency": shared.HrisEarningFrequency.SEMIMONTHLY,
            "id": "36c2a2ce-5d66-48ee-8387-0812206e6d51",
            "metadata": [],
            "notes": "Deporto truculenter vinum beatae.",
            "start_at": parse_datetime("2022-07-26T18:43:09.764Z"),
            "status": shared.HrisEarningStatus.ENDED,
            "updated_at": parse_datetime("2020-02-09T05:42:41.559Z"),
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