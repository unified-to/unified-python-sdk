# TenderType

normalized tender category; the provider's original label stays in payment_method

## Example Usage

```python
from unified_python_sdk.models.shared import TenderType

value = TenderType.CARD

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                | Value               |
| ------------------- | ------------------- |
| `CARD`              | CARD                |
| `CASH`              | CASH                |
| `GIFT_CARD`         | GIFT_CARD           |
| `BANK_TRANSFER`     | BANK_TRANSFER       |
| `WALLET`            | WALLET              |
| `CHECK`             | CHECK               |
| `STORE_CREDIT`      | STORE_CREDIT        |
| `BUY_NOW_PAY_LATER` | BUY_NOW_PAY_LATER   |
| `EXTERNAL`          | EXTERNAL            |
| `OTHER`             | OTHER               |