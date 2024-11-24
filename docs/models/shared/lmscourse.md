# LmsCourse


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `categories`                                                         | List[*str*]                                                          | :heavy_minus_sign:                                                   | N/A                                                                  |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `currency`                                                           | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `description`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `instructor_ids`                                                     | List[*str*]                                                          | :heavy_minus_sign:                                                   | N/A                                                                  |
| `is_active`                                                          | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | N/A                                                                  |
| `is_private`                                                         | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | N/A                                                                  |
| `languages`                                                          | List[*str*]                                                          | :heavy_minus_sign:                                                   | N/A                                                                  |
| `media`                                                              | List[[shared.LmsMedia](../../models/shared/lmsmedia.md)]             | :heavy_minus_sign:                                                   | N/A                                                                  |
| `price_amount`                                                       | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | N/A                                                                  |
| `raw`                                                                | Dict[str, *Any*]                                                     | :heavy_minus_sign:                                                   | N/A                                                                  |
| `student_ids`                                                        | List[*str*]                                                          | :heavy_minus_sign:                                                   | N/A                                                                  |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |