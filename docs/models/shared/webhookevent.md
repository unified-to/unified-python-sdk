# WebhookEvent

The event to subscribe to. "deleted" is supported on native webhooks, and on virtual webhooks where the integration supports it. Check the integration's Feature Support tab.

## Example Usage

```python
from unified_python_sdk.models.shared import WebhookEvent

value = WebhookEvent.UPDATED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `UPDATED` | updated   |
| `CREATED` | created   |
| `DELETED` | deleted   |