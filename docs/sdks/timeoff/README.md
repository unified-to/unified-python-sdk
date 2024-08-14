# Timeoff
(*timeoff*)

### Available Operations

* [get_hris_timeoff](#get_hris_timeoff) - Retrieve a timeoff
* [list_hris_timeoffs](#list_hris_timeoffs) - List all timeoffs

## get_hris_timeoff

Retrieve a timeoff

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.timeoff.get_hris_timeoff(request=operations.GetHrisTimeoffRequest(
    connection_id='<value>',
    id='<id>',
))

if res.hris_timeoff is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetHrisTimeoffRequest](../../models/operations/gethristimeoffrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetHrisTimeoffResponse](../../models/operations/gethristimeoffresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_hris_timeoffs

List all timeoffs

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.timeoff.list_hris_timeoffs(request=operations.ListHrisTimeoffsRequest(
    connection_id='<value>',
))

if res.hris_timeoffs is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListHrisTimeoffsRequest](../../models/operations/listhristimeoffsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ListHrisTimeoffsResponse](../../models/operations/listhristimeoffsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
