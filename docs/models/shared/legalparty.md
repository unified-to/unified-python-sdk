# LegalParty


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `company_id`                                                             | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | pointer to a CRM Company                                                 |
| `contact_id`                                                             | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | pointer to a CRM Contact                                                 |
| `description`                                                            | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | the vendor's free-text relationship description                          |
| `role`                                                                   | [Optional[shared.LegalPartyRole]](../../models/shared/legalpartyrole.md) | :heavy_minus_sign:                                                       | the party role on the matter                                             |