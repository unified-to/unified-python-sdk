# QmsAffectedItem

A part, lot or serial affected by a quality record


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `document_id`                                                     | *Optional[str]*                                                   | :heavy_minus_sign:                                                | The PlmDocument ID, when the same vendor also provides PLM        |
| `lot_number`                                                      | *Optional[str]*                                                   | :heavy_minus_sign:                                                | N/A                                                               |
| `part_id`                                                         | *Optional[str]*                                                   | :heavy_minus_sign:                                                | The PlmPart (revision) ID, when the same vendor also provides PLM |
| `part_number`                                                     | *Optional[str]*                                                   | :heavy_minus_sign:                                                | N/A                                                               |
| `quantity`                                                        | *Optional[float]*                                                 | :heavy_minus_sign:                                                | Quantity affected                                                 |
| `revision`                                                        | *Optional[str]*                                                   | :heavy_minus_sign:                                                | N/A                                                               |
| `serial_number`                                                   | *Optional[str]*                                                   | :heavy_minus_sign:                                                | N/A                                                               |