<!-- Start SDK Example Usage [usage] -->
```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.accounting.create_accounting_account(request=operations.CreateAccountingAccountRequest(
    connection_id='<value>',
))

if res.accounting_account is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->