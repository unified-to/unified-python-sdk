<!-- Start SDK Example Usage -->


```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteTicketingConnectionIDAgentIDRequest(
    connection_id='corrupti',
    id='9bd9d8d6-9a67-44e0-b467-cc8796ed151a',
)

res = s.agent.delete_ticketing_connection_id_agent_id(req, operations.DeleteTicketingConnectionIDAgentIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->