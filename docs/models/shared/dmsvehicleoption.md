# DmsVehicleOption

An installed vehicle option or package


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `code`                                                                               | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | Option or RPO code                                                                   |
| `cost_amount`                                                                        | *Optional[float]*                                                                    | :heavy_minus_sign:                                                                   | Dealer cost                                                                          |
| `description`                                                                        | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | N/A                                                                                  |
| `price_amount`                                                                       | *Optional[float]*                                                                    | :heavy_minus_sign:                                                                   | Retail price                                                                         |
| `type`                                                                               | [Optional[shared.DmsVehicleOptionType]](../../models/shared/dmsvehicleoptiontype.md) | :heavy_minus_sign:                                                                   | Factory-fitted or dealer-added                                                       |