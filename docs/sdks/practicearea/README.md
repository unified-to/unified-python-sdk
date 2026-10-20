# Practicearea

## Overview

### Available Operations

* [create_legal_practicearea](#create_legal_practicearea) - Create a practicearea
* [get_legal_practicearea](#get_legal_practicearea) - Retrieve a practicearea
* [list_legal_practiceareas](#list_legal_practiceareas) - List all practiceareas
* [patch_legal_practicearea](#patch_legal_practicearea) - Update a practicearea
* [remove_legal_practicearea](#remove_legal_practicearea) - Remove a practicearea
* [update_legal_practicearea](#update_legal_practicearea) - Update a practicearea

## create_legal_practicearea

Create a practicearea

### Example Usage

<!-- UsageSnippet language="python" operationID="createLegalPracticearea" method="post" path="/legal/{connection_id}/practicearea" example="legal_practicearea" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.practicearea.create_legal_practicearea(request={
        "legal_practicearea": {
            "code": "QCA",
            "created_at": parse_datetime("2023-01-28T21:00:26.264Z"),
            "id": "b714c3b8-a3ef-4583-b136-964481b7d4fa",
            "metadata": [],
            "name": "witty Law",
            "type": shared.LegalPracticeareaType.EDUCATION,
            "updated_at": parse_datetime("2025-08-26T20:58:36.166Z"),
        },
        "connection_id": "<id>",
    })

    assert res.legal_practicearea is not None

    # Handle response
    print(res.legal_practicearea)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateLegalPracticeareaRequest](../../models/operations/createlegalpracticearearequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateLegalPracticeareaResponse](../../models/operations/createlegalpracticearearesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_legal_practicearea

Retrieve a practicearea

### Example Usage

<!-- UsageSnippet language="python" operationID="getLegalPracticearea" method="get" path="/legal/{connection_id}/practicearea/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.practicearea.get_legal_practicearea(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.legal_practicearea is not None

    # Handle response
    print(res.legal_practicearea)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetLegalPracticeareaRequest](../../models/operations/getlegalpracticearearequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetLegalPracticeareaResponse](../../models/operations/getlegalpracticearearesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_legal_practiceareas

List all practiceareas

### Example Usage

<!-- UsageSnippet language="python" operationID="listLegalPracticeareas" method="get" path="/legal/{connection_id}/practicearea" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.practicearea.list_legal_practiceareas(request={
        "connection_id": "<id>",
    })

    assert res.legal_practiceareas is not None

    # Handle response
    print(res.legal_practiceareas)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListLegalPracticeareasRequest](../../models/operations/listlegalpracticeareasrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListLegalPracticeareasResponse](../../models/operations/listlegalpracticeareasresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_legal_practicearea

Update a practicearea

### Example Usage

<!-- UsageSnippet language="python" operationID="patchLegalPracticearea" method="patch" path="/legal/{connection_id}/practicearea/{id}" example="legal_practicearea" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.practicearea.patch_legal_practicearea(request={
        "legal_practicearea": {
            "code": "QCA",
            "created_at": parse_datetime("2023-01-28T21:00:26.264Z"),
            "id": "7fb49568-9a93-407d-a52b-7732ec1cfa57",
            "metadata": [],
            "name": "witty Law",
            "type": shared.LegalPracticeareaType.EDUCATION,
            "updated_at": parse_datetime("2025-08-26T20:58:36.182Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.legal_practicearea is not None

    # Handle response
    print(res.legal_practicearea)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchLegalPracticeareaRequest](../../models/operations/patchlegalpracticearearequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchLegalPracticeareaResponse](../../models/operations/patchlegalpracticearearesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_legal_practicearea

Remove a practicearea

### Example Usage

<!-- UsageSnippet language="python" operationID="removeLegalPracticearea" method="delete" path="/legal/{connection_id}/practicearea/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.practicearea.remove_legal_practicearea(request={
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
| `request`                                                                                              | [operations.RemoveLegalPracticeareaRequest](../../models/operations/removelegalpracticearearequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveLegalPracticeareaResponse](../../models/operations/removelegalpracticearearesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_legal_practicearea

Update a practicearea

### Example Usage

<!-- UsageSnippet language="python" operationID="updateLegalPracticearea" method="put" path="/legal/{connection_id}/practicearea/{id}" example="legal_practicearea" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.practicearea.update_legal_practicearea(request={
        "legal_practicearea": {
            "code": "QCA",
            "created_at": parse_datetime("2023-01-28T21:00:26.264Z"),
            "id": "7fb49568-9a93-407d-a52b-7732ec1cfa57",
            "metadata": [],
            "name": "witty Law",
            "type": shared.LegalPracticeareaType.EDUCATION,
            "updated_at": parse_datetime("2025-08-26T20:58:36.182Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.legal_practicearea is not None

    # Handle response
    print(res.legal_practicearea)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateLegalPracticeareaRequest](../../models/operations/updatelegalpracticearearequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateLegalPracticeareaResponse](../../models/operations/updatelegalpracticearearesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |