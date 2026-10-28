# Call

## Overview

### Available Operations

* [create_uc_call](#create_uc_call) - Create a call
* [get_uc_call](#get_uc_call) - Retrieve a call
* [list_uc_calls](#list_uc_calls) - List all calls
* [patch_uc_call](#patch_uc_call) - Update a call
* [update_uc_call](#update_uc_call) - Update a call

## create_uc_call

Creates a UcCall. Provide the unified UcCall fields in the request body; they are mapped to the provider's API. Returns the created UcCall.

### Example Usage

<!-- UsageSnippet language="python" operationID="createUcCall" method="post" path="/uc/{connection_id}/call" example="uc_call" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.call.create_uc_call(request={
        "uc_call": {
            "answer_at": parse_datetime("2025-05-17T18:43:46.540Z"),
            "contacts": [],
            "conversation_identifier": "4885cf9d-f798-4370-9d01-9305de9c1a95",
            "cost_amount": 1.564,
            "created_at": parse_datetime("2023-04-22T19:05:34.882Z"),
            "currency": "USD",
            "duration_seconds": 2556.0,
            "end_at": parse_datetime("2024-06-01T06:53:22.752Z"),
            "id": "4885cf9d-f798-4370-9d01-9305de9c1a95",
            "is_private": False,
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.UcMetadataFormat.PRICE,
                    "id": "4d997d09-af0e-487e-96e8-47736f453d49",
                    "namespace": "custom",
                    "slug": "custom_field",
                    "value": "tui",
                },
            ],
            "start_at": parse_datetime("2023-12-18T17:34:06.179Z"),
            "status": shared.UcCallStatus.IN_PROGRESS,
            "telephone": {
                "telephone": "(493) 534-0768",
                "type": shared.PropertyUcCallTelephoneType.MOBILE,
            },
            "type": shared.UcCallType.INBOUND,
            "updated_at": parse_datetime("2023-08-03T22:08:05.450Z"),
            "user_phone": "819-894-3317 x163",
        },
        "connection_id": "<id>",
    })

    assert res.uc_call is not None

    # Handle response
    print(res.uc_call)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.CreateUcCallRequest](../../models/operations/createuccallrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.CreateUcCallResponse](../../models/operations/createuccallresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_uc_call

Retrieves a single UcCall by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUcCall" method="get" path="/uc/{connection_id}/call/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.call.get_uc_call(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_call is not None

    # Handle response
    print(res.uc_call)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetUcCallRequest](../../models/operations/getuccallrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.GetUcCallResponse](../../models/operations/getuccallresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_uc_calls

Returns a list of UcCalls. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listUcCalls" method="get" path="/uc/{connection_id}/call" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.call.list_uc_calls(request={
        "connection_id": "<id>",
    })

    assert res.uc_calls is not None

    # Handle response
    print(res.uc_calls)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ListUcCallsRequest](../../models/operations/listuccallsrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.ListUcCallsResponse](../../models/operations/listuccallsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_uc_call

Updates the UcCall identified by `id`. Provide the unified UcCall fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchUcCall" method="patch" path="/uc/{connection_id}/call/{id}" example="uc_call" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.call.patch_uc_call(request={
        "uc_call": {
            "answer_at": parse_datetime("2025-05-17T18:43:46.560Z"),
            "contacts": [],
            "conversation_identifier": "cb2ca4d9-0758-4877-9276-dffdf8d4e22e",
            "cost_amount": 1.564,
            "created_at": parse_datetime("2023-04-22T19:05:34.882Z"),
            "currency": "USD",
            "duration_seconds": 2556.0,
            "end_at": parse_datetime("2024-06-01T06:53:22.763Z"),
            "id": "cb2ca4d9-0758-4877-9276-dffdf8d4e22e",
            "is_private": False,
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.UcMetadataFormat.PRICE,
                    "id": "15450b99-002d-4c41-8926-8ead5939867b",
                    "namespace": "custom",
                    "slug": "custom_field",
                    "value": "tui",
                },
            ],
            "start_at": parse_datetime("2023-12-18T17:34:06.185Z"),
            "status": shared.UcCallStatus.IN_PROGRESS,
            "telephone": {
                "telephone": "(493) 534-0768",
                "type": shared.PropertyUcCallTelephoneType.MOBILE,
            },
            "type": shared.UcCallType.INBOUND,
            "updated_at": parse_datetime("2023-08-03T22:08:05.453Z"),
            "user_phone": "819-894-3317 x163",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_call is not None

    # Handle response
    print(res.uc_call)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.PatchUcCallRequest](../../models/operations/patchuccallrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.PatchUcCallResponse](../../models/operations/patchuccallresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_uc_call

Updates the UcCall identified by `id`. Provide the unified UcCall fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateUcCall" method="put" path="/uc/{connection_id}/call/{id}" example="uc_call" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.call.update_uc_call(request={
        "uc_call": {
            "answer_at": parse_datetime("2025-05-17T18:43:46.560Z"),
            "contacts": [],
            "conversation_identifier": "cb2ca4d9-0758-4877-9276-dffdf8d4e22e",
            "cost_amount": 1.564,
            "created_at": parse_datetime("2023-04-22T19:05:34.882Z"),
            "currency": "USD",
            "duration_seconds": 2556.0,
            "end_at": parse_datetime("2024-06-01T06:53:22.763Z"),
            "id": "cb2ca4d9-0758-4877-9276-dffdf8d4e22e",
            "is_private": False,
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.UcMetadataFormat.PRICE,
                    "id": "15450b99-002d-4c41-8926-8ead5939867b",
                    "namespace": "custom",
                    "slug": "custom_field",
                    "value": "tui",
                },
            ],
            "start_at": parse_datetime("2023-12-18T17:34:06.185Z"),
            "status": shared.UcCallStatus.IN_PROGRESS,
            "telephone": {
                "telephone": "(493) 534-0768",
                "type": shared.PropertyUcCallTelephoneType.MOBILE,
            },
            "type": shared.UcCallType.INBOUND,
            "updated_at": parse_datetime("2023-08-03T22:08:05.453Z"),
            "user_phone": "819-894-3317 x163",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_call is not None

    # Handle response
    print(res.uc_call)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpdateUcCallRequest](../../models/operations/updateuccallrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.UpdateUcCallResponse](../../models/operations/updateuccallresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |