# PrintingShipment

A shipment of a print order


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `carrier`                                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Carrier name                                                         |
| `delivered_at`                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | (ISO-8601 / YYYY-MM-DDTHH:MM:SSZ format)                             |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Shipment identifier                                                  |
| `service`                                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Delivery service name                                                |
| `shipped_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | (ISO-8601 / YYYY-MM-DDTHH:MM:SSZ format)                             |
| `tracking_number`                                                    | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `tracking_url`                                                       | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |