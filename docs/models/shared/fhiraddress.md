# FhirAddress


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `city`                                            | *Optional[str]*                                   | :heavy_minus_sign:                                | Name of city, town etc.                           |
| `country`                                         | *Optional[str]*                                   | :heavy_minus_sign:                                | Country (e.g. can be ISO 3166 2 or 3 letter code) |
| `line`                                            | List[*str*]                                       | :heavy_minus_sign:                                | Street name, number, direction and P.O. Box etc.  |
| `postal_code`                                     | *Optional[str]*                                   | :heavy_minus_sign:                                | Postal code for area                              |
| `state`                                           | *Optional[str]*                                   | :heavy_minus_sign:                                | Sub-unit of country (abbreviations ok)            |
| `type`                                            | *Optional[str]*                                   | :heavy_minus_sign:                                | postal \| physical \| both                        |
| `use`                                             | *Optional[str]*                                   | :heavy_minus_sign:                                | home \| work \| temp \| old \| billing            |