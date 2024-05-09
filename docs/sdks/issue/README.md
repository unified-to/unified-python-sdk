# Issue
(*issue*)

### Available Operations

* [list_unified_issues](#list_unified_issues) - List support issues
* [list_unified_supports](#list_unified_supports) - Get support info

## list_unified_issues

List support issues

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

res = s.issue.list_unified_issues(request=operations.ListUnifiedIssuesRequest())

if res.issues is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListUnifiedIssuesRequest](../../models/operations/listunifiedissuesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.ListUnifiedIssuesResponse](../../models/operations/listunifiedissuesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_unified_supports

Get support info

### Example Usage

```python
import unified_to
from unified_to.models import shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

res = s.issue.list_unified_supports()

if res.undefined is not None:
    # handle response
    pass

```


### Response

**[operations.ListUnifiedSupportsResponse](../../models/operations/listunifiedsupportsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
