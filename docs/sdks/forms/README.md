# Forms

## Overview

### Available Operations

* [create_forms_form](#create_forms_form) - Create a form
* [get_forms_form](#get_forms_form) - Retrieve a form
* [get_forms_submission](#get_forms_submission) - Retrieve a submission
* [list_forms_forms](#list_forms_forms) - List all forms
* [list_forms_submissions](#list_forms_submissions) - List all submissions
* [patch_forms_form](#patch_forms_form) - Update a form
* [remove_forms_form](#remove_forms_form) - Remove a form
* [update_forms_form](#update_forms_form) - Update a form

## create_forms_form

Creates a FormsForm. Provide the unified FormsForm fields in the request body; they are mapped to the provider's API. Returns the created FormsForm.

### Example Usage

<!-- UsageSnippet language="python" operationID="createFormsForm" method="post" path="/forms/{connection_id}/form" example="forms_form" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.forms.create_forms_form(request={
        "forms_form": {
            "confirmation_message": "Alo crebro vado utique.",
            "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
            "description": "Qui pauper triumphus adipisci comitatus tamen stabilis clementia culpo tolero.",
            "fields": [
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "34ab8c2d-f553-486b-aa9e-2f9b0678d9ee",
                    "is_active": True,
                    "is_required": True,
                    "max_length": 146.0,
                    "name": "cornu creta confugo",
                    "order": 0.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2025-05-04T06:43:21.964Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "f235bfbb-cb96-492c-8bee-f0c0c90d1888",
                    "is_active": True,
                    "is_required": False,
                    "name": "tracto nostrum desidero",
                    "order": 1.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-09-05T10:21:25.728Z"),
                },
                {
                    "choices": [
                        "conor",
                        "patior",
                        "crur",
                        "vinculum",
                        "tredecim",
                    ],
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "default_value": "somniculosus",
                    "id": "c00282b1-42f0-4f04-9b48-1824aef00f5a",
                    "is_active": True,
                    "is_required": False,
                    "name": "officia supra consequatur",
                    "order": 2.0,
                    "type": shared.FormFieldType.MULTIPLE_SELECT,
                    "updated_at": parse_datetime("2024-02-27T18:19:20.818Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "description": "Antepono cursim aurum voluptatum placeat audax tripudio amo.",
                    "id": "b14158ab-2364-461d-ab7a-074db446ece2",
                    "is_active": True,
                    "is_required": False,
                    "name": "curtus fugiat audentia",
                    "order": 3.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-12-01T12:43:45.592Z"),
                },
            ],
            "has_multiple_submissions": False,
            "has_progress_bar": False,
            "has_shuffle_questions": True,
            "id": "999a2bb6-dd4b-48fd-b537-46941c969fd1",
            "is_active": False,
            "metadata": [],
            "name": "tandem tracto vivo Form",
            "published_url": "https://massive-blowgun.info",
            "response_count": 423.0,
            "updated_at": parse_datetime("2024-08-27T23:38:46.956Z"),
        },
        "connection_id": "<id>",
    })

    assert res.forms_form is not None

    # Handle response
    print(res.forms_form)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateFormsFormRequest](../../models/operations/createformsformrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.CreateFormsFormResponse](../../models/operations/createformsformresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_forms_form

Retrieves a single FormsForm by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getFormsForm" method="get" path="/forms/{connection_id}/form/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.forms.get_forms_form(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.forms_form is not None

    # Handle response
    print(res.forms_form)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetFormsFormRequest](../../models/operations/getformsformrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GetFormsFormResponse](../../models/operations/getformsformresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_forms_submission

Retrieves a single FormsSubmission by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getFormsSubmission" method="get" path="/forms/{connection_id}/submission/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.forms.get_forms_submission(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.forms_submission is not None

    # Handle response
    print(res.forms_submission)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetFormsSubmissionRequest](../../models/operations/getformssubmissionrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetFormsSubmissionResponse](../../models/operations/getformssubmissionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_forms_forms

Returns a list of FormsForms. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listFormsForms" method="get" path="/forms/{connection_id}/form" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.forms.list_forms_forms(request={
        "connection_id": "<id>",
    })

    assert res.forms_forms is not None

    # Handle response
    print(res.forms_forms)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListFormsFormsRequest](../../models/operations/listformsformsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListFormsFormsResponse](../../models/operations/listformsformsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_forms_submissions

Returns a list of FormsSubmissions. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listFormsSubmissions" method="get" path="/forms/{connection_id}/submission" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.forms.list_forms_submissions(request={
        "connection_id": "<id>",
    })

    assert res.forms_submissions is not None

    # Handle response
    print(res.forms_submissions)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListFormsSubmissionsRequest](../../models/operations/listformssubmissionsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListFormsSubmissionsResponse](../../models/operations/listformssubmissionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_forms_form

Updates the FormsForm identified by `id`. Provide the unified FormsForm fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchFormsForm" method="patch" path="/forms/{connection_id}/form/{id}" example="forms_form" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.forms.patch_forms_form(request={
        "forms_form": {
            "confirmation_message": "Alo crebro vado utique.",
            "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
            "description": "Qui pauper triumphus adipisci comitatus tamen stabilis clementia culpo tolero.",
            "fields": [
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "c79b8df0-9b65-4d69-8792-6fec4d614ca6",
                    "is_active": True,
                    "is_required": True,
                    "max_length": 146.0,
                    "name": "cornu creta confugo",
                    "order": 0.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2025-05-04T06:43:21.976Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "2443484e-7d61-486f-9bfa-9c428689d380",
                    "is_active": True,
                    "is_required": False,
                    "name": "tracto nostrum desidero",
                    "order": 1.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-09-05T10:21:25.734Z"),
                },
                {
                    "choices": [
                        "conor",
                        "patior",
                        "crur",
                        "vinculum",
                        "tredecim",
                    ],
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "default_value": "somniculosus",
                    "id": "ab7379b5-3599-4672-8d3c-3bdb196fc68b",
                    "is_active": True,
                    "is_required": False,
                    "name": "officia supra consequatur",
                    "order": 2.0,
                    "type": shared.FormFieldType.MULTIPLE_SELECT,
                    "updated_at": parse_datetime("2024-02-27T18:19:20.821Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "description": "Antepono cursim aurum voluptatum placeat audax tripudio amo.",
                    "id": "8bc7617a-4f40-4305-a973-dbe6428f1822",
                    "is_active": True,
                    "is_required": False,
                    "name": "curtus fugiat audentia",
                    "order": 3.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-12-01T12:43:45.600Z"),
                },
            ],
            "has_multiple_submissions": False,
            "has_progress_bar": False,
            "has_shuffle_questions": True,
            "id": "33711e32-70da-4a1b-867b-c4a4885edc82",
            "is_active": False,
            "metadata": [],
            "name": "tandem tracto vivo Form",
            "published_url": "https://massive-blowgun.info",
            "response_count": 423.0,
            "updated_at": parse_datetime("2024-08-27T23:38:46.962Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.forms_form is not None

    # Handle response
    print(res.forms_form)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchFormsFormRequest](../../models/operations/patchformsformrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.PatchFormsFormResponse](../../models/operations/patchformsformresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_forms_form

Deletes the FormsForm identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeFormsForm" method="delete" path="/forms/{connection_id}/form/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.forms.remove_forms_form(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.RemoveFormsFormRequest](../../models/operations/removeformsformrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.RemoveFormsFormResponse](../../models/operations/removeformsformresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_forms_form

Updates the FormsForm identified by `id`. Provide the unified FormsForm fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateFormsForm" method="put" path="/forms/{connection_id}/form/{id}" example="forms_form" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.forms.update_forms_form(request={
        "forms_form": {
            "confirmation_message": "Alo crebro vado utique.",
            "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
            "description": "Qui pauper triumphus adipisci comitatus tamen stabilis clementia culpo tolero.",
            "fields": [
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "c79b8df0-9b65-4d69-8792-6fec4d614ca6",
                    "is_active": True,
                    "is_required": True,
                    "max_length": 146.0,
                    "name": "cornu creta confugo",
                    "order": 0.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2025-05-04T06:43:21.976Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "2443484e-7d61-486f-9bfa-9c428689d380",
                    "is_active": True,
                    "is_required": False,
                    "name": "tracto nostrum desidero",
                    "order": 1.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-09-05T10:21:25.734Z"),
                },
                {
                    "choices": [
                        "conor",
                        "patior",
                        "crur",
                        "vinculum",
                        "tredecim",
                    ],
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "default_value": "somniculosus",
                    "id": "ab7379b5-3599-4672-8d3c-3bdb196fc68b",
                    "is_active": True,
                    "is_required": False,
                    "name": "officia supra consequatur",
                    "order": 2.0,
                    "type": shared.FormFieldType.MULTIPLE_SELECT,
                    "updated_at": parse_datetime("2024-02-27T18:19:20.821Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "description": "Antepono cursim aurum voluptatum placeat audax tripudio amo.",
                    "id": "8bc7617a-4f40-4305-a973-dbe6428f1822",
                    "is_active": True,
                    "is_required": False,
                    "name": "curtus fugiat audentia",
                    "order": 3.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-12-01T12:43:45.600Z"),
                },
            ],
            "has_multiple_submissions": False,
            "has_progress_bar": False,
            "has_shuffle_questions": True,
            "id": "33711e32-70da-4a1b-867b-c4a4885edc82",
            "is_active": False,
            "metadata": [],
            "name": "tandem tracto vivo Form",
            "published_url": "https://massive-blowgun.info",
            "response_count": 423.0,
            "updated_at": parse_datetime("2024-08-27T23:38:46.962Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.forms_form is not None

    # Handle response
    print(res.forms_form)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateFormsFormRequest](../../models/operations/updateformsformrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.UpdateFormsFormResponse](../../models/operations/updateformsformresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |