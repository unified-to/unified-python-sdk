# Inspection

## Overview

### Available Operations

* [create_qms_inspection](#create_qms_inspection) - Create an inspection
* [get_qms_inspection](#get_qms_inspection) - Retrieve an inspection
* [list_qms_inspections](#list_qms_inspections) - List all inspections
* [patch_qms_inspection](#patch_qms_inspection) - Update an inspection
* [update_qms_inspection](#update_qms_inspection) - Update an inspection

## create_qms_inspection

Creates a QmsInspection. Provide the unified QmsInspection fields in the request body; they are mapped to the provider's API. Returns the created QmsInspection.

### Example Usage

<!-- UsageSnippet language="python" operationID="createQmsInspection" method="post" path="/qms/{connection_id}/inspection" example="qms_inspection" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.inspection.create_qms_inspection(request={
        "qms_inspection": {
            "characteristics": [
                {
                    "lower_limit": 152.9,
                    "measured_value": "152.94",
                    "name": "Hole position",
                    "nominal_value": 153.0,
                    "result": shared.Result.PASS,
                    "unit_of_measure": "mm",
                    "upper_limit": 153.1,
                },
                {
                    "lower_limit": 24.95,
                    "measured_value": "25.03",
                    "name": "Flatness",
                    "nominal_value": 25.0,
                    "result": shared.Result.PASS,
                    "unit_of_measure": "mm",
                    "upper_limit": 25.05,
                },
                {
                    "lower_limit": 53.99,
                    "measured_value": "53.99",
                    "name": "Bore diameter",
                    "nominal_value": 54.0,
                    "result": shared.Result.PASS,
                    "unit_of_measure": "mm",
                    "upper_limit": 54.01,
                },
            ],
            "created_at": parse_datetime("2020-04-18T21:23:54.000Z"),
            "file_ids": [],
            "id": "9fac1a66-162d-4961-9aa7-0d9474056788",
            "inspected_at": parse_datetime("2021-02-07T09:05:12.937Z"),
            "issue_ids": [],
            "lifecycle_state": "Complete",
            "metadata": [],
            "name": "Source inspection",
            "number": "INSP-96996",
            "part_number": "PRT-048483",
            "quantity_accepted": 41.0,
            "quantity_inspected": 41.0,
            "quantity_rejected": 0.0,
            "result": shared.QmsInspectionResult.PASS,
            "revision": "A",
            "status": shared.QmsInspectionStatus.CLOSED,
            "supplier_name": "Gerlach LLC",
            "type": shared.QmsInspectionType.SOURCE,
            "updated_at": parse_datetime("2026-05-08T16:33:40.323Z"),
            "url": "https://purple-newsprint.name/",
        },
        "connection_id": "<id>",
    })

    assert res.qms_inspection is not None

    # Handle response
    print(res.qms_inspection)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateQmsInspectionRequest](../../models/operations/createqmsinspectionrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreateQmsInspectionResponse](../../models/operations/createqmsinspectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_qms_inspection

Retrieves a single QmsInspection by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getQmsInspection" method="get" path="/qms/{connection_id}/inspection/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.inspection.get_qms_inspection(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.qms_inspection is not None

    # Handle response
    print(res.qms_inspection)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetQmsInspectionRequest](../../models/operations/getqmsinspectionrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetQmsInspectionResponse](../../models/operations/getqmsinspectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_qms_inspections

Returns a list of QmsInspections. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listQmsInspections" method="get" path="/qms/{connection_id}/inspection" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.inspection.list_qms_inspections(request={
        "connection_id": "<id>",
    })

    assert res.qms_inspections is not None

    # Handle response
    print(res.qms_inspections)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListQmsInspectionsRequest](../../models/operations/listqmsinspectionsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListQmsInspectionsResponse](../../models/operations/listqmsinspectionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_qms_inspection

Updates the QmsInspection identified by `id`. Provide the unified QmsInspection fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchQmsInspection" method="patch" path="/qms/{connection_id}/inspection/{id}" example="qms_inspection" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.inspection.patch_qms_inspection(request={
        "qms_inspection": {
            "characteristics": [
                {
                    "lower_limit": 152.9,
                    "measured_value": "152.94",
                    "name": "Hole position",
                    "nominal_value": 153.0,
                    "result": shared.Result.PASS,
                    "unit_of_measure": "mm",
                    "upper_limit": 153.1,
                },
                {
                    "lower_limit": 24.95,
                    "measured_value": "25.03",
                    "name": "Flatness",
                    "nominal_value": 25.0,
                    "result": shared.Result.PASS,
                    "unit_of_measure": "mm",
                    "upper_limit": 25.05,
                },
                {
                    "lower_limit": 53.99,
                    "measured_value": "53.99",
                    "name": "Bore diameter",
                    "nominal_value": 54.0,
                    "result": shared.Result.PASS,
                    "unit_of_measure": "mm",
                    "upper_limit": 54.01,
                },
            ],
            "created_at": parse_datetime("2020-04-18T21:23:54.000Z"),
            "file_ids": [],
            "id": "3259b6e9-0ad7-4113-9ba2-a0c335d3f1c1",
            "inspected_at": parse_datetime("2021-02-07T09:05:12.940Z"),
            "issue_ids": [],
            "lifecycle_state": "Complete",
            "metadata": [],
            "name": "Source inspection",
            "number": "INSP-96996",
            "part_number": "PRT-048483",
            "quantity_accepted": 41.0,
            "quantity_inspected": 41.0,
            "quantity_rejected": 0.0,
            "result": shared.QmsInspectionResult.PASS,
            "revision": "A",
            "status": shared.QmsInspectionStatus.CLOSED,
            "supplier_name": "Gerlach LLC",
            "type": shared.QmsInspectionType.SOURCE,
            "updated_at": parse_datetime("2026-05-08T16:33:40.347Z"),
            "url": "https://purple-newsprint.name/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.qms_inspection is not None

    # Handle response
    print(res.qms_inspection)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchQmsInspectionRequest](../../models/operations/patchqmsinspectionrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.PatchQmsInspectionResponse](../../models/operations/patchqmsinspectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_qms_inspection

Updates the QmsInspection identified by `id`. Provide the unified QmsInspection fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateQmsInspection" method="put" path="/qms/{connection_id}/inspection/{id}" example="qms_inspection" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.inspection.update_qms_inspection(request={
        "qms_inspection": {
            "characteristics": [
                {
                    "lower_limit": 152.9,
                    "measured_value": "152.94",
                    "name": "Hole position",
                    "nominal_value": 153.0,
                    "result": shared.Result.PASS,
                    "unit_of_measure": "mm",
                    "upper_limit": 153.1,
                },
                {
                    "lower_limit": 24.95,
                    "measured_value": "25.03",
                    "name": "Flatness",
                    "nominal_value": 25.0,
                    "result": shared.Result.PASS,
                    "unit_of_measure": "mm",
                    "upper_limit": 25.05,
                },
                {
                    "lower_limit": 53.99,
                    "measured_value": "53.99",
                    "name": "Bore diameter",
                    "nominal_value": 54.0,
                    "result": shared.Result.PASS,
                    "unit_of_measure": "mm",
                    "upper_limit": 54.01,
                },
            ],
            "created_at": parse_datetime("2020-04-18T21:23:54.000Z"),
            "file_ids": [],
            "id": "3259b6e9-0ad7-4113-9ba2-a0c335d3f1c1",
            "inspected_at": parse_datetime("2021-02-07T09:05:12.940Z"),
            "issue_ids": [],
            "lifecycle_state": "Complete",
            "metadata": [],
            "name": "Source inspection",
            "number": "INSP-96996",
            "part_number": "PRT-048483",
            "quantity_accepted": 41.0,
            "quantity_inspected": 41.0,
            "quantity_rejected": 0.0,
            "result": shared.QmsInspectionResult.PASS,
            "revision": "A",
            "status": shared.QmsInspectionStatus.CLOSED,
            "supplier_name": "Gerlach LLC",
            "type": shared.QmsInspectionType.SOURCE,
            "updated_at": parse_datetime("2026-05-08T16:33:40.347Z"),
            "url": "https://purple-newsprint.name/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.qms_inspection is not None

    # Handle response
    print(res.qms_inspection)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateQmsInspectionRequest](../../models/operations/updateqmsinspectionrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.UpdateQmsInspectionResponse](../../models/operations/updateqmsinspectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |