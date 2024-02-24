# Taxrate
(*taxrate*)

### Available Operations

* [create_accounting_taxrate](#create_accounting_taxrate) - Create a taxrate
* [get_accounting_taxrate](#get_accounting_taxrate) - Retrieve a taxrate
* [list_accounting_taxrates](#list_accounting_taxrates) - List all taxrates
* [patch_accounting_taxrate](#patch_accounting_taxrate) - Update a taxrate
* [remove_accounting_taxrate](#remove_accounting_taxrate) - Remove a taxrate
* [update_accounting_taxrate](#update_accounting_taxrate) - Update a taxrate

## create_accounting_taxrate

Create a taxrate

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateAccountingTaxrateRequest(
    connection_id='<value>',
)

res = s.taxrate.create_accounting_taxrate(req, operations.CreateAccountingTaxrateSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_taxrate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateAccountingTaxrateRequest](../../models/operations/createaccountingtaxraterequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.CreateAccountingTaxrateSecurity](../../models/operations/createaccountingtaxratesecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.CreateAccountingTaxrateResponse](../../models/operations/createaccountingtaxrateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_accounting_taxrate

Retrieve a taxrate

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAccountingTaxrateRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.taxrate.get_accounting_taxrate(req, operations.GetAccountingTaxrateSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_taxrate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetAccountingTaxrateRequest](../../models/operations/getaccountingtaxraterequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.GetAccountingTaxrateSecurity](../../models/operations/getaccountingtaxratesecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.GetAccountingTaxrateResponse](../../models/operations/getaccountingtaxrateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_accounting_taxrates

List all taxrates

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAccountingTaxratesRequest(
    connection_id='<value>',
)

res = s.taxrate.list_accounting_taxrates(req, operations.ListAccountingTaxratesSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_taxrates is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListAccountingTaxratesRequest](../../models/operations/listaccountingtaxratesrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.ListAccountingTaxratesSecurity](../../models/operations/listaccountingtaxratessecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.ListAccountingTaxratesResponse](../../models/operations/listaccountingtaxratesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_accounting_taxrate

Update a taxrate

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchAccountingTaxrateRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.taxrate.patch_accounting_taxrate(req, operations.PatchAccountingTaxrateSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_taxrate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PatchAccountingTaxrateRequest](../../models/operations/patchaccountingtaxraterequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.PatchAccountingTaxrateSecurity](../../models/operations/patchaccountingtaxratesecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.PatchAccountingTaxrateResponse](../../models/operations/patchaccountingtaxrateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_accounting_taxrate

Remove a taxrate

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveAccountingTaxrateRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.taxrate.remove_accounting_taxrate(req, operations.RemoveAccountingTaxrateSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RemoveAccountingTaxrateRequest](../../models/operations/removeaccountingtaxraterequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.RemoveAccountingTaxrateSecurity](../../models/operations/removeaccountingtaxratesecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.RemoveAccountingTaxrateResponse](../../models/operations/removeaccountingtaxrateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_accounting_taxrate

Update a taxrate

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateAccountingTaxrateRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.taxrate.update_accounting_taxrate(req, operations.UpdateAccountingTaxrateSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_taxrate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateAccountingTaxrateRequest](../../models/operations/updateaccountingtaxraterequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.UpdateAccountingTaxrateSecurity](../../models/operations/updateaccountingtaxratesecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.UpdateAccountingTaxrateResponse](../../models/operations/updateaccountingtaxrateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
