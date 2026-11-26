# FhirHumanName


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `family`                                                      | *Optional[str]*                                               | :heavy_minus_sign:                                            | Family name (often called surname)                            |
| `given`                                                       | List[*str*]                                                   | :heavy_minus_sign:                                            | Given names (not always first), including middle names        |
| `prefix`                                                      | List[*str*]                                                   | :heavy_minus_sign:                                            | Parts that come before the name, eg. Dr                       |
| `text`                                                        | *Optional[str]*                                               | :heavy_minus_sign:                                            | Text representation of the full name                          |
| `use`                                                         | *Optional[str]*                                               | :heavy_minus_sign:                                            | usual \| official \| temp \| nickname \| anonymous \| old \| maiden |