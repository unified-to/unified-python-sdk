<!-- Start SDK Example Usage -->


```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.CreateTicketingAgentRequest(
    ticketing_agent=shared.TicketingAgent(
        emails=[
            shared.TicketingEmail(
                email='Paolo.Cole8@yahoo.com',
            ),
        ],
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='scarcely Soap navigating',
            ),
        ],
    ),
    connection_id='smoothly Algeria',
)

res = s.agent.create_ticketing_agent(req)

if res.ticketing_agent is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->