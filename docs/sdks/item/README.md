# Item
(*item*)

### Available Operations

* [create_commerce_item](#create_commerce_item) - Create an item/product
* [get_commerce_item](#get_commerce_item) - Retrieve an item/product
* [list_commerce_items](#list_commerce_items) - List all items/products
* [patch_commerce_item](#patch_commerce_item) - Update an item/product
* [remove_commerce_item](#remove_commerce_item) - Remove an item/product
* [update_commerce_item](#update_commerce_item) - Update an item/product

## create_commerce_item

Create an item/product

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.CreateCommerceItemRequest(
    commerce_item=shared.CommerceItem(
        media=[
            shared.CommerceItemMedia(
                url='http://loud-minister.name',
            ),
        ],
        name='string',
        raw={
            'key': 'string',
        },
        tags=[
            'string',
        ],
        variants=[
            shared.CommerceItemVariant(
                media=[
                    shared.CommerceItemMedia(
                        url='http://other-external.info',
                    ),
                ],
                name='string',
                options=[
                    shared.CommerceItemOption(
                        id='<ID>',
                        name='string',
                        values=[
                            'string',
                        ],
                    ),
                ],
                prices=[
                    shared.CommerceItemPrice(
                        price=3330.74,
                    ),
                ],
                tags=[
                    'string',
                ],
            ),
        ],
    ),
    connection_id='string',
)

res = s.item.create_commerce_item(req)

if res.commerce_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateCommerceItemRequest](../../models/operations/createcommerceitemrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreateCommerceItemResponse](../../models/operations/createcommerceitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_commerce_item

Retrieve an item/product

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.GetCommerceItemRequest(
    connection_id='string',
    fields=[
        'string',
    ],
    id='<ID>',
)

res = s.item.get_commerce_item(req)

if res.commerce_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetCommerceItemRequest](../../models/operations/getcommerceitemrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetCommerceItemResponse](../../models/operations/getcommerceitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_commerce_items

List all items/products

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.ListCommerceItemsRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.item.list_commerce_items(req)

if res.commerce_items is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListCommerceItemsRequest](../../models/operations/listcommerceitemsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.ListCommerceItemsResponse](../../models/operations/listcommerceitemsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_commerce_item

Update an item/product

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.PatchCommerceItemRequest(
    commerce_item=shared.CommerceItem(
        media=[
            shared.CommerceItemMedia(
                url='http://frank-galley.biz',
            ),
        ],
        name='string',
        raw={
            'key': 'string',
        },
        tags=[
            'string',
        ],
        variants=[
            shared.CommerceItemVariant(
                media=[
                    shared.CommerceItemMedia(
                        url='http://irresponsible-reason.biz',
                    ),
                ],
                name='string',
                options=[
                    shared.CommerceItemOption(
                        id='<ID>',
                        name='string',
                        values=[
                            'string',
                        ],
                    ),
                ],
                prices=[
                    shared.CommerceItemPrice(
                        price=4506.62,
                    ),
                ],
                tags=[
                    'string',
                ],
            ),
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.item.patch_commerce_item(req)

if res.commerce_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchCommerceItemRequest](../../models/operations/patchcommerceitemrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.PatchCommerceItemResponse](../../models/operations/patchcommerceitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_commerce_item

Remove an item/product

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.RemoveCommerceItemRequest(
    connection_id='string',
    id='<ID>',
)

res = s.item.remove_commerce_item(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveCommerceItemRequest](../../models/operations/removecommerceitemrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.RemoveCommerceItemResponse](../../models/operations/removecommerceitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_commerce_item

Update an item/product

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.UpdateCommerceItemRequest(
    commerce_item=shared.CommerceItem(
        media=[
            shared.CommerceItemMedia(
                url='https://aggressive-major-league.org',
            ),
        ],
        name='string',
        raw={
            'key': 'string',
        },
        tags=[
            'string',
        ],
        variants=[
            shared.CommerceItemVariant(
                media=[
                    shared.CommerceItemMedia(
                        url='https://reasonable-cast.biz',
                    ),
                ],
                name='string',
                options=[
                    shared.CommerceItemOption(
                        id='<ID>',
                        name='string',
                        values=[
                            'string',
                        ],
                    ),
                ],
                prices=[
                    shared.CommerceItemPrice(
                        price=8467.25,
                    ),
                ],
                tags=[
                    'string',
                ],
            ),
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.item.update_commerce_item(req)

if res.commerce_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateCommerceItemRequest](../../models/operations/updatecommerceitemrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.UpdateCommerceItemResponse](../../models/operations/updatecommerceitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
