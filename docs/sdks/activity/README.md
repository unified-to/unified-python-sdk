# Activity

## Overview

### Available Operations

* [create_ats_activity](#create_ats_activity) - Create an activity
* [create_lms_activity](#create_lms_activity) - Create an activity
* [get_ats_activity](#get_ats_activity) - Retrieve an activity
* [get_clubs_activity](#get_clubs_activity) - Retrieve an activity
* [get_lms_activity](#get_lms_activity) - Retrieve an activity
* [list_ats_activities](#list_ats_activities) - List all activities
* [list_clubs_activities](#list_clubs_activities) - List all activities
* [list_lms_activities](#list_lms_activities) - List all activities
* [patch_ats_activity](#patch_ats_activity) - Update an activity
* [patch_lms_activity](#patch_lms_activity) - Update an activity
* [remove_ats_activity](#remove_ats_activity) - Remove an activity
* [remove_lms_activity](#remove_lms_activity) - Remove an activity
* [update_ats_activity](#update_ats_activity) - Update an activity
* [update_lms_activity](#update_lms_activity) - Update an activity

## create_ats_activity

Create an activity

### Example Usage

<!-- UsageSnippet language="python" operationID="createAtsActivity" method="post" path="/ats/{connection_id}/activity" example="ats_activity" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.activity.create_ats_activity(request={
        "ats_activity": {
            "bcc": [
                {
                    "email": "Mabel_Schuppe-Schowalter42@hotmail.com",
                    "name": "Rochelle Franey-Bechtelar",
                    "type": shared.AtsEmailType.HOME,
                },
            ],
            "cc": [
                {
                    "email": "Sasha24@hotmail.com",
                    "name": "Dr. Elbert Kuvalis",
                    "type": shared.AtsEmailType.HOME,
                },
                {
                    "email": "Rosetta_Donnelly@gmail.com",
                    "name": "Ramon Daniel",
                    "type": shared.AtsEmailType.OTHER,
                },
                {
                    "email": "Kathryne_Jast@yahoo.com",
                    "name": "Christian Jacobson",
                    "type": shared.AtsEmailType.OTHER,
                },
                {
                    "email": "Eldred95@yahoo.com",
                    "name": "Edna Bogan",
                    "type": shared.AtsEmailType.OTHER,
                },
            ],
            "created_at": parse_datetime("2022-08-07T03:16:43.865Z"),
            "description": "Amplus.",
            "from_": {
                "email": "Norwood.Wiza47@yahoo.com",
                "name": "Toby Grant",
                "type": shared.PropertyAtsActivityFromType.OTHER,
            },
            "id": "6be4b122-76fb-4cad-84d5-335d82ccd2ed",
            "is_private": False,
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "7954f594-97a3-4e21-8800-5d0be0b77840",
                    "namespace": "activity",
                    "slug": "acer",
                    "value": "Pauci eius cena adamo summisse arguo pectus communis arcesso tergeo.",
                },
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "9d7a338d-2cd7-4f69-9e18-04b15da8c838",
                    "namespace": "activity",
                    "slug": "tremo",
                    "value": "Amita delectus dicta temptatio utroque ex.",
                },
            ],
            "sub_type": "TASK",
            "title": "Senior Interactions Manager",
            "to": [
                {
                    "email": "Sister91@hotmail.com",
                    "name": "Eddie Nienow PhD",
                    "type": shared.AtsEmailType.WORK,
                },
            ],
            "type": shared.AtsActivityType.TASK,
            "updated_at": parse_datetime("2026-03-26T13:56:55.214Z"),
        },
        "connection_id": "<id>",
    })

    assert res.ats_activity is not None

    # Handle response
    print(res.ats_activity)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateAtsActivityRequest](../../models/operations/createatsactivityrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateAtsActivityResponse](../../models/operations/createatsactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_lms_activity

Create an activity

### Example Usage

<!-- UsageSnippet language="python" operationID="createLmsActivity" method="post" path="/lms/{connection_id}/activity" example="lms_activity" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.activity.create_lms_activity(request={
        "lms_activity": {
            "assigned_grade": "summopere",
            "completed_at": parse_datetime("2025-04-23T20:07:20.202Z"),
            "created_at": parse_datetime("2020-10-17T01:25:21.745Z"),
            "duration_minutes": 55.0,
            "id": "c74a1c6c-6830-4491-b2e3-58dd58a94c5a",
            "is_completed": True,
            "progress_percentage": 100.0,
            "started_at": parse_datetime("2023-12-24T04:54:05.825Z"),
            "updated_at": parse_datetime("2022-01-28T20:13:19.234Z"),
        },
        "connection_id": "<id>",
    })

    assert res.lms_activity is not None

    # Handle response
    print(res.lms_activity)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateLmsActivityRequest](../../models/operations/createlmsactivityrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateLmsActivityResponse](../../models/operations/createlmsactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ats_activity

Retrieve an activity

### Example Usage

<!-- UsageSnippet language="python" operationID="getAtsActivity" method="get" path="/ats/{connection_id}/activity/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.activity.get_ats_activity(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_activity is not None

    # Handle response
    print(res.ats_activity)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetAtsActivityRequest](../../models/operations/getatsactivityrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetAtsActivityResponse](../../models/operations/getatsactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_clubs_activity

Retrieve an activity

### Example Usage

<!-- UsageSnippet language="python" operationID="getClubsActivity" method="get" path="/clubs/{connection_id}/activity/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.activity.get_clubs_activity(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.clubs_activity is not None

    # Handle response
    print(res.clubs_activity)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetClubsActivityRequest](../../models/operations/getclubsactivityrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetClubsActivityResponse](../../models/operations/getclubsactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_lms_activity

Retrieve an activity

### Example Usage

<!-- UsageSnippet language="python" operationID="getLmsActivity" method="get" path="/lms/{connection_id}/activity/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.activity.get_lms_activity(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_activity is not None

    # Handle response
    print(res.lms_activity)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetLmsActivityRequest](../../models/operations/getlmsactivityrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetLmsActivityResponse](../../models/operations/getlmsactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ats_activities

List all activities

### Example Usage

<!-- UsageSnippet language="python" operationID="listAtsActivities" method="get" path="/ats/{connection_id}/activity" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.activity.list_ats_activities(request={
        "connection_id": "<id>",
    })

    assert res.ats_activities is not None

    # Handle response
    print(res.ats_activities)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListAtsActivitiesRequest](../../models/operations/listatsactivitiesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListAtsActivitiesResponse](../../models/operations/listatsactivitiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_clubs_activities

List all activities

### Example Usage

<!-- UsageSnippet language="python" operationID="listClubsActivities" method="get" path="/clubs/{connection_id}/activity" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.activity.list_clubs_activities(request={
        "connection_id": "<id>",
    })

    assert res.clubs_activities is not None

    # Handle response
    print(res.clubs_activities)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListClubsActivitiesRequest](../../models/operations/listclubsactivitiesrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListClubsActivitiesResponse](../../models/operations/listclubsactivitiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_lms_activities

List all activities

### Example Usage

<!-- UsageSnippet language="python" operationID="listLmsActivities" method="get" path="/lms/{connection_id}/activity" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.activity.list_lms_activities(request={
        "connection_id": "<id>",
    })

    assert res.lms_activities is not None

    # Handle response
    print(res.lms_activities)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListLmsActivitiesRequest](../../models/operations/listlmsactivitiesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListLmsActivitiesResponse](../../models/operations/listlmsactivitiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ats_activity

Update an activity

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAtsActivity" method="patch" path="/ats/{connection_id}/activity/{id}" example="ats_activity" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.activity.patch_ats_activity(request={
        "ats_activity": {
            "bcc": [
                {
                    "email": "Mabel_Schuppe-Schowalter42@hotmail.com",
                    "name": "Rochelle Franey-Bechtelar",
                    "type": shared.AtsEmailType.HOME,
                },
            ],
            "cc": [
                {
                    "email": "Sasha24@hotmail.com",
                    "name": "Dr. Elbert Kuvalis",
                    "type": shared.AtsEmailType.HOME,
                },
                {
                    "email": "Rosetta_Donnelly@gmail.com",
                    "name": "Ramon Daniel",
                    "type": shared.AtsEmailType.OTHER,
                },
                {
                    "email": "Kathryne_Jast@yahoo.com",
                    "name": "Christian Jacobson",
                    "type": shared.AtsEmailType.OTHER,
                },
                {
                    "email": "Eldred95@yahoo.com",
                    "name": "Edna Bogan",
                    "type": shared.AtsEmailType.OTHER,
                },
            ],
            "created_at": parse_datetime("2022-08-07T03:16:43.865Z"),
            "description": "Amplus.",
            "from_": {
                "email": "Norwood.Wiza47@yahoo.com",
                "name": "Toby Grant",
                "type": shared.PropertyAtsActivityFromType.OTHER,
            },
            "id": "e636b4b1-e83d-4f0f-acf2-47f3c66decae",
            "is_private": False,
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "ae84be1e-6cf7-4196-9c09-889abd2e3fdc",
                    "namespace": "activity",
                    "slug": "acer",
                    "value": "Pauci eius cena adamo summisse arguo pectus communis arcesso tergeo.",
                },
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "7b63204a-0b7e-4486-817b-e8b1e5c85692",
                    "namespace": "activity",
                    "slug": "tremo",
                    "value": "Amita delectus dicta temptatio utroque ex.",
                },
            ],
            "sub_type": "TASK",
            "title": "Senior Interactions Manager",
            "to": [
                {
                    "email": "Sister91@hotmail.com",
                    "name": "Eddie Nienow PhD",
                    "type": shared.AtsEmailType.WORK,
                },
            ],
            "type": shared.AtsActivityType.TASK,
            "updated_at": parse_datetime("2026-03-26T13:56:55.244Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_activity is not None

    # Handle response
    print(res.ats_activity)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchAtsActivityRequest](../../models/operations/patchatsactivityrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchAtsActivityResponse](../../models/operations/patchatsactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_lms_activity

Update an activity

### Example Usage

<!-- UsageSnippet language="python" operationID="patchLmsActivity" method="patch" path="/lms/{connection_id}/activity/{id}" example="lms_activity" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.activity.patch_lms_activity(request={
        "lms_activity": {
            "assigned_grade": "summopere",
            "completed_at": parse_datetime("2025-04-23T20:07:20.207Z"),
            "created_at": parse_datetime("2020-10-17T01:25:21.745Z"),
            "duration_minutes": 55.0,
            "id": "380c2529-7209-45ee-93ee-cb22fa3b39e8",
            "is_completed": True,
            "progress_percentage": 100.0,
            "started_at": parse_datetime("2023-12-24T04:54:05.825Z"),
            "updated_at": parse_datetime("2022-01-28T20:13:19.237Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_activity is not None

    # Handle response
    print(res.lms_activity)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchLmsActivityRequest](../../models/operations/patchlmsactivityrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchLmsActivityResponse](../../models/operations/patchlmsactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ats_activity

Remove an activity

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAtsActivity" method="delete" path="/ats/{connection_id}/activity/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.activity.remove_ats_activity(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveAtsActivityRequest](../../models/operations/removeatsactivityrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveAtsActivityResponse](../../models/operations/removeatsactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_lms_activity

Remove an activity

### Example Usage

<!-- UsageSnippet language="python" operationID="removeLmsActivity" method="delete" path="/lms/{connection_id}/activity/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.activity.remove_lms_activity(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveLmsActivityRequest](../../models/operations/removelmsactivityrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveLmsActivityResponse](../../models/operations/removelmsactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ats_activity

Update an activity

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAtsActivity" method="put" path="/ats/{connection_id}/activity/{id}" example="ats_activity" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.activity.update_ats_activity(request={
        "ats_activity": {
            "bcc": [
                {
                    "email": "Mabel_Schuppe-Schowalter42@hotmail.com",
                    "name": "Rochelle Franey-Bechtelar",
                    "type": shared.AtsEmailType.HOME,
                },
            ],
            "cc": [
                {
                    "email": "Sasha24@hotmail.com",
                    "name": "Dr. Elbert Kuvalis",
                    "type": shared.AtsEmailType.HOME,
                },
                {
                    "email": "Rosetta_Donnelly@gmail.com",
                    "name": "Ramon Daniel",
                    "type": shared.AtsEmailType.OTHER,
                },
                {
                    "email": "Kathryne_Jast@yahoo.com",
                    "name": "Christian Jacobson",
                    "type": shared.AtsEmailType.OTHER,
                },
                {
                    "email": "Eldred95@yahoo.com",
                    "name": "Edna Bogan",
                    "type": shared.AtsEmailType.OTHER,
                },
            ],
            "created_at": parse_datetime("2022-08-07T03:16:43.865Z"),
            "description": "Amplus.",
            "from_": {
                "email": "Norwood.Wiza47@yahoo.com",
                "name": "Toby Grant",
                "type": shared.PropertyAtsActivityFromType.OTHER,
            },
            "id": "e636b4b1-e83d-4f0f-acf2-47f3c66decae",
            "is_private": False,
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "ae84be1e-6cf7-4196-9c09-889abd2e3fdc",
                    "namespace": "activity",
                    "slug": "acer",
                    "value": "Pauci eius cena adamo summisse arguo pectus communis arcesso tergeo.",
                },
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "7b63204a-0b7e-4486-817b-e8b1e5c85692",
                    "namespace": "activity",
                    "slug": "tremo",
                    "value": "Amita delectus dicta temptatio utroque ex.",
                },
            ],
            "sub_type": "TASK",
            "title": "Senior Interactions Manager",
            "to": [
                {
                    "email": "Sister91@hotmail.com",
                    "name": "Eddie Nienow PhD",
                    "type": shared.AtsEmailType.WORK,
                },
            ],
            "type": shared.AtsActivityType.TASK,
            "updated_at": parse_datetime("2026-03-26T13:56:55.244Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_activity is not None

    # Handle response
    print(res.ats_activity)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateAtsActivityRequest](../../models/operations/updateatsactivityrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateAtsActivityResponse](../../models/operations/updateatsactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_lms_activity

Update an activity

### Example Usage

<!-- UsageSnippet language="python" operationID="updateLmsActivity" method="put" path="/lms/{connection_id}/activity/{id}" example="lms_activity" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.activity.update_lms_activity(request={
        "lms_activity": {
            "assigned_grade": "summopere",
            "completed_at": parse_datetime("2025-04-23T20:07:20.207Z"),
            "created_at": parse_datetime("2020-10-17T01:25:21.745Z"),
            "duration_minutes": 55.0,
            "id": "380c2529-7209-45ee-93ee-cb22fa3b39e8",
            "is_completed": True,
            "progress_percentage": 100.0,
            "started_at": parse_datetime("2023-12-24T04:54:05.825Z"),
            "updated_at": parse_datetime("2022-01-28T20:13:19.237Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_activity is not None

    # Handle response
    print(res.lms_activity)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateLmsActivityRequest](../../models/operations/updatelmsactivityrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateLmsActivityResponse](../../models/operations/updatelmsactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |