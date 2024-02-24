# Organization
(*organization*)

### Available Operations

* [get_accounting_organization](#get_accounting_organization) - Retrieve an organization
* [list_accounting_organizations](#list_accounting_organizations) - List all organizations

## get_accounting_organization

Retrieve an organization

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAccountingOrganizationRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.organization.get_accounting_organization(req, operations.GetAccountingOrganizationSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_organization is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetAccountingOrganizationRequest](../../models/operations/getaccountingorganizationrequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.GetAccountingOrganizationSecurity](../../models/operations/getaccountingorganizationsecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.GetAccountingOrganizationResponse](../../models/operations/getaccountingorganizationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_accounting_organizations

List all organizations

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAccountingOrganizationsRequest(
    connection_id='<value>',
)

res = s.organization.list_accounting_organizations(req, operations.ListAccountingOrganizationsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_organizations is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.ListAccountingOrganizationsRequest](../../models/operations/listaccountingorganizationsrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.ListAccountingOrganizationsSecurity](../../models/operations/listaccountingorganizationssecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.ListAccountingOrganizationsResponse](../../models/operations/listaccountingorganizationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
