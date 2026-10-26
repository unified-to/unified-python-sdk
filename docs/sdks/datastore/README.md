# Datastore

## Overview

### Available Operations

* [create_datastore_database](#create_datastore_database) - Create a database
* [create_datastore_query](#create_datastore_query) - Create a query
* [create_datastore_record](#create_datastore_record) - Create a record
* [create_datastore_table](#create_datastore_table) - Create a table
* [get_datastore_database](#get_datastore_database) - Retrieve a database
* [get_datastore_record](#get_datastore_record) - Retrieve a record
* [get_datastore_table](#get_datastore_table) - Retrieve a table
* [list_datastore_databases](#list_datastore_databases) - List all databases
* [list_datastore_records](#list_datastore_records) - List all records
* [list_datastore_tables](#list_datastore_tables) - List all tables
* [patch_datastore_database](#patch_datastore_database) - Update a database
* [patch_datastore_record](#patch_datastore_record) - Update a record
* [patch_datastore_table](#patch_datastore_table) - Update a table
* [remove_datastore_database](#remove_datastore_database) - Remove a database
* [remove_datastore_record](#remove_datastore_record) - Remove a record
* [remove_datastore_table](#remove_datastore_table) - Remove a table
* [update_datastore_database](#update_datastore_database) - Update a database
* [update_datastore_record](#update_datastore_record) - Update a record
* [update_datastore_table](#update_datastore_table) - Update a table

## create_datastore_database

Creates a DatastoreDatabase. Provide the unified DatastoreDatabase fields in the request body; they are mapped to the provider's API. Returns the created DatastoreDatabase.

### Example Usage

<!-- UsageSnippet language="python" operationID="createDatastoreDatabase" method="post" path="/datastore/{connection_id}/database" example="datastore_database" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.datastore.create_datastore_database(request={
        "datastore_database": {
            "created_at": parse_datetime("2019-03-05T14:31:00.223Z"),
            "description": "Substantia tantillus coniuratio repellat coerceo amet vito vorago.",
            "id": "0268297c-40b3-41af-8a35-04938b47f53a",
            "is_active": True,
            "metadata": [],
            "name": "Rau - O'Reilly",
            "password": "iYLhYwOHm0NLDvI",
            "region": "France",
            "updated_at": parse_datetime("2023-07-03T16:13:05.445Z"),
            "web_url": "https://optimal-signature.name",
        },
        "connection_id": "<id>",
    })

    assert res.datastore_database is not None

    # Handle response
    print(res.datastore_database)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateDatastoreDatabaseRequest](../../models/operations/createdatastoredatabaserequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateDatastoreDatabaseResponse](../../models/operations/createdatastoredatabaseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_datastore_query

Creates a DatastoreQuery. Provide the unified DatastoreQuery fields in the request body; they are mapped to the provider's API. Returns the created DatastoreQuery.

### Example Usage

<!-- UsageSnippet language="python" operationID="createDatastoreQuery" method="post" path="/datastore/{connection_id}/query" example="datastore_query" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.datastore.create_datastore_query(request={
        "datastore_query": {
            "metadata": [],
            "query": {
                "filter_": {
                    "type": shared.PropertyDatastoreQueryQueryFilterType.OR,
                },
                "select": [
                    "*",
                ],
                "sql": "",
            },
        },
        "connection_id": "<id>",
    })

    assert res.datastore_query is not None

    # Handle response
    print(res.datastore_query)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateDatastoreQueryRequest](../../models/operations/createdatastorequeryrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateDatastoreQueryResponse](../../models/operations/createdatastorequeryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_datastore_record

Creates a DatastoreRecord. Provide the unified DatastoreRecord fields in the request body; they are mapped to the provider's API. Returns the created DatastoreRecord.

### Example Usage

<!-- UsageSnippet language="python" operationID="createDatastoreRecord" method="post" path="/datastore/{connection_id}/record" example="datastore_record" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.datastore.create_datastore_record(request={
        "datastore_record": {
            "created_at": parse_datetime("2022-07-10T04:42:03.076Z"),
            "fields": {

            },
            "id": "6133cf04-340d-45d1-b1b1-91dde533b35f",
            "metadata": [],
            "row_number": 33.0,
            "updated_at": parse_datetime("2025-03-08T06:00:18.214Z"),
        },
        "connection_id": "<id>",
    })

    assert res.datastore_record is not None

    # Handle response
    print(res.datastore_record)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateDatastoreRecordRequest](../../models/operations/createdatastorerecordrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateDatastoreRecordResponse](../../models/operations/createdatastorerecordresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.datastore.create_datastore_table(request={
        "datastore_table": {
            "created_at": parse_datetime("2022-05-22T04:49:00.762Z"),
            "description": "Quasi adhuc paulatim ducimus carpo vomito magni tantum tubineus corona.",
            "fields": [
                {
                    "description": "Antea soluta itaque clamo despecto basium accendo.",
                    "id": "e9db9cfe-a824-432a-9684-8172c1b019a5",
                    "is_indexed": True,
                    "is_unique": True,
                    "name": "Ferry LLC",
                    "original_type": "conservo",
                    "scale": 64.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Nulla cattus aequus sumo neque alter cauda subseco.",
                    "id": "672c8e70-b516-43bc-bf36-3cc60cd52792",
                    "is_nullable": True,
                    "is_unique": True,
                    "name": "Hand - Nader",
                    "original_type": "conservo",
                    "precision": 57.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Utilis callide adhuc verumtamen doloremque ceno sui sint.",
                    "id": "3aaa87b3-480a-4de6-9b37-1381df24b685",
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
                    "id": "0136a4c7-f7b7-4a10-bfdf-02fb95e7e182",
                    "name": "Gislason, Gorczany and Hegmann",
                    "original_type": "tego",
                    "precision": 94.0,
                    "scale": 24.0,
                    "type": shared.DatastoreFieldType.RELATION,
                },
                {
                    "description": "Communis coma cura audio aduro acer canis expedita.",
                    "id": "bf526d9b-9df4-46ad-ac1c-6236dc1444e4",
                    "is_indexed": True,
                    "is_primary_key": True,
                    "is_required": True,
                    "name": "Graham, Steuber and Kshlerin",
                    "original_type": "defessus",
                    "scale": 68.0,
                    "type": shared.DatastoreFieldType.EMAIL,
                },
            ],
            "id": "53546efa-764a-45fd-9b80-9fa3b9ea9dee",
            "metadata": [],
            "name": "Rogahn, Lowe and Heller",
            "relationships": [
                {
                    "field": "Macejkovic - Shields",
                    "name": "Hyatt, Ryan and Nienow",
                    "table_id": "53546efa-764a-45fd-9b80-9fa3b9ea9dee",
                    "type": shared.DatastoreRelationshipType.MANY,
                },
            ],
            "updated_at": parse_datetime("2022-08-13T02:37:11.026Z"),
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

## get_datastore_database

Retrieves a single DatastoreDatabase by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDatastoreDatabase" method="get" path="/datastore/{connection_id}/database/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.datastore.get_datastore_database(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.datastore_database is not None

    # Handle response
    print(res.datastore_database)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetDatastoreDatabaseRequest](../../models/operations/getdatastoredatabaserequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetDatastoreDatabaseResponse](../../models/operations/getdatastoredatabaseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_datastore_record

Retrieves a single DatastoreRecord by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDatastoreRecord" method="get" path="/datastore/{connection_id}/record/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.datastore.get_datastore_record(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.datastore_record is not None

    # Handle response
    print(res.datastore_record)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetDatastoreRecordRequest](../../models/operations/getdatastorerecordrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetDatastoreRecordResponse](../../models/operations/getdatastorerecordresponse.md)**

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

    res = unified_to.datastore.get_datastore_table(request={
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

## list_datastore_databases

Returns a list of DatastoreDatabases. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listDatastoreDatabases" method="get" path="/datastore/{connection_id}/database" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.datastore.list_datastore_databases(request={
        "connection_id": "<id>",
    })

    assert res.datastore_databases is not None

    # Handle response
    print(res.datastore_databases)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListDatastoreDatabasesRequest](../../models/operations/listdatastoredatabasesrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListDatastoreDatabasesResponse](../../models/operations/listdatastoredatabasesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_datastore_records

Returns a list of DatastoreRecords. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listDatastoreRecords" method="get" path="/datastore/{connection_id}/record" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.datastore.list_datastore_records(request={
        "connection_id": "<id>",
    })

    assert res.datastore_records is not None

    # Handle response
    print(res.datastore_records)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListDatastoreRecordsRequest](../../models/operations/listdatastorerecordsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListDatastoreRecordsResponse](../../models/operations/listdatastorerecordsresponse.md)**

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

    res = unified_to.datastore.list_datastore_tables(request={
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

## patch_datastore_database

Updates the DatastoreDatabase identified by `id`. Provide the unified DatastoreDatabase fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchDatastoreDatabase" method="patch" path="/datastore/{connection_id}/database/{id}" example="datastore_database" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.datastore.patch_datastore_database(request={
        "datastore_database": {
            "created_at": parse_datetime("2019-03-05T14:31:00.223Z"),
            "description": "Substantia tantillus coniuratio repellat coerceo amet vito vorago.",
            "id": "17cbcc05-3597-4584-98bc-42aef4660e5a",
            "is_active": True,
            "metadata": [],
            "name": "Rau - O'Reilly",
            "password": "iYLhYwOHm0NLDvI",
            "region": "France",
            "updated_at": parse_datetime("2023-07-03T16:13:05.454Z"),
            "web_url": "https://optimal-signature.name",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.datastore_database is not None

    # Handle response
    print(res.datastore_database)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchDatastoreDatabaseRequest](../../models/operations/patchdatastoredatabaserequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchDatastoreDatabaseResponse](../../models/operations/patchdatastoredatabaseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_datastore_record

Updates the DatastoreRecord identified by `id`. Provide the unified DatastoreRecord fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchDatastoreRecord" method="patch" path="/datastore/{connection_id}/record/{id}" example="datastore_record" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.datastore.patch_datastore_record(request={
        "datastore_record": {
            "created_at": parse_datetime("2022-07-10T04:42:03.076Z"),
            "fields": {

            },
            "id": "46d6bff3-7961-4a39-ac56-d3a2d8b6d0b9",
            "metadata": [],
            "row_number": 33.0,
            "updated_at": parse_datetime("2025-03-08T06:00:18.225Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.datastore_record is not None

    # Handle response
    print(res.datastore_record)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchDatastoreRecordRequest](../../models/operations/patchdatastorerecordrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchDatastoreRecordResponse](../../models/operations/patchdatastorerecordresponse.md)**

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

    res = unified_to.datastore.patch_datastore_table(request={
        "datastore_table": {
            "created_at": parse_datetime("2022-05-22T04:49:00.762Z"),
            "description": "Quasi adhuc paulatim ducimus carpo vomito magni tantum tubineus corona.",
            "fields": [
                {
                    "description": "Antea soluta itaque clamo despecto basium accendo.",
                    "id": "4a2a94ae-baae-4750-9c16-a40e49db19cc",
                    "is_indexed": True,
                    "is_unique": True,
                    "name": "Ferry LLC",
                    "original_type": "conservo",
                    "scale": 64.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Nulla cattus aequus sumo neque alter cauda subseco.",
                    "id": "d1cdcecc-abe3-4fa5-baee-92722d577faa",
                    "is_nullable": True,
                    "is_unique": True,
                    "name": "Hand - Nader",
                    "original_type": "conservo",
                    "precision": 57.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Utilis callide adhuc verumtamen doloremque ceno sui sint.",
                    "id": "d1c236d2-3391-4b0e-b080-c250f0645476",
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
                    "id": "f0816611-dc29-4850-86ed-c24a50dc60c6",
                    "name": "Gislason, Gorczany and Hegmann",
                    "original_type": "tego",
                    "precision": 94.0,
                    "scale": 24.0,
                    "type": shared.DatastoreFieldType.RELATION,
                },
                {
                    "description": "Communis coma cura audio aduro acer canis expedita.",
                    "id": "cd8a5a3e-05dd-4593-ab2b-016e6dc44f04",
                    "is_indexed": True,
                    "is_primary_key": True,
                    "is_required": True,
                    "name": "Graham, Steuber and Kshlerin",
                    "original_type": "defessus",
                    "scale": 68.0,
                    "type": shared.DatastoreFieldType.EMAIL,
                },
            ],
            "id": "0caa5578-3f35-4289-94dd-c611f43aeb93",
            "metadata": [],
            "name": "Rogahn, Lowe and Heller",
            "relationships": [
                {
                    "field": "Macejkovic - Shields",
                    "name": "Hyatt, Ryan and Nienow",
                    "table_id": "0caa5578-3f35-4289-94dd-c611f43aeb93",
                    "type": shared.DatastoreRelationshipType.MANY,
                },
            ],
            "updated_at": parse_datetime("2022-08-13T02:37:11.027Z"),
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

## remove_datastore_database

Deletes the DatastoreDatabase identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeDatastoreDatabase" method="delete" path="/datastore/{connection_id}/database/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.datastore.remove_datastore_database(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveDatastoreDatabaseRequest](../../models/operations/removedatastoredatabaserequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveDatastoreDatabaseResponse](../../models/operations/removedatastoredatabaseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_datastore_record

Deletes the DatastoreRecord identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeDatastoreRecord" method="delete" path="/datastore/{connection_id}/record/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.datastore.remove_datastore_record(request={
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
| `request`                                                                                          | [operations.RemoveDatastoreRecordRequest](../../models/operations/removedatastorerecordrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveDatastoreRecordResponse](../../models/operations/removedatastorerecordresponse.md)**

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

    res = unified_to.datastore.remove_datastore_table(request={
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

## update_datastore_database

Updates the DatastoreDatabase identified by `id`. Provide the unified DatastoreDatabase fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateDatastoreDatabase" method="put" path="/datastore/{connection_id}/database/{id}" example="datastore_database" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.datastore.update_datastore_database(request={
        "datastore_database": {
            "created_at": parse_datetime("2019-03-05T14:31:00.223Z"),
            "description": "Substantia tantillus coniuratio repellat coerceo amet vito vorago.",
            "id": "17cbcc05-3597-4584-98bc-42aef4660e5a",
            "is_active": True,
            "metadata": [],
            "name": "Rau - O'Reilly",
            "password": "iYLhYwOHm0NLDvI",
            "region": "France",
            "updated_at": parse_datetime("2023-07-03T16:13:05.454Z"),
            "web_url": "https://optimal-signature.name",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.datastore_database is not None

    # Handle response
    print(res.datastore_database)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateDatastoreDatabaseRequest](../../models/operations/updatedatastoredatabaserequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateDatastoreDatabaseResponse](../../models/operations/updatedatastoredatabaseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_datastore_record

Updates the DatastoreRecord identified by `id`. Provide the unified DatastoreRecord fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateDatastoreRecord" method="put" path="/datastore/{connection_id}/record/{id}" example="datastore_record" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.datastore.update_datastore_record(request={
        "datastore_record": {
            "created_at": parse_datetime("2022-07-10T04:42:03.076Z"),
            "fields": {

            },
            "id": "46d6bff3-7961-4a39-ac56-d3a2d8b6d0b9",
            "metadata": [],
            "row_number": 33.0,
            "updated_at": parse_datetime("2025-03-08T06:00:18.225Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.datastore_record is not None

    # Handle response
    print(res.datastore_record)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateDatastoreRecordRequest](../../models/operations/updatedatastorerecordrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateDatastoreRecordResponse](../../models/operations/updatedatastorerecordresponse.md)**

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

    res = unified_to.datastore.update_datastore_table(request={
        "datastore_table": {
            "created_at": parse_datetime("2022-05-22T04:49:00.762Z"),
            "description": "Quasi adhuc paulatim ducimus carpo vomito magni tantum tubineus corona.",
            "fields": [
                {
                    "description": "Antea soluta itaque clamo despecto basium accendo.",
                    "id": "4a2a94ae-baae-4750-9c16-a40e49db19cc",
                    "is_indexed": True,
                    "is_unique": True,
                    "name": "Ferry LLC",
                    "original_type": "conservo",
                    "scale": 64.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Nulla cattus aequus sumo neque alter cauda subseco.",
                    "id": "d1cdcecc-abe3-4fa5-baee-92722d577faa",
                    "is_nullable": True,
                    "is_unique": True,
                    "name": "Hand - Nader",
                    "original_type": "conservo",
                    "precision": 57.0,
                    "type": shared.DatastoreFieldType.SINGLE_SELECT,
                },
                {
                    "description": "Utilis callide adhuc verumtamen doloremque ceno sui sint.",
                    "id": "d1c236d2-3391-4b0e-b080-c250f0645476",
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
                    "id": "f0816611-dc29-4850-86ed-c24a50dc60c6",
                    "name": "Gislason, Gorczany and Hegmann",
                    "original_type": "tego",
                    "precision": 94.0,
                    "scale": 24.0,
                    "type": shared.DatastoreFieldType.RELATION,
                },
                {
                    "description": "Communis coma cura audio aduro acer canis expedita.",
                    "id": "cd8a5a3e-05dd-4593-ab2b-016e6dc44f04",
                    "is_indexed": True,
                    "is_primary_key": True,
                    "is_required": True,
                    "name": "Graham, Steuber and Kshlerin",
                    "original_type": "defessus",
                    "scale": 68.0,
                    "type": shared.DatastoreFieldType.EMAIL,
                },
            ],
            "id": "0caa5578-3f35-4289-94dd-c611f43aeb93",
            "metadata": [],
            "name": "Rogahn, Lowe and Heller",
            "relationships": [
                {
                    "field": "Macejkovic - Shields",
                    "name": "Hyatt, Ryan and Nienow",
                    "table_id": "0caa5578-3f35-4289-94dd-c611f43aeb93",
                    "type": shared.DatastoreRelationshipType.MANY,
                },
            ],
            "updated_at": parse_datetime("2022-08-13T02:37:11.027Z"),
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