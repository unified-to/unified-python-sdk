# Item
(*item*)

### Available Operations

* [create_commerce_item](#create_commerce_item) - Create an item
* [get_commerce_item](#get_commerce_item) - Retrieve an item
* [list_commerce_items](#list_commerce_items) - List all items
* [patch_commerce_item](#patch_commerce_item) - Update an item
* [remove_commerce_item](#remove_commerce_item) - Remove an item
* [update_commerce_item](#update_commerce_item) - Update an item

## create_commerce_item

Create an item

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateCommerceItemRequest(
    connection_id='<value>',
)

res = s.item.create_commerce_item(req, operations.CreateCommerceItemSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateCommerceItemRequest](../../models/operations/createcommerceitemrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.CreateCommerceItemSecurity](../../models/operations/createcommerceitemsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.CreateCommerceItemResponse](../../models/operations/createcommerceitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_commerce_item

Retrieve an item

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCommerceItemRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.item.get_commerce_item(req, operations.GetCommerceItemSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetCommerceItemRequest](../../models/operations/getcommerceitemrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.GetCommerceItemSecurity](../../models/operations/getcommerceitemsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.GetCommerceItemResponse](../../models/operations/getcommerceitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_commerce_items

List all items

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListCommerceItemsRequest(
    connection_id='<value>',
)

res = s.item.list_commerce_items(req, operations.ListCommerceItemsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_items is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListCommerceItemsRequest](../../models/operations/listcommerceitemsrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.ListCommerceItemsSecurity](../../models/operations/listcommerceitemssecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.ListCommerceItemsResponse](../../models/operations/listcommerceitemsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_commerce_item

Update an item

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchCommerceItemRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.item.patch_commerce_item(req, operations.PatchCommerceItemSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchCommerceItemRequest](../../models/operations/patchcommerceitemrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.PatchCommerceItemSecurity](../../models/operations/patchcommerceitemsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.PatchCommerceItemResponse](../../models/operations/patchcommerceitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_commerce_item

Remove an item

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveCommerceItemRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.item.remove_commerce_item(req, operations.RemoveCommerceItemSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.RemoveCommerceItemRequest](../../models/operations/removecommerceitemrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.RemoveCommerceItemSecurity](../../models/operations/removecommerceitemsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.RemoveCommerceItemResponse](../../models/operations/removecommerceitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_commerce_item

Update an item

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateCommerceItemRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.item.update_commerce_item(req, operations.UpdateCommerceItemSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateCommerceItemRequest](../../models/operations/updatecommerceitemrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.UpdateCommerceItemSecurity](../../models/operations/updatecommerceitemsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.UpdateCommerceItemResponse](../../models/operations/updatecommerceitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
