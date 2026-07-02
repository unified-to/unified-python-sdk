# Property

## Overview

### Available Operations

* [create_analytics_property](#create_analytics_property) - Create a property
* [get_analytics_property](#get_analytics_property) - Retrieve a property
* [list_analytics_properties](#list_analytics_properties) - List all properties
* [patch_analytics_property](#patch_analytics_property) - Update a property
* [remove_analytics_property](#remove_analytics_property) - Remove a property
* [update_analytics_property](#update_analytics_property) - Update a property

## create_analytics_property

Create a property

### Example Usage

<!-- UsageSnippet language="python" operationID="createAnalyticsProperty" method="post" path="/analytics/{connection_id}/property" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.create_analytics_property(request={
        "analytics_property": {},
        "connection_id": "<id>",
    })

    assert res.analytics_property is not None

    # Handle response
    print(res.analytics_property)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAnalyticsPropertyRequest](../../models/operations/createanalyticspropertyrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateAnalyticsPropertyResponse](../../models/operations/createanalyticspropertyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_analytics_property

Retrieve a property

### Example Usage

<!-- UsageSnippet language="python" operationID="getAnalyticsProperty" method="get" path="/analytics/{connection_id}/property/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.get_analytics_property(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_property is not None

    # Handle response
    print(res.analytics_property)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAnalyticsPropertyRequest](../../models/operations/getanalyticspropertyrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetAnalyticsPropertyResponse](../../models/operations/getanalyticspropertyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_analytics_properties

List all properties

### Example Usage

<!-- UsageSnippet language="python" operationID="listAnalyticsProperties" method="get" path="/analytics/{connection_id}/property" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.list_analytics_properties(request={
        "connection_id": "<id>",
    })

    assert res.analytics_properties is not None

    # Handle response
    print(res.analytics_properties)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListAnalyticsPropertiesRequest](../../models/operations/listanalyticspropertiesrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.ListAnalyticsPropertiesResponse](../../models/operations/listanalyticspropertiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_analytics_property

Update a property

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAnalyticsProperty" method="patch" path="/analytics/{connection_id}/property/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.patch_analytics_property(request={
        "analytics_property": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_property is not None

    # Handle response
    print(res.analytics_property)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchAnalyticsPropertyRequest](../../models/operations/patchanalyticspropertyrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchAnalyticsPropertyResponse](../../models/operations/patchanalyticspropertyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_analytics_property

Remove a property

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAnalyticsProperty" method="delete" path="/analytics/{connection_id}/property/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.remove_analytics_property(request={
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
| `request`                                                                                              | [operations.RemoveAnalyticsPropertyRequest](../../models/operations/removeanalyticspropertyrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveAnalyticsPropertyResponse](../../models/operations/removeanalyticspropertyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_analytics_property

Update a property

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAnalyticsProperty" method="put" path="/analytics/{connection_id}/property/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.update_analytics_property(request={
        "analytics_property": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_property is not None

    # Handle response
    print(res.analytics_property)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateAnalyticsPropertyRequest](../../models/operations/updateanalyticspropertyrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateAnalyticsPropertyResponse](../../models/operations/updateanalyticspropertyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |