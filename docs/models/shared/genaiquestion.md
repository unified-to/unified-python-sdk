# GenaiQuestion


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `id`                                                                          | *str*                                                                         | :heavy_check_mark:                                                            | A caller-chosen key; the matching answer is returned with the same id.        |
| `instructions`                                                                | *str*                                                                         | :heavy_check_mark:                                                            | The question to evaluate.                                                     |
| `options`                                                                     | List[*str*]                                                                   | :heavy_minus_sign:                                                            | CHOICE: the options to select from; SCORE: the ordered levels (lowest first). |
| `type`                                                                        | [shared.GenaiQuestionType](../../models/shared/genaiquestiontype.md)          | :heavy_check_mark:                                                            | N/A                                                                           |