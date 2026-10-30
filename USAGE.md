<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_account(request={
        "accounting_account": {
            "balance": 12092.0,
            "created_at": parse_datetime("2022-07-03T17:57:07.391Z"),
            "currency": "CAD",
            "customer_defined_code": "6170",
            "description": "Voluptatibus valde spoliatio.",
            "id": "427e8dd8-1c54-4931-b853-9b3c8b5596a6",
            "is_payable": False,
            "metadata": [],
            "name": "Auto Loan Account",
            "status": shared.Status.ARCHIVED,
            "taxonomy": [
                {
                    "original_type": "vilitas",
                    "type": shared.AccountingAccountTaxonomyType.SUBGROUP,
                    "value": "comedo",
                },
            ],
            "type": shared.Type.ACCOUNTS_RECEIVABLE,
            "updated_at": parse_datetime("2023-08-09T04:48:43.304Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_account is not None

    # Handle response
    print(res.accounting_account)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime

async def main():

    async with UnifiedTo(
        security=shared.Security(
            jwt="<YOUR_API_KEY_HERE>",
        ),
    ) as unified_to:

        res = await unified_to.accounting.create_accounting_account_async(request={
            "accounting_account": {
                "balance": 12092.0,
                "created_at": parse_datetime("2022-07-03T17:57:07.391Z"),
                "currency": "CAD",
                "customer_defined_code": "6170",
                "description": "Voluptatibus valde spoliatio.",
                "id": "427e8dd8-1c54-4931-b853-9b3c8b5596a6",
                "is_payable": False,
                "metadata": [],
                "name": "Auto Loan Account",
                "status": shared.Status.ARCHIVED,
                "taxonomy": [
                    {
                        "original_type": "vilitas",
                        "type": shared.AccountingAccountTaxonomyType.SUBGROUP,
                        "value": "comedo",
                    },
                ],
                "type": shared.Type.ACCOUNTS_RECEIVABLE,
                "updated_at": parse_datetime("2023-08-09T04:48:43.304Z"),
            },
            "connection_id": "<id>",
        })

        assert res.accounting_account is not None

        # Handle response
        print(res.accounting_account)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->