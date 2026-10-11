# PaymentCollectionMethod

When set to charging_automatically, an automated attempt will occur to pay this invoice using the default payment source attached to the contactcustomer. When set to send_invoice, an will email will be sent with this invoice to the contact/customer with payment instructions.

## Example Usage

```python
from unified_python_sdk.models.shared import PaymentCollectionMethod

value = PaymentCollectionMethod.SEND_INVOICE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                   | Value                  |
| ---------------------- | ---------------------- |
| `SEND_INVOICE`         | send_invoice           |
| `CHARGE_AUTOMATICALLY` | charge_automatically   |