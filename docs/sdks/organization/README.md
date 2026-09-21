# Organization

## Overview

### Available Operations

* [create_ads_organization](#create_ads_organization) - Create an organization
* [create_genai_organization](#create_genai_organization) - Create an organization
* [create_repo_organization](#create_repo_organization) - Create an organization
* [get_accounting_organization](#get_accounting_organization) - Retrieve an organization
* [get_ads_organization](#get_ads_organization) - Retrieve an organization
* [get_genai_organization](#get_genai_organization) - Retrieve an organization
* [get_repo_organization](#get_repo_organization) - Retrieve an organization
* [list_accounting_organizations](#list_accounting_organizations) - List all organizations
* [list_ads_organizations](#list_ads_organizations) - List all organizations
* [list_genai_organizations](#list_genai_organizations) - List all organizations
* [list_repo_organizations](#list_repo_organizations) - List all organizations
* [patch_ads_organization](#patch_ads_organization) - Update an organization
* [patch_genai_organization](#patch_genai_organization) - Update an organization
* [patch_repo_organization](#patch_repo_organization) - Update an organization
* [remove_ads_organization](#remove_ads_organization) - Remove an organization
* [remove_genai_organization](#remove_genai_organization) - Remove an organization
* [remove_repo_organization](#remove_repo_organization) - Remove an organization
* [update_ads_organization](#update_ads_organization) - Update an organization
* [update_genai_organization](#update_genai_organization) - Update an organization
* [update_repo_organization](#update_repo_organization) - Update an organization

## create_ads_organization

Create an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="createAdsOrganization" method="post" path="/ads/{connection_id}/organization" example="ads_organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.organization.create_ads_organization(request={
        "ads_organization": {
            "account_number": "LQUJx8zQBW",
            "created_at": parse_datetime("2020-07-23T21:47:11.440Z"),
            "currency": "USD",
            "id": "7aa99529-0bf9-46b7-8885-0326ecbc4707",
            "managers": [
                {
                    "id": "e4fd87df-9f8b-4fa0-a77b-b7d18669e350",
                    "name": "Parker, Leannon and Gibson",
                },
            ],
            "name": "Ankunding Inc",
            "status": shared.AdsOrganizationStatus.PROCESSING,
            "timezone": "Europe/Chisinau",
            "updated_at": parse_datetime("2026-03-01T15:36:04.753Z"),
        },
        "connection_id": "<id>",
    })

    assert res.ads_organization is not None

    # Handle response
    print(res.ads_organization)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateAdsOrganizationRequest](../../models/operations/createadsorganizationrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateAdsOrganizationResponse](../../models/operations/createadsorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_genai_organization

Create an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="createGenaiOrganization" method="post" path="/genai/{connection_id}/organization" example="genai_organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.organization.create_genai_organization(request={
        "genai_organization": {
            "created_at": parse_datetime("2020-10-27T16:03:47.122Z"),
            "description": "Voluptates abeo subseco.",
            "id": "c6b6737d-7782-41e3-a20e-674fb9c33d86",
            "is_active": False,
            "name": "officially about",
            "updated_at": parse_datetime("2023-01-15T02:14:43.003Z"),
        },
        "connection_id": "<id>",
    })

    assert res.genai_organization is not None

    # Handle response
    print(res.genai_organization)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateGenaiOrganizationRequest](../../models/operations/creategenaiorganizationrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateGenaiOrganizationResponse](../../models/operations/creategenaiorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_repo_organization

Create an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="createRepoOrganization" method="post" path="/repo/{connection_id}/organization" example="repo_organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.organization.create_repo_organization(request={
        "repo_organization": {
            "avatar_url": "https://picsum.photos/seed/fGl6Lb/3157/3173",
            "created_at": parse_datetime("2022-07-07T00:18:40.748Z"),
            "description": "Trepide defendo supra testimonium ager.",
            "id": "e5e80293-ffea-4c50-8f72-f34ace46e72d",
            "name": "Denesik - Lemke",
            "updated_at": parse_datetime("2023-08-13T17:10:28.255Z"),
            "web_url": "https://turbulent-overheard.biz",
        },
        "connection_id": "<id>",
    })

    assert res.repo_organization is not None

    # Handle response
    print(res.repo_organization)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateRepoOrganizationRequest](../../models/operations/createrepoorganizationrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.CreateRepoOrganizationResponse](../../models/operations/createrepoorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_organization

Retrieve an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingOrganization" method="get" path="/accounting/{connection_id}/organization/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.organization.get_accounting_organization(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_organization is not None

    # Handle response
    print(res.accounting_organization)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetAccountingOrganizationRequest](../../models/operations/getaccountingorganizationrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.GetAccountingOrganizationResponse](../../models/operations/getaccountingorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ads_organization

Retrieve an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="getAdsOrganization" method="get" path="/ads/{connection_id}/organization/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.organization.get_ads_organization(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_organization is not None

    # Handle response
    print(res.ads_organization)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAdsOrganizationRequest](../../models/operations/getadsorganizationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetAdsOrganizationResponse](../../models/operations/getadsorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_genai_organization

Retrieve an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="getGenaiOrganization" method="get" path="/genai/{connection_id}/organization/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.organization.get_genai_organization(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_organization is not None

    # Handle response
    print(res.genai_organization)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetGenaiOrganizationRequest](../../models/operations/getgenaiorganizationrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetGenaiOrganizationResponse](../../models/operations/getgenaiorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_repo_organization

Retrieve an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="getRepoOrganization" method="get" path="/repo/{connection_id}/organization/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.organization.get_repo_organization(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_organization is not None

    # Handle response
    print(res.repo_organization)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetRepoOrganizationRequest](../../models/operations/getrepoorganizationrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetRepoOrganizationResponse](../../models/operations/getrepoorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_organizations

List all organizations

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingOrganizations" method="get" path="/accounting/{connection_id}/organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.organization.list_accounting_organizations(request={
        "connection_id": "<id>",
    })

    assert res.accounting_organizations is not None

    # Handle response
    print(res.accounting_organizations)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.ListAccountingOrganizationsRequest](../../models/operations/listaccountingorganizationsrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.ListAccountingOrganizationsResponse](../../models/operations/listaccountingorganizationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ads_organizations

List all organizations

### Example Usage

<!-- UsageSnippet language="python" operationID="listAdsOrganizations" method="get" path="/ads/{connection_id}/organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.organization.list_ads_organizations(request={
        "connection_id": "<id>",
    })

    assert res.ads_organizations is not None

    # Handle response
    print(res.ads_organizations)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListAdsOrganizationsRequest](../../models/operations/listadsorganizationsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListAdsOrganizationsResponse](../../models/operations/listadsorganizationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_genai_organizations

List all organizations

### Example Usage

<!-- UsageSnippet language="python" operationID="listGenaiOrganizations" method="get" path="/genai/{connection_id}/organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.organization.list_genai_organizations(request={
        "connection_id": "<id>",
    })

    assert res.genai_organizations is not None

    # Handle response
    print(res.genai_organizations)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListGenaiOrganizationsRequest](../../models/operations/listgenaiorganizationsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListGenaiOrganizationsResponse](../../models/operations/listgenaiorganizationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_repo_organizations

List all organizations

### Example Usage

<!-- UsageSnippet language="python" operationID="listRepoOrganizations" method="get" path="/repo/{connection_id}/organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.organization.list_repo_organizations(request={
        "connection_id": "<id>",
    })

    assert res.repo_organizations is not None

    # Handle response
    print(res.repo_organizations)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListRepoOrganizationsRequest](../../models/operations/listrepoorganizationsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListRepoOrganizationsResponse](../../models/operations/listrepoorganizationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ads_organization

Update an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAdsOrganization" method="patch" path="/ads/{connection_id}/organization/{id}" example="ads_organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.organization.patch_ads_organization(request={
        "ads_organization": {
            "account_number": "LQUJx8zQBW",
            "created_at": parse_datetime("2020-07-23T21:47:11.440Z"),
            "currency": "USD",
            "id": "efbf089b-dc01-4dbe-bdc5-3d5f86e0b1c3",
            "managers": [
                {
                    "id": "e4fd87df-9f8b-4fa0-a77b-b7d18669e350",
                    "name": "Parker, Leannon and Gibson",
                },
            ],
            "name": "Ankunding Inc",
            "status": shared.AdsOrganizationStatus.PROCESSING,
            "timezone": "Europe/Chisinau",
            "updated_at": parse_datetime("2026-03-01T15:36:04.765Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_organization is not None

    # Handle response
    print(res.ads_organization)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchAdsOrganizationRequest](../../models/operations/patchadsorganizationrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchAdsOrganizationResponse](../../models/operations/patchadsorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_genai_organization

Update an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="patchGenaiOrganization" method="patch" path="/genai/{connection_id}/organization/{id}" example="genai_organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.organization.patch_genai_organization(request={
        "genai_organization": {
            "created_at": parse_datetime("2020-10-27T16:03:47.122Z"),
            "description": "Voluptates abeo subseco.",
            "id": "e466e490-09c0-476e-9a38-d324960c1635",
            "is_active": False,
            "name": "officially about",
            "updated_at": parse_datetime("2023-01-15T02:14:43.005Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_organization is not None

    # Handle response
    print(res.genai_organization)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchGenaiOrganizationRequest](../../models/operations/patchgenaiorganizationrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchGenaiOrganizationResponse](../../models/operations/patchgenaiorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_repo_organization

Update an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="patchRepoOrganization" method="patch" path="/repo/{connection_id}/organization/{id}" example="repo_organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.organization.patch_repo_organization(request={
        "repo_organization": {
            "avatar_url": "https://picsum.photos/seed/fGl6Lb/3157/3173",
            "created_at": parse_datetime("2022-07-07T00:18:40.748Z"),
            "description": "Trepide defendo supra testimonium ager.",
            "id": "2c0e48fb-7221-429b-aeed-0a403672f821",
            "name": "Denesik - Lemke",
            "updated_at": parse_datetime("2023-08-13T17:10:28.257Z"),
            "web_url": "https://turbulent-overheard.biz",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_organization is not None

    # Handle response
    print(res.repo_organization)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PatchRepoOrganizationRequest](../../models/operations/patchrepoorganizationrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.PatchRepoOrganizationResponse](../../models/operations/patchrepoorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ads_organization

Remove an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAdsOrganization" method="delete" path="/ads/{connection_id}/organization/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.organization.remove_ads_organization(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RemoveAdsOrganizationRequest](../../models/operations/removeadsorganizationrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveAdsOrganizationResponse](../../models/operations/removeadsorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_genai_organization

Remove an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="removeGenaiOrganization" method="delete" path="/genai/{connection_id}/organization/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.organization.remove_genai_organization(request={
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
| `request`                                                                                              | [operations.RemoveGenaiOrganizationRequest](../../models/operations/removegenaiorganizationrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveGenaiOrganizationResponse](../../models/operations/removegenaiorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_repo_organization

Remove an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="removeRepoOrganization" method="delete" path="/repo/{connection_id}/organization/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.organization.remove_repo_organization(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.RemoveRepoOrganizationRequest](../../models/operations/removerepoorganizationrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.RemoveRepoOrganizationResponse](../../models/operations/removerepoorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ads_organization

Update an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAdsOrganization" method="put" path="/ads/{connection_id}/organization/{id}" example="ads_organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.organization.update_ads_organization(request={
        "ads_organization": {
            "account_number": "LQUJx8zQBW",
            "created_at": parse_datetime("2020-07-23T21:47:11.440Z"),
            "currency": "USD",
            "id": "efbf089b-dc01-4dbe-bdc5-3d5f86e0b1c3",
            "managers": [
                {
                    "id": "e4fd87df-9f8b-4fa0-a77b-b7d18669e350",
                    "name": "Parker, Leannon and Gibson",
                },
            ],
            "name": "Ankunding Inc",
            "status": shared.AdsOrganizationStatus.PROCESSING,
            "timezone": "Europe/Chisinau",
            "updated_at": parse_datetime("2026-03-01T15:36:04.765Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_organization is not None

    # Handle response
    print(res.ads_organization)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateAdsOrganizationRequest](../../models/operations/updateadsorganizationrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateAdsOrganizationResponse](../../models/operations/updateadsorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_genai_organization

Update an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="updateGenaiOrganization" method="put" path="/genai/{connection_id}/organization/{id}" example="genai_organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.organization.update_genai_organization(request={
        "genai_organization": {
            "created_at": parse_datetime("2020-10-27T16:03:47.122Z"),
            "description": "Voluptates abeo subseco.",
            "id": "e466e490-09c0-476e-9a38-d324960c1635",
            "is_active": False,
            "name": "officially about",
            "updated_at": parse_datetime("2023-01-15T02:14:43.005Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_organization is not None

    # Handle response
    print(res.genai_organization)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateGenaiOrganizationRequest](../../models/operations/updategenaiorganizationrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateGenaiOrganizationResponse](../../models/operations/updategenaiorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_repo_organization

Update an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="updateRepoOrganization" method="put" path="/repo/{connection_id}/organization/{id}" example="repo_organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.organization.update_repo_organization(request={
        "repo_organization": {
            "avatar_url": "https://picsum.photos/seed/fGl6Lb/3157/3173",
            "created_at": parse_datetime("2022-07-07T00:18:40.748Z"),
            "description": "Trepide defendo supra testimonium ager.",
            "id": "2c0e48fb-7221-429b-aeed-0a403672f821",
            "name": "Denesik - Lemke",
            "updated_at": parse_datetime("2023-08-13T17:10:28.257Z"),
            "web_url": "https://turbulent-overheard.biz",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_organization is not None

    # Handle response
    print(res.repo_organization)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdateRepoOrganizationRequest](../../models/operations/updaterepoorganizationrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.UpdateRepoOrganizationResponse](../../models/operations/updaterepoorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |