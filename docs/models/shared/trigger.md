# Trigger

What started the deployment

## Example Usage

```python
from unified_python_sdk.models.shared import Trigger

value = Trigger.GIT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `GIT`      | GIT        |
| `MANUAL`   | MANUAL     |
| `API`      | API        |
| `ROLLBACK` | ROLLBACK   |
| `OTHER`    | OTHER      |