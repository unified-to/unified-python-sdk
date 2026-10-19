# Matter

## Overview

### Available Operations

* [create_legal_matter](#create_legal_matter) - Create a matter
* [get_legal_matter](#get_legal_matter) - Retrieve a matter
* [list_legal_matters](#list_legal_matters) - List all matters
* [patch_legal_matter](#patch_legal_matter) - Update a matter
* [remove_legal_matter](#remove_legal_matter) - Remove a matter
* [update_legal_matter](#update_legal_matter) - Update a matter

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

    res = unified_to.matter.create_legal_matter(request={
        "legal_matter": {
            "billing_method": shared.BillingMethod.OTHER,
            "client_reference": "qSrjIBAD",
            "company_ids": [],
            "contact_ids": [],
            "created_at": parse_datetime("2023-05-28T04:10:42.375Z"),
            "currency": "BOB",
            "description": "Speciosus cresco aut cotidie temeritas arma.",
            "id": "a536d382-c588-4b31-8d7b-3413e36341d1",
            "metadata": [],
            "name": "Walter v. Franecki - Spinka",
            "number": "2023-3062",
            "opened_at": parse_datetime("2023-07-05T04:35:25.005Z"),
            "parties": [
                {
                    "description": "Urban Walter",
                    "role": shared.LegalPartyRole.EXPERT,
                },
            ],
            "stage": "currus",
            "status": shared.LegalMatterStatus.OPEN,
            "statute_of_limitations_at": parse_datetime("2027-06-26T13:03:53.053Z"),
            "updated_at": parse_datetime("2023-07-17T07:49:07.165Z"),
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

    res = unified_to.matter.get_legal_matter(request={
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

    res = unified_to.matter.list_legal_matters(request={
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

    res = unified_to.matter.patch_legal_matter(request={
        "legal_matter": {
            "billing_method": shared.BillingMethod.OTHER,
            "client_reference": "qSrjIBAD",
            "company_ids": [],
            "contact_ids": [],
            "created_at": parse_datetime("2023-05-28T04:10:42.375Z"),
            "currency": "BOB",
            "description": "Speciosus cresco aut cotidie temeritas arma.",
            "id": "5a7f93e3-63e1-4f59-81ec-3ee365983edb",
            "metadata": [],
            "name": "Walter v. Franecki - Spinka",
            "number": "2023-3062",
            "opened_at": parse_datetime("2023-07-05T04:35:25.006Z"),
            "parties": [
                {
                    "description": "Urban Walter",
                    "role": shared.LegalPartyRole.EXPERT,
                },
            ],
            "stage": "currus",
            "status": shared.LegalMatterStatus.OPEN,
            "statute_of_limitations_at": parse_datetime("2027-06-26T13:03:53.079Z"),
            "updated_at": parse_datetime("2023-07-17T07:49:07.166Z"),
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

    res = unified_to.matter.remove_legal_matter(request={
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

    res = unified_to.matter.update_legal_matter(request={
        "legal_matter": {
            "billing_method": shared.BillingMethod.OTHER,
            "client_reference": "qSrjIBAD",
            "company_ids": [],
            "contact_ids": [],
            "created_at": parse_datetime("2023-05-28T04:10:42.375Z"),
            "currency": "BOB",
            "description": "Speciosus cresco aut cotidie temeritas arma.",
            "id": "5a7f93e3-63e1-4f59-81ec-3ee365983edb",
            "metadata": [],
            "name": "Walter v. Franecki - Spinka",
            "number": "2023-3062",
            "opened_at": parse_datetime("2023-07-05T04:35:25.006Z"),
            "parties": [
                {
                    "description": "Urban Walter",
                    "role": shared.LegalPartyRole.EXPERT,
                },
            ],
            "stage": "currus",
            "status": shared.LegalMatterStatus.OPEN,
            "statute_of_limitations_at": parse_datetime("2027-06-26T13:03:53.079Z"),
            "updated_at": parse_datetime("2023-07-17T07:49:07.166Z"),
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