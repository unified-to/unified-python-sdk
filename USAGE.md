<!-- Start SDK Example Usage -->


```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.CreateAccountingCustomerRequest(
    accounting_customer=shared.AccountingCustomer(
        billing_address=shared.PropertyAccountingCustomerBillingAddress(),
        emails=[
            shared.AccountingEmail(
                email='Kevon_Schultz42@gmail.com',
            ),
        ],
        raw=shared.PropertyAccountingCustomerRaw(),
        shipping_address=shared.PropertyAccountingCustomerShippingAddress(),
        telephones=[
            shared.AccountingTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
)

res = s.accounting.create_accounting_customer(req)

if res.accounting_customer is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->