# UpdateAccountingInvoiceRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `accounting_invoice`                                                 | [shared.AccountingInvoice](../../models/shared/accountinginvoice.md) | :heavy_check_mark:                                                   | N/A                                                                  |
| `connection_id`                                                      | *str*                                                                | :heavy_check_mark:                                                   | ID of the connection                                                 |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | ID of the Invoice                                                    |
| `fields`                                                             | List[*str*]                                                          | :heavy_minus_sign:                                                   | Comma-delimited fields to return                                     |