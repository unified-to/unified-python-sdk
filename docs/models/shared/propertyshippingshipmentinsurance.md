# PropertyShippingShipmentInsurance

Insurance details


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `coverage_amount`                                                    | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Coverage amount (may differ from insured_value)                      |
| `coverage_type`                                                      | [Optional[shared.CoverageType]](../../models/shared/coveragetype.md) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `currency`                                                           | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `insurance_cost`                                                     | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Cost of insurance                                                    |
| `insurance_cost_currency`                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `insurance_provider`                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Insurance provider name                                              |
| `insurance_provider_code`                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Provider code                                                        |
| `insured_value`                                                      | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Insured value                                                        |