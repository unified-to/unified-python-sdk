# Assessment

## Overview

### Available Operations

* [create_assessment_order](#create_assessment_order) - Create an order
* [create_assessment_package](#create_assessment_package) - Create an assessment package
* [get_assessment_order](#get_assessment_order) - Retrieve an order
* [get_assessment_package](#get_assessment_package) - Get an assessment package
* [list_assessment_packages](#list_assessment_packages) - List assessment packages
* [patch_assessment_order](#patch_assessment_order) - Update an order
* [patch_assessment_package](#patch_assessment_package) - Update an assessment package
* [remove_assessment_package](#remove_assessment_package) - Delete an assessment package
* [update_assessment_order](#update_assessment_order) - Update an order
* [update_assessment_package](#update_assessment_package) - Update an assessment package

## create_assessment_order

Create an order

### Example Usage

<!-- UsageSnippet language="python" operationID="createAssessmentOrder" method="post" path="/assessment/{connection_id}/order" example="assessment_order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.assessment.create_assessment_order(request={
        "assessment_order": {
            "connection_id": "<id>",
            "created_at": parse_datetime("2021-09-18T10:33:57.803Z"),
            "id": "75b9083c-54f1-4b02-b8c7-84d5f2f175ac",
            "parameters": [],
            "profile_addresses": [],
            "profile_date_of_birth": "1989-07-22T16:18:37.650Z",
            "profile_emails": [
                "Cleta.Daugherty@gmail.com",
            ],
            "profile_first_name": "Amy",
            "profile_gender": shared.ProfileGender.NON_BINARY,
            "profile_last_name": "Kris-Windler",
            "profile_name": "Amy Kris-Windler",
            "profile_resume_url": "https://enchanted-cycle.biz/",
            "profile_social_media_urls": [],
            "profile_telephones": [
                "(828) 263-1594 x5248",
            ],
            "reference": "ab",
            "response_attributes": [],
            "response_details": [],
            "response_download_urls": [],
            "response_max_score": 82.0,
            "response_score": 92.0,
            "response_status": shared.ResponseStatus.FAILED,
            "response_url": "https://irresponsible-trench.info/",
            "status": shared.AssessmentOrderStatus.REJECTED,
            "target_url": "https://cautious-turret.info",
            "updated_at": parse_datetime("2023-01-17T07:49:06.732Z"),
            "workspace_id": "<id>",
        },
        "connection_id": "<id>",
    })

    assert res.assessment_order is not None

    # Handle response
    print(res.assessment_order)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateAssessmentOrderRequest](../../models/operations/createassessmentorderrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateAssessmentOrderResponse](../../models/operations/createassessmentorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_assessment_package

Create an assessment package

### Example Usage

<!-- UsageSnippet language="python" operationID="createAssessmentPackage" method="post" path="/assessment/{connection_id}/package" example="assessment_package" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.assessment.create_assessment_package(request={
        "assessment_package": {
            "aliases": [
                "quia",
            ],
            "created_at": parse_datetime("2022-11-18T19:48:39.433Z"),
            "description": "Eos aedificium consectetur urbs. Admitto summa accusator tabesco distinctio vapulus culpo templum ancilla.",
            "has_redirect_url": True,
            "has_target_url": False,
            "id": "433a8200-4753-4c77-9162-8da12af89693",
            "info_url": "https://ugly-instance.biz/",
            "integration_types": [
                "viridis",
            ],
            "max_score": 22.0,
            "name": "Carus sed vox doloremque vigor surgo tabella cupiditas abduco clarus.",
            "needs_ip_address": True,
            "parameters": [],
            "regions": [],
            "tags": [
                "clamo",
            ],
            "type": shared.AssessmentPackageType.VIDEO_INTERVIEW,
            "updated_at": parse_datetime("2023-09-18T10:20:01.019Z"),
        },
        "connection_id": "<id>",
    })

    assert res.assessment_package is not None

    # Handle response
    print(res.assessment_package)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAssessmentPackageRequest](../../models/operations/createassessmentpackagerequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateAssessmentPackageResponse](../../models/operations/createassessmentpackageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_assessment_order

Retrieve an order

### Example Usage

<!-- UsageSnippet language="python" operationID="getAssessmentOrder" method="get" path="/assessment/{connection_id}/order/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.assessment.get_assessment_order(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.assessment_order is not None

    # Handle response
    print(res.assessment_order)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAssessmentOrderRequest](../../models/operations/getassessmentorderrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetAssessmentOrderResponse](../../models/operations/getassessmentorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_assessment_package

Get an assessment package

### Example Usage

<!-- UsageSnippet language="python" operationID="getAssessmentPackage" method="get" path="/assessment/{connection_id}/package/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.assessment.get_assessment_package(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.assessment_package is not None

    # Handle response
    print(res.assessment_package)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAssessmentPackageRequest](../../models/operations/getassessmentpackagerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetAssessmentPackageResponse](../../models/operations/getassessmentpackageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_assessment_packages

List assessment packages

### Example Usage

<!-- UsageSnippet language="python" operationID="listAssessmentPackages" method="get" path="/assessment/{connection_id}/package" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.assessment.list_assessment_packages(request={
        "connection_id": "<id>",
    })

    assert res.assessment_packages is not None

    # Handle response
    print(res.assessment_packages)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAssessmentPackagesRequest](../../models/operations/listassessmentpackagesrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListAssessmentPackagesResponse](../../models/operations/listassessmentpackagesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_assessment_order

Update an order

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAssessmentOrder" method="patch" path="/assessment/{connection_id}/order/{id}" example="assessment_order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.assessment.patch_assessment_order(request={
        "assessment_order": {
            "connection_id": "<id>",
            "created_at": parse_datetime("2021-09-18T10:33:57.803Z"),
            "id": "e54ed0f8-45d9-4a44-8229-a457d8684592",
            "parameters": [],
            "profile_addresses": [],
            "profile_date_of_birth": "1989-07-22T16:18:37.650Z",
            "profile_emails": [
                "Cleta.Daugherty@gmail.com",
            ],
            "profile_first_name": "Amy",
            "profile_gender": shared.ProfileGender.NON_BINARY,
            "profile_last_name": "Kris-Windler",
            "profile_name": "Amy Kris-Windler",
            "profile_resume_url": "https://enchanted-cycle.biz/",
            "profile_social_media_urls": [],
            "profile_telephones": [
                "(828) 263-1594 x5248",
            ],
            "reference": "ab",
            "response_attributes": [],
            "response_details": [],
            "response_download_urls": [],
            "response_max_score": 82.0,
            "response_score": 92.0,
            "response_status": shared.ResponseStatus.FAILED,
            "response_url": "https://irresponsible-trench.info/",
            "status": shared.AssessmentOrderStatus.REJECTED,
            "target_url": "https://cautious-turret.info",
            "updated_at": parse_datetime("2023-01-17T07:49:06.745Z"),
            "workspace_id": "<id>",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.assessment_order is not None

    # Handle response
    print(res.assessment_order)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchAssessmentOrderRequest](../../models/operations/patchassessmentorderrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchAssessmentOrderResponse](../../models/operations/patchassessmentorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_assessment_package

Update an assessment package

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAssessmentPackage" method="patch" path="/assessment/{connection_id}/package/{id}" example="assessment_package" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.assessment.patch_assessment_package(request={
        "assessment_package": {
            "aliases": [
                "quia",
            ],
            "created_at": parse_datetime("2022-11-18T19:48:39.433Z"),
            "description": "Eos aedificium consectetur urbs. Admitto summa accusator tabesco distinctio vapulus culpo templum ancilla.",
            "has_redirect_url": True,
            "has_target_url": False,
            "id": "9947de10-865c-437e-bf8b-7f5b15acefec",
            "info_url": "https://ugly-instance.biz/",
            "integration_types": [
                "viridis",
            ],
            "max_score": 22.0,
            "name": "Carus sed vox doloremque vigor surgo tabella cupiditas abduco clarus.",
            "needs_ip_address": True,
            "parameters": [],
            "regions": [],
            "tags": [
                "clamo",
            ],
            "type": shared.AssessmentPackageType.VIDEO_INTERVIEW,
            "updated_at": parse_datetime("2023-09-18T10:20:01.024Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.assessment_package is not None

    # Handle response
    print(res.assessment_package)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchAssessmentPackageRequest](../../models/operations/patchassessmentpackagerequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchAssessmentPackageResponse](../../models/operations/patchassessmentpackageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_assessment_package

Delete an assessment package

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAssessmentPackage" method="delete" path="/assessment/{connection_id}/package/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.assessment.remove_assessment_package(request={
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
| `request`                                                                                              | [operations.RemoveAssessmentPackageRequest](../../models/operations/removeassessmentpackagerequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveAssessmentPackageResponse](../../models/operations/removeassessmentpackageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_assessment_order

Update an order

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAssessmentOrder" method="put" path="/assessment/{connection_id}/order/{id}" example="assessment_order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.assessment.update_assessment_order(request={
        "assessment_order": {
            "connection_id": "<id>",
            "created_at": parse_datetime("2021-09-18T10:33:57.803Z"),
            "id": "e54ed0f8-45d9-4a44-8229-a457d8684592",
            "parameters": [],
            "profile_addresses": [],
            "profile_date_of_birth": "1989-07-22T16:18:37.650Z",
            "profile_emails": [
                "Cleta.Daugherty@gmail.com",
            ],
            "profile_first_name": "Amy",
            "profile_gender": shared.ProfileGender.NON_BINARY,
            "profile_last_name": "Kris-Windler",
            "profile_name": "Amy Kris-Windler",
            "profile_resume_url": "https://enchanted-cycle.biz/",
            "profile_social_media_urls": [],
            "profile_telephones": [
                "(828) 263-1594 x5248",
            ],
            "reference": "ab",
            "response_attributes": [],
            "response_details": [],
            "response_download_urls": [],
            "response_max_score": 82.0,
            "response_score": 92.0,
            "response_status": shared.ResponseStatus.FAILED,
            "response_url": "https://irresponsible-trench.info/",
            "status": shared.AssessmentOrderStatus.REJECTED,
            "target_url": "https://cautious-turret.info",
            "updated_at": parse_datetime("2023-01-17T07:49:06.745Z"),
            "workspace_id": "<id>",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.assessment_order is not None

    # Handle response
    print(res.assessment_order)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateAssessmentOrderRequest](../../models/operations/updateassessmentorderrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateAssessmentOrderResponse](../../models/operations/updateassessmentorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_assessment_package

Update an assessment package

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAssessmentPackage" method="put" path="/assessment/{connection_id}/package/{id}" example="assessment_package" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.assessment.update_assessment_package(request={
        "assessment_package": {
            "aliases": [
                "quia",
            ],
            "created_at": parse_datetime("2022-11-18T19:48:39.433Z"),
            "description": "Eos aedificium consectetur urbs. Admitto summa accusator tabesco distinctio vapulus culpo templum ancilla.",
            "has_redirect_url": True,
            "has_target_url": False,
            "id": "9947de10-865c-437e-bf8b-7f5b15acefec",
            "info_url": "https://ugly-instance.biz/",
            "integration_types": [
                "viridis",
            ],
            "max_score": 22.0,
            "name": "Carus sed vox doloremque vigor surgo tabella cupiditas abduco clarus.",
            "needs_ip_address": True,
            "parameters": [],
            "regions": [],
            "tags": [
                "clamo",
            ],
            "type": shared.AssessmentPackageType.VIDEO_INTERVIEW,
            "updated_at": parse_datetime("2023-09-18T10:20:01.024Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.assessment_package is not None

    # Handle response
    print(res.assessment_package)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateAssessmentPackageRequest](../../models/operations/updateassessmentpackagerequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateAssessmentPackageResponse](../../models/operations/updateassessmentpackageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |