# PropertyShippingShipmentToAddress

Destination address


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `address1`                                 | *Optional[str]*                            | :heavy_minus_sign:                         | N/A                                        |
| `address2`                                 | *Optional[str]*                            | :heavy_minus_sign:                         | N/A                                        |
| `city`                                     | *Optional[str]*                            | :heavy_minus_sign:                         | N/A                                        |
| `company_name`                             | *Optional[str]*                            | :heavy_minus_sign:                         | Company name (for commercial addresses)    |
| `country`                                  | *Optional[str]*                            | :heavy_minus_sign:                         | N/A                                        |
| `country_code`                             | *Optional[str]*                            | :heavy_minus_sign:                         | ISO 2-digit country code                   |
| `delivery_instructions`                    | *Optional[str]*                            | :heavy_minus_sign:                         | Special delivery notes                     |
| `email`                                    | *Optional[str]*                            | :heavy_minus_sign:                         | Email address (for delivery notifications) |
| `is_residential`                           | *Optional[bool]*                           | :heavy_minus_sign:                         | Alias for address_type === 'RESIDENTIAL'   |
| `is_validated`                             | *Optional[bool]*                           | :heavy_minus_sign:                         | Whether address has been validated         |
| `name`                                     | *Optional[str]*                            | :heavy_minus_sign:                         | Recipientsender name                       |
| `postal_code`                              | *Optional[str]*                            | :heavy_minus_sign:                         | N/A                                        |
| `region`                                   | *Optional[str]*                            | :heavy_minus_sign:                         | N/A                                        |
| `region_code`                              | *Optional[str]*                            | :heavy_minus_sign:                         | N/A                                        |
| `telephone`                                | *Optional[str]*                            | :heavy_minus_sign:                         | Phone number (required by FedEx, UPS, DHL) |