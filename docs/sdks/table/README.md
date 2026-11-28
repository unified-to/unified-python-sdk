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
            "description": "Carpo vomito magni tantum tubineus corona deputo.",
            "fields": [
                {
                    "description": "Basium accendo conservo curto thesis amet supellex.",
                    "id": "ad5b1b77-4869-4426-b47c-c2036f6cfd7f",
                    "is_indexed": True,
                    "is_unique": True,
                    "name": "Cassin - Greenfelder",
                    "original_type": "tenus",
                    "scale": 64.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Alo admiratio vallum decet tamquam utilis callide adhuc verumtamen.",
                    "id": "72b9effe-8a9b-4fd3-a566-b073ed52b5ea",
                    "is_nullable": True,
                    "is_unique": True,
                    "name": "Gerhold, Hermiston and Schmidt",
                    "original_type": "doloremque",
                    "precision": 57.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Celer charisma coniuratio usus audax articulus triumphus tametsi cura.",
                    "id": "8c16edec-ef61-4c47-8c1d-790242b06d2c",
                    "is_indexed": True,
                    "is_nullable": True,
                    "is_unique": True,
                    "max_length": 62.0,
                    "name": "McDermott LLC",
                    "original_type": "tenetur",
                    "precision": 47.0,
                    "type": shared.DatastoreFieldType.NUMBER,
                },
                {
                    "description": "Adficio voluptatibus ciminatio.",
                    "id": "77a83984-0cf7-44c5-909b-dffeb1a225fa",
                    "name": "Koch - Krajcik",
                    "original_type": "umbra",
                    "precision": 94.0,
                    "scale": 24.0,
                    "type": shared.DatastoreFieldType.RELATION,
                },
                {
                    "description": "Demitto ullam solium bellicus urbs concedo.",
                    "id": "9049996d-37f4-4942-8fdf-a65ca422ca1d",
                    "is_indexed": True,
                    "is_primary_key": True,
                    "is_required": True,
                    "name": "Kling - Bosco",
                    "original_type": "venustas",
                    "scale": 68.0,
                    "type": shared.DatastoreFieldType.EMAIL,
                },
            ],
            "id": "98f55f18-6e9b-4110-ba9a-3e4434727f43",
            "metadata": [],
            "name": "Bauch LLC",
            "relationships": [
                {
                    "field": "Nikolaus - Kub",
                    "name": "Brakus and Sons",
                    "table_id": "98f55f18-6e9b-4110-ba9a-3e4434727f43",
                    "type": shared.DatastoreRelationshipType.MANY,
                },
            ],
            "updated_at": parse_datetime("2022-08-14T19:11:08.242Z"),
            "web_url": "https://torn-bench.biz/",
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
            "description": "Carpo vomito magni tantum tubineus corona deputo.",
            "fields": [
                {
                    "description": "Basium accendo conservo curto thesis amet supellex.",
                    "id": "65b581b3-1680-4c80-adbb-d76df35adacd",
                    "is_indexed": True,
                    "is_unique": True,
                    "name": "Cassin - Greenfelder",
                    "original_type": "tenus",
                    "scale": 64.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Alo admiratio vallum decet tamquam utilis callide adhuc verumtamen.",
                    "id": "46cb3813-e1b3-4d64-a9cb-7b284ea27031",
                    "is_nullable": True,
                    "is_unique": True,
                    "name": "Gerhold, Hermiston and Schmidt",
                    "original_type": "doloremque",
                    "precision": 57.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Celer charisma coniuratio usus audax articulus triumphus tametsi cura.",
                    "id": "2ad0cd00-07e8-4fff-af6e-4858a318bc25",
                    "is_indexed": True,
                    "is_nullable": True,
                    "is_unique": True,
                    "max_length": 62.0,
                    "name": "McDermott LLC",
                    "original_type": "tenetur",
                    "precision": 47.0,
                    "type": shared.DatastoreFieldType.NUMBER,
                },
                {
                    "description": "Adficio voluptatibus ciminatio.",
                    "id": "f3950a5c-962e-4e0e-97c9-685227e779f1",
                    "name": "Koch - Krajcik",
                    "original_type": "umbra",
                    "precision": 94.0,
                    "scale": 24.0,
                    "type": shared.DatastoreFieldType.RELATION,
                },
                {
                    "description": "Demitto ullam solium bellicus urbs concedo.",
                    "id": "cfc3d5d0-4c16-4ca1-b129-011d663a9e03",
                    "is_indexed": True,
                    "is_primary_key": True,
                    "is_required": True,
                    "name": "Kling - Bosco",
                    "original_type": "venustas",
                    "scale": 68.0,
                    "type": shared.DatastoreFieldType.EMAIL,
                },
            ],
            "id": "3b2e41f8-7fe5-4c04-bd78-c78c24bc3455",
            "metadata": [],
            "name": "Bauch LLC",
            "relationships": [
                {
                    "field": "Nikolaus - Kub",
                    "name": "Brakus and Sons",
                    "table_id": "3b2e41f8-7fe5-4c04-bd78-c78c24bc3455",
                    "type": shared.DatastoreRelationshipType.MANY,
                },
            ],
            "updated_at": parse_datetime("2022-08-14T19:11:08.243Z"),
            "web_url": "https://torn-bench.biz/",
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
            "description": "Carpo vomito magni tantum tubineus corona deputo.",
            "fields": [
                {
                    "description": "Basium accendo conservo curto thesis amet supellex.",
                    "id": "65b581b3-1680-4c80-adbb-d76df35adacd",
                    "is_indexed": True,
                    "is_unique": True,
                    "name": "Cassin - Greenfelder",
                    "original_type": "tenus",
                    "scale": 64.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Alo admiratio vallum decet tamquam utilis callide adhuc verumtamen.",
                    "id": "46cb3813-e1b3-4d64-a9cb-7b284ea27031",
                    "is_nullable": True,
                    "is_unique": True,
                    "name": "Gerhold, Hermiston and Schmidt",
                    "original_type": "doloremque",
                    "precision": 57.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Celer charisma coniuratio usus audax articulus triumphus tametsi cura.",
                    "id": "2ad0cd00-07e8-4fff-af6e-4858a318bc25",
                    "is_indexed": True,
                    "is_nullable": True,
                    "is_unique": True,
                    "max_length": 62.0,
                    "name": "McDermott LLC",
                    "original_type": "tenetur",
                    "precision": 47.0,
                    "type": shared.DatastoreFieldType.NUMBER,
                },
                {
                    "description": "Adficio voluptatibus ciminatio.",
                    "id": "f3950a5c-962e-4e0e-97c9-685227e779f1",
                    "name": "Koch - Krajcik",
                    "original_type": "umbra",
                    "precision": 94.0,
                    "scale": 24.0,
                    "type": shared.DatastoreFieldType.RELATION,
                },
                {
                    "description": "Demitto ullam solium bellicus urbs concedo.",
                    "id": "cfc3d5d0-4c16-4ca1-b129-011d663a9e03",
                    "is_indexed": True,
                    "is_primary_key": True,
                    "is_required": True,
                    "name": "Kling - Bosco",
                    "original_type": "venustas",
                    "scale": 68.0,
                    "type": shared.DatastoreFieldType.EMAIL,
                },
            ],
            "id": "3b2e41f8-7fe5-4c04-bd78-c78c24bc3455",
            "metadata": [],
            "name": "Bauch LLC",
            "relationships": [
                {
                    "field": "Nikolaus - Kub",
                    "name": "Brakus and Sons",
                    "table_id": "3b2e41f8-7fe5-4c04-bd78-c78c24bc3455",
                    "type": shared.DatastoreRelationshipType.MANY,
                },
            ],
            "updated_at": parse_datetime("2022-08-14T19:11:08.243Z"),
            "web_url": "https://torn-bench.biz/",
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