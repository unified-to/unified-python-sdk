<!-- Start SDK Example Usage [usage] -->
```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.CreateAccountingAccountRequest(
    connection_id='string',
)

res = s.accounting.create_accounting_account(req)

if res.accounting_account is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->