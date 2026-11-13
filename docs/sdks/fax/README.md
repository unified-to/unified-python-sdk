# Fax

## Overview

### Available Operations

* [create_uc_fax](#create_uc_fax) - Create a fax
* [get_uc_fax](#get_uc_fax) - Retrieve a fax
* [list_uc_faxes](#list_uc_faxes) - List all faxes
* [remove_uc_fax](#remove_uc_fax) - Remove a fax

## create_uc_fax

Creates a UcFax. Provide the unified UcFax fields in the request body; they are mapped to the provider's API. Returns the created UcFax.

### Example Usage

<!-- UsageSnippet language="python" operationID="createUcFax" method="post" path="/uc/{connection_id}/fax" example="uc_fax" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.fax.create_uc_fax(request={
        "uc_fax": {
            "cost_amount": 1.2207,
            "created_at": parse_datetime("2022-10-25T13:37:51.431Z"),
            "currency": "USD",
            "from_telephone": "+13605107540",
            "id": "0d91e252-d5e9-4466-b219-2bd817d15bd6",
            "media_url": "https://doting-jump.biz",
            "metadata": [],
            "pages": 20.0,
            "status": shared.UcFaxStatus.DELIVERED,
            "to_telephone": "+19083998866",
            "type": shared.UcFaxType.INBOUND,
            "updated_at": parse_datetime("2023-04-16T11:36:01.434Z"),
        },
        "connection_id": "<id>",
    })

    assert res.uc_fax is not None

    # Handle response
    print(res.uc_fax)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.CreateUcFaxRequest](../../models/operations/createucfaxrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.CreateUcFaxResponse](../../models/operations/createucfaxresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_uc_fax

Retrieves a single UcFax by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUcFax" method="get" path="/uc/{connection_id}/fax/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.fax.get_uc_fax(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_fax is not None

    # Handle response
    print(res.uc_fax)

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetUcFaxRequest](../../models/operations/getucfaxrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |

### Response

**[operations.GetUcFaxResponse](../../models/operations/getucfaxresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_uc_faxes

Returns a list of UcFaxes. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listUcFaxes" method="get" path="/uc/{connection_id}/fax" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.fax.list_uc_faxes(request={
        "connection_id": "<id>",
    })

    assert res.uc_faxes is not None

    # Handle response
    print(res.uc_faxes)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ListUcFaxesRequest](../../models/operations/listucfaxesrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.ListUcFaxesResponse](../../models/operations/listucfaxesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_uc_fax

Deletes the UcFax identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeUcFax" method="delete" path="/uc/{connection_id}/fax/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.fax.remove_uc_fax(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.RemoveUcFaxRequest](../../models/operations/removeucfaxrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.RemoveUcFaxResponse](../../models/operations/removeucfaxresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |