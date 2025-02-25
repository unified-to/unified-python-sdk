# PatchAccountingTaxrateRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `accounting_taxrate`                                                 | [shared.AccountingTaxrate](../../models/shared/accountingtaxrate.md) | :heavy_check_mark:                                                   | N/A                                                                  |
| `connection_id`                                                      | *str*                                                                | :heavy_check_mark:                                                   | ID of the connection                                                 |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | ID of the Taxrate                                                    |
| `fields`                                                             | List[*str*]                                                          | :heavy_minus_sign:                                                   | Comma-delimited fields to return                                     |