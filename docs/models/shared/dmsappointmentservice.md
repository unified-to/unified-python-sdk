# DmsAppointmentService

A service requested on an appointment


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `complaint`                                                | *Optional[str]*                                            | :heavy_minus_sign:                                         | Customer's own words                                       |
| `estimate_amount`                                          | *Optional[float]*                                          | :heavy_minus_sign:                                         | Estimated price                                            |
| `estimated_hours`                                          | *Optional[float]*                                          | :heavy_minus_sign:                                         | N/A                                                        |
| `id`                                                       | *Optional[str]*                                            | :heavy_minus_sign:                                         | Line identifier                                            |
| `name`                                                     | *Optional[str]*                                            | :heavy_minus_sign:                                         | Service or operation description                           |
| `opcode_id`                                                | *Optional[str]*                                            | :heavy_minus_sign:                                         | The DmsOpcode ID                                           |
| `pay_type`                                                 | [Optional[shared.PayType]](../../models/shared/paytype.md) | :heavy_minus_sign:                                         | N/A                                                        |
| `technician_user_ids`                                      | List[*str*]                                                | :heavy_minus_sign:                                         | Pre-assigned technicians, as HR Employees                  |