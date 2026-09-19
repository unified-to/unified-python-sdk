# Application

## Overview

### Available Operations

* [create_ats_application](#create_ats_application) - Create an application
* [get_ats_application](#get_ats_application) - Retrieve an application
* [list_ats_applications](#list_ats_applications) - List all applications
* [patch_ats_application](#patch_ats_application) - Update an application
* [remove_ats_application](#remove_ats_application) - Remove an application
* [update_ats_application](#update_ats_application) - Update an application

## create_ats_application

Create an application

### Example Usage

<!-- UsageSnippet language="python" operationID="createAtsApplication" method="post" path="/ats/{connection_id}/application" example="ats_application" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.application.create_ats_application(request={
        "ats_application": {
            "answers": [],
            "applied_at": parse_datetime("2025-09-08T23:18:28.182Z"),
            "created_at": parse_datetime("2023-10-17T07:19:48.787Z"),
            "hired_at": parse_datetime("2026-04-15T09:38:27.860Z"),
            "id": "f82d92ea-18b4-40a5-8544-7ed8efb9e96b",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "a1302a79-0341-40e6-b91a-daeb95584617",
                    "namespace": "application",
                    "slug": "despecto",
                    "value": "Argentum decretum cultellus aveho distinctio verecundia stella depono.",
                },
            ],
            "offers": [],
            "original_status": "vomica",
            "original_substatus": "allatus",
            "rejected_at": parse_datetime("2026-09-09T18:00:57.612Z"),
            "rejected_reason": "Cometes amplitudo videlicet talio.",
            "source": "credo",
            "status": shared.AtsApplicationStatus.REVIEWING,
            "summary": "Comburo quidem vesica vulnus curatio. Appositus amita attonbitus conatus degenero charisma sordeo villa victoria varius. Cenaculum acsi officia.",
            "updated_at": parse_datetime("2026-09-16T09:27:50.464Z"),
        },
        "connection_id": "<id>",
    })

    assert res.ats_application is not None

    # Handle response
    print(res.ats_application)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateAtsApplicationRequest](../../models/operations/createatsapplicationrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateAtsApplicationResponse](../../models/operations/createatsapplicationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ats_application

Retrieve an application

### Example Usage

<!-- UsageSnippet language="python" operationID="getAtsApplication" method="get" path="/ats/{connection_id}/application/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.application.get_ats_application(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_application is not None

    # Handle response
    print(res.ats_application)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetAtsApplicationRequest](../../models/operations/getatsapplicationrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetAtsApplicationResponse](../../models/operations/getatsapplicationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ats_applications

List all applications

### Example Usage

<!-- UsageSnippet language="python" operationID="listAtsApplications" method="get" path="/ats/{connection_id}/application" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.application.list_ats_applications(request={
        "connection_id": "<id>",
    })

    assert res.ats_applications is not None

    # Handle response
    print(res.ats_applications)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListAtsApplicationsRequest](../../models/operations/listatsapplicationsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListAtsApplicationsResponse](../../models/operations/listatsapplicationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ats_application

Update an application

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAtsApplication" method="patch" path="/ats/{connection_id}/application/{id}" example="ats_application" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.application.patch_ats_application(request={
        "ats_application": {
            "answers": [],
            "applied_at": parse_datetime("2025-09-08T23:18:28.197Z"),
            "created_at": parse_datetime("2023-10-17T07:19:48.787Z"),
            "hired_at": parse_datetime("2026-04-15T09:38:27.880Z"),
            "id": "ecdbe009-647e-486f-86d0-51f912b2a426",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "a1302a79-0341-40e6-b91a-daeb95584617",
                    "namespace": "application",
                    "slug": "despecto",
                    "value": "Argentum decretum cultellus aveho distinctio verecundia stella depono.",
                },
            ],
            "offers": [],
            "original_status": "vomica",
            "original_substatus": "allatus",
            "rejected_at": parse_datetime("2026-09-09T18:00:57.635Z"),
            "rejected_reason": "Cometes amplitudo videlicet talio.",
            "source": "credo",
            "status": shared.AtsApplicationStatus.REVIEWING,
            "summary": "Comburo quidem vesica vulnus curatio. Appositus amita attonbitus conatus degenero charisma sordeo villa victoria varius. Cenaculum acsi officia.",
            "updated_at": parse_datetime("2026-09-16T09:27:50.487Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_application is not None

    # Handle response
    print(res.ats_application)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchAtsApplicationRequest](../../models/operations/patchatsapplicationrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchAtsApplicationResponse](../../models/operations/patchatsapplicationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ats_application

Remove an application

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAtsApplication" method="delete" path="/ats/{connection_id}/application/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.application.remove_ats_application(request={
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
| `request`                                                                                        | [operations.RemoveAtsApplicationRequest](../../models/operations/removeatsapplicationrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.RemoveAtsApplicationResponse](../../models/operations/removeatsapplicationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ats_application

Update an application

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAtsApplication" method="put" path="/ats/{connection_id}/application/{id}" example="ats_application" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.application.update_ats_application(request={
        "ats_application": {
            "answers": [],
            "applied_at": parse_datetime("2025-09-08T23:18:28.197Z"),
            "created_at": parse_datetime("2023-10-17T07:19:48.787Z"),
            "hired_at": parse_datetime("2026-04-15T09:38:27.880Z"),
            "id": "ecdbe009-647e-486f-86d0-51f912b2a426",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "a1302a79-0341-40e6-b91a-daeb95584617",
                    "namespace": "application",
                    "slug": "despecto",
                    "value": "Argentum decretum cultellus aveho distinctio verecundia stella depono.",
                },
            ],
            "offers": [],
            "original_status": "vomica",
            "original_substatus": "allatus",
            "rejected_at": parse_datetime("2026-09-09T18:00:57.635Z"),
            "rejected_reason": "Cometes amplitudo videlicet talio.",
            "source": "credo",
            "status": shared.AtsApplicationStatus.REVIEWING,
            "summary": "Comburo quidem vesica vulnus curatio. Appositus amita attonbitus conatus degenero charisma sordeo villa victoria varius. Cenaculum acsi officia.",
            "updated_at": parse_datetime("2026-09-16T09:27:50.487Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_application is not None

    # Handle response
    print(res.ats_application)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateAtsApplicationRequest](../../models/operations/updateatsapplicationrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateAtsApplicationResponse](../../models/operations/updateatsapplicationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |