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
                    "id": "89299113-7074-4c83-95e7-92d2223213f9",
                    "is_active": True,
                    "is_required": True,
                    "max_length": 146.0,
                    "name": "voluntarius argumentum decumbo",
                    "order": 0.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2025-05-18T04:51:36.067Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "5b96097c-f653-4e61-8b39-70c6fa4fb1d1",
                    "is_active": True,
                    "is_required": False,
                    "name": "desidero clibanus calcar",
                    "order": 1.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-09-13T12:52:14.467Z"),
                },
                {
                    "choices": [
                        "crur",
                        "vinculum",
                        "tredecim",
                        "somniculosus",
                        "curtus",
                    ],
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "default_value": "fugiat",
                    "id": "ec7cce1b-69b9-4aaa-98e1-ac36772a189e",
                    "is_active": True,
                    "is_required": False,
                    "name": "consequatur error cena",
                    "order": 2.0,
                    "type": shared.FormFieldType.MULTIPLE_SELECT,
                    "updated_at": parse_datetime("2024-03-02T06:18:09.637Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "description": "Aurum voluptatum placeat audax tripudio amo.",
                    "id": "627135ee-4741-4673-863e-1b38dd131020",
                    "is_active": True,
                    "is_required": False,
                    "name": "audentia subseco antepono",
                    "order": 3.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-12-11T17:44:07.588Z"),
                },
            ],
            "has_multiple_submissions": False,
            "has_progress_bar": False,
            "has_shuffle_questions": True,
            "id": "557b4c61-2921-48f1-b52e-5331d2d8e639",
            "is_active": False,
            "metadata": [],
            "name": "tandem tracto vivo Form",
            "published_url": "https://massive-blowgun.info",
            "response_count": 423.0,
            "updated_at": parse_datetime("2024-09-04T21:15:48.500Z"),
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
                    "id": "1b3d0bc5-bdb0-4b8d-9490-ad18aa7f3c00",
                    "is_active": True,
                    "is_required": True,
                    "max_length": 146.0,
                    "name": "voluntarius argumentum decumbo",
                    "order": 0.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2025-05-18T04:51:36.079Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "e87894c9-3002-45fd-be21-8f325652ab8e",
                    "is_active": True,
                    "is_required": False,
                    "name": "desidero clibanus calcar",
                    "order": 1.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-09-13T12:52:14.474Z"),
                },
                {
                    "choices": [
                        "crur",
                        "vinculum",
                        "tredecim",
                        "somniculosus",
                        "curtus",
                    ],
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "default_value": "fugiat",
                    "id": "ba04a1a0-badc-4e56-b87a-4218d06996a3",
                    "is_active": True,
                    "is_required": False,
                    "name": "consequatur error cena",
                    "order": 2.0,
                    "type": shared.FormFieldType.MULTIPLE_SELECT,
                    "updated_at": parse_datetime("2024-03-02T06:18:09.640Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "description": "Aurum voluptatum placeat audax tripudio amo.",
                    "id": "44cb6040-c891-45f1-b866-65a00f72199a",
                    "is_active": True,
                    "is_required": False,
                    "name": "audentia subseco antepono",
                    "order": 3.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-12-11T17:44:07.597Z"),
                },
            ],
            "has_multiple_submissions": False,
            "has_progress_bar": False,
            "has_shuffle_questions": True,
            "id": "8c9923c4-058b-4b5c-b80e-b41c47fb0cd6",
            "is_active": False,
            "metadata": [],
            "name": "tandem tracto vivo Form",
            "published_url": "https://massive-blowgun.info",
            "response_count": 423.0,
            "updated_at": parse_datetime("2024-09-04T21:15:48.507Z"),
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
                    "id": "1b3d0bc5-bdb0-4b8d-9490-ad18aa7f3c00",
                    "is_active": True,
                    "is_required": True,
                    "max_length": 146.0,
                    "name": "voluntarius argumentum decumbo",
                    "order": 0.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2025-05-18T04:51:36.079Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "e87894c9-3002-45fd-be21-8f325652ab8e",
                    "is_active": True,
                    "is_required": False,
                    "name": "desidero clibanus calcar",
                    "order": 1.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-09-13T12:52:14.474Z"),
                },
                {
                    "choices": [
                        "crur",
                        "vinculum",
                        "tredecim",
                        "somniculosus",
                        "curtus",
                    ],
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "default_value": "fugiat",
                    "id": "ba04a1a0-badc-4e56-b87a-4218d06996a3",
                    "is_active": True,
                    "is_required": False,
                    "name": "consequatur error cena",
                    "order": 2.0,
                    "type": shared.FormFieldType.MULTIPLE_SELECT,
                    "updated_at": parse_datetime("2024-03-02T06:18:09.640Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "description": "Aurum voluptatum placeat audax tripudio amo.",
                    "id": "44cb6040-c891-45f1-b866-65a00f72199a",
                    "is_active": True,
                    "is_required": False,
                    "name": "audentia subseco antepono",
                    "order": 3.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-12-11T17:44:07.597Z"),
                },
            ],
            "has_multiple_submissions": False,
            "has_progress_bar": False,
            "has_shuffle_questions": True,
            "id": "8c9923c4-058b-4b5c-b80e-b41c47fb0cd6",
            "is_active": False,
            "metadata": [],
            "name": "tandem tracto vivo Form",
            "published_url": "https://massive-blowgun.info",
            "response_count": 423.0,
            "updated_at": parse_datetime("2024-09-04T21:15:48.507Z"),
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