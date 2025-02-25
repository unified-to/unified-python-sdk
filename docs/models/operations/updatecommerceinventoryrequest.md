# UpdateCommerceInventoryRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `commerce_inventory`                                                 | [shared.CommerceInventory](../../models/shared/commerceinventory.md) | :heavy_check_mark:                                                   | N/A                                                                  |
| `connection_id`                                                      | *str*                                                                | :heavy_check_mark:                                                   | ID of the connection                                                 |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | ID of the Inventory                                                  |
| `fields`                                                             | List[*str*]                                                          | :heavy_minus_sign:                                                   | Comma-delimited fields to return                                     |