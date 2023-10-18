<!-- Start SDK Example Usage -->


```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetUnifiedApicallRequest(
    id='<ID>',
)

res = s.apicall.get_unified_apicall(req)

if res.api_call is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->