# PropertyFhirEncounterClass

Classification of patient encounter


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `code`                                                             | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Classification of patient encounter, eg. AMB, EMER, IMP, VR        |
| `extension`                                                        | List[[shared.FhirExtension](../../models/shared/fhirextension.md)] | :heavy_minus_sign:                                                 | data-absent-reason when the encounter class is unknown             |
| `system`                                                           | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Identity of the terminology system (v3-ActCode)                    |