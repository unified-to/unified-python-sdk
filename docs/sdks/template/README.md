# Template

## Overview

### Available Operations

* [get_signing_template](#get_signing_template) - Retrieve a template
* [list_signing_templates](#list_signing_templates) - List all templates

## get_signing_template

Retrieve a template

### Example Usage

<!-- UsageSnippet language="python" operationID="getSigningTemplate" method="get" path="/signing/{connection_id}/template/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.template.get_signing_template(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.signing_template is not None

    # Handle response
    print(res.signing_template)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetSigningTemplateRequest](../../models/operations/getsigningtemplaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetSigningTemplateResponse](../../models/operations/getsigningtemplateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_signing_templates

List all templates

### Example Usage

<!-- UsageSnippet language="python" operationID="listSigningTemplates" method="get" path="/signing/{connection_id}/template" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.template.list_signing_templates(request={
        "connection_id": "<id>",
    })

    assert res.signing_templates is not None

    # Handle response
    print(res.signing_templates)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListSigningTemplatesRequest](../../models/operations/listsigningtemplatesrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListSigningTemplatesResponse](../../models/operations/listsigningtemplatesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |