# Profile

## Overview

### Available Operations

* [create_cdp_profile](#create_cdp_profile) - Create a profile
* [get_cdp_profile](#get_cdp_profile) - Retrieve a profile
* [list_cdp_profiles](#list_cdp_profiles) - List all profiles
* [patch_cdp_profile](#patch_cdp_profile) - Update a profile
* [remove_cdp_profile](#remove_cdp_profile) - Remove a profile
* [update_cdp_profile](#update_cdp_profile) - Update a profile

## create_cdp_profile

Create a profile

### Example Usage

<!-- UsageSnippet language="python" operationID="createCdpProfile" method="post" path="/cdp/{connection_id}/profile" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.profile.create_cdp_profile(request={
        "cdp_profile": {},
        "connection_id": "<id>",
    })

    assert res.cdp_profile is not None

    # Handle response
    print(res.cdp_profile)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateCdpProfileRequest](../../models/operations/createcdpprofilerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreateCdpProfileResponse](../../models/operations/createcdpprofileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_cdp_profile

Retrieve a profile

### Example Usage

<!-- UsageSnippet language="python" operationID="getCdpProfile" method="get" path="/cdp/{connection_id}/profile/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.profile.get_cdp_profile(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_profile is not None

    # Handle response
    print(res.cdp_profile)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetCdpProfileRequest](../../models/operations/getcdpprofilerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetCdpProfileResponse](../../models/operations/getcdpprofileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_cdp_profiles

List all profiles

### Example Usage

<!-- UsageSnippet language="python" operationID="listCdpProfiles" method="get" path="/cdp/{connection_id}/profile" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.profile.list_cdp_profiles(request={
        "connection_id": "<id>",
    })

    assert res.cdp_profiles is not None

    # Handle response
    print(res.cdp_profiles)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListCdpProfilesRequest](../../models/operations/listcdpprofilesrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListCdpProfilesResponse](../../models/operations/listcdpprofilesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_cdp_profile

Update a profile

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCdpProfile" method="patch" path="/cdp/{connection_id}/profile/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.profile.patch_cdp_profile(request={
        "cdp_profile": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_profile is not None

    # Handle response
    print(res.cdp_profile)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchCdpProfileRequest](../../models/operations/patchcdpprofilerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchCdpProfileResponse](../../models/operations/patchcdpprofileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_cdp_profile

Remove a profile

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCdpProfile" method="delete" path="/cdp/{connection_id}/profile/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.profile.remove_cdp_profile(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.RemoveCdpProfileRequest](../../models/operations/removecdpprofilerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemoveCdpProfileResponse](../../models/operations/removecdpprofileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_cdp_profile

Update a profile

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCdpProfile" method="put" path="/cdp/{connection_id}/profile/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.profile.update_cdp_profile(request={
        "cdp_profile": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_profile is not None

    # Handle response
    print(res.cdp_profile)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateCdpProfileRequest](../../models/operations/updatecdpprofilerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdateCdpProfileResponse](../../models/operations/updatecdpprofileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |