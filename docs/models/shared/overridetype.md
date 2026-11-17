# OverrideType

replaces the calculated withholding with a flat amount or percentage

## Example Usage

```python
from unified_python_sdk.models.shared import OverrideType

value = OverrideType.NONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `NONE`         | NONE           |
| `FIXED_AMOUNT` | FIXED_AMOUNT   |
| `PERCENT`      | PERCENT        |