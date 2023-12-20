# Login
(*login*)

### Available Operations

* [get_unified_integration_login](#get_unified_integration_login) - Sign in a user

## get_unified_integration_login

Returns an authentication URL for the specified integration.  Once a successful authentication occurs, the name and email are returned inside a jwt parameter, which is a JSON web token that is base-64 encoded.

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.GetUnifiedIntegrationLoginRequest(
    integration_type='string',
    workspace_id='string',
)

res = s.login.get_unified_integration_login(req)

if res.res is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetUnifiedIntegrationLoginRequest](../../models/operations/getunifiedintegrationloginrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetUnifiedIntegrationLoginResponse](../../models/operations/getunifiedintegrationloginresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
