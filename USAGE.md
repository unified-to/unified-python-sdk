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
            "currency": "BOB",
            "customer_defined_code": "quo",
            "description": "Spoliatio comedo vilitas harum cupiditate.",
            "id": "fe4277ef-5da1-4ca9-9359-50f8d62f8e9f",
            "is_payable": True,
            "name": "Electronic Aluminum Tuna",
            "status": shared.Status.ARCHIVED,
            "taxonomy": [
                {
                    "original_type": "vesper",
                    "type": shared.AccountingAccountTaxonomyType.SUBGROUP,
                    "value": "iste",
                },
                {
                    "original_type": "adamo",
                    "type": shared.AccountingAccountTaxonomyType.SUBGROUP,
                    "value": "peccatus",
                },
            ],
            "type": shared.Type.BANK,
            "updated_at": parse_datetime("2023-01-03T11:11:55.467Z"),
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
                "currency": "BOB",
                "customer_defined_code": "quo",
                "description": "Spoliatio comedo vilitas harum cupiditate.",
                "id": "fe4277ef-5da1-4ca9-9359-50f8d62f8e9f",
                "is_payable": True,
                "name": "Electronic Aluminum Tuna",
                "status": shared.Status.ARCHIVED,
                "taxonomy": [
                    {
                        "original_type": "vesper",
                        "type": shared.AccountingAccountTaxonomyType.SUBGROUP,
                        "value": "iste",
                    },
                    {
                        "original_type": "adamo",
                        "type": shared.AccountingAccountTaxonomyType.SUBGROUP,
                        "value": "peccatus",
                    },
                ],
                "type": shared.Type.BANK,
                "updated_at": parse_datetime("2023-01-03T11:11:55.467Z"),
            },
            "connection_id": "<id>",
        })

        assert res.accounting_account is not None

        # Handle response
        print(res.accounting_account)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->