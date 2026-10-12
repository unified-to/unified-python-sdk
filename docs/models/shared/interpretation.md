# Interpretation

Interpretation of the result (e.g. high, low)

## Example Usage

```python
from unified_python_sdk.models.shared import Interpretation

value = Interpretation.NORMAL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `NORMAL`        | NORMAL          |
| `ABNORMAL`      | ABNORMAL        |
| `LOW`           | LOW             |
| `HIGH`          | HIGH            |
| `CRITICAL_LOW`  | CRITICAL_LOW    |
| `CRITICAL_HIGH` | CRITICAL_HIGH   |
| `OTHER`         | OTHER           |