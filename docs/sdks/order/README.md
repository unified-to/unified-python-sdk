# Order

## Overview

### Available Operations

* [create_accounting_order](#create_accounting_order) - Create an order
* [create_assessment_order](#create_assessment_order) - Create an order
* [get_accounting_order](#get_accounting_order) - Retrieve an order
* [get_assessment_order](#get_assessment_order) - Retrieve an order
* [list_accounting_orders](#list_accounting_orders) - List all orders
* [patch_accounting_order](#patch_accounting_order) - Update an order
* [patch_assessment_order](#patch_assessment_order) - Update an order
* [remove_accounting_order](#remove_accounting_order) - Remove an order
* [update_accounting_order](#update_accounting_order) - Update an order
* [update_assessment_order](#update_assessment_order) - Update an order

## create_accounting_order

Create an order

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
                "address1": "802 Bechtelar Park",
                "address2": "Apt. 436",
                "city": "Daniellaville",
                "country_code": "US",
                "postal_code": "36947",
                "region": "Wisconsin",
                "region_code": "NY",
            },
            "created_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "currency": "USD",
            "id": "445e9028-1570-4f8f-9d13-775af36237a6",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2022-04-05T16:02:41.218Z"),
            "shipping_address": {
                "address1": "9745 Betty Shore",
                "city": "South Alainaland",
                "country_code": "US",
                "postal_code": "25274-7654",
                "region": "New Hampshire",
                "region_code": "LA",
            },
            "status": shared.AccountingOrderStatus.SUBMITTED,
            "total_amount": 0.0,
            "type": shared.AccountingOrderType.PURCHASE,
            "updated_at": parse_datetime("2021-06-18T05:17:48.570Z"),
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

    res = unified_to.order.create_assessment_order(request={
        "assessment_order": {
            "connection_id": "<id>",
            "created_at": parse_datetime("2021-09-18T10:33:57.803Z"),
            "id": "1499537e-e281-4923-954e-5811125006ae",
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
            "updated_at": parse_datetime("2023-01-17T19:43:52.338Z"),
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

## get_accounting_order

Retrieve an order

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

## list_accounting_orders

List all orders

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

## patch_accounting_order

Update an order

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
                "address1": "802 Bechtelar Park",
                "address2": "Apt. 436",
                "city": "Daniellaville",
                "country_code": "US",
                "postal_code": "36947",
                "region": "Wisconsin",
                "region_code": "NY",
            },
            "created_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "currency": "USD",
            "id": "bdf36a05-6b7f-4eef-9179-63e8d329f593",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2022-04-05T16:02:41.231Z"),
            "shipping_address": {
                "address1": "9745 Betty Shore",
                "city": "South Alainaland",
                "country_code": "US",
                "postal_code": "25274-7654",
                "region": "New Hampshire",
                "region_code": "LA",
            },
            "status": shared.AccountingOrderStatus.SUBMITTED,
            "total_amount": 0.0,
            "type": shared.AccountingOrderType.PURCHASE,
            "updated_at": parse_datetime("2021-06-18T05:17:48.576Z"),
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

    res = unified_to.order.patch_assessment_order(request={
        "assessment_order": {
            "connection_id": "<id>",
            "created_at": parse_datetime("2021-09-18T10:33:57.803Z"),
            "id": "b8f60359-7023-4173-8480-808975596d56",
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
            "updated_at": parse_datetime("2023-01-17T19:43:52.350Z"),
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

## remove_accounting_order

Remove an order

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

## update_accounting_order

Update an order

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
                "address1": "802 Bechtelar Park",
                "address2": "Apt. 436",
                "city": "Daniellaville",
                "country_code": "US",
                "postal_code": "36947",
                "region": "Wisconsin",
                "region_code": "NY",
            },
            "created_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "currency": "USD",
            "id": "bdf36a05-6b7f-4eef-9179-63e8d329f593",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2022-04-05T16:02:41.231Z"),
            "shipping_address": {
                "address1": "9745 Betty Shore",
                "city": "South Alainaland",
                "country_code": "US",
                "postal_code": "25274-7654",
                "region": "New Hampshire",
                "region_code": "LA",
            },
            "status": shared.AccountingOrderStatus.SUBMITTED,
            "total_amount": 0.0,
            "type": shared.AccountingOrderType.PURCHASE,
            "updated_at": parse_datetime("2021-06-18T05:17:48.576Z"),
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

    res = unified_to.order.update_assessment_order(request={
        "assessment_order": {
            "connection_id": "<id>",
            "created_at": parse_datetime("2021-09-18T10:33:57.803Z"),
            "id": "b8f60359-7023-4173-8480-808975596d56",
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
            "updated_at": parse_datetime("2023-01-17T19:43:52.350Z"),
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