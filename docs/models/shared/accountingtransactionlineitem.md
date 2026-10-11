# AccountingTransactionLineItem


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `account_id`                                                   | *Optional[str]*                                                | :heavy_minus_sign:                                             | (reference to AccountingAccount)                               |
| `category_ids`                                                 | List[*str*]                                                    | :heavy_minus_sign:                                             | N/A                                                            |
| `description`                                                  | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            |
| `id`                                                           | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            |
| `name`                                                         | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            |
| `object_type`                                                  | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            |
| `taxrate_id`                                                   | *Optional[str]*                                                | :heavy_minus_sign:                                             | ref -> AccountingTaxrate applied to the line                   |
| `total_amount`                                                 | *Optional[float]*                                              | :heavy_minus_sign:                                             | will be a positive value for a debit and negative for a credit |
| `unit_amount`                                                  | *Optional[float]*                                              | :heavy_minus_sign:                                             | N/A                                                            |
| `unit_quantity`                                                | *Optional[float]*                                              | :heavy_minus_sign:                                             | N/A                                                            |