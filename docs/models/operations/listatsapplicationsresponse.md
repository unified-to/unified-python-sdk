# ListAtsApplicationsResponse


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `ats_applications`                                                                    | List[[shared.AtsApplication](../../models/shared/atsapplication.md)]                  | :heavy_minus_sign:                                                                    | Successful                                                                            |
| `content_type`                                                                        | *str*                                                                                 | :heavy_check_mark:                                                                    | HTTP response content type for this operation                                         |
| `status_code`                                                                         | *int*                                                                                 | :heavy_check_mark:                                                                    | HTTP response status code for this operation                                          |
| `raw_response`                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_minus_sign:                                                                    | Raw HTTP response; suitable for custom response parsing                               |