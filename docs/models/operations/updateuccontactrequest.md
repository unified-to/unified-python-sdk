# UpdateUcContactRequest


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `uc_contact`                                                            | [shared.UcContact](../../models/shared/uccontact.md)                    | :heavy_check_mark:                                                      | A contact represents a person that optionally is associated with a call |
| `connection_id`                                                         | *str*                                                                   | :heavy_check_mark:                                                      | ID of the connection                                                    |
| `fields`                                                                | List[*str*]                                                             | :heavy_minus_sign:                                                      | Comma-delimited fields to return                                        |
| `id`                                                                    | *str*                                                                   | :heavy_check_mark:                                                      | ID of the Contact                                                       |