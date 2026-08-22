# Event

## Example Usage

```python
from unified_python_sdk.models.shared import Event

value = Event.USER_CREATED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                         | Value                        |
| ---------------------------- | ---------------------------- |
| `USER_CREATED`               | USER_CREATED                 |
| `USER_DELETED`               | USER_DELETED                 |
| `CONNECTION_HEALTHY`         | CONNECTION_HEALTHY           |
| `CONNECTION_UNHEALTHY`       | CONNECTION_UNHEALTHY         |
| `CONNECTION_CREATED`         | CONNECTION_CREATED           |
| `CONNECTION_UPDATED`         | CONNECTION_UPDATED           |
| `CONNECTION_DELETED`         | CONNECTION_DELETED           |
| `CONNECTION_PAUSED`          | CONNECTION_PAUSED            |
| `CONNECTION_UNPAUSED`        | CONNECTION_UNPAUSED          |
| `INTEGRATION_ACTIVATED`      | INTEGRATION_ACTIVATED        |
| `INTEGRATION_DEACTIVATED`    | INTEGRATION_DEACTIVATED      |
| `INTEGRATION_UPDATED`        | INTEGRATION_UPDATED          |
| `WORKSPACE_UPDATED`          | WORKSPACE_UPDATED            |
| `WORKSPACE_OVER_LIMIT`       | WORKSPACE_OVER_LIMIT         |
| `WORKSPACE_80_PERCENT_LIMIT` | WORKSPACE_80PERCENT_LIMIT    |
| `WEBHOOK_CREATED`            | WEBHOOK_CREATED              |
| `WEBHOOK_DELETED`            | WEBHOOK_DELETED              |
| `WEBHOOK_UNHEALTHY`          | WEBHOOK_UNHEALTHY            |
| `WEBHOOK_PAUSED`             | WEBHOOK_PAUSED               |
| `WEBHOOK_UNPAUSED`           | WEBHOOK_UNPAUSED             |