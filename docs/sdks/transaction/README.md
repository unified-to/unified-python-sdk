# Transaction
(*transaction*)

### Available Operations

* [create_accounting_transaction](#create_accounting_transaction) - Create a transaction
* [get_accounting_transaction](#get_accounting_transaction) - Retrieve a transaction
* [list_accounting_transactions](#list_accounting_transactions) - List all transactions
* [patch_accounting_transaction](#patch_accounting_transaction) - Update a transaction
* [remove_accounting_transaction](#remove_accounting_transaction) - Remove a transaction
* [update_accounting_transaction](#update_accounting_transaction) - Update a transaction

## create_accounting_transaction

Create a transaction

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateAccountingTransactionRequest(
    connection_id='<value>',
)

res = s.transaction.create_accounting_transaction(req, operations.CreateAccountingTransactionSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_transaction is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.CreateAccountingTransactionRequest](../../models/operations/createaccountingtransactionrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.CreateAccountingTransactionSecurity](../../models/operations/createaccountingtransactionsecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.CreateAccountingTransactionResponse](../../models/operations/createaccountingtransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_accounting_transaction

Retrieve a transaction

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAccountingTransactionRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.transaction.get_accounting_transaction(req, operations.GetAccountingTransactionSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_transaction is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetAccountingTransactionRequest](../../models/operations/getaccountingtransactionrequest.md)   | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.GetAccountingTransactionSecurity](../../models/operations/getaccountingtransactionsecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |


### Response

**[operations.GetAccountingTransactionResponse](../../models/operations/getaccountingtransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_accounting_transactions

List all transactions

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAccountingTransactionsRequest(
    connection_id='<value>',
)

res = s.transaction.list_accounting_transactions(req, operations.ListAccountingTransactionsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_transactions is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.ListAccountingTransactionsRequest](../../models/operations/listaccountingtransactionsrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.ListAccountingTransactionsSecurity](../../models/operations/listaccountingtransactionssecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.ListAccountingTransactionsResponse](../../models/operations/listaccountingtransactionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_accounting_transaction

Update a transaction

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchAccountingTransactionRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.transaction.patch_accounting_transaction(req, operations.PatchAccountingTransactionSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_transaction is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PatchAccountingTransactionRequest](../../models/operations/patchaccountingtransactionrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.PatchAccountingTransactionSecurity](../../models/operations/patchaccountingtransactionsecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.PatchAccountingTransactionResponse](../../models/operations/patchaccountingtransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_accounting_transaction

Remove a transaction

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveAccountingTransactionRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.transaction.remove_accounting_transaction(req, operations.RemoveAccountingTransactionSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.RemoveAccountingTransactionRequest](../../models/operations/removeaccountingtransactionrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.RemoveAccountingTransactionSecurity](../../models/operations/removeaccountingtransactionsecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.RemoveAccountingTransactionResponse](../../models/operations/removeaccountingtransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_accounting_transaction

Update a transaction

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateAccountingTransactionRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.transaction.update_accounting_transaction(req, operations.UpdateAccountingTransactionSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_transaction is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.UpdateAccountingTransactionRequest](../../models/operations/updateaccountingtransactionrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.UpdateAccountingTransactionSecurity](../../models/operations/updateaccountingtransactionsecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.UpdateAccountingTransactionResponse](../../models/operations/updateaccountingtransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
