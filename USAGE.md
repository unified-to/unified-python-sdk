<!-- Start SDK Example Usage -->


```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteTicketingConnectionIDAgentIDRequest(
    connection_id='navigate',
    id='<ID>',
)

res = s.agent.delete_ticketing_connection_id_agent_id(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->