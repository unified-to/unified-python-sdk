# Template

## Overview

### Available Operations

* [get_signing_template2](#get_signing_template2) - Retrieve a template
* [list_signing_templates2](#list_signing_templates2) - List all templates

## get_signing_template2

Retrieve a template

### Example Usage

<!-- UsageSnippet language="python" operationID="getSigningTemplate2" method="get" path="/signing/{connection_id}/template/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.template.get_signing_template2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.signing_template is not None

    # Handle response
    print(res.signing_template)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetSigningTemplate2Request](../../models/operations/getsigningtemplate2request.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetSigningTemplate2Response](../../models/operations/getsigningtemplate2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_signing_templates2

List all templates

### Example Usage

<!-- UsageSnippet language="python" operationID="listSigningTemplates2" method="get" path="/signing/{connection_id}/template" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.template.list_signing_templates2(request={
        "connection_id": "<id>",
    })

    assert res.signing_templates is not None

    # Handle response
    print(res.signing_templates)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListSigningTemplates2Request](../../models/operations/listsigningtemplates2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListSigningTemplates2Response](../../models/operations/listsigningtemplates2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |