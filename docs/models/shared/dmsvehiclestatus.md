# DmsVehicleStatus

Stock status; only set for inventory units

## Example Usage

```python
from unified_python_sdk.models.shared import DmsVehicleStatus

value = DmsVehicleStatus.AVAILABLE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `AVAILABLE`   | AVAILABLE     |
| `ON_ORDER`    | ON_ORDER      |
| `IN_TRANSIT`  | IN_TRANSIT    |
| `RESERVED`    | RESERVED      |
| `SOLD`        | SOLD          |
| `UNAVAILABLE` | UNAVAILABLE   |
| `OTHER`       | OTHER         |