# UcFaxStatus

The current or final status of the fax

## Example Usage

```python
from unified_python_sdk.models.shared import UcFaxStatus

value = UcFaxStatus.QUEUED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `QUEUED`    | QUEUED      |
| `SENDING`   | SENDING     |
| `DELIVERED` | DELIVERED   |
| `RECEIVING` | RECEIVING   |
| `RECEIVED`  | RECEIVED    |
| `FAILED`    | FAILED      |
| `CANCELED`  | CANCELED    |
| `OTHER`     | OTHER       |