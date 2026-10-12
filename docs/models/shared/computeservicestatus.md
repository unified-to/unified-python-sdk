# ComputeServiceStatus

Normalized status; set to SUSPENDED or LIVE on update to suspend or resume

## Example Usage

```python
from unified_python_sdk.models.shared import ComputeServiceStatus

value = ComputeServiceStatus.CREATING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `CREATING`  | CREATING    |
| `DEPLOYING` | DEPLOYING   |
| `LIVE`      | LIVE        |
| `SUSPENDED` | SUSPENDED   |
| `FAILED`    | FAILED      |
| `OTHER`     | OTHER       |