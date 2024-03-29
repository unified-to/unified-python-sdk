# MarketingMember

A member represents a person


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `emails`                                                             | List[[shared.MarketingEmail](../../models/shared/marketingemail.md)] | :heavy_minus_sign:                                                   | An array of email addresses for this member                          |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `list_ids`                                                           | List[*str*]                                                          | :heavy_minus_sign:                                                   | An array of list IDs associated with this member                     |
| `name`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `raw`                                                                | Dict[str, *Any*]                                                     | :heavy_minus_sign:                                                   | The raw data returned by the integration for this member             |
| `tags`                                                               | List[*str*]                                                          | :heavy_minus_sign:                                                   | An array of tags associated with this member                         |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |