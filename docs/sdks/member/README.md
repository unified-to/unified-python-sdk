# Member

## Overview

### Available Operations

* [create_martech_member2](#create_martech_member2) - Create a member
* [get_clubs_member2](#get_clubs_member2) - Retrieve a member
* [get_martech_member2](#get_martech_member2) - Retrieve a member
* [list_clubs_members2](#list_clubs_members2) - List all members
* [list_martech_members2](#list_martech_members2) - List all members
* [patch_martech_member2](#patch_martech_member2) - Update a member
* [remove_martech_member2](#remove_martech_member2) - Remove a member
* [update_martech_member2](#update_martech_member2) - Update a member

## create_martech_member2

Create a member

### Example Usage

<!-- UsageSnippet language="python" operationID="createMartechMember2" method="post" path="/martech/{connection_id}/member" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.member.create_martech_member2(request={
        "marketing_member": {},
        "connection_id": "<id>",
    })

    assert res.marketing_member is not None

    # Handle response
    print(res.marketing_member)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateMartechMember2Request](../../models/operations/createmartechmember2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateMartechMember2Response](../../models/operations/createmartechmember2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_clubs_member2

Retrieve a member

### Example Usage

<!-- UsageSnippet language="python" operationID="getClubsMember2" method="get" path="/clubs/{connection_id}/member/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.member.get_clubs_member2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.clubs_member is not None

    # Handle response
    print(res.clubs_member)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetClubsMember2Request](../../models/operations/getclubsmember2request.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetClubsMember2Response](../../models/operations/getclubsmember2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_martech_member2

Retrieve a member

### Example Usage

<!-- UsageSnippet language="python" operationID="getMartechMember2" method="get" path="/martech/{connection_id}/member/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.member.get_martech_member2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.marketing_member is not None

    # Handle response
    print(res.marketing_member)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetMartechMember2Request](../../models/operations/getmartechmember2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetMartechMember2Response](../../models/operations/getmartechmember2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_clubs_members2

List all members

### Example Usage

<!-- UsageSnippet language="python" operationID="listClubsMembers2" method="get" path="/clubs/{connection_id}/member" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.member.list_clubs_members2(request={
        "connection_id": "<id>",
    })

    assert res.clubs_members is not None

    # Handle response
    print(res.clubs_members)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListClubsMembers2Request](../../models/operations/listclubsmembers2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListClubsMembers2Response](../../models/operations/listclubsmembers2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_martech_members2

List all members

### Example Usage

<!-- UsageSnippet language="python" operationID="listMartechMembers2" method="get" path="/martech/{connection_id}/member" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.member.list_martech_members2(request={
        "connection_id": "<id>",
    })

    assert res.marketing_members is not None

    # Handle response
    print(res.marketing_members)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListMartechMembers2Request](../../models/operations/listmartechmembers2request.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListMartechMembers2Response](../../models/operations/listmartechmembers2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_martech_member2

Update a member

### Example Usage

<!-- UsageSnippet language="python" operationID="patchMartechMember2" method="patch" path="/martech/{connection_id}/member/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.member.patch_martech_member2(request={
        "marketing_member": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.marketing_member is not None

    # Handle response
    print(res.marketing_member)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchMartechMember2Request](../../models/operations/patchmartechmember2request.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchMartechMember2Response](../../models/operations/patchmartechmember2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_martech_member2

Remove a member

### Example Usage

<!-- UsageSnippet language="python" operationID="removeMartechMember2" method="delete" path="/martech/{connection_id}/member/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.member.remove_martech_member2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RemoveMartechMember2Request](../../models/operations/removemartechmember2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.RemoveMartechMember2Response](../../models/operations/removemartechmember2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_martech_member2

Update a member

### Example Usage

<!-- UsageSnippet language="python" operationID="updateMartechMember2" method="put" path="/martech/{connection_id}/member/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.member.update_martech_member2(request={
        "marketing_member": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.marketing_member is not None

    # Handle response
    print(res.marketing_member)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateMartechMember2Request](../../models/operations/updatemartechmember2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateMartechMember2Response](../../models/operations/updatemartechmember2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |