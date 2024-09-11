# CreateUcContactRequest


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `connection_id`                                                         | *str*                                                                   | :heavy_check_mark:                                                      | ID of the connection                                                    |
| `uc_contact`                                                            | [Optional[shared.UcContact]](../../models/shared/uccontact.md)          | :heavy_minus_sign:                                                      | A contact represents a person that optionally is associated with a call |
| `fields`                                                                | List[*str*]                                                             | :heavy_minus_sign:                                                      | Comma-delimited fields to return                                        |