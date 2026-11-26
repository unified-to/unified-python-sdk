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
                    "id": "5f356920-8d57-4cf3-9c32-3042c999c1b8",
                    "is_indexed": True,
                    "is_unique": True,
                    "name": "Cassin - Greenfelder",
                    "original_type": "tenus",
                    "scale": 64.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Alo admiratio vallum decet tamquam utilis callide adhuc verumtamen.",
                    "id": "c1d380ef-add8-44f1-bf93-1b0b12364eb2",
                    "is_nullable": True,
                    "is_unique": True,
                    "name": "Gerhold, Hermiston and Schmidt",
                    "original_type": "doloremque",
                    "precision": 57.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Celer charisma coniuratio usus audax articulus triumphus tametsi cura.",
                    "id": "ac2c0251-9b38-4dc8-b372-acaed346b938",
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
                    "id": "20335e1f-53f3-47f5-a1c7-2ad36f3347de",
                    "name": "Koch - Krajcik",
                    "original_type": "umbra",
                    "precision": 94.0,
                    "scale": 24.0,
                    "type": shared.DatastoreFieldType.RELATION,
                },
                {
                    "description": "Demitto ullam solium bellicus urbs concedo.",
                    "id": "48c44851-3561-4c1a-98ca-4cb13d871e3c",
                    "is_indexed": True,
                    "is_primary_key": True,
                    "is_required": True,
                    "name": "Kling - Bosco",
                    "original_type": "venustas",
                    "scale": 68.0,
                    "type": shared.DatastoreFieldType.EMAIL,
                },
            ],
            "id": "e9ee7aa4-1a15-432c-91d0-18e315fecc87",
            "metadata": [],
            "name": "Bauch LLC",
            "relationships": [
                {
                    "field": "Nikolaus - Kub",
                    "name": "Brakus and Sons",
                    "table_id": "e9ee7aa4-1a15-432c-91d0-18e315fecc87",
                    "type": shared.DatastoreRelationshipType.MANY,
                },
            ],
            "updated_at": parse_datetime("2022-08-14T16:38:36.038Z"),
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
                    "id": "0c22e0df-531a-49f4-8744-3aa146c9fd85",
                    "is_indexed": True,
                    "is_unique": True,
                    "name": "Cassin - Greenfelder",
                    "original_type": "tenus",
                    "scale": 64.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Alo admiratio vallum decet tamquam utilis callide adhuc verumtamen.",
                    "id": "fb66dcd7-319f-4c14-a3ff-71e874b28cf3",
                    "is_nullable": True,
                    "is_unique": True,
                    "name": "Gerhold, Hermiston and Schmidt",
                    "original_type": "doloremque",
                    "precision": 57.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Celer charisma coniuratio usus audax articulus triumphus tametsi cura.",
                    "id": "2260a2fa-9e84-4909-97bd-8d2212731364",
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
                    "id": "c3be7703-5845-4731-879a-0ada3cb8e3ea",
                    "name": "Koch - Krajcik",
                    "original_type": "umbra",
                    "precision": 94.0,
                    "scale": 24.0,
                    "type": shared.DatastoreFieldType.RELATION,
                },
                {
                    "description": "Demitto ullam solium bellicus urbs concedo.",
                    "id": "c6fa7111-ddd0-41bd-b114-c5adb39f62c2",
                    "is_indexed": True,
                    "is_primary_key": True,
                    "is_required": True,
                    "name": "Kling - Bosco",
                    "original_type": "venustas",
                    "scale": 68.0,
                    "type": shared.DatastoreFieldType.EMAIL,
                },
            ],
            "id": "bd6693ee-a7d0-4ca1-89d5-8055745e13e3",
            "metadata": [],
            "name": "Bauch LLC",
            "relationships": [
                {
                    "field": "Nikolaus - Kub",
                    "name": "Brakus and Sons",
                    "table_id": "bd6693ee-a7d0-4ca1-89d5-8055745e13e3",
                    "type": shared.DatastoreRelationshipType.MANY,
                },
            ],
            "updated_at": parse_datetime("2022-08-14T16:38:36.040Z"),
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
                    "id": "0c22e0df-531a-49f4-8744-3aa146c9fd85",
                    "is_indexed": True,
                    "is_unique": True,
                    "name": "Cassin - Greenfelder",
                    "original_type": "tenus",
                    "scale": 64.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Alo admiratio vallum decet tamquam utilis callide adhuc verumtamen.",
                    "id": "fb66dcd7-319f-4c14-a3ff-71e874b28cf3",
                    "is_nullable": True,
                    "is_unique": True,
                    "name": "Gerhold, Hermiston and Schmidt",
                    "original_type": "doloremque",
                    "precision": 57.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Celer charisma coniuratio usus audax articulus triumphus tametsi cura.",
                    "id": "2260a2fa-9e84-4909-97bd-8d2212731364",
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
                    "id": "c3be7703-5845-4731-879a-0ada3cb8e3ea",
                    "name": "Koch - Krajcik",
                    "original_type": "umbra",
                    "precision": 94.0,
                    "scale": 24.0,
                    "type": shared.DatastoreFieldType.RELATION,
                },
                {
                    "description": "Demitto ullam solium bellicus urbs concedo.",
                    "id": "c6fa7111-ddd0-41bd-b114-c5adb39f62c2",
                    "is_indexed": True,
                    "is_primary_key": True,
                    "is_required": True,
                    "name": "Kling - Bosco",
                    "original_type": "venustas",
                    "scale": 68.0,
                    "type": shared.DatastoreFieldType.EMAIL,
                },
            ],
            "id": "bd6693ee-a7d0-4ca1-89d5-8055745e13e3",
            "metadata": [],
            "name": "Bauch LLC",
            "relationships": [
                {
                    "field": "Nikolaus - Kub",
                    "name": "Brakus and Sons",
                    "table_id": "bd6693ee-a7d0-4ca1-89d5-8055745e13e3",
                    "type": shared.DatastoreRelationshipType.MANY,
                },
            ],
            "updated_at": parse_datetime("2022-08-14T16:38:36.040Z"),
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