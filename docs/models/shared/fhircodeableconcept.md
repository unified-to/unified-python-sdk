# FhirCodeableConcept


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `coding`                                                              | List[[shared.FhirCoding](../../models/shared/fhircoding.md)]          | :heavy_minus_sign:                                                    | Codes defined by a terminology system                                 |
| `extension`                                                           | List[[shared.FhirExtension](../../models/shared/fhirextension.md)]    | :heavy_minus_sign:                                                    | Extensions, eg. data-absent-reason when a required concept is unknown |
| `text`                                                                | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Plain text representation of the concept                              |