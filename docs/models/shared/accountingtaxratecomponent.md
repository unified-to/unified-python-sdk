# AccountingTaxrateComponent


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `is_compound`                                                      | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | True when this component is charged on top of the other components |
| `name`                                                             | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Name of the tax component, e.g. GST or PST                         |
| `rate`                                                             | *Optional[float]*                                                  | :heavy_minus_sign:                                                 | Rate of this component, in %                                       |