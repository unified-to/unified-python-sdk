# Package
(*package*)

## Overview

### Available Operations

* [get_verification_package](#get_verification_package) - Retrieve a package
* [list_verification_packages](#list_verification_packages) - List all packages

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