# ComputeInstanceStatus

Normalized lifecycle status; set on update to start, stop, pause, resume, restart or terminate

## Example Usage

```python
from unified_python_sdk.models.shared import ComputeInstanceStatus

value = ComputeInstanceStatus.PROVISIONING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `PROVISIONING` | PROVISIONING   |
| `STARTING`     | STARTING       |
| `RUNNING`      | RUNNING        |
| `STOPPING`     | STOPPING       |
| `STOPPED`      | STOPPED        |
| `PAUSING`      | PAUSING        |
| `PAUSED`       | PAUSED         |
| `RESUMING`     | RESUMING       |
| `RESTARTING`   | RESTARTING     |
| `TERMINATING`  | TERMINATING    |
| `TERMINATED`   | TERMINATED     |
| `PREEMPTED`    | PREEMPTED      |
| `ERROR`        | ERROR          |
| `OTHER`        | OTHER          |