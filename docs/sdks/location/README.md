# Location
(*location*)

### Available Operations

* [create_commerce_location](#create_commerce_location) - Create a location
* [get_commerce_location](#get_commerce_location) - Retrieve a location
* [list_commerce_locations](#list_commerce_locations) - List all locations
* [patch_commerce_location](#patch_commerce_location) - Update a location
* [remove_commerce_location](#remove_commerce_location) - Remove a location
* [update_commerce_location](#update_commerce_location) - Update a location

## create_commerce_location

Create a location

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateCommerceLocationRequest(
    connection_id='<value>',
)

res = s.location.create_commerce_location(req, operations.CreateCommerceLocationSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_location is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateCommerceLocationRequest](../../models/operations/createcommercelocationrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.CreateCommerceLocationSecurity](../../models/operations/createcommercelocationsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.CreateCommerceLocationResponse](../../models/operations/createcommercelocationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_commerce_location

Retrieve a location

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCommerceLocationRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.location.get_commerce_location(req, operations.GetCommerceLocationSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_location is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetCommerceLocationRequest](../../models/operations/getcommercelocationrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.GetCommerceLocationSecurity](../../models/operations/getcommercelocationsecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.GetCommerceLocationResponse](../../models/operations/getcommercelocationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_commerce_locations

List all locations

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListCommerceLocationsRequest(
    connection_id='<value>',
)

res = s.location.list_commerce_locations(req, operations.ListCommerceLocationsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_locations is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListCommerceLocationsRequest](../../models/operations/listcommercelocationsrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.ListCommerceLocationsSecurity](../../models/operations/listcommercelocationssecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.ListCommerceLocationsResponse](../../models/operations/listcommercelocationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_commerce_location

Update a location

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchCommerceLocationRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.location.patch_commerce_location(req, operations.PatchCommerceLocationSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_location is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchCommerceLocationRequest](../../models/operations/patchcommercelocationrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.PatchCommerceLocationSecurity](../../models/operations/patchcommercelocationsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.PatchCommerceLocationResponse](../../models/operations/patchcommercelocationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_commerce_location

Remove a location

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveCommerceLocationRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.location.remove_commerce_location(req, operations.RemoveCommerceLocationSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveCommerceLocationRequest](../../models/operations/removecommercelocationrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.RemoveCommerceLocationSecurity](../../models/operations/removecommercelocationsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.RemoveCommerceLocationResponse](../../models/operations/removecommercelocationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_commerce_location

Update a location

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateCommerceLocationRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.location.update_commerce_location(req, operations.UpdateCommerceLocationSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_location is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateCommerceLocationRequest](../../models/operations/updatecommercelocationrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.UpdateCommerceLocationSecurity](../../models/operations/updatecommercelocationsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.UpdateCommerceLocationResponse](../../models/operations/updatecommercelocationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
