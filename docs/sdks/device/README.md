# Device

## Overview

### Available Operations

* [create_hris_device](#create_hris_device) - Create a device
* [get_hris_device](#get_hris_device) - Retrieve a device
* [list_hris_devices](#list_hris_devices) - List all devices
* [patch_hris_device](#patch_hris_device) - Update a device
* [remove_hris_device](#remove_hris_device) - Remove a device
* [update_hris_device](#update_hris_device) - Update a device

## create_hris_device

Creates a HrisDevice. Provide the unified HrisDevice fields in the request body; they are mapped to the provider's API. Returns the created HrisDevice.

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisDevice" method="post" path="/hris/{connection_id}/device" example="hris_device" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.device.create_hris_device(request={
        "hris_device": {
            "admin_user_ids": [],
            "asset_tag": "fJNacaaoWi",
            "created_at": parse_datetime("2019-04-04T17:11:40.322Z"),
            "has_antivirus": True,
            "has_firewall": True,
            "has_hd_encrypted": True,
            "has_password_manager": True,
            "has_screenlock": False,
            "id": "aa60e3fd-9c3e-4733-bf04-21c1540596d6",
            "is_missing": False,
            "manufacturer": "Hackett Inc",
            "metadata": [],
            "model": "Fantastic",
            "name": "august-laptop",
            "os": "transmitter",
            "os_version": "8.4.8",
            "updated_at": parse_datetime("2023-06-12T04:47:46.641Z"),
            "version": "4.15.7",
        },
        "connection_id": "<id>",
    })

    assert res.hris_device is not None

    # Handle response
    print(res.hris_device)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateHrisDeviceRequest](../../models/operations/createhrisdevicerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreateHrisDeviceResponse](../../models/operations/createhrisdeviceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_device

Retrieves a single HrisDevice by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisDevice" method="get" path="/hris/{connection_id}/device/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.device.get_hris_device(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_device is not None

    # Handle response
    print(res.hris_device)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetHrisDeviceRequest](../../models/operations/gethrisdevicerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetHrisDeviceResponse](../../models/operations/gethrisdeviceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_devices

Returns a list of HrisDevices. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisDevices" method="get" path="/hris/{connection_id}/device" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.device.list_hris_devices(request={
        "connection_id": "<id>",
    })

    assert res.hris_devices is not None

    # Handle response
    print(res.hris_devices)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListHrisDevicesRequest](../../models/operations/listhrisdevicesrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListHrisDevicesResponse](../../models/operations/listhrisdevicesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_device

Updates the HrisDevice identified by `id`. Provide the unified HrisDevice fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisDevice" method="patch" path="/hris/{connection_id}/device/{id}" example="hris_device" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.device.patch_hris_device(request={
        "hris_device": {
            "admin_user_ids": [],
            "asset_tag": "fJNacaaoWi",
            "created_at": parse_datetime("2019-04-04T17:11:40.322Z"),
            "has_antivirus": True,
            "has_firewall": True,
            "has_hd_encrypted": True,
            "has_password_manager": True,
            "has_screenlock": False,
            "id": "71f60aa7-6213-43c0-9034-adf35aaa60e7",
            "is_missing": False,
            "manufacturer": "Hackett Inc",
            "metadata": [],
            "model": "Fantastic",
            "name": "august-laptop",
            "os": "transmitter",
            "os_version": "8.4.8",
            "updated_at": parse_datetime("2023-06-12T04:47:46.650Z"),
            "version": "4.15.7",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_device is not None

    # Handle response
    print(res.hris_device)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchHrisDeviceRequest](../../models/operations/patchhrisdevicerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchHrisDeviceResponse](../../models/operations/patchhrisdeviceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_device

Deletes the HrisDevice identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisDevice" method="delete" path="/hris/{connection_id}/device/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.device.remove_hris_device(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.RemoveHrisDeviceRequest](../../models/operations/removehrisdevicerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemoveHrisDeviceResponse](../../models/operations/removehrisdeviceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_device

Updates the HrisDevice identified by `id`. Provide the unified HrisDevice fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisDevice" method="put" path="/hris/{connection_id}/device/{id}" example="hris_device" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.device.update_hris_device(request={
        "hris_device": {
            "admin_user_ids": [],
            "asset_tag": "fJNacaaoWi",
            "created_at": parse_datetime("2019-04-04T17:11:40.322Z"),
            "has_antivirus": True,
            "has_firewall": True,
            "has_hd_encrypted": True,
            "has_password_manager": True,
            "has_screenlock": False,
            "id": "71f60aa7-6213-43c0-9034-adf35aaa60e7",
            "is_missing": False,
            "manufacturer": "Hackett Inc",
            "metadata": [],
            "model": "Fantastic",
            "name": "august-laptop",
            "os": "transmitter",
            "os_version": "8.4.8",
            "updated_at": parse_datetime("2023-06-12T04:47:46.650Z"),
            "version": "4.15.7",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_device is not None

    # Handle response
    print(res.hris_device)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateHrisDeviceRequest](../../models/operations/updatehrisdevicerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdateHrisDeviceResponse](../../models/operations/updatehrisdeviceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |