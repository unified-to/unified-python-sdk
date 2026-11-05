# CalendarBotStatus

## Example Usage

```python
from unified_python_sdk.models.shared import CalendarBotStatus

value = CalendarBotStatus.READY

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                           | Value                          |
| ------------------------------ | ------------------------------ |
| `READY`                        | READY                          |
| `JOINING_CALL`                 | JOINING_CALL                   |
| `IN_WAITING_ROOM`              | IN_WAITING_ROOM                |
| `IN_CALL_NOT_RECORDING`        | IN_CALL_NOT_RECORDING          |
| `RECORDING_PERMISSION_ALLOWED` | RECORDING_PERMISSION_ALLOWED   |
| `RECORDING_PERMISSION_DENIED`  | RECORDING_PERMISSION_DENIED    |
| `IN_CALL_RECORDING`            | IN_CALL_RECORDING              |
| `CALL_ENDED`                   | CALL_ENDED                     |
| `DONE`                         | DONE                           |
| `FATAL`                        | FATAL                          |