# Order

## Overview

### Available Operations

* [~~create_accounting_order~~](#create_accounting_order) - Create an order :warning: **Deprecated**
* [create_assessment_order](#create_assessment_order) - Create an order
* [~~get_accounting_order~~](#get_accounting_order) - Retrieve an order :warning: **Deprecated**
* [get_assessment_order](#get_assessment_order) - Retrieve an order
* [~~list_accounting_orders~~](#list_accounting_orders) - List all orders :warning: **Deprecated**
* [~~patch_accounting_order~~](#patch_accounting_order) - Update an order :warning: **Deprecated**
* [patch_assessment_order](#patch_assessment_order) - Update an order
* [~~remove_accounting_order~~](#remove_accounting_order) - Remove an order :warning: **Deprecated**
* [~~update_accounting_order~~](#update_accounting_order) - Update an order :warning: **Deprecated**
* [update_assessment_order](#update_assessment_order) - Update an order

## ~~create_accounting_order~~

Creates a AccountingOrder. Provide the unified AccountingOrder fields in the request body; they are mapped to the provider's API. Returns the created AccountingOrder.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingOrder" method="post" path="/accounting/{connection_id}/order" example="accounting_order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.create_accounting_order(request={
        "accounting_order": {
            "billing_address": {
                "address1": "7654 Treutel Square",
                "city": "Forrestport",
                "country_code": "US",
                "postal_code": "42190-3694",
                "region": "Maine",
                "region_code": "OR",
            },
            "created_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "currency": "GBP",
            "id": "28d3b89f-0446-43dd-9b12-88dae6df1211",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "shipping_address": {
                "address1": "4974 Beatty Corners",
                "city": "Alizeport",
                "country_code": "US",
                "postal_code": "56252",
                "region": "Alaska",
                "region_code": "VT",
            },
            "status": shared.AccountingOrderStatus.AUTHORIZED,
            "total_amount": 0.0,
            "type": shared.AccountingOrderType.SALES,
            "updated_at": parse_datetime("2022-02-08T12:12:41.888Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_order is not None

    # Handle response
    print(res.accounting_order)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateAccountingOrderRequest](../../models/operations/createaccountingorderrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateAccountingOrderResponse](../../models/operations/createaccountingorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_assessment_order

Creates a AssessmentOrder. Provide the unified AssessmentOrder fields in the request body; they are mapped to the provider's API. Returns the created AssessmentOrder.

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

    res = unified_to.order.create_assessment_order(request={
        "assessment_order": {
            "connection_id": "<id>",
            "created_at": parse_datetime("2021-09-18T10:33:57.803Z"),
            "id": "8f2ded2a-b22c-42ae-a1c7-7dffc14e2cc3",
            "metadata": [],
            "parameters": [],
            "profile_addresses": [],
            "profile_date_of_birth": "1989-07-22T16:18:37.650Z",
            "profile_emails": [
                "amy.kris.windler@icloud.com",
            ],
            "profile_first_name": "Amy",
            "profile_gender": shared.ProfileGender.NON_BINARY,
            "profile_last_name": "Kris-Windler",
            "profile_name": "Amy Kris-Windler",
            "profile_resume_url": "https://enchanted-cycle.biz/",
            "profile_social_media_urls": [],
            "profile_telephones": [
                "(341) 425-5828",
            ],
            "reference": "ab",
            "response_attributes": [],
            "response_details": [],
            "response_download_urls": [],
            "response_max_score": 84.0,
            "response_score": 82.0,
            "response_status": shared.ResponseStatus.REJECTED,
            "response_url": "https://rowdy-fisherman.biz/",
            "status": shared.AssessmentOrderStatus.REJECTED,
            "target_url": "https://cautious-turret.info",
            "updated_at": parse_datetime("2023-01-26T02:54:10.939Z"),
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

## ~~get_accounting_order~~

Retrieves a single AccountingOrder by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingOrder" method="get" path="/accounting/{connection_id}/order/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.get_accounting_order(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_order is not None

    # Handle response
    print(res.accounting_order)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAccountingOrderRequest](../../models/operations/getaccountingorderrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetAccountingOrderResponse](../../models/operations/getaccountingorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_assessment_order

Retrieves a single AssessmentOrder by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

    res = unified_to.order.get_assessment_order(request={
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

## ~~list_accounting_orders~~

Returns a list of AccountingOrders. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingOrders" method="get" path="/accounting/{connection_id}/order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.list_accounting_orders(request={
        "connection_id": "<id>",
    })

    assert res.accounting_orders is not None

    # Handle response
    print(res.accounting_orders)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListAccountingOrdersRequest](../../models/operations/listaccountingordersrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListAccountingOrdersResponse](../../models/operations/listaccountingordersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## ~~patch_accounting_order~~

Updates the AccountingOrder identified by `id`. Provide the unified AccountingOrder fields to change in the request body.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingOrder" method="patch" path="/accounting/{connection_id}/order/{id}" example="accounting_order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.patch_accounting_order(request={
        "accounting_order": {
            "billing_address": {
                "address1": "7654 Treutel Square",
                "city": "Forrestport",
                "country_code": "US",
                "postal_code": "42190-3694",
                "region": "Maine",
                "region_code": "OR",
            },
            "created_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "currency": "GBP",
            "id": "a2722865-e3c2-4eb8-9c96-bde5f90cfaf2",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "shipping_address": {
                "address1": "4974 Beatty Corners",
                "city": "Alizeport",
                "country_code": "US",
                "postal_code": "56252",
                "region": "Alaska",
                "region_code": "VT",
            },
            "status": shared.AccountingOrderStatus.AUTHORIZED,
            "total_amount": 0.0,
            "type": shared.AccountingOrderType.SALES,
            "updated_at": parse_datetime("2022-02-08T12:12:41.895Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_order is not None

    # Handle response
    print(res.accounting_order)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchAccountingOrderRequest](../../models/operations/patchaccountingorderrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchAccountingOrderResponse](../../models/operations/patchaccountingorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_assessment_order

Updates the AssessmentOrder identified by `id`. Provide the unified AssessmentOrder fields to change in the request body.

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

    res = unified_to.order.patch_assessment_order(request={
        "assessment_order": {
            "connection_id": "<id>",
            "created_at": parse_datetime("2021-09-18T10:33:57.803Z"),
            "id": "a89a5324-7724-4a6a-a3f2-52534dfbbf5a",
            "metadata": [],
            "parameters": [],
            "profile_addresses": [],
            "profile_date_of_birth": "1989-07-22T16:18:37.650Z",
            "profile_emails": [
                "amy.kris.windler@icloud.com",
            ],
            "profile_first_name": "Amy",
            "profile_gender": shared.ProfileGender.NON_BINARY,
            "profile_last_name": "Kris-Windler",
            "profile_name": "Amy Kris-Windler",
            "profile_resume_url": "https://enchanted-cycle.biz/",
            "profile_social_media_urls": [],
            "profile_telephones": [
                "(341) 425-5828",
            ],
            "reference": "ab",
            "response_attributes": [],
            "response_details": [],
            "response_download_urls": [],
            "response_max_score": 84.0,
            "response_score": 82.0,
            "response_status": shared.ResponseStatus.REJECTED,
            "response_url": "https://rowdy-fisherman.biz/",
            "status": shared.AssessmentOrderStatus.REJECTED,
            "target_url": "https://cautious-turret.info",
            "updated_at": parse_datetime("2023-01-26T02:54:10.953Z"),
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

## ~~remove_accounting_order~~

Deletes the AccountingOrder identified by `id`.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingOrder" method="delete" path="/accounting/{connection_id}/order/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.remove_accounting_order(request={
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
| `request`                                                                                          | [operations.RemoveAccountingOrderRequest](../../models/operations/removeaccountingorderrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveAccountingOrderResponse](../../models/operations/removeaccountingorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## ~~update_accounting_order~~

Updates the AccountingOrder identified by `id`. Provide the unified AccountingOrder fields to change in the request body.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingOrder" method="put" path="/accounting/{connection_id}/order/{id}" example="accounting_order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.update_accounting_order(request={
        "accounting_order": {
            "billing_address": {
                "address1": "7654 Treutel Square",
                "city": "Forrestport",
                "country_code": "US",
                "postal_code": "42190-3694",
                "region": "Maine",
                "region_code": "OR",
            },
            "created_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "currency": "GBP",
            "id": "a2722865-e3c2-4eb8-9c96-bde5f90cfaf2",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "shipping_address": {
                "address1": "4974 Beatty Corners",
                "city": "Alizeport",
                "country_code": "US",
                "postal_code": "56252",
                "region": "Alaska",
                "region_code": "VT",
            },
            "status": shared.AccountingOrderStatus.AUTHORIZED,
            "total_amount": 0.0,
            "type": shared.AccountingOrderType.SALES,
            "updated_at": parse_datetime("2022-02-08T12:12:41.895Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_order is not None

    # Handle response
    print(res.accounting_order)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateAccountingOrderRequest](../../models/operations/updateaccountingorderrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateAccountingOrderResponse](../../models/operations/updateaccountingorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_assessment_order

Updates the AssessmentOrder identified by `id`. Provide the unified AssessmentOrder fields to change in the request body.

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

    res = unified_to.order.update_assessment_order(request={
        "assessment_order": {
            "connection_id": "<id>",
            "created_at": parse_datetime("2021-09-18T10:33:57.803Z"),
            "id": "a89a5324-7724-4a6a-a3f2-52534dfbbf5a",
            "metadata": [],
            "parameters": [],
            "profile_addresses": [],
            "profile_date_of_birth": "1989-07-22T16:18:37.650Z",
            "profile_emails": [
                "amy.kris.windler@icloud.com",
            ],
            "profile_first_name": "Amy",
            "profile_gender": shared.ProfileGender.NON_BINARY,
            "profile_last_name": "Kris-Windler",
            "profile_name": "Amy Kris-Windler",
            "profile_resume_url": "https://enchanted-cycle.biz/",
            "profile_social_media_urls": [],
            "profile_telephones": [
                "(341) 425-5828",
            ],
            "reference": "ab",
            "response_attributes": [],
            "response_details": [],
            "response_download_urls": [],
            "response_max_score": 84.0,
            "response_score": 82.0,
            "response_status": shared.ResponseStatus.REJECTED,
            "response_url": "https://rowdy-fisherman.biz/",
            "status": shared.AssessmentOrderStatus.REJECTED,
            "target_url": "https://cautious-turret.info",
            "updated_at": parse_datetime("2023-01-26T02:54:10.953Z"),
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