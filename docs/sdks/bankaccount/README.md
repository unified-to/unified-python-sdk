# Bankaccount

## Overview

### Available Operations

* [create_hris_bankaccount](#create_hris_bankaccount) - Create a bankaccount
* [get_hris_bankaccount](#get_hris_bankaccount) - Retrieve a bankaccount
* [list_hris_bankaccounts](#list_hris_bankaccounts) - List all bankaccounts
* [patch_hris_bankaccount](#patch_hris_bankaccount) - Update a bankaccount
* [remove_hris_bankaccount](#remove_hris_bankaccount) - Remove a bankaccount
* [update_hris_bankaccount](#update_hris_bankaccount) - Update a bankaccount

## create_hris_bankaccount

Creates a HrisBankaccount. Provide the unified HrisBankaccount fields in the request body; they are mapped to the provider's API. Returns the created HrisBankaccount.

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisBankaccount" method="post" path="/hris/{connection_id}/bankaccount" example="hris_bankaccount" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bankaccount.create_hris_bankaccount(request={
        "hris_bankaccount": {
            "account_number": "****3777",
            "account_number_last4": "3777",
            "account_type": shared.HrisBankaccountAccountType.CHECKING,
            "bank_name": "Huel Group",
            "country_code": "US",
            "created_at": parse_datetime("2019-11-16T16:43:45.976Z"),
            "currency": "USD",
            "id": "3468ebd9-250e-4abe-9b97-508bf2361433",
            "is_primary": True,
            "metadata": [],
            "name": "Granville Schumm - Checking",
            "priority": 2.0,
            "routing_number": "448650724",
            "split_amount": 98.0,
            "split_type": shared.SplitType.PERCENTAGE,
            "updated_at": parse_datetime("2025-07-02T01:38:52.642Z"),
        },
        "connection_id": "<id>",
    })

    assert res.hris_bankaccount is not None

    # Handle response
    print(res.hris_bankaccount)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateHrisBankaccountRequest](../../models/operations/createhrisbankaccountrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateHrisBankaccountResponse](../../models/operations/createhrisbankaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_bankaccount

Retrieves a single HrisBankaccount by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisBankaccount" method="get" path="/hris/{connection_id}/bankaccount/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bankaccount.get_hris_bankaccount(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_bankaccount is not None

    # Handle response
    print(res.hris_bankaccount)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetHrisBankaccountRequest](../../models/operations/gethrisbankaccountrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetHrisBankaccountResponse](../../models/operations/gethrisbankaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_bankaccounts

Returns a list of HrisBankaccounts. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisBankaccounts" method="get" path="/hris/{connection_id}/bankaccount" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bankaccount.list_hris_bankaccounts(request={
        "connection_id": "<id>",
    })

    assert res.hris_bankaccounts is not None

    # Handle response
    print(res.hris_bankaccounts)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListHrisBankaccountsRequest](../../models/operations/listhrisbankaccountsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListHrisBankaccountsResponse](../../models/operations/listhrisbankaccountsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_bankaccount

Updates the HrisBankaccount identified by `id`. Provide the unified HrisBankaccount fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisBankaccount" method="patch" path="/hris/{connection_id}/bankaccount/{id}" example="hris_bankaccount" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bankaccount.patch_hris_bankaccount(request={
        "hris_bankaccount": {
            "account_number": "****3777",
            "account_number_last4": "3777",
            "account_type": shared.HrisBankaccountAccountType.CHECKING,
            "bank_name": "Huel Group",
            "country_code": "US",
            "created_at": parse_datetime("2019-11-16T16:43:45.976Z"),
            "currency": "USD",
            "id": "b83bd056-9674-4f6e-a525-95182b7b0bd0",
            "is_primary": True,
            "metadata": [],
            "name": "Granville Schumm - Checking",
            "priority": 2.0,
            "routing_number": "448650724",
            "split_amount": 98.0,
            "split_type": shared.SplitType.PERCENTAGE,
            "updated_at": parse_datetime("2025-07-02T01:38:52.658Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_bankaccount is not None

    # Handle response
    print(res.hris_bankaccount)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchHrisBankaccountRequest](../../models/operations/patchhrisbankaccountrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchHrisBankaccountResponse](../../models/operations/patchhrisbankaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_bankaccount

Deletes the HrisBankaccount identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisBankaccount" method="delete" path="/hris/{connection_id}/bankaccount/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bankaccount.remove_hris_bankaccount(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RemoveHrisBankaccountRequest](../../models/operations/removehrisbankaccountrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveHrisBankaccountResponse](../../models/operations/removehrisbankaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_bankaccount

Updates the HrisBankaccount identified by `id`. Provide the unified HrisBankaccount fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisBankaccount" method="put" path="/hris/{connection_id}/bankaccount/{id}" example="hris_bankaccount" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bankaccount.update_hris_bankaccount(request={
        "hris_bankaccount": {
            "account_number": "****3777",
            "account_number_last4": "3777",
            "account_type": shared.HrisBankaccountAccountType.CHECKING,
            "bank_name": "Huel Group",
            "country_code": "US",
            "created_at": parse_datetime("2019-11-16T16:43:45.976Z"),
            "currency": "USD",
            "id": "b83bd056-9674-4f6e-a525-95182b7b0bd0",
            "is_primary": True,
            "metadata": [],
            "name": "Granville Schumm - Checking",
            "priority": 2.0,
            "routing_number": "448650724",
            "split_amount": 98.0,
            "split_type": shared.SplitType.PERCENTAGE,
            "updated_at": parse_datetime("2025-07-02T01:38:52.658Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_bankaccount is not None

    # Handle response
    print(res.hris_bankaccount)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateHrisBankaccountRequest](../../models/operations/updatehrisbankaccountrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateHrisBankaccountResponse](../../models/operations/updatehrisbankaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |