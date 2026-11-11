# Table

## Overview

### Available Operations

* [create_datastore_table](#create_datastore_table) - Create a table
* [get_commerce_table](#get_commerce_table) - Retrieve a table
* [get_datastore_table](#get_datastore_table) - Retrieve a table
* [list_commerce_tables](#list_commerce_tables) - List all tables
* [list_datastore_tables](#list_datastore_tables) - List all tables
* [patch_datastore_table](#patch_datastore_table) - Update a table
* [remove_datastore_table](#remove_datastore_table) - Remove a table
* [update_datastore_table](#update_datastore_table) - Update a table

## create_datastore_table

Creates a DatastoreTable. Provide the unified DatastoreTable fields in the request body; they are mapped to the provider's API. Returns the created DatastoreTable.

### Example Usage

<!-- UsageSnippet language="python" operationID="createDatastoreTable" method="post" path="/datastore/{connection_id}/table" example="datastore_table" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.table.create_datastore_table(request={
        "datastore_table": {
            "created_at": parse_datetime("2022-05-22T04:49:00.762Z"),
            "description": "Quasi adhuc paulatim ducimus carpo vomito magni tantum tubineus corona.",
            "fields": [
                {
                    "description": "Antea soluta itaque clamo despecto basium accendo.",
                    "id": "a752deab-9f4a-4304-8fc7-9905d5a0e86c",
                    "is_indexed": True,
                    "is_unique": True,
                    "name": "Ferry LLC",
                    "original_type": "conservo",
                    "scale": 64.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Nulla cattus aequus sumo neque alter cauda subseco.",
                    "id": "960cecde-ae34-48ae-a052-49cb57460ad8",
                    "is_nullable": True,
                    "is_unique": True,
                    "name": "Hand - Nader",
                    "original_type": "conservo",
                    "precision": 57.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Utilis callide adhuc verumtamen doloremque ceno sui sint.",
                    "id": "dd8c9410-798e-414f-b360-783a0cefda34",
                    "is_indexed": True,
                    "is_nullable": True,
                    "is_unique": True,
                    "max_length": 62.0,
                    "name": "Toy - Kiehn",
                    "original_type": "sursum",
                    "precision": 47.0,
                    "type": shared.DatastoreFieldType.NUMBER,
                },
                {
                    "description": "Audax articulus triumphus tametsi cura tenetur colligo arcesso bestia.",
                    "id": "e125ad0a-15dd-47ff-a11f-8c411c303bc3",
                    "name": "Gislason, Gorczany and Hegmann",
                    "original_type": "tego",
                    "precision": 94.0,
                    "scale": 24.0,
                    "type": shared.DatastoreFieldType.RELATION,
                },
                {
                    "description": "Communis coma cura audio aduro acer canis expedita.",
                    "id": "277f38de-2ea7-4cb0-85c1-cbcfd06222a8",
                    "is_indexed": True,
                    "is_primary_key": True,
                    "is_required": True,
                    "name": "Graham, Steuber and Kshlerin",
                    "original_type": "defessus",
                    "scale": 68.0,
                    "type": shared.DatastoreFieldType.EMAIL,
                },
            ],
            "id": "4e59e472-ea01-4ec0-b309-0b5f08b49771",
            "metadata": [],
            "name": "Rogahn, Lowe and Heller",
            "relationships": [
                {
                    "field": "Macejkovic - Shields",
                    "name": "Hyatt, Ryan and Nienow",
                    "table_id": "4e59e472-ea01-4ec0-b309-0b5f08b49771",
                    "type": shared.DatastoreRelationshipType.MANY,
                },
            ],
            "updated_at": parse_datetime("2022-08-13T22:08:31.059Z"),
            "web_url": "https://nervous-deck.com",
        },
        "connection_id": "<id>",
    })

    assert res.datastore_table is not None

    # Handle response
    print(res.datastore_table)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateDatastoreTableRequest](../../models/operations/createdatastoretablerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateDatastoreTableResponse](../../models/operations/createdatastoretableresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_commerce_table

Retrieves a single CommerceTable by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCommerceTable" method="get" path="/commerce/{connection_id}/table/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.table.get_commerce_table(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_table is not None

    # Handle response
    print(res.commerce_table)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetCommerceTableRequest](../../models/operations/getcommercetablerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetCommerceTableResponse](../../models/operations/getcommercetableresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_datastore_table

Retrieves a single DatastoreTable by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDatastoreTable" method="get" path="/datastore/{connection_id}/table/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.table.get_datastore_table(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.datastore_table is not None

    # Handle response
    print(res.datastore_table)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetDatastoreTableRequest](../../models/operations/getdatastoretablerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetDatastoreTableResponse](../../models/operations/getdatastoretableresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_commerce_tables

Returns a list of CommerceTables. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listCommerceTables" method="get" path="/commerce/{connection_id}/table" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.table.list_commerce_tables(request={
        "connection_id": "<id>",
    })

    assert res.commerce_tables is not None

    # Handle response
    print(res.commerce_tables)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListCommerceTablesRequest](../../models/operations/listcommercetablesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListCommerceTablesResponse](../../models/operations/listcommercetablesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_datastore_tables

Returns a list of DatastoreTables. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listDatastoreTables" method="get" path="/datastore/{connection_id}/table" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.table.list_datastore_tables(request={
        "connection_id": "<id>",
    })

    assert res.datastore_tables is not None

    # Handle response
    print(res.datastore_tables)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListDatastoreTablesRequest](../../models/operations/listdatastoretablesrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListDatastoreTablesResponse](../../models/operations/listdatastoretablesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_datastore_table

Updates the DatastoreTable identified by `id`. Provide the unified DatastoreTable fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchDatastoreTable" method="patch" path="/datastore/{connection_id}/table/{id}" example="datastore_table" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.table.patch_datastore_table(request={
        "datastore_table": {
            "created_at": parse_datetime("2022-05-22T04:49:00.762Z"),
            "description": "Quasi adhuc paulatim ducimus carpo vomito magni tantum tubineus corona.",
            "fields": [
                {
                    "description": "Antea soluta itaque clamo despecto basium accendo.",
                    "id": "5aed8fa1-ae3d-4ceb-8ad7-02a9f0d41a16",
                    "is_indexed": True,
                    "is_unique": True,
                    "name": "Ferry LLC",
                    "original_type": "conservo",
                    "scale": 64.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Nulla cattus aequus sumo neque alter cauda subseco.",
                    "id": "a902386c-c469-4923-b301-9e3bc090785f",
                    "is_nullable": True,
                    "is_unique": True,
                    "name": "Hand - Nader",
                    "original_type": "conservo",
                    "precision": 57.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Utilis callide adhuc verumtamen doloremque ceno sui sint.",
                    "id": "86147934-b9e2-49e5-99b2-e931871e9351",
                    "is_indexed": True,
                    "is_nullable": True,
                    "is_unique": True,
                    "max_length": 62.0,
                    "name": "Toy - Kiehn",
                    "original_type": "sursum",
                    "precision": 47.0,
                    "type": shared.DatastoreFieldType.NUMBER,
                },
                {
                    "description": "Audax articulus triumphus tametsi cura tenetur colligo arcesso bestia.",
                    "id": "f713407c-8181-436f-8339-000235b1ed07",
                    "name": "Gislason, Gorczany and Hegmann",
                    "original_type": "tego",
                    "precision": 94.0,
                    "scale": 24.0,
                    "type": shared.DatastoreFieldType.RELATION,
                },
                {
                    "description": "Communis coma cura audio aduro acer canis expedita.",
                    "id": "53f0cd46-1b04-42c4-9619-278a7819b5b1",
                    "is_indexed": True,
                    "is_primary_key": True,
                    "is_required": True,
                    "name": "Graham, Steuber and Kshlerin",
                    "original_type": "defessus",
                    "scale": 68.0,
                    "type": shared.DatastoreFieldType.EMAIL,
                },
            ],
            "id": "c8ba605f-3b6f-409d-84fd-011067089376",
            "metadata": [],
            "name": "Rogahn, Lowe and Heller",
            "relationships": [
                {
                    "field": "Macejkovic - Shields",
                    "name": "Hyatt, Ryan and Nienow",
                    "table_id": "c8ba605f-3b6f-409d-84fd-011067089376",
                    "type": shared.DatastoreRelationshipType.MANY,
                },
            ],
            "updated_at": parse_datetime("2022-08-13T22:08:31.061Z"),
            "web_url": "https://nervous-deck.com",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.datastore_table is not None

    # Handle response
    print(res.datastore_table)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchDatastoreTableRequest](../../models/operations/patchdatastoretablerequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchDatastoreTableResponse](../../models/operations/patchdatastoretableresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_datastore_table

Deletes the DatastoreTable identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeDatastoreTable" method="delete" path="/datastore/{connection_id}/table/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.table.remove_datastore_table(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RemoveDatastoreTableRequest](../../models/operations/removedatastoretablerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.RemoveDatastoreTableResponse](../../models/operations/removedatastoretableresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_datastore_table

Updates the DatastoreTable identified by `id`. Provide the unified DatastoreTable fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateDatastoreTable" method="put" path="/datastore/{connection_id}/table/{id}" example="datastore_table" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.table.update_datastore_table(request={
        "datastore_table": {
            "created_at": parse_datetime("2022-05-22T04:49:00.762Z"),
            "description": "Quasi adhuc paulatim ducimus carpo vomito magni tantum tubineus corona.",
            "fields": [
                {
                    "description": "Antea soluta itaque clamo despecto basium accendo.",
                    "id": "5aed8fa1-ae3d-4ceb-8ad7-02a9f0d41a16",
                    "is_indexed": True,
                    "is_unique": True,
                    "name": "Ferry LLC",
                    "original_type": "conservo",
                    "scale": 64.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Nulla cattus aequus sumo neque alter cauda subseco.",
                    "id": "a902386c-c469-4923-b301-9e3bc090785f",
                    "is_nullable": True,
                    "is_unique": True,
                    "name": "Hand - Nader",
                    "original_type": "conservo",
                    "precision": 57.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Utilis callide adhuc verumtamen doloremque ceno sui sint.",
                    "id": "86147934-b9e2-49e5-99b2-e931871e9351",
                    "is_indexed": True,
                    "is_nullable": True,
                    "is_unique": True,
                    "max_length": 62.0,
                    "name": "Toy - Kiehn",
                    "original_type": "sursum",
                    "precision": 47.0,
                    "type": shared.DatastoreFieldType.NUMBER,
                },
                {
                    "description": "Audax articulus triumphus tametsi cura tenetur colligo arcesso bestia.",
                    "id": "f713407c-8181-436f-8339-000235b1ed07",
                    "name": "Gislason, Gorczany and Hegmann",
                    "original_type": "tego",
                    "precision": 94.0,
                    "scale": 24.0,
                    "type": shared.DatastoreFieldType.RELATION,
                },
                {
                    "description": "Communis coma cura audio aduro acer canis expedita.",
                    "id": "53f0cd46-1b04-42c4-9619-278a7819b5b1",
                    "is_indexed": True,
                    "is_primary_key": True,
                    "is_required": True,
                    "name": "Graham, Steuber and Kshlerin",
                    "original_type": "defessus",
                    "scale": 68.0,
                    "type": shared.DatastoreFieldType.EMAIL,
                },
            ],
            "id": "c8ba605f-3b6f-409d-84fd-011067089376",
            "metadata": [],
            "name": "Rogahn, Lowe and Heller",
            "relationships": [
                {
                    "field": "Macejkovic - Shields",
                    "name": "Hyatt, Ryan and Nienow",
                    "table_id": "c8ba605f-3b6f-409d-84fd-011067089376",
                    "type": shared.DatastoreRelationshipType.MANY,
                },
            ],
            "updated_at": parse_datetime("2022-08-13T22:08:31.061Z"),
            "web_url": "https://nervous-deck.com",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.datastore_table is not None

    # Handle response
    print(res.datastore_table)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateDatastoreTableRequest](../../models/operations/updatedatastoretablerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateDatastoreTableResponse](../../models/operations/updatedatastoretableresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |