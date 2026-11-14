# QmsCharacteristic

A characteristic measured or checked during an inspection


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `lower_limit`                                            | *Optional[float]*                                        | :heavy_minus_sign:                                       | N/A                                                      |
| `measured_value`                                         | *Optional[str]*                                          | :heavy_minus_sign:                                       | Measured or observed value; text so attribute checks fit |
| `name`                                                   | *Optional[str]*                                          | :heavy_minus_sign:                                       | N/A                                                      |
| `nominal_value`                                          | *Optional[float]*                                        | :heavy_minus_sign:                                       | N/A                                                      |
| `notes`                                                  | *Optional[str]*                                          | :heavy_minus_sign:                                       | N/A                                                      |
| `result`                                                 | [Optional[shared.Result]](../../models/shared/result.md) | :heavy_minus_sign:                                       | N/A                                                      |
| `specification`                                          | *Optional[str]*                                          | :heavy_minus_sign:                                       | Requirement or drawing reference                         |
| `unit_of_measure`                                        | *Optional[str]*                                          | :heavy_minus_sign:                                       | N/A                                                      |
| `upper_limit`                                            | *Optional[float]*                                        | :heavy_minus_sign:                                       | N/A                                                      |