<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_account(request={
        "accounting_account": {},
        "connection_id": "<id>",
    })

    assert res.accounting_account is not None

    # Handle response
    print(res.accounting_account)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

async def main():

    async with UnifiedTo(
        security=shared.Security(
            jwt="<YOUR_API_KEY_HERE>",
        ),
    ) as unified_to:

        res = await unified_to.accounting.create_accounting_account_async(request={
            "accounting_account": {},
            "connection_id": "<id>",
        })

        assert res.accounting_account is not None

        # Handle response
        print(res.accounting_account)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->