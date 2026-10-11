# WebhookType

"native" registers with the integration, which sends events as they happen. "virtual" checks for changes on "interval". Optional on create; if omitted, Unified.to picks a supported type for the object. Requesting a type the integration doesn't support returns 400. Set on create only: changes sent on update are ignored without an error. Delete and recreate the webhook to change type.

## Example Usage

```python
from unified_python_sdk.models.shared import WebhookType

value = WebhookType.VIRTUAL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `VIRTUAL` | virtual   |
| `NATIVE`  | native    |