# Audit

## Overview

### Available Operations

* [create_qms_audit](#create_qms_audit) - Create an audit
* [get_qms_audit](#get_qms_audit) - Retrieve an audit
* [list_qms_audits](#list_qms_audits) - List all audits
* [patch_qms_audit](#patch_qms_audit) - Update an audit
* [update_qms_audit](#update_qms_audit) - Update an audit

## create_qms_audit

Creates a QmsAudit. Provide the unified QmsAudit fields in the request body; they are mapped to the provider's API. Returns the created QmsAudit.

### Example Usage

<!-- UsageSnippet language="python" operationID="createQmsAudit" method="post" path="/qms/{connection_id}/audit" example="qms_audit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.audit.create_qms_audit(request={
        "qms_audit": {
            "created_at": parse_datetime("2021-02-20T23:02:37.667Z"),
            "end_at": parse_datetime("2026-04-07T02:48:57.156Z"),
            "file_ids": [],
            "id": "2524399e-7652-40b3-af0f-bd7462c373a6",
            "issue_ids": [],
            "lifecycle_state": "In Review",
            "metadata": [],
            "name": "afraid certification audit",
            "number": "AUD-215",
            "scheduled_at": parse_datetime("2021-02-20T23:02:37.667Z"),
            "scope": "Calibration",
            "standard": "ISO 9001:2015",
            "start_at": parse_datetime("2023-01-29T01:57:27.529Z"),
            "status": shared.QmsAuditStatus.IN_REVIEW,
            "type": shared.QmsAuditType.CERTIFICATION,
            "updated_at": parse_datetime("2024-02-14T19:09:50.998Z"),
            "url": "https://mushy-obesity.name/",
        },
        "connection_id": "<id>",
    })

    assert res.qms_audit is not None

    # Handle response
    print(res.qms_audit)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateQmsAuditRequest](../../models/operations/createqmsauditrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.CreateQmsAuditResponse](../../models/operations/createqmsauditresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_qms_audit

Retrieves a single QmsAudit by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getQmsAudit" method="get" path="/qms/{connection_id}/audit/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.audit.get_qms_audit(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.qms_audit is not None

    # Handle response
    print(res.qms_audit)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetQmsAuditRequest](../../models/operations/getqmsauditrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.GetQmsAuditResponse](../../models/operations/getqmsauditresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_qms_audits

Returns a list of QmsAudits. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listQmsAudits" method="get" path="/qms/{connection_id}/audit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.audit.list_qms_audits(request={
        "connection_id": "<id>",
    })

    assert res.qms_audits is not None

    # Handle response
    print(res.qms_audits)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListQmsAuditsRequest](../../models/operations/listqmsauditsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.ListQmsAuditsResponse](../../models/operations/listqmsauditsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_qms_audit

Updates the QmsAudit identified by `id`. Provide the unified QmsAudit fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchQmsAudit" method="patch" path="/qms/{connection_id}/audit/{id}" example="qms_audit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.audit.patch_qms_audit(request={
        "qms_audit": {
            "created_at": parse_datetime("2021-02-20T23:02:37.667Z"),
            "end_at": parse_datetime("2026-04-07T02:48:57.169Z"),
            "file_ids": [],
            "id": "1a8797b8-d598-4f0c-b804-1f3523491f3b",
            "issue_ids": [],
            "lifecycle_state": "In Review",
            "metadata": [],
            "name": "afraid certification audit",
            "number": "AUD-215",
            "scheduled_at": parse_datetime("2021-02-20T23:02:37.667Z"),
            "scope": "Calibration",
            "standard": "ISO 9001:2015",
            "start_at": parse_datetime("2023-01-29T01:57:27.534Z"),
            "status": shared.QmsAuditStatus.IN_REVIEW,
            "type": shared.QmsAuditType.CERTIFICATION,
            "updated_at": parse_datetime("2024-02-14T19:09:51.006Z"),
            "url": "https://mushy-obesity.name/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.qms_audit is not None

    # Handle response
    print(res.qms_audit)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.PatchQmsAuditRequest](../../models/operations/patchqmsauditrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.PatchQmsAuditResponse](../../models/operations/patchqmsauditresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_qms_audit

Updates the QmsAudit identified by `id`. Provide the unified QmsAudit fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateQmsAudit" method="put" path="/qms/{connection_id}/audit/{id}" example="qms_audit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.audit.update_qms_audit(request={
        "qms_audit": {
            "created_at": parse_datetime("2021-02-20T23:02:37.667Z"),
            "end_at": parse_datetime("2026-04-07T02:48:57.169Z"),
            "file_ids": [],
            "id": "1a8797b8-d598-4f0c-b804-1f3523491f3b",
            "issue_ids": [],
            "lifecycle_state": "In Review",
            "metadata": [],
            "name": "afraid certification audit",
            "number": "AUD-215",
            "scheduled_at": parse_datetime("2021-02-20T23:02:37.667Z"),
            "scope": "Calibration",
            "standard": "ISO 9001:2015",
            "start_at": parse_datetime("2023-01-29T01:57:27.534Z"),
            "status": shared.QmsAuditStatus.IN_REVIEW,
            "type": shared.QmsAuditType.CERTIFICATION,
            "updated_at": parse_datetime("2024-02-14T19:09:51.006Z"),
            "url": "https://mushy-obesity.name/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.qms_audit is not None

    # Handle response
    print(res.qms_audit)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateQmsAuditRequest](../../models/operations/updateqmsauditrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.UpdateQmsAuditResponse](../../models/operations/updateqmsauditresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |