<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.accounting.create_accounting_account(request={
    "connection_id": "<value>",
})

if res.accounting_account is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from unified_python_sdk import UnifiedTo

async def main():
    s = UnifiedTo()
    res = await s.accounting.create_accounting_account_async(request={
        "connection_id": "<value>",
    })
    if res.accounting_account is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->