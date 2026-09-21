# Pullrequest

## Overview

### Available Operations

* [create_repo_pullrequest](#create_repo_pullrequest) - Create a pullrequest
* [get_repo_pullrequest](#get_repo_pullrequest) - Retrieve a pullrequest
* [list_repo_pullrequests](#list_repo_pullrequests) - List all pullrequests
* [patch_repo_pullrequest](#patch_repo_pullrequest) - Update a pullrequest
* [remove_repo_pullrequest](#remove_repo_pullrequest) - Remove a pullrequest
* [update_repo_pullrequest](#update_repo_pullrequest) - Update a pullrequest

## create_repo_pullrequest

Create a pullrequest

### Example Usage

<!-- UsageSnippet language="python" operationID="createRepoPullrequest" method="post" path="/repo/{connection_id}/pullrequest" example="repo_pullrequest" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.pullrequest.create_repo_pullrequest(request={
        "repo_pullrequest": {
            "closed_at": parse_datetime("2025-04-13T13:31:25.872Z"),
            "created_at": parse_datetime("2023-02-27T09:37:13.663Z"),
            "id": "180cb6d6-bd73-4c3a-a6aa-fe91dcbcbe6c",
            "labels": [
                "adhuc",
                "quaerat",
            ],
            "notes": "Coadunatio turbo curtus ceno consuasor aggero. Suggero adeo creptio tutamen vulnus aqua delicate adopto derelinquo caritas. Maiores vulgivagus succurro temporibus.",
            "source_branch_id": "microchip-navigate",
            "status": shared.RepoPullrequestStatus.REJECTED,
            "target_branch_id": "feed-reboot",
            "title": "Cunae aegrus averto texo advoco bibo amet asporto.",
            "updated_at": parse_datetime("2025-01-01T10:29:22.188Z"),
        },
        "connection_id": "<id>",
    })

    assert res.repo_pullrequest is not None

    # Handle response
    print(res.repo_pullrequest)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateRepoPullrequestRequest](../../models/operations/createrepopullrequestrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateRepoPullrequestResponse](../../models/operations/createrepopullrequestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_repo_pullrequest

Retrieve a pullrequest

### Example Usage

<!-- UsageSnippet language="python" operationID="getRepoPullrequest" method="get" path="/repo/{connection_id}/pullrequest/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.pullrequest.get_repo_pullrequest(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_pullrequest is not None

    # Handle response
    print(res.repo_pullrequest)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetRepoPullrequestRequest](../../models/operations/getrepopullrequestrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetRepoPullrequestResponse](../../models/operations/getrepopullrequestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_repo_pullrequests

List all pullrequests

### Example Usage

<!-- UsageSnippet language="python" operationID="listRepoPullrequests" method="get" path="/repo/{connection_id}/pullrequest" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.pullrequest.list_repo_pullrequests(request={
        "connection_id": "<id>",
    })

    assert res.repo_pullrequests is not None

    # Handle response
    print(res.repo_pullrequests)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListRepoPullrequestsRequest](../../models/operations/listrepopullrequestsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListRepoPullrequestsResponse](../../models/operations/listrepopullrequestsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_repo_pullrequest

Update a pullrequest

### Example Usage

<!-- UsageSnippet language="python" operationID="patchRepoPullrequest" method="patch" path="/repo/{connection_id}/pullrequest/{id}" example="repo_pullrequest" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.pullrequest.patch_repo_pullrequest(request={
        "repo_pullrequest": {
            "closed_at": parse_datetime("2025-04-13T13:31:25.880Z"),
            "created_at": parse_datetime("2023-02-27T09:37:13.663Z"),
            "id": "52711ad8-d8ff-496a-839b-5a2193de9d59",
            "labels": [
                "adhuc",
                "quaerat",
            ],
            "notes": "Coadunatio turbo curtus ceno consuasor aggero. Suggero adeo creptio tutamen vulnus aqua delicate adopto derelinquo caritas. Maiores vulgivagus succurro temporibus.",
            "source_branch_id": "microchip-navigate",
            "status": shared.RepoPullrequestStatus.REJECTED,
            "target_branch_id": "feed-reboot",
            "title": "Cunae aegrus averto texo advoco bibo amet asporto.",
            "updated_at": parse_datetime("2025-01-01T10:29:22.195Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_pullrequest is not None

    # Handle response
    print(res.repo_pullrequest)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchRepoPullrequestRequest](../../models/operations/patchrepopullrequestrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchRepoPullrequestResponse](../../models/operations/patchrepopullrequestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_repo_pullrequest

Remove a pullrequest

### Example Usage

<!-- UsageSnippet language="python" operationID="removeRepoPullrequest" method="delete" path="/repo/{connection_id}/pullrequest/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.pullrequest.remove_repo_pullrequest(request={
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
| `request`                                                                                          | [operations.RemoveRepoPullrequestRequest](../../models/operations/removerepopullrequestrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveRepoPullrequestResponse](../../models/operations/removerepopullrequestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_repo_pullrequest

Update a pullrequest

### Example Usage

<!-- UsageSnippet language="python" operationID="updateRepoPullrequest" method="put" path="/repo/{connection_id}/pullrequest/{id}" example="repo_pullrequest" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.pullrequest.update_repo_pullrequest(request={
        "repo_pullrequest": {
            "closed_at": parse_datetime("2025-04-13T13:31:25.880Z"),
            "created_at": parse_datetime("2023-02-27T09:37:13.663Z"),
            "id": "52711ad8-d8ff-496a-839b-5a2193de9d59",
            "labels": [
                "adhuc",
                "quaerat",
            ],
            "notes": "Coadunatio turbo curtus ceno consuasor aggero. Suggero adeo creptio tutamen vulnus aqua delicate adopto derelinquo caritas. Maiores vulgivagus succurro temporibus.",
            "source_branch_id": "microchip-navigate",
            "status": shared.RepoPullrequestStatus.REJECTED,
            "target_branch_id": "feed-reboot",
            "title": "Cunae aegrus averto texo advoco bibo amet asporto.",
            "updated_at": parse_datetime("2025-01-01T10:29:22.195Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_pullrequest is not None

    # Handle response
    print(res.repo_pullrequest)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateRepoPullrequestRequest](../../models/operations/updaterepopullrequestrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateRepoPullrequestResponse](../../models/operations/updaterepopullrequestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |