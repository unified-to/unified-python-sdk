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

Create a bankaccount

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
            "created_at": parse_datetime("2019-11-16T16:43:45.976Z"),
            "id": "4e298ff9-1f66-4c1f-b1ec-5ee895cda7bf",
            "is_primary": False,
            "name": "Checking Account",
            "routing_number": "448650724",
            "updated_at": parse_datetime("2025-06-04T11:30:29.787Z"),
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

Retrieve a bankaccount

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

List all bankaccounts

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

Update a bankaccount

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
            "created_at": parse_datetime("2019-11-16T16:43:45.976Z"),
            "id": "6b53796b-c6e2-4608-939f-57d8d920c7b2",
            "is_primary": False,
            "name": "Checking Account",
            "routing_number": "448650724",
            "updated_at": parse_datetime("2025-06-04T11:30:29.792Z"),
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

Remove a bankaccount

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

Update a bankaccount

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
            "created_at": parse_datetime("2019-11-16T16:43:45.976Z"),
            "id": "6b53796b-c6e2-4608-939f-57d8d920c7b2",
            "is_primary": False,
            "name": "Checking Account",
            "routing_number": "448650724",
            "updated_at": parse_datetime("2025-06-04T11:30:29.792Z"),
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