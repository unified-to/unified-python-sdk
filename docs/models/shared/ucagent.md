# UcAgent

Represents an agent


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `created_at`                                                                 | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_minus_sign:                                                           | N/A                                                                          |
| `emails`                                                                     | list[[UcEmail](../../models/shared/ucemail.md)]                              | :heavy_minus_sign:                                                           | An array of email addresses for this agent                                   |
| `id`                                                                         | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `name`                                                                       | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `raw`                                                                        | [PropertyUcAgentRaw](../../models/shared/propertyucagentraw.md)              | :heavy_check_mark:                                                           | The raw data returned by the integration for this agent                      |
| `telephones`                                                                 | list[[UcTelephone](../../models/shared/uctelephone.md)]                      | :heavy_minus_sign:                                                           | N/A                                                                          |
| `updated_at`                                                                 | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_minus_sign:                                                           | N/A                                                                          |