# Issue
(*issue*)

### Available Operations

* [list_unified_issues](#list_unified_issues) - List support issues

## list_unified_issues

List support issues

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListUnifiedIssuesRequest()

res = s.issue.list_unified_issues(req, operations.ListUnifiedIssuesSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.issues is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListUnifiedIssuesRequest](../../models/operations/listunifiedissuesrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.ListUnifiedIssuesSecurity](../../models/operations/listunifiedissuessecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.ListUnifiedIssuesResponse](../../models/operations/listunifiedissuesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
