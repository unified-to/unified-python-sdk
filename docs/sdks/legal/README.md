# Legal

## Overview

### Available Operations

* [create_legal_expense](#create_legal_expense) - Create an expense
* [create_legal_matter](#create_legal_matter) - Create a matter
* [create_legal_practicearea](#create_legal_practicearea) - Create a practicearea
* [create_legal_timeentry](#create_legal_timeentry) - Create a timeentry
* [get_legal_expense](#get_legal_expense) - Retrieve an expense
* [get_legal_matter](#get_legal_matter) - Retrieve a matter
* [get_legal_practicearea](#get_legal_practicearea) - Retrieve a practicearea
* [get_legal_timeentry](#get_legal_timeentry) - Retrieve a timeentry
* [list_legal_expenses](#list_legal_expenses) - List all expenses
* [list_legal_matters](#list_legal_matters) - List all matters
* [list_legal_practiceareas](#list_legal_practiceareas) - List all practiceareas
* [list_legal_timeentries](#list_legal_timeentries) - List all timeentries
* [patch_legal_expense](#patch_legal_expense) - Update an expense
* [patch_legal_matter](#patch_legal_matter) - Update a matter
* [patch_legal_practicearea](#patch_legal_practicearea) - Update a practicearea
* [patch_legal_timeentry](#patch_legal_timeentry) - Update a timeentry
* [remove_legal_expense](#remove_legal_expense) - Remove an expense
* [remove_legal_matter](#remove_legal_matter) - Remove a matter
* [remove_legal_practicearea](#remove_legal_practicearea) - Remove a practicearea
* [remove_legal_timeentry](#remove_legal_timeentry) - Remove a timeentry
* [update_legal_expense](#update_legal_expense) - Update an expense
* [update_legal_matter](#update_legal_matter) - Update a matter
* [update_legal_practicearea](#update_legal_practicearea) - Update a practicearea
* [update_legal_timeentry](#update_legal_timeentry) - Update a timeentry

## create_legal_expense

Create an expense

### Example Usage

<!-- UsageSnippet language="python" operationID="createLegalExpense" method="post" path="/legal/{connection_id}/expense" example="legal_expense" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.create_legal_expense(request={
        "legal_expense": {
            "category": "Kids",
            "created_at": parse_datetime("2020-11-08T00:41:42.356Z"),
            "currency": "MVR",
            "description": "Temporibus agnitio sui.",
            "id": "1ee376be-0adb-4828-b758-59deb2908bdf",
            "incurred_at": parse_datetime("2020-11-08T00:41:42.356Z"),
            "is_billed": False,
            "metadata": [],
            "price_amount": 100.0,
            "quantity": 3.0,
            "total_amount": 300.0,
            "type": shared.LegalExpenseType.OTHER,
            "updated_at": parse_datetime("2024-03-29T05:31:38.514Z"),
        },
        "connection_id": "<id>",
    })

    assert res.legal_expense is not None

    # Handle response
    print(res.legal_expense)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateLegalExpenseRequest](../../models/operations/createlegalexpenserequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateLegalExpenseResponse](../../models/operations/createlegalexpenseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_legal_matter

Create a matter

### Example Usage

<!-- UsageSnippet language="python" operationID="createLegalMatter" method="post" path="/legal/{connection_id}/matter" example="legal_matter" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.create_legal_matter(request={
        "legal_matter": {
            "billing_method": shared.BillingMethod.OTHER,
            "client_reference": "qSrjIBAD",
            "company_ids": [],
            "contact_ids": [],
            "created_at": parse_datetime("2023-05-28T04:10:42.375Z"),
            "currency": "BOB",
            "description": "Speciosus cresco aut cotidie temeritas arma.",
            "id": "2bf59873-6c48-4dfb-89db-3eebc3aab7b1",
            "metadata": [],
            "name": "Walter v. Franecki - Spinka",
            "number": "2023-3062",
            "opened_at": parse_datetime("2023-07-05T04:03:43.456Z"),
            "parties": [
                {
                    "description": "Urban Walter",
                    "role": shared.LegalPartyRole.EXPERT,
                },
            ],
            "stage": "currus",
            "status": shared.LegalMatterStatus.OPEN,
            "statute_of_limitations_at": parse_datetime("2027-06-25T19:50:36.872Z"),
            "updated_at": parse_datetime("2023-07-17T07:07:18.669Z"),
        },
        "connection_id": "<id>",
    })

    assert res.legal_matter is not None

    # Handle response
    print(res.legal_matter)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateLegalMatterRequest](../../models/operations/createlegalmatterrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateLegalMatterResponse](../../models/operations/createlegalmatterresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_legal_practicearea

Create a practicearea

### Example Usage

<!-- UsageSnippet language="python" operationID="createLegalPracticearea" method="post" path="/legal/{connection_id}/practicearea" example="legal_practicearea" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.create_legal_practicearea(request={
        "legal_practicearea": {
            "code": "QCA",
            "created_at": parse_datetime("2023-01-28T21:00:26.264Z"),
            "id": "5d7bbe39-2102-4c76-aebd-c216f615d34e",
            "metadata": [],
            "name": "witty Law",
            "type": shared.LegalPracticeareaType.EDUCATION,
            "updated_at": parse_datetime("2025-08-25T14:23:03.312Z"),
        },
        "connection_id": "<id>",
    })

    assert res.legal_practicearea is not None

    # Handle response
    print(res.legal_practicearea)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateLegalPracticeareaRequest](../../models/operations/createlegalpracticearearequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateLegalPracticeareaResponse](../../models/operations/createlegalpracticearearesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_legal_timeentry

Create a timeentry

### Example Usage

<!-- UsageSnippet language="python" operationID="createLegalTimeentry" method="post" path="/legal/{connection_id}/timeentry" example="legal_timeentry" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.create_legal_timeentry(request={
        "legal_timeentry": {
            "billable_minutes": 390.0,
            "created_at": parse_datetime("2022-05-06T03:26:03.756Z"),
            "currency": "ZAR",
            "description": "Ea derideo adulatio torrens.",
            "id": "50126ca0-3705-4c9a-b501-a3f3b98908ea",
            "is_billable": True,
            "metadata": [],
            "minutes": 390.0,
            "rate_amount": 637.0,
            "total_amount": 4140.5,
            "updated_at": parse_datetime("2022-06-29T23:21:00.135Z"),
            "worked_at": parse_datetime("2022-05-06T03:26:03.756Z"),
        },
        "connection_id": "<id>",
    })

    assert res.legal_timeentry is not None

    # Handle response
    print(res.legal_timeentry)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateLegalTimeentryRequest](../../models/operations/createlegaltimeentryrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateLegalTimeentryResponse](../../models/operations/createlegaltimeentryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_legal_expense

Retrieve an expense

### Example Usage

<!-- UsageSnippet language="python" operationID="getLegalExpense" method="get" path="/legal/{connection_id}/expense/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.get_legal_expense(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.legal_expense is not None

    # Handle response
    print(res.legal_expense)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetLegalExpenseRequest](../../models/operations/getlegalexpenserequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetLegalExpenseResponse](../../models/operations/getlegalexpenseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_legal_matter

Retrieve a matter

### Example Usage

<!-- UsageSnippet language="python" operationID="getLegalMatter" method="get" path="/legal/{connection_id}/matter/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.get_legal_matter(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.legal_matter is not None

    # Handle response
    print(res.legal_matter)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetLegalMatterRequest](../../models/operations/getlegalmatterrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetLegalMatterResponse](../../models/operations/getlegalmatterresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_legal_practicearea

Retrieve a practicearea

### Example Usage

<!-- UsageSnippet language="python" operationID="getLegalPracticearea" method="get" path="/legal/{connection_id}/practicearea/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.get_legal_practicearea(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.legal_practicearea is not None

    # Handle response
    print(res.legal_practicearea)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetLegalPracticeareaRequest](../../models/operations/getlegalpracticearearequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetLegalPracticeareaResponse](../../models/operations/getlegalpracticearearesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_legal_timeentry

Retrieve a timeentry

### Example Usage

<!-- UsageSnippet language="python" operationID="getLegalTimeentry" method="get" path="/legal/{connection_id}/timeentry/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.get_legal_timeentry(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.legal_timeentry is not None

    # Handle response
    print(res.legal_timeentry)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetLegalTimeentryRequest](../../models/operations/getlegaltimeentryrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetLegalTimeentryResponse](../../models/operations/getlegaltimeentryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_legal_expenses

List all expenses

### Example Usage

<!-- UsageSnippet language="python" operationID="listLegalExpenses" method="get" path="/legal/{connection_id}/expense" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.list_legal_expenses(request={
        "connection_id": "<id>",
    })

    assert res.legal_expenses is not None

    # Handle response
    print(res.legal_expenses)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListLegalExpensesRequest](../../models/operations/listlegalexpensesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListLegalExpensesResponse](../../models/operations/listlegalexpensesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_legal_matters

List all matters

### Example Usage

<!-- UsageSnippet language="python" operationID="listLegalMatters" method="get" path="/legal/{connection_id}/matter" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.list_legal_matters(request={
        "connection_id": "<id>",
    })

    assert res.legal_matters is not None

    # Handle response
    print(res.legal_matters)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListLegalMattersRequest](../../models/operations/listlegalmattersrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListLegalMattersResponse](../../models/operations/listlegalmattersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_legal_practiceareas

List all practiceareas

### Example Usage

<!-- UsageSnippet language="python" operationID="listLegalPracticeareas" method="get" path="/legal/{connection_id}/practicearea" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.list_legal_practiceareas(request={
        "connection_id": "<id>",
    })

    assert res.legal_practiceareas is not None

    # Handle response
    print(res.legal_practiceareas)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListLegalPracticeareasRequest](../../models/operations/listlegalpracticeareasrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListLegalPracticeareasResponse](../../models/operations/listlegalpracticeareasresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_legal_timeentries

List all timeentries

### Example Usage

<!-- UsageSnippet language="python" operationID="listLegalTimeentries" method="get" path="/legal/{connection_id}/timeentry" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.list_legal_timeentries(request={
        "connection_id": "<id>",
    })

    assert res.legal_timeentries is not None

    # Handle response
    print(res.legal_timeentries)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListLegalTimeentriesRequest](../../models/operations/listlegaltimeentriesrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListLegalTimeentriesResponse](../../models/operations/listlegaltimeentriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_legal_expense

Update an expense

### Example Usage

<!-- UsageSnippet language="python" operationID="patchLegalExpense" method="patch" path="/legal/{connection_id}/expense/{id}" example="legal_expense" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.patch_legal_expense(request={
        "legal_expense": {
            "category": "Kids",
            "created_at": parse_datetime("2020-11-08T00:41:42.356Z"),
            "currency": "MVR",
            "description": "Temporibus agnitio sui.",
            "id": "64db8fc4-2a8f-4264-b81c-99dcf6d7eece",
            "incurred_at": parse_datetime("2020-11-08T00:41:42.356Z"),
            "is_billed": False,
            "metadata": [],
            "price_amount": 100.0,
            "quantity": 3.0,
            "total_amount": 300.0,
            "type": shared.LegalExpenseType.OTHER,
            "updated_at": parse_datetime("2024-03-29T05:31:38.522Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.legal_expense is not None

    # Handle response
    print(res.legal_expense)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchLegalExpenseRequest](../../models/operations/patchlegalexpenserequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchLegalExpenseResponse](../../models/operations/patchlegalexpenseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_legal_matter

Update a matter

### Example Usage

<!-- UsageSnippet language="python" operationID="patchLegalMatter" method="patch" path="/legal/{connection_id}/matter/{id}" example="legal_matter" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.patch_legal_matter(request={
        "legal_matter": {
            "billing_method": shared.BillingMethod.OTHER,
            "client_reference": "qSrjIBAD",
            "company_ids": [],
            "contact_ids": [],
            "created_at": parse_datetime("2023-05-28T04:10:42.375Z"),
            "currency": "BOB",
            "description": "Speciosus cresco aut cotidie temeritas arma.",
            "id": "29732a6f-0343-4794-a081-6b85c9db3454",
            "metadata": [],
            "name": "Walter v. Franecki - Spinka",
            "number": "2023-3062",
            "opened_at": parse_datetime("2023-07-05T04:03:43.457Z"),
            "parties": [
                {
                    "description": "Urban Walter",
                    "role": shared.LegalPartyRole.EXPERT,
                },
            ],
            "stage": "currus",
            "status": shared.LegalMatterStatus.OPEN,
            "statute_of_limitations_at": parse_datetime("2027-06-25T19:50:36.911Z"),
            "updated_at": parse_datetime("2023-07-17T07:07:18.671Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.legal_matter is not None

    # Handle response
    print(res.legal_matter)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchLegalMatterRequest](../../models/operations/patchlegalmatterrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchLegalMatterResponse](../../models/operations/patchlegalmatterresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_legal_practicearea

Update a practicearea

### Example Usage

<!-- UsageSnippet language="python" operationID="patchLegalPracticearea" method="patch" path="/legal/{connection_id}/practicearea/{id}" example="legal_practicearea" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.patch_legal_practicearea(request={
        "legal_practicearea": {
            "code": "QCA",
            "created_at": parse_datetime("2023-01-28T21:00:26.264Z"),
            "id": "a4aefd8d-6ed9-4d7e-8a11-2d6f87de46a3",
            "metadata": [],
            "name": "witty Law",
            "type": shared.LegalPracticeareaType.EDUCATION,
            "updated_at": parse_datetime("2025-08-25T14:23:03.325Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.legal_practicearea is not None

    # Handle response
    print(res.legal_practicearea)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchLegalPracticeareaRequest](../../models/operations/patchlegalpracticearearequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchLegalPracticeareaResponse](../../models/operations/patchlegalpracticearearesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_legal_timeentry

Update a timeentry

### Example Usage

<!-- UsageSnippet language="python" operationID="patchLegalTimeentry" method="patch" path="/legal/{connection_id}/timeentry/{id}" example="legal_timeentry" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.patch_legal_timeentry(request={
        "legal_timeentry": {
            "billable_minutes": 390.0,
            "created_at": parse_datetime("2022-05-06T03:26:03.756Z"),
            "currency": "ZAR",
            "description": "Ea derideo adulatio torrens.",
            "id": "1d5eb0f3-c5db-494c-b3b2-92054092bb2d",
            "is_billable": True,
            "metadata": [],
            "minutes": 390.0,
            "rate_amount": 637.0,
            "total_amount": 4140.5,
            "updated_at": parse_datetime("2022-06-29T23:21:00.136Z"),
            "worked_at": parse_datetime("2022-05-06T03:26:03.756Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.legal_timeentry is not None

    # Handle response
    print(res.legal_timeentry)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchLegalTimeentryRequest](../../models/operations/patchlegaltimeentryrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchLegalTimeentryResponse](../../models/operations/patchlegaltimeentryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_legal_expense

Remove an expense

### Example Usage

<!-- UsageSnippet language="python" operationID="removeLegalExpense" method="delete" path="/legal/{connection_id}/expense/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.remove_legal_expense(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveLegalExpenseRequest](../../models/operations/removelegalexpenserequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveLegalExpenseResponse](../../models/operations/removelegalexpenseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_legal_matter

Remove a matter

### Example Usage

<!-- UsageSnippet language="python" operationID="removeLegalMatter" method="delete" path="/legal/{connection_id}/matter/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.remove_legal_matter(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveLegalMatterRequest](../../models/operations/removelegalmatterrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveLegalMatterResponse](../../models/operations/removelegalmatterresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_legal_practicearea

Remove a practicearea

### Example Usage

<!-- UsageSnippet language="python" operationID="removeLegalPracticearea" method="delete" path="/legal/{connection_id}/practicearea/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.remove_legal_practicearea(request={
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
| `request`                                                                                              | [operations.RemoveLegalPracticeareaRequest](../../models/operations/removelegalpracticearearequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveLegalPracticeareaResponse](../../models/operations/removelegalpracticearearesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_legal_timeentry

Remove a timeentry

### Example Usage

<!-- UsageSnippet language="python" operationID="removeLegalTimeentry" method="delete" path="/legal/{connection_id}/timeentry/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.remove_legal_timeentry(request={
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
| `request`                                                                                        | [operations.RemoveLegalTimeentryRequest](../../models/operations/removelegaltimeentryrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.RemoveLegalTimeentryResponse](../../models/operations/removelegaltimeentryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_legal_expense

Update an expense

### Example Usage

<!-- UsageSnippet language="python" operationID="updateLegalExpense" method="put" path="/legal/{connection_id}/expense/{id}" example="legal_expense" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.update_legal_expense(request={
        "legal_expense": {
            "category": "Kids",
            "created_at": parse_datetime("2020-11-08T00:41:42.356Z"),
            "currency": "MVR",
            "description": "Temporibus agnitio sui.",
            "id": "64db8fc4-2a8f-4264-b81c-99dcf6d7eece",
            "incurred_at": parse_datetime("2020-11-08T00:41:42.356Z"),
            "is_billed": False,
            "metadata": [],
            "price_amount": 100.0,
            "quantity": 3.0,
            "total_amount": 300.0,
            "type": shared.LegalExpenseType.OTHER,
            "updated_at": parse_datetime("2024-03-29T05:31:38.522Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.legal_expense is not None

    # Handle response
    print(res.legal_expense)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateLegalExpenseRequest](../../models/operations/updatelegalexpenserequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateLegalExpenseResponse](../../models/operations/updatelegalexpenseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_legal_matter

Update a matter

### Example Usage

<!-- UsageSnippet language="python" operationID="updateLegalMatter" method="put" path="/legal/{connection_id}/matter/{id}" example="legal_matter" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.update_legal_matter(request={
        "legal_matter": {
            "billing_method": shared.BillingMethod.OTHER,
            "client_reference": "qSrjIBAD",
            "company_ids": [],
            "contact_ids": [],
            "created_at": parse_datetime("2023-05-28T04:10:42.375Z"),
            "currency": "BOB",
            "description": "Speciosus cresco aut cotidie temeritas arma.",
            "id": "29732a6f-0343-4794-a081-6b85c9db3454",
            "metadata": [],
            "name": "Walter v. Franecki - Spinka",
            "number": "2023-3062",
            "opened_at": parse_datetime("2023-07-05T04:03:43.457Z"),
            "parties": [
                {
                    "description": "Urban Walter",
                    "role": shared.LegalPartyRole.EXPERT,
                },
            ],
            "stage": "currus",
            "status": shared.LegalMatterStatus.OPEN,
            "statute_of_limitations_at": parse_datetime("2027-06-25T19:50:36.911Z"),
            "updated_at": parse_datetime("2023-07-17T07:07:18.671Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.legal_matter is not None

    # Handle response
    print(res.legal_matter)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateLegalMatterRequest](../../models/operations/updatelegalmatterrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateLegalMatterResponse](../../models/operations/updatelegalmatterresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_legal_practicearea

Update a practicearea

### Example Usage

<!-- UsageSnippet language="python" operationID="updateLegalPracticearea" method="put" path="/legal/{connection_id}/practicearea/{id}" example="legal_practicearea" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.update_legal_practicearea(request={
        "legal_practicearea": {
            "code": "QCA",
            "created_at": parse_datetime("2023-01-28T21:00:26.264Z"),
            "id": "a4aefd8d-6ed9-4d7e-8a11-2d6f87de46a3",
            "metadata": [],
            "name": "witty Law",
            "type": shared.LegalPracticeareaType.EDUCATION,
            "updated_at": parse_datetime("2025-08-25T14:23:03.325Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.legal_practicearea is not None

    # Handle response
    print(res.legal_practicearea)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateLegalPracticeareaRequest](../../models/operations/updatelegalpracticearearequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateLegalPracticeareaResponse](../../models/operations/updatelegalpracticearearesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_legal_timeentry

Update a timeentry

### Example Usage

<!-- UsageSnippet language="python" operationID="updateLegalTimeentry" method="put" path="/legal/{connection_id}/timeentry/{id}" example="legal_timeentry" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.legal.update_legal_timeentry(request={
        "legal_timeentry": {
            "billable_minutes": 390.0,
            "created_at": parse_datetime("2022-05-06T03:26:03.756Z"),
            "currency": "ZAR",
            "description": "Ea derideo adulatio torrens.",
            "id": "1d5eb0f3-c5db-494c-b3b2-92054092bb2d",
            "is_billable": True,
            "metadata": [],
            "minutes": 390.0,
            "rate_amount": 637.0,
            "total_amount": 4140.5,
            "updated_at": parse_datetime("2022-06-29T23:21:00.136Z"),
            "worked_at": parse_datetime("2022-05-06T03:26:03.756Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.legal_timeentry is not None

    # Handle response
    print(res.legal_timeentry)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateLegalTimeentryRequest](../../models/operations/updatelegaltimeentryrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateLegalTimeentryResponse](../../models/operations/updatelegaltimeentryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |