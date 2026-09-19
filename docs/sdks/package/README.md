# Package

## Overview

### Available Operations

* [create_assessment_package](#create_assessment_package) - Create an assessment package
* [get_assessment_package](#get_assessment_package) - Get an assessment package
* [get_verification_package](#get_verification_package) - Retrieve a package
* [list_assessment_packages](#list_assessment_packages) - List assessment packages
* [list_verification_packages](#list_verification_packages) - List all packages
* [patch_assessment_package](#patch_assessment_package) - Update an assessment package
* [remove_assessment_package](#remove_assessment_package) - Delete an assessment package
* [update_assessment_package](#update_assessment_package) - Update an assessment package

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

    res = unified_to.package.create_assessment_package(request={
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

    res = unified_to.package.get_assessment_package(request={
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

## get_verification_package

Retrieve a package

### Example Usage

<!-- UsageSnippet language="python" operationID="getVerificationPackage" method="get" path="/verification/{connection_id}/package/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.package.get_verification_package(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.verification_package is not None

    # Handle response
    print(res.verification_package)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetVerificationPackageRequest](../../models/operations/getverificationpackagerequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.GetVerificationPackageResponse](../../models/operations/getverificationpackageresponse.md)**

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

    res = unified_to.package.list_assessment_packages(request={
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

## list_verification_packages

List all packages

### Example Usage

<!-- UsageSnippet language="python" operationID="listVerificationPackages" method="get" path="/verification/{connection_id}/package" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.package.list_verification_packages(request={
        "connection_id": "<id>",
    })

    assert res.verification_packages is not None

    # Handle response
    print(res.verification_packages)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListVerificationPackagesRequest](../../models/operations/listverificationpackagesrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.ListVerificationPackagesResponse](../../models/operations/listverificationpackagesresponse.md)**

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

    res = unified_to.package.patch_assessment_package(request={
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

    res = unified_to.package.remove_assessment_package(request={
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

    res = unified_to.package.update_assessment_package(request={
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