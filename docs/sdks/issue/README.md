# Issue

## Overview

### Available Operations

* [create_qms_issue](#create_qms_issue) - Create an issue
* [get_qms_issue](#get_qms_issue) - Retrieve an issue
* [get_unified_issue](#get_unified_issue) - Retrieve support issue
* [list_qms_issues](#list_qms_issues) - List all issues
* [list_unified_issues](#list_unified_issues) - List support issues
* [patch_qms_issue](#patch_qms_issue) - Update an issue
* [update_qms_issue](#update_qms_issue) - Update an issue

## create_qms_issue

Creates a QmsIssue. Provide the unified QmsIssue fields in the request body; they are mapped to the provider's API. Returns the created QmsIssue.

### Example Usage

<!-- UsageSnippet language="python" operationID="createQmsIssue" method="post" path="/qms/{connection_id}/issue" example="qms_issue" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.issue.create_qms_issue(request={
        "qms_issue": {
            "action_ids": [],
            "affected_items": [
                {
                    "part_number": "PRT-051260",
                    "quantity": 27.0,
                    "revision": "B",
                    "serial_number": "SN-419784",
                },
            ],
            "change_ids": [],
            "created_at": parse_datetime("2020-06-10T05:10:42.904Z"),
            "description": "Adfero delectatio earum contabesco convoco uxor avaritia volaticus dens.",
            "due_at": parse_datetime("2024-07-24T01:11:22.395Z"),
            "file_ids": [],
            "id": "f904b225-1c49-4922-8faa-afbbb1e80aa7",
            "lifecycle_state": "In Progress",
            "metadata": [],
            "name": "Labeling error on tuxedo",
            "number": "CMP-5154",
            "opened_at": parse_datetime("2024-07-09T00:36:58.603Z"),
            "original_type": "Customer Complaint",
            "severity": shared.Severity.MEDIUM,
            "source": shared.QmsIssueSource.CUSTOMER,
            "status": shared.QmsIssueStatus.IN_PROGRESS,
            "type": shared.QmsIssueType.COMPLAINT,
            "updated_at": parse_datetime("2021-03-13T04:59:55.019Z"),
            "url": "https://annual-cycle.org/",
        },
        "connection_id": "<id>",
    })

    assert res.qms_issue is not None

    # Handle response
    print(res.qms_issue)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateQmsIssueRequest](../../models/operations/createqmsissuerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.CreateQmsIssueResponse](../../models/operations/createqmsissueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_qms_issue

Retrieves a single QmsIssue by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getQmsIssue" method="get" path="/qms/{connection_id}/issue/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.issue.get_qms_issue(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.qms_issue is not None

    # Handle response
    print(res.qms_issue)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetQmsIssueRequest](../../models/operations/getqmsissuerequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.GetQmsIssueResponse](../../models/operations/getqmsissueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_unified_issue

Retrieve support issue

### Example Usage

<!-- UsageSnippet language="python" operationID="getUnifiedIssue" method="get" path="/unified/issue/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.issue.get_unified_issue(request={
        "id": "<id>",
    })

    assert res.issue is not None

    # Handle response
    print(res.issue)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetUnifiedIssueRequest](../../models/operations/getunifiedissuerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetUnifiedIssueResponse](../../models/operations/getunifiedissueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_qms_issues

Returns a list of QmsIssues. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listQmsIssues" method="get" path="/qms/{connection_id}/issue" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.issue.list_qms_issues(request={
        "connection_id": "<id>",
    })

    assert res.qms_issues is not None

    # Handle response
    print(res.qms_issues)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListQmsIssuesRequest](../../models/operations/listqmsissuesrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.ListQmsIssuesResponse](../../models/operations/listqmsissuesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_unified_issues

List support issues

### Example Usage

<!-- UsageSnippet language="python" operationID="listUnifiedIssues" method="get" path="/unified/issue" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.issue.list_unified_issues(request={})

    assert res.issues is not None

    # Handle response
    print(res.issues)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListUnifiedIssuesRequest](../../models/operations/listunifiedissuesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListUnifiedIssuesResponse](../../models/operations/listunifiedissuesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_qms_issue

Updates the QmsIssue identified by `id`. Provide the unified QmsIssue fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchQmsIssue" method="patch" path="/qms/{connection_id}/issue/{id}" example="qms_issue" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.issue.patch_qms_issue(request={
        "qms_issue": {
            "action_ids": [],
            "affected_items": [
                {
                    "part_number": "PRT-051260",
                    "quantity": 27.0,
                    "revision": "B",
                    "serial_number": "SN-419784",
                },
            ],
            "change_ids": [],
            "created_at": parse_datetime("2020-06-10T05:10:42.904Z"),
            "description": "Adfero delectatio earum contabesco convoco uxor avaritia volaticus dens.",
            "due_at": parse_datetime("2024-07-24T01:11:22.412Z"),
            "file_ids": [],
            "id": "ae757622-84a2-49f9-bc77-9e4ef2ca3c48",
            "lifecycle_state": "In Progress",
            "metadata": [],
            "name": "Labeling error on tuxedo",
            "number": "CMP-5154",
            "opened_at": parse_datetime("2024-07-09T00:36:58.620Z"),
            "original_type": "Customer Complaint",
            "severity": shared.Severity.MEDIUM,
            "source": shared.QmsIssueSource.CUSTOMER,
            "status": shared.QmsIssueStatus.IN_PROGRESS,
            "type": shared.QmsIssueType.COMPLAINT,
            "updated_at": parse_datetime("2021-03-13T04:59:55.022Z"),
            "url": "https://annual-cycle.org/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.qms_issue is not None

    # Handle response
    print(res.qms_issue)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.PatchQmsIssueRequest](../../models/operations/patchqmsissuerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.PatchQmsIssueResponse](../../models/operations/patchqmsissueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_qms_issue

Updates the QmsIssue identified by `id`. Provide the unified QmsIssue fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateQmsIssue" method="put" path="/qms/{connection_id}/issue/{id}" example="qms_issue" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.issue.update_qms_issue(request={
        "qms_issue": {
            "action_ids": [],
            "affected_items": [
                {
                    "part_number": "PRT-051260",
                    "quantity": 27.0,
                    "revision": "B",
                    "serial_number": "SN-419784",
                },
            ],
            "change_ids": [],
            "created_at": parse_datetime("2020-06-10T05:10:42.904Z"),
            "description": "Adfero delectatio earum contabesco convoco uxor avaritia volaticus dens.",
            "due_at": parse_datetime("2024-07-24T01:11:22.412Z"),
            "file_ids": [],
            "id": "ae757622-84a2-49f9-bc77-9e4ef2ca3c48",
            "lifecycle_state": "In Progress",
            "metadata": [],
            "name": "Labeling error on tuxedo",
            "number": "CMP-5154",
            "opened_at": parse_datetime("2024-07-09T00:36:58.620Z"),
            "original_type": "Customer Complaint",
            "severity": shared.Severity.MEDIUM,
            "source": shared.QmsIssueSource.CUSTOMER,
            "status": shared.QmsIssueStatus.IN_PROGRESS,
            "type": shared.QmsIssueType.COMPLAINT,
            "updated_at": parse_datetime("2021-03-13T04:59:55.022Z"),
            "url": "https://annual-cycle.org/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.qms_issue is not None

    # Handle response
    print(res.qms_issue)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateQmsIssueRequest](../../models/operations/updateqmsissuerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.UpdateQmsIssueResponse](../../models/operations/updateqmsissueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |