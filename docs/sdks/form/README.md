# Form

## Overview

### Available Operations

* [create_forms_form](#create_forms_form) - Create a form
* [get_forms_form](#get_forms_form) - Retrieve a form
* [list_forms_forms](#list_forms_forms) - List all forms
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

    res = unified_to.form.create_forms_form(request={
        "forms_form": {
            "confirmation_message": "Alo crebro vado utique.",
            "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
            "description": "Qui pauper triumphus adipisci comitatus tamen stabilis clementia culpo tolero.",
            "fields": [
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "828b6125-a896-412e-b3e6-757234b2f34c",
                    "is_active": True,
                    "is_required": True,
                    "max_length": 146.0,
                    "name": "cornu creta confugo",
                    "order": 0.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2025-05-13T01:50:27.781Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "a5ab497c-5e02-4665-9a5d-d42c6b9b6ce0",
                    "is_active": True,
                    "is_required": False,
                    "name": "tracto nostrum desidero",
                    "order": 1.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-09-10T13:15:24.608Z"),
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
                    "id": "e25b2785-bf43-48a6-b106-75df9b854bbe",
                    "is_active": True,
                    "is_required": False,
                    "name": "officia supra consequatur",
                    "order": 2.0,
                    "type": shared.FormFieldType.MULTIPLE_SELECT,
                    "updated_at": parse_datetime("2024-02-29T23:23:01.546Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "description": "Antepono cursim aurum voluptatum placeat audax tripudio amo.",
                    "id": "c9c79964-1074-4cba-a130-f53d49dd3ecc",
                    "is_active": True,
                    "is_required": False,
                    "name": "curtus fugiat audentia",
                    "order": 3.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-12-07T23:31:54.456Z"),
                },
            ],
            "has_multiple_submissions": False,
            "has_progress_bar": False,
            "has_shuffle_questions": True,
            "id": "b11d00f8-0818-448f-b250-a01e421fbc9a",
            "is_active": False,
            "metadata": [],
            "name": "tandem tracto vivo Form",
            "published_url": "https://massive-blowgun.info",
            "response_count": 423.0,
            "updated_at": parse_datetime("2024-09-01T23:27:08.427Z"),
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

    res = unified_to.form.get_forms_form(request={
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

    res = unified_to.form.list_forms_forms(request={
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

    res = unified_to.form.patch_forms_form(request={
        "forms_form": {
            "confirmation_message": "Alo crebro vado utique.",
            "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
            "description": "Qui pauper triumphus adipisci comitatus tamen stabilis clementia culpo tolero.",
            "fields": [
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "1d587010-360a-4888-bd46-2ec2072d81fc",
                    "is_active": True,
                    "is_required": True,
                    "max_length": 146.0,
                    "name": "cornu creta confugo",
                    "order": 0.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2025-05-13T01:50:27.787Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "f3eceb88-a74a-4b42-beb6-746e596b1dec",
                    "is_active": True,
                    "is_required": False,
                    "name": "tracto nostrum desidero",
                    "order": 1.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-09-10T13:15:24.612Z"),
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
                    "id": "2b82c440-9d02-481e-87e6-0621fc3830ea",
                    "is_active": True,
                    "is_required": False,
                    "name": "officia supra consequatur",
                    "order": 2.0,
                    "type": shared.FormFieldType.MULTIPLE_SELECT,
                    "updated_at": parse_datetime("2024-02-29T23:23:01.548Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "description": "Antepono cursim aurum voluptatum placeat audax tripudio amo.",
                    "id": "e1bbdc58-a390-4b52-bdc2-00c632b2f499",
                    "is_active": True,
                    "is_required": False,
                    "name": "curtus fugiat audentia",
                    "order": 3.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-12-07T23:31:54.461Z"),
                },
            ],
            "has_multiple_submissions": False,
            "has_progress_bar": False,
            "has_shuffle_questions": True,
            "id": "98dfd82b-4a7c-4d41-9484-c8f5672e722d",
            "is_active": False,
            "metadata": [],
            "name": "tandem tracto vivo Form",
            "published_url": "https://massive-blowgun.info",
            "response_count": 423.0,
            "updated_at": parse_datetime("2024-09-01T23:27:08.431Z"),
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

    res = unified_to.form.remove_forms_form(request={
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

    res = unified_to.form.update_forms_form(request={
        "forms_form": {
            "confirmation_message": "Alo crebro vado utique.",
            "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
            "description": "Qui pauper triumphus adipisci comitatus tamen stabilis clementia culpo tolero.",
            "fields": [
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "1d587010-360a-4888-bd46-2ec2072d81fc",
                    "is_active": True,
                    "is_required": True,
                    "max_length": 146.0,
                    "name": "cornu creta confugo",
                    "order": 0.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2025-05-13T01:50:27.787Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "f3eceb88-a74a-4b42-beb6-746e596b1dec",
                    "is_active": True,
                    "is_required": False,
                    "name": "tracto nostrum desidero",
                    "order": 1.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-09-10T13:15:24.612Z"),
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
                    "id": "2b82c440-9d02-481e-87e6-0621fc3830ea",
                    "is_active": True,
                    "is_required": False,
                    "name": "officia supra consequatur",
                    "order": 2.0,
                    "type": shared.FormFieldType.MULTIPLE_SELECT,
                    "updated_at": parse_datetime("2024-02-29T23:23:01.548Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "description": "Antepono cursim aurum voluptatum placeat audax tripudio amo.",
                    "id": "e1bbdc58-a390-4b52-bdc2-00c632b2f499",
                    "is_active": True,
                    "is_required": False,
                    "name": "curtus fugiat audentia",
                    "order": 3.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-12-07T23:31:54.461Z"),
                },
            ],
            "has_multiple_submissions": False,
            "has_progress_bar": False,
            "has_shuffle_questions": True,
            "id": "98dfd82b-4a7c-4d41-9484-c8f5672e722d",
            "is_active": False,
            "metadata": [],
            "name": "tandem tracto vivo Form",
            "published_url": "https://massive-blowgun.info",
            "response_count": 423.0,
            "updated_at": parse_datetime("2024-09-01T23:27:08.431Z"),
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