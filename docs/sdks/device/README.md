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

Create a device

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
            "asset_tag": "dpho9OuFNG",
            "created_at": parse_datetime("2019-04-04T17:11:40.322Z"),
            "has_antivirus": False,
            "has_firewall": True,
            "has_hd_encrypted": True,
            "has_password_manager": True,
            "has_screenlock": True,
            "id": "e592d58c-449d-47c3-b4f2-cc9f41866826",
            "is_missing": False,
            "manufacturer": "Sanford - Hamill",
            "model": "Refined",
            "name": "cross_contamination_if.rar",
            "os": "monitor",
            "os_version": "1.12.16",
            "updated_at": parse_datetime("2023-05-22T14:06:09.513Z"),
            "version": "2.20.17",
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

Retrieve a device

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

List all devices

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

Update a device

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
            "asset_tag": "dpho9OuFNG",
            "created_at": parse_datetime("2019-04-04T17:11:40.322Z"),
            "has_antivirus": False,
            "has_firewall": True,
            "has_hd_encrypted": True,
            "has_password_manager": True,
            "has_screenlock": True,
            "id": "52148932-32c0-49fe-bd1f-9a5c66b73d70",
            "is_missing": False,
            "manufacturer": "Sanford - Hamill",
            "model": "Refined",
            "name": "cross_contamination_if.rar",
            "os": "monitor",
            "os_version": "1.12.16",
            "updated_at": parse_datetime("2023-05-22T14:06:09.520Z"),
            "version": "2.20.17",
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

Remove a device

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

Update a device

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
            "asset_tag": "dpho9OuFNG",
            "created_at": parse_datetime("2019-04-04T17:11:40.322Z"),
            "has_antivirus": False,
            "has_firewall": True,
            "has_hd_encrypted": True,
            "has_password_manager": True,
            "has_screenlock": True,
            "id": "52148932-32c0-49fe-bd1f-9a5c66b73d70",
            "is_missing": False,
            "manufacturer": "Sanford - Hamill",
            "model": "Refined",
            "name": "cross_contamination_if.rar",
            "os": "monitor",
            "os_version": "1.12.16",
            "updated_at": parse_datetime("2023-05-22T14:06:09.520Z"),
            "version": "2.20.17",
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