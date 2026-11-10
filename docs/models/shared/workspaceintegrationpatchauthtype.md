# WorkspaceIntegrationPatchAuthType

the authentication method to use for this workspace integration; when set, it overrides the default auth-method selection (e.g. force 'token' even when Unified OAUTH credentials exist)

## Example Usage

```python
from unified_python_sdk.models.shared import WorkspaceIntegrationPatchAuthType

value = WorkspaceIntegrationPatchAuthType.OAUTH2

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `OAUTH2` | oauth2   |
| `OTHER`  | other    |
| `TOKEN`  | token    |