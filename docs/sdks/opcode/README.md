# Opcode

## Overview

### Available Operations

* [create_dms_opcode](#create_dms_opcode) - Create an opcode
* [get_dms_opcode](#get_dms_opcode) - Retrieve an opcode
* [list_dms_opcodes](#list_dms_opcodes) - List all opcodes
* [patch_dms_opcode](#patch_dms_opcode) - Update an opcode
* [update_dms_opcode](#update_dms_opcode) - Update an opcode

## create_dms_opcode

Creates a DmsOpcode. Provide the unified DmsOpcode fields in the request body; they are mapped to the provider's API. Returns the created DmsOpcode.

### Example Usage

<!-- UsageSnippet language="python" operationID="createDmsOpcode" method="post" path="/dms/{connection_id}/opcode" example="dms_opcode" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.opcode.create_dms_opcode(request={
        "dms_opcode": {
            "category": "Electrical",
            "code": "02AUS",
            "created_at": parse_datetime("2021-01-12T19:03:17.545Z"),
            "currency": "USD",
            "description": "Oil and filter change",
            "estimated_hours": 3.2,
            "flat_rate_hours": 3.5,
            "id": "ccba54df-c730-4902-90d0-95c7ccbd59f7",
            "is_active": True,
            "labor_rate_amount": 216.0,
            "metadata": [],
            "oem_code": "05604A3",
            "parts": [],
            "pay_type": shared.DmsOpcodePayType.CUSTOMER,
            "skill_code": "A",
            "type": shared.DmsOpcodeType.LABOR,
            "updated_at": parse_datetime("2021-11-03T15:52:02.214Z"),
        },
        "connection_id": "<id>",
    })

    assert res.dms_opcode is not None

    # Handle response
    print(res.dms_opcode)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateDmsOpcodeRequest](../../models/operations/createdmsopcoderequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.CreateDmsOpcodeResponse](../../models/operations/createdmsopcoderesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dms_opcode

Retrieves a single DmsOpcode by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDmsOpcode" method="get" path="/dms/{connection_id}/opcode/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.opcode.get_dms_opcode(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_opcode is not None

    # Handle response
    print(res.dms_opcode)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetDmsOpcodeRequest](../../models/operations/getdmsopcoderequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GetDmsOpcodeResponse](../../models/operations/getdmsopcoderesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_dms_opcodes

Returns a list of DmsOpcodes. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listDmsOpcodes" method="get" path="/dms/{connection_id}/opcode" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.opcode.list_dms_opcodes(request={
        "connection_id": "<id>",
    })

    assert res.dms_opcodes is not None

    # Handle response
    print(res.dms_opcodes)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListDmsOpcodesRequest](../../models/operations/listdmsopcodesrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListDmsOpcodesResponse](../../models/operations/listdmsopcodesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_dms_opcode

Updates the DmsOpcode identified by `id`. Provide the unified DmsOpcode fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchDmsOpcode" method="patch" path="/dms/{connection_id}/opcode/{id}" example="dms_opcode" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.opcode.patch_dms_opcode(request={
        "dms_opcode": {
            "category": "Electrical",
            "code": "02AUS",
            "created_at": parse_datetime("2021-01-12T19:03:17.545Z"),
            "currency": "USD",
            "description": "Oil and filter change",
            "estimated_hours": 3.2,
            "flat_rate_hours": 3.5,
            "id": "e4a94368-53be-45f0-b65c-df20583d81cf",
            "is_active": True,
            "labor_rate_amount": 216.0,
            "metadata": [],
            "oem_code": "05604A3",
            "parts": [],
            "pay_type": shared.DmsOpcodePayType.CUSTOMER,
            "skill_code": "A",
            "type": shared.DmsOpcodeType.LABOR,
            "updated_at": parse_datetime("2021-11-03T15:52:02.217Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_opcode is not None

    # Handle response
    print(res.dms_opcode)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchDmsOpcodeRequest](../../models/operations/patchdmsopcoderequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.PatchDmsOpcodeResponse](../../models/operations/patchdmsopcoderesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_dms_opcode

Updates the DmsOpcode identified by `id`. Provide the unified DmsOpcode fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateDmsOpcode" method="put" path="/dms/{connection_id}/opcode/{id}" example="dms_opcode" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.opcode.update_dms_opcode(request={
        "dms_opcode": {
            "category": "Electrical",
            "code": "02AUS",
            "created_at": parse_datetime("2021-01-12T19:03:17.545Z"),
            "currency": "USD",
            "description": "Oil and filter change",
            "estimated_hours": 3.2,
            "flat_rate_hours": 3.5,
            "id": "e4a94368-53be-45f0-b65c-df20583d81cf",
            "is_active": True,
            "labor_rate_amount": 216.0,
            "metadata": [],
            "oem_code": "05604A3",
            "parts": [],
            "pay_type": shared.DmsOpcodePayType.CUSTOMER,
            "skill_code": "A",
            "type": shared.DmsOpcodeType.LABOR,
            "updated_at": parse_datetime("2021-11-03T15:52:02.217Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_opcode is not None

    # Handle response
    print(res.dms_opcode)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateDmsOpcodeRequest](../../models/operations/updatedmsopcoderequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.UpdateDmsOpcodeResponse](../../models/operations/updatedmsopcoderesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |