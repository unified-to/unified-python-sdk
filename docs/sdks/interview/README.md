# Interview

## Overview

### Available Operations

* [create_ats_interview](#create_ats_interview) - Create an interview
* [get_ats_interview](#get_ats_interview) - Retrieve an interview
* [list_ats_interviews](#list_ats_interviews) - List all interviews
* [patch_ats_interview](#patch_ats_interview) - Update an interview
* [remove_ats_interview](#remove_ats_interview) - Remove an interview
* [update_ats_interview](#update_ats_interview) - Update an interview

## create_ats_interview

Create an interview

### Example Usage

<!-- UsageSnippet language="python" operationID="createAtsInterview" method="post" path="/ats/{connection_id}/interview" example="ats_interview" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.interview.create_ats_interview(request={
        "ats_interview": {
            "created_at": parse_datetime("2021-11-28T03:14:47.774Z"),
            "end_at": parse_datetime("2025-10-11T15:19:17.918Z"),
            "external_event_xref": "9baa5590-c4dc-4c3d-b113-c85d1379590e",
            "id": "9c85c819-e23c-428a-a4dc-276a4df6d45e",
            "location": "26596 Halle Trafficway",
            "start_at": parse_datetime("2025-06-04T21:28:05.302Z"),
            "status": shared.AtsInterviewStatus.SCHEDULED,
            "updated_at": parse_datetime("2026-02-24T01:42:35.199Z"),
        },
        "connection_id": "<id>",
    })

    assert res.ats_interview is not None

    # Handle response
    print(res.ats_interview)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateAtsInterviewRequest](../../models/operations/createatsinterviewrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateAtsInterviewResponse](../../models/operations/createatsinterviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ats_interview

Retrieve an interview

### Example Usage

<!-- UsageSnippet language="python" operationID="getAtsInterview" method="get" path="/ats/{connection_id}/interview/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.interview.get_ats_interview(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_interview is not None

    # Handle response
    print(res.ats_interview)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetAtsInterviewRequest](../../models/operations/getatsinterviewrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetAtsInterviewResponse](../../models/operations/getatsinterviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ats_interviews

List all interviews

### Example Usage

<!-- UsageSnippet language="python" operationID="listAtsInterviews" method="get" path="/ats/{connection_id}/interview" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.interview.list_ats_interviews(request={
        "connection_id": "<id>",
    })

    assert res.ats_interviews is not None

    # Handle response
    print(res.ats_interviews)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListAtsInterviewsRequest](../../models/operations/listatsinterviewsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListAtsInterviewsResponse](../../models/operations/listatsinterviewsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ats_interview

Update an interview

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAtsInterview" method="patch" path="/ats/{connection_id}/interview/{id}" example="ats_interview" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.interview.patch_ats_interview(request={
        "ats_interview": {
            "created_at": parse_datetime("2021-11-28T03:14:47.774Z"),
            "end_at": parse_datetime("2025-10-11T15:19:17.927Z"),
            "external_event_xref": "71df181b-f93f-42b3-b644-ac1a7b06eb01",
            "id": "c3b5b607-9564-43ce-a832-2823e43008ee",
            "location": "26596 Halle Trafficway",
            "start_at": parse_datetime("2025-06-04T21:28:05.310Z"),
            "status": shared.AtsInterviewStatus.SCHEDULED,
            "updated_at": parse_datetime("2026-02-24T01:42:35.208Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_interview is not None

    # Handle response
    print(res.ats_interview)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchAtsInterviewRequest](../../models/operations/patchatsinterviewrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchAtsInterviewResponse](../../models/operations/patchatsinterviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ats_interview

Remove an interview

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAtsInterview" method="delete" path="/ats/{connection_id}/interview/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.interview.remove_ats_interview(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveAtsInterviewRequest](../../models/operations/removeatsinterviewrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveAtsInterviewResponse](../../models/operations/removeatsinterviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ats_interview

Update an interview

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAtsInterview" method="put" path="/ats/{connection_id}/interview/{id}" example="ats_interview" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.interview.update_ats_interview(request={
        "ats_interview": {
            "created_at": parse_datetime("2021-11-28T03:14:47.774Z"),
            "end_at": parse_datetime("2025-10-11T15:19:17.927Z"),
            "external_event_xref": "71df181b-f93f-42b3-b644-ac1a7b06eb01",
            "id": "c3b5b607-9564-43ce-a832-2823e43008ee",
            "location": "26596 Halle Trafficway",
            "start_at": parse_datetime("2025-06-04T21:28:05.310Z"),
            "status": shared.AtsInterviewStatus.SCHEDULED,
            "updated_at": parse_datetime("2026-02-24T01:42:35.208Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_interview is not None

    # Handle response
    print(res.ats_interview)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateAtsInterviewRequest](../../models/operations/updateatsinterviewrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateAtsInterviewResponse](../../models/operations/updateatsinterviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |