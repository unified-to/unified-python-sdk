# PropertyCrmEventEmail

The email object, when type = email


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `body`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `cc`                                                                 | List[*str*]                                                          | :heavy_minus_sign:                                                   | The event email's cc name & email (name <test@test.com>)             |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `from_`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `subject`                                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `to`                                                                 | List[*str*]                                                          | :heavy_minus_sign:                                                   | The event email's "to" name & email (name <test@test.com>)           |