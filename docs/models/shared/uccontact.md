# UcContact

A contact represents a person that optionally is associated with a call


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `company`                                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `emails`                                                             | List[[shared.UcEmail](../../models/shared/ucemail.md)]               | :heavy_minus_sign:                                                   | An array of email addresses for this contact                         |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `name`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `raw`                                                                | Dict[str, *Any*]                                                     | :heavy_minus_sign:                                                   | N/A                                                                  |
| `telephones`                                                         | List[[shared.UcTelephone](../../models/shared/uctelephone.md)]       | :heavy_minus_sign:                                                   | An array of telephones for this contact                              |
| `title`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |