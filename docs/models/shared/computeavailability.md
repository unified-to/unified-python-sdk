# ComputeAvailability


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `level`                                                    | [Optional[shared.Level]](../../models/shared/level.md)     | :heavy_minus_sign:                                         | Normalized stock level                                     |
| `quantity`                                                 | *Optional[float]*                                          | :heavy_minus_sign:                                         | Number of units available, when the vendor reports a count |
| `region_id`                                                | *Optional[str]*                                            | :heavy_minus_sign:                                         | The region this availability applies to                    |