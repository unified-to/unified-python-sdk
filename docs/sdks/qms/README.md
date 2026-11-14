# Qms

## Overview

### Available Operations

* [create_qms_action](#create_qms_action) - Create an action
* [create_qms_audit](#create_qms_audit) - Create an audit
* [create_qms_inspection](#create_qms_inspection) - Create an inspection
* [create_qms_issue](#create_qms_issue) - Create an issue
* [get_qms_action](#get_qms_action) - Retrieve an action
* [get_qms_audit](#get_qms_audit) - Retrieve an audit
* [get_qms_inspection](#get_qms_inspection) - Retrieve an inspection
* [get_qms_issue](#get_qms_issue) - Retrieve an issue
* [list_qms_actions](#list_qms_actions) - List all actions
* [list_qms_audits](#list_qms_audits) - List all audits
* [list_qms_inspections](#list_qms_inspections) - List all inspections
* [list_qms_issues](#list_qms_issues) - List all issues
* [patch_qms_action](#patch_qms_action) - Update an action
* [patch_qms_audit](#patch_qms_audit) - Update an audit
* [patch_qms_inspection](#patch_qms_inspection) - Update an inspection
* [patch_qms_issue](#patch_qms_issue) - Update an issue
* [update_qms_action](#update_qms_action) - Update an action
* [update_qms_audit](#update_qms_audit) - Update an audit
* [update_qms_inspection](#update_qms_inspection) - Update an inspection
* [update_qms_issue](#update_qms_issue) - Update an issue

## create_qms_action

Creates a QmsAction. Provide the unified QmsAction fields in the request body; they are mapped to the provider's API. Returns the created QmsAction.

### Example Usage

<!-- UsageSnippet language="python" operationID="createQmsAction" method="post" path="/qms/{connection_id}/action" example="qms_action" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.qms.create_qms_action(request={
        "qms_action": {
            "affected_items": [],
            "created_at": parse_datetime("2022-03-07T03:01:29.933Z"),
            "description": "Auditor sunt tego apparatus aegre ascisco.",
            "due_at": parse_datetime("2022-04-04T03:42:01.290Z"),
            "file_ids": [],
            "id": "3fc477f2-2e9e-4b41-baf1-07b71958e121",
            "issue_ids": [],
            "lifecycle_state": "Cancelled",
            "metadata": [],
            "name": "Add inspection step",
            "number": "CAPA-6268",
            "original_type": "Corrective Action",
            "priority": "Medium",
            "root_cause": "Worn tooling",
            "status": shared.QmsActionStatus.CANCELLED,
            "type": shared.QmsActionType.CORRECTIVE,
            "updated_at": parse_datetime("2025-02-17T01:04:17.971Z"),
            "url": "https://incomplete-conservation.org",
        },
        "connection_id": "<id>",
    })

    assert res.qms_action is not None

    # Handle response
    print(res.qms_action)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateQmsActionRequest](../../models/operations/createqmsactionrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.CreateQmsActionResponse](../../models/operations/createqmsactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.qms.create_qms_audit(request={
        "qms_audit": {
            "created_at": parse_datetime("2021-02-20T23:02:37.667Z"),
            "end_at": parse_datetime("2026-03-27T12:26:36.979Z"),
            "file_ids": [],
            "id": "ff627485-169a-492a-a33f-40da7b245b42",
            "issue_ids": [],
            "lifecycle_state": "In Review",
            "metadata": [],
            "name": "soggy certification audit",
            "number": "AUD-215",
            "scheduled_at": parse_datetime("2021-02-20T23:02:37.667Z"),
            "scope": "Calibration",
            "standard": "ISO 9001:2015",
            "start_at": parse_datetime("2023-01-25T01:49:43.876Z"),
            "status": shared.QmsAuditStatus.IN_REVIEW,
            "type": shared.QmsAuditType.CERTIFICATION,
            "updated_at": parse_datetime("2024-02-08T15:08:35.921Z"),
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

    res = unified_to.qms.create_qms_inspection(request={
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

    res = unified_to.qms.create_qms_issue(request={
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

## get_qms_action

Retrieves a single QmsAction by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getQmsAction" method="get" path="/qms/{connection_id}/action/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.qms.get_qms_action(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.qms_action is not None

    # Handle response
    print(res.qms_action)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetQmsActionRequest](../../models/operations/getqmsactionrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GetQmsActionResponse](../../models/operations/getqmsactionresponse.md)**

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

    res = unified_to.qms.get_qms_audit(request={
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

    res = unified_to.qms.get_qms_inspection(request={
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

    res = unified_to.qms.get_qms_issue(request={
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

## list_qms_actions

Returns a list of QmsActions. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listQmsActions" method="get" path="/qms/{connection_id}/action" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.qms.list_qms_actions(request={
        "connection_id": "<id>",
    })

    assert res.qms_actions is not None

    # Handle response
    print(res.qms_actions)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListQmsActionsRequest](../../models/operations/listqmsactionsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListQmsActionsResponse](../../models/operations/listqmsactionsresponse.md)**

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

    res = unified_to.qms.list_qms_audits(request={
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

    res = unified_to.qms.list_qms_inspections(request={
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

    res = unified_to.qms.list_qms_issues(request={
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

## patch_qms_action

Updates the QmsAction identified by `id`. Provide the unified QmsAction fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchQmsAction" method="patch" path="/qms/{connection_id}/action/{id}" example="qms_action" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.qms.patch_qms_action(request={
        "qms_action": {
            "affected_items": [],
            "created_at": parse_datetime("2022-03-07T03:01:29.933Z"),
            "description": "Auditor sunt tego apparatus aegre ascisco.",
            "due_at": parse_datetime("2022-04-04T03:42:01.290Z"),
            "file_ids": [],
            "id": "5836bb23-031c-4200-bd54-c19e0895874a",
            "issue_ids": [],
            "lifecycle_state": "Cancelled",
            "metadata": [],
            "name": "Add inspection step",
            "number": "CAPA-6268",
            "original_type": "Corrective Action",
            "priority": "Medium",
            "root_cause": "Worn tooling",
            "status": shared.QmsActionStatus.CANCELLED,
            "type": shared.QmsActionType.CORRECTIVE,
            "updated_at": parse_datetime("2025-02-17T01:04:17.987Z"),
            "url": "https://incomplete-conservation.org",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.qms_action is not None

    # Handle response
    print(res.qms_action)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchQmsActionRequest](../../models/operations/patchqmsactionrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.PatchQmsActionResponse](../../models/operations/patchqmsactionresponse.md)**

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

    res = unified_to.qms.patch_qms_audit(request={
        "qms_audit": {
            "created_at": parse_datetime("2021-02-20T23:02:37.667Z"),
            "end_at": parse_datetime("2026-03-27T12:26:36.998Z"),
            "file_ids": [],
            "id": "18e53ee0-00c7-4fed-a51e-c895953dba12",
            "issue_ids": [],
            "lifecycle_state": "In Review",
            "metadata": [],
            "name": "soggy certification audit",
            "number": "AUD-215",
            "scheduled_at": parse_datetime("2021-02-20T23:02:37.667Z"),
            "scope": "Calibration",
            "standard": "ISO 9001:2015",
            "start_at": parse_datetime("2023-01-25T01:49:43.883Z"),
            "status": shared.QmsAuditStatus.IN_REVIEW,
            "type": shared.QmsAuditType.CERTIFICATION,
            "updated_at": parse_datetime("2024-02-08T15:08:35.931Z"),
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

    res = unified_to.qms.patch_qms_inspection(request={
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

    res = unified_to.qms.patch_qms_issue(request={
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

## update_qms_action

Updates the QmsAction identified by `id`. Provide the unified QmsAction fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateQmsAction" method="put" path="/qms/{connection_id}/action/{id}" example="qms_action" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.qms.update_qms_action(request={
        "qms_action": {
            "affected_items": [],
            "created_at": parse_datetime("2022-03-07T03:01:29.933Z"),
            "description": "Auditor sunt tego apparatus aegre ascisco.",
            "due_at": parse_datetime("2022-04-04T03:42:01.290Z"),
            "file_ids": [],
            "id": "5836bb23-031c-4200-bd54-c19e0895874a",
            "issue_ids": [],
            "lifecycle_state": "Cancelled",
            "metadata": [],
            "name": "Add inspection step",
            "number": "CAPA-6268",
            "original_type": "Corrective Action",
            "priority": "Medium",
            "root_cause": "Worn tooling",
            "status": shared.QmsActionStatus.CANCELLED,
            "type": shared.QmsActionType.CORRECTIVE,
            "updated_at": parse_datetime("2025-02-17T01:04:17.987Z"),
            "url": "https://incomplete-conservation.org",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.qms_action is not None

    # Handle response
    print(res.qms_action)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateQmsActionRequest](../../models/operations/updateqmsactionrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.UpdateQmsActionResponse](../../models/operations/updateqmsactionresponse.md)**

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

    res = unified_to.qms.update_qms_audit(request={
        "qms_audit": {
            "created_at": parse_datetime("2021-02-20T23:02:37.667Z"),
            "end_at": parse_datetime("2026-03-27T12:26:36.998Z"),
            "file_ids": [],
            "id": "18e53ee0-00c7-4fed-a51e-c895953dba12",
            "issue_ids": [],
            "lifecycle_state": "In Review",
            "metadata": [],
            "name": "soggy certification audit",
            "number": "AUD-215",
            "scheduled_at": parse_datetime("2021-02-20T23:02:37.667Z"),
            "scope": "Calibration",
            "standard": "ISO 9001:2015",
            "start_at": parse_datetime("2023-01-25T01:49:43.883Z"),
            "status": shared.QmsAuditStatus.IN_REVIEW,
            "type": shared.QmsAuditType.CERTIFICATION,
            "updated_at": parse_datetime("2024-02-08T15:08:35.931Z"),
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

    res = unified_to.qms.update_qms_inspection(request={
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

    res = unified_to.qms.update_qms_issue(request={
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