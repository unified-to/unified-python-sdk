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

Create a form

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
            "confirmation_message": "Cultura temeritas aptus celebrer volo pecus culpa annus aurum.",
            "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
            "description": "Sodalitas cupiditas terebro conduco.",
            "fields": [
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "565f27cf-2cf7-4c30-ad97-4340d859b584",
                    "is_active": True,
                    "is_required": True,
                    "max_length": 146.0,
                    "name": "vulgivagus audio accendo",
                    "order": 0.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2025-04-12T04:46:23.830Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "82b263f9-2d16-4cdf-8e99-d05ba46ce817",
                    "is_active": True,
                    "is_required": False,
                    "name": "alo crebro vado",
                    "order": 1.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-08-23T13:51:14.877Z"),
                },
                {
                    "choices": [
                        "vallum",
                        "vae",
                        "nesciunt",
                        "commodi",
                        "appositus",
                    ],
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "default_value": "cattus",
                    "id": "d7c963e5-2d3d-4436-a57d-a6e337d9d170",
                    "is_active": True,
                    "is_required": False,
                    "name": "casso tenus nesciunt",
                    "order": 2.0,
                    "type": shared.FormFieldType.MULTIPLE_SELECT,
                    "updated_at": parse_datetime("2024-02-22T05:07:40.251Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "description": "Sequi antea delectatio.",
                    "id": "e45efb8f-439b-40f6-8370-99c8ec66b065",
                    "is_active": True,
                    "is_required": False,
                    "name": "comburo utique ipsa",
                    "order": 3.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-11-15T08:08:38.111Z"),
                },
            ],
            "has_multiple_submissions": False,
            "has_progress_bar": False,
            "has_shuffle_questions": True,
            "id": "11618bab-d496-4338-8f1e-75eec9205ffa",
            "is_active": False,
            "name": "voluptatibus omnis audax Form",
            "published_url": "https://impartial-institute.org/",
            "response_count": 423.0,
            "updated_at": parse_datetime("2024-08-15T10:54:33.247Z"),
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

Retrieve a form

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

List all forms

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

Update a form

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
            "confirmation_message": "Cultura temeritas aptus celebrer volo pecus culpa annus aurum.",
            "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
            "description": "Sodalitas cupiditas terebro conduco.",
            "fields": [
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "565f27cf-2cf7-4c30-ad97-4340d859b584",
                    "is_active": True,
                    "is_required": True,
                    "max_length": 146.0,
                    "name": "vulgivagus audio accendo",
                    "order": 0.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2025-04-12T04:46:23.845Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "82b263f9-2d16-4cdf-8e99-d05ba46ce817",
                    "is_active": True,
                    "is_required": False,
                    "name": "alo crebro vado",
                    "order": 1.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-08-23T13:51:14.885Z"),
                },
                {
                    "choices": [
                        "vallum",
                        "vae",
                        "nesciunt",
                        "commodi",
                        "appositus",
                    ],
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "default_value": "cattus",
                    "id": "d7c963e5-2d3d-4436-a57d-a6e337d9d170",
                    "is_active": True,
                    "is_required": False,
                    "name": "casso tenus nesciunt",
                    "order": 2.0,
                    "type": shared.FormFieldType.MULTIPLE_SELECT,
                    "updated_at": parse_datetime("2024-02-22T05:07:40.255Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "description": "Sequi antea delectatio.",
                    "id": "e45efb8f-439b-40f6-8370-99c8ec66b065",
                    "is_active": True,
                    "is_required": False,
                    "name": "comburo utique ipsa",
                    "order": 3.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-11-15T08:08:38.121Z"),
                },
            ],
            "has_multiple_submissions": False,
            "has_progress_bar": False,
            "has_shuffle_questions": True,
            "id": "d66b2dac-71cd-4252-af7e-6694b58bc863",
            "is_active": False,
            "name": "voluptatibus omnis audax Form",
            "published_url": "https://impartial-institute.org/",
            "response_count": 423.0,
            "updated_at": parse_datetime("2024-08-15T10:54:33.255Z"),
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

Remove a form

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

Update a form

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
            "confirmation_message": "Cultura temeritas aptus celebrer volo pecus culpa annus aurum.",
            "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
            "description": "Sodalitas cupiditas terebro conduco.",
            "fields": [
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "565f27cf-2cf7-4c30-ad97-4340d859b584",
                    "is_active": True,
                    "is_required": True,
                    "max_length": 146.0,
                    "name": "vulgivagus audio accendo",
                    "order": 0.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2025-04-12T04:46:23.845Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "id": "82b263f9-2d16-4cdf-8e99-d05ba46ce817",
                    "is_active": True,
                    "is_required": False,
                    "name": "alo crebro vado",
                    "order": 1.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-08-23T13:51:14.885Z"),
                },
                {
                    "choices": [
                        "vallum",
                        "vae",
                        "nesciunt",
                        "commodi",
                        "appositus",
                    ],
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "default_value": "cattus",
                    "id": "d7c963e5-2d3d-4436-a57d-a6e337d9d170",
                    "is_active": True,
                    "is_required": False,
                    "name": "casso tenus nesciunt",
                    "order": 2.0,
                    "type": shared.FormFieldType.MULTIPLE_SELECT,
                    "updated_at": parse_datetime("2024-02-22T05:07:40.255Z"),
                },
                {
                    "created_at": parse_datetime("2023-10-05T21:34:29.094Z"),
                    "description": "Sequi antea delectatio.",
                    "id": "e45efb8f-439b-40f6-8370-99c8ec66b065",
                    "is_active": True,
                    "is_required": False,
                    "name": "comburo utique ipsa",
                    "order": 3.0,
                    "type": shared.FormFieldType.TEXTAREA,
                    "updated_at": parse_datetime("2024-11-15T08:08:38.121Z"),
                },
            ],
            "has_multiple_submissions": False,
            "has_progress_bar": False,
            "has_shuffle_questions": True,
            "id": "d66b2dac-71cd-4252-af7e-6694b58bc863",
            "is_active": False,
            "name": "voluptatibus omnis audax Form",
            "published_url": "https://impartial-institute.org/",
            "response_count": 423.0,
            "updated_at": parse_datetime("2024-08-15T10:54:33.255Z"),
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