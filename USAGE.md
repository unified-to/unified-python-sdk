<!-- Start SDK Example Usage [usage] -->
```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.CreateAccountingAccountRequest(
    accounting_account=shared.AccountingAccount(
        name='string',
        raw=shared.PropertyAccountingAccountRaw(),
    ),
    connection_id='string',
)

res = s.accounting.create_accounting_account(req)

if res.accounting_account is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->