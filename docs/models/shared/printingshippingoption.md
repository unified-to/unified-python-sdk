# PrintingShippingoption

A shipping method available for a quote, with its price


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `amount`                                                    | *Optional[float]*                                           | :heavy_minus_sign:                                          | Shipping price                                              |
| `code`                                                      | *Optional[str]*                                             | :heavy_minus_sign:                                          | Shipping method code, used as `shipping_method` on an order |
| `currency`                                                  | *Optional[str]*                                             | :heavy_minus_sign:                                          | ISO 4217 currency code                                      |
| `max_delivery_days`                                         | *Optional[float]*                                           | :heavy_minus_sign:                                          | Estimated maximum number of days to delivery                |
| `min_delivery_days`                                         | *Optional[float]*                                           | :heavy_minus_sign:                                          | Estimated minimum number of days to delivery                |
| `name`                                                      | *Optional[str]*                                             | :heavy_minus_sign:                                          | Display name                                                |