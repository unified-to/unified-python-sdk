# DmsVehiclesaleTradein

A vehicle traded in on a vehicle sale


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `actual_cash_value_amount`                       | *Optional[float]*                                | :heavy_minus_sign:                               | Actual cash value (dealer valuation)             |
| `allowance_amount`                               | *Optional[float]*                                | :heavy_minus_sign:                               | Trade allowance given to the buyer               |
| `lienholder_name`                                | *Optional[str]*                                  | :heavy_minus_sign:                               | Lender owed the payoff                           |
| `make`                                           | *Optional[str]*                                  | :heavy_minus_sign:                               | N/A                                              |
| `model`                                          | *Optional[str]*                                  | :heavy_minus_sign:                               | N/A                                              |
| `odometer`                                       | *Optional[float]*                                | :heavy_minus_sign:                               | N/A                                              |
| `payoff_amount`                                  | *Optional[float]*                                | :heavy_minus_sign:                               | Outstanding loan payoff                          |
| `vehicle_id`                                     | *Optional[str]*                                  | :heavy_minus_sign:                               | The DmsVehicle ID of the trade-in, when recorded |
| `vin`                                            | *Optional[str]*                                  | :heavy_minus_sign:                               | N/A                                              |
| `year`                                           | *Optional[float]*                                | :heavy_minus_sign:                               | N/A                                              |