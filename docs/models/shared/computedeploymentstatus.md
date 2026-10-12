# ComputeDeploymentStatus

Normalized deployment status; set to CANCELED on update to cancel

## Example Usage

```python
from unified_python_sdk.models.shared import ComputeDeploymentStatus

value = ComputeDeploymentStatus.QUEUED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `QUEUED`     | QUEUED       |
| `BUILDING`   | BUILDING     |
| `DEPLOYING`  | DEPLOYING    |
| `LIVE`       | LIVE         |
| `FAILED`     | FAILED       |
| `CANCELED`   | CANCELED     |
| `SUPERSEDED` | SUPERSEDED   |
| `OTHER`      | OTHER        |