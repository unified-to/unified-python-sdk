# UcCallStatus

The current or final status of the call

## Example Usage

```python
from unified_python_sdk.models.shared import UcCallStatus

value = UcCallStatus.QUEUED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `QUEUED`      | QUEUED        |
| `RINGING`     | RINGING       |
| `IN_PROGRESS` | IN_PROGRESS   |
| `COMPLETED`   | COMPLETED     |
| `BUSY`        | BUSY          |
| `NO_ANSWER`   | NO_ANSWER     |
| `FAILED`      | FAILED        |
| `CANCELED`    | CANCELED      |
| `OTHER`       | OTHER         |