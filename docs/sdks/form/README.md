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
                    "id": "bfc8551c-bf62-47e5-83af-f4141a7b7d91",
                    "is_active": True,
                    "is_required": True,
                    "max_length": 146.0,
                    "name": "cornu creta confugo",
                    "order": 0.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2025-05-14T01:58:49.376Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "a2347750-2162-41f5-bbb3-318717d3380b",
                    "is_active": True,
                    "is_required": False,
                    "name": "tracto nostrum desidero",
                    "order": 1.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-09-11T03:18:33.211Z"),
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
                    "id": "2887535c-ece7-4819-87ef-c6e87dd4be53",
                    "is_active": True,
                    "is_required": False,
                    "name": "officia supra consequatur",
                    "order": 2.0,
                    "type": shared.FormFieldType.MULTIPLE_SELECT,
                    "updated_at": parse_datetime("2024-03-01T05:27:02.918Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "description": "Antepono cursim aurum voluptatum placeat audax tripudio amo.",
                    "id": "1ebe07e8-fa3a-4d8f-b732-58a809bfdffd",
                    "is_active": True,
                    "is_required": False,
                    "name": "curtus fugiat audentia",
                    "order": 3.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-12-08T17:13:55.042Z"),
                },
            ],
            "has_multiple_submissions": False,
            "has_progress_bar": False,
            "has_shuffle_questions": True,
            "id": "056f16ed-7668-454f-a3f8-abc1bc4ebf51",
            "is_active": False,
            "metadata": [],
            "name": "tandem tracto vivo Form",
            "published_url": "https://massive-blowgun.info",
            "response_count": 423.0,
            "updated_at": parse_datetime("2024-09-02T13:09:03.575Z"),
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
                    "id": "68967ea1-8979-4f10-8ebb-918b8f216c09",
                    "is_active": True,
                    "is_required": True,
                    "max_length": 146.0,
                    "name": "cornu creta confugo",
                    "order": 0.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2025-05-14T01:58:49.386Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "782a818a-cc4b-405b-bc0c-b68854e752f9",
                    "is_active": True,
                    "is_required": False,
                    "name": "tracto nostrum desidero",
                    "order": 1.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-09-11T03:18:33.217Z"),
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
                    "id": "5177f723-9729-4ccc-a536-a8a58713dc54",
                    "is_active": True,
                    "is_required": False,
                    "name": "officia supra consequatur",
                    "order": 2.0,
                    "type": shared.FormFieldType.MULTIPLE_SELECT,
                    "updated_at": parse_datetime("2024-03-01T05:27:02.920Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "description": "Antepono cursim aurum voluptatum placeat audax tripudio amo.",
                    "id": "e1ceb281-a612-4fec-85fd-dcf0a5f60cd3",
                    "is_active": True,
                    "is_required": False,
                    "name": "curtus fugiat audentia",
                    "order": 3.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-12-08T17:13:55.050Z"),
                },
            ],
            "has_multiple_submissions": False,
            "has_progress_bar": False,
            "has_shuffle_questions": True,
            "id": "c864f85e-4d40-45c1-ba13-e7c156b5a129",
            "is_active": False,
            "metadata": [],
            "name": "tandem tracto vivo Form",
            "published_url": "https://massive-blowgun.info",
            "response_count": 423.0,
            "updated_at": parse_datetime("2024-09-02T13:09:03.581Z"),
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
                    "id": "68967ea1-8979-4f10-8ebb-918b8f216c09",
                    "is_active": True,
                    "is_required": True,
                    "max_length": 146.0,
                    "name": "cornu creta confugo",
                    "order": 0.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2025-05-14T01:58:49.386Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "782a818a-cc4b-405b-bc0c-b68854e752f9",
                    "is_active": True,
                    "is_required": False,
                    "name": "tracto nostrum desidero",
                    "order": 1.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-09-11T03:18:33.217Z"),
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
                    "id": "5177f723-9729-4ccc-a536-a8a58713dc54",
                    "is_active": True,
                    "is_required": False,
                    "name": "officia supra consequatur",
                    "order": 2.0,
                    "type": shared.FormFieldType.MULTIPLE_SELECT,
                    "updated_at": parse_datetime("2024-03-01T05:27:02.920Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "description": "Antepono cursim aurum voluptatum placeat audax tripudio amo.",
                    "id": "e1ceb281-a612-4fec-85fd-dcf0a5f60cd3",
                    "is_active": True,
                    "is_required": False,
                    "name": "curtus fugiat audentia",
                    "order": 3.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-12-08T17:13:55.050Z"),
                },
            ],
            "has_multiple_submissions": False,
            "has_progress_bar": False,
            "has_shuffle_questions": True,
            "id": "c864f85e-4d40-45c1-ba13-e7c156b5a129",
            "is_active": False,
            "metadata": [],
            "name": "tandem tracto vivo Form",
            "published_url": "https://massive-blowgun.info",
            "response_count": 423.0,
            "updated_at": parse_datetime("2024-09-02T13:09:03.581Z"),
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