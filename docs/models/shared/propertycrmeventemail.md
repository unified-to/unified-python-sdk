# PropertyCrmEventEmail

The email object, when type = email


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `attachment_file_ids`                                              | List[*str*]                                                        | :heavy_minus_sign:                                                 | N/A                                                                |
| `body`                                                             | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The event email's body                                             |
| `cc`                                                               | List[*str*]                                                        | :heavy_minus_sign:                                                 | The event email's cc name & email (name <test@test.com>)           |
| `from_`                                                            | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The event email's from name & email address (name <test@test.com>) |
| `subject`                                                          | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The event email's subject                                          |
| `to`                                                               | List[*str*]                                                        | :heavy_minus_sign:                                                 | The event email's "to" name & email (name <test@test.com>)         |