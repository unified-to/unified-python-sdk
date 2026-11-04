# Table

## Overview

### Available Operations

* [create_datastore_table](#create_datastore_table) - Create a table
* [get_datastore_table](#get_datastore_table) - Retrieve a table
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
                    "id": "6e9927f9-f84a-4240-bc45-7c45d8496ead",
                    "is_indexed": True,
                    "is_unique": True,
                    "name": "Ferry LLC",
                    "original_type": "conservo",
                    "scale": 64.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Nulla cattus aequus sumo neque alter cauda subseco.",
                    "id": "9a474856-7316-41fa-ba60-f00a00898a01",
                    "is_nullable": True,
                    "is_unique": True,
                    "name": "Hand - Nader",
                    "original_type": "conservo",
                    "precision": 57.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Utilis callide adhuc verumtamen doloremque ceno sui sint.",
                    "id": "8d21d3ee-ca3e-4f71-92c1-a1bc9664e6b5",
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
                    "id": "bb478f4d-1492-4f1e-846c-c1bdae361e45",
                    "name": "Gislason, Gorczany and Hegmann",
                    "original_type": "tego",
                    "precision": 94.0,
                    "scale": 24.0,
                    "type": shared.DatastoreFieldType.RELATION,
                },
                {
                    "description": "Communis coma cura audio aduro acer canis expedita.",
                    "id": "056a8179-d850-4a26-90e9-f805f4f80830",
                    "is_indexed": True,
                    "is_primary_key": True,
                    "is_required": True,
                    "name": "Graham, Steuber and Kshlerin",
                    "original_type": "defessus",
                    "scale": 68.0,
                    "type": shared.DatastoreFieldType.EMAIL,
                },
            ],
            "id": "90d42297-bac3-44e7-b03e-1f7495429efd",
            "metadata": [],
            "name": "Rogahn, Lowe and Heller",
            "relationships": [
                {
                    "field": "Macejkovic - Shields",
                    "name": "Hyatt, Ryan and Nienow",
                    "table_id": "90d42297-bac3-44e7-b03e-1f7495429efd",
                    "type": shared.DatastoreRelationshipType.MANY,
                },
            ],
            "updated_at": parse_datetime("2022-08-13T13:40:01.044Z"),
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
                    "id": "ba6c8c89-4529-41ac-8cf9-59ba1bd02ddf",
                    "is_indexed": True,
                    "is_unique": True,
                    "name": "Ferry LLC",
                    "original_type": "conservo",
                    "scale": 64.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Nulla cattus aequus sumo neque alter cauda subseco.",
                    "id": "764e4a33-6eb0-4b79-8081-7433ce66c8ff",
                    "is_nullable": True,
                    "is_unique": True,
                    "name": "Hand - Nader",
                    "original_type": "conservo",
                    "precision": 57.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Utilis callide adhuc verumtamen doloremque ceno sui sint.",
                    "id": "68303bb0-41fe-40d3-ab30-034368fa30c8",
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
                    "id": "02b7c271-be7c-4601-9554-6a2fb7ce0c9e",
                    "name": "Gislason, Gorczany and Hegmann",
                    "original_type": "tego",
                    "precision": 94.0,
                    "scale": 24.0,
                    "type": shared.DatastoreFieldType.RELATION,
                },
                {
                    "description": "Communis coma cura audio aduro acer canis expedita.",
                    "id": "df31daed-2447-4cce-8aa2-aa5b907c5e97",
                    "is_indexed": True,
                    "is_primary_key": True,
                    "is_required": True,
                    "name": "Graham, Steuber and Kshlerin",
                    "original_type": "defessus",
                    "scale": 68.0,
                    "type": shared.DatastoreFieldType.EMAIL,
                },
            ],
            "id": "12f6ba39-6330-44d1-a705-ce0748b2417b",
            "metadata": [],
            "name": "Rogahn, Lowe and Heller",
            "relationships": [
                {
                    "field": "Macejkovic - Shields",
                    "name": "Hyatt, Ryan and Nienow",
                    "table_id": "12f6ba39-6330-44d1-a705-ce0748b2417b",
                    "type": shared.DatastoreRelationshipType.MANY,
                },
            ],
            "updated_at": parse_datetime("2022-08-13T13:40:01.045Z"),
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
                    "id": "ba6c8c89-4529-41ac-8cf9-59ba1bd02ddf",
                    "is_indexed": True,
                    "is_unique": True,
                    "name": "Ferry LLC",
                    "original_type": "conservo",
                    "scale": 64.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Nulla cattus aequus sumo neque alter cauda subseco.",
                    "id": "764e4a33-6eb0-4b79-8081-7433ce66c8ff",
                    "is_nullable": True,
                    "is_unique": True,
                    "name": "Hand - Nader",
                    "original_type": "conservo",
                    "precision": 57.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Utilis callide adhuc verumtamen doloremque ceno sui sint.",
                    "id": "68303bb0-41fe-40d3-ab30-034368fa30c8",
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
                    "id": "02b7c271-be7c-4601-9554-6a2fb7ce0c9e",
                    "name": "Gislason, Gorczany and Hegmann",
                    "original_type": "tego",
                    "precision": 94.0,
                    "scale": 24.0,
                    "type": shared.DatastoreFieldType.RELATION,
                },
                {
                    "description": "Communis coma cura audio aduro acer canis expedita.",
                    "id": "df31daed-2447-4cce-8aa2-aa5b907c5e97",
                    "is_indexed": True,
                    "is_primary_key": True,
                    "is_required": True,
                    "name": "Graham, Steuber and Kshlerin",
                    "original_type": "defessus",
                    "scale": 68.0,
                    "type": shared.DatastoreFieldType.EMAIL,
                },
            ],
            "id": "12f6ba39-6330-44d1-a705-ce0748b2417b",
            "metadata": [],
            "name": "Rogahn, Lowe and Heller",
            "relationships": [
                {
                    "field": "Macejkovic - Shields",
                    "name": "Hyatt, Ryan and Nienow",
                    "table_id": "12f6ba39-6330-44d1-a705-ce0748b2417b",
                    "type": shared.DatastoreRelationshipType.MANY,
                },
            ],
            "updated_at": parse_datetime("2022-08-13T13:40:01.045Z"),
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