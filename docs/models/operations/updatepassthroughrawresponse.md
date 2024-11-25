# UpdatePassthroughRawResponse


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `content_type`                                               | *str*                                                        | :heavy_check_mark:                                           | HTTP response content type for this operation                |
| `headers`                                                    | Dict[str, List[*str*]]                                       | :heavy_check_mark:                                           | N/A                                                          |
| `status_code`                                                | *int*                                                        | :heavy_check_mark:                                           | HTTP response status code for this operation                 |
| `raw_response`                                               | [httpx.Response](https://www.python-httpx.org/api/#response) | :heavy_check_mark:                                           | Raw HTTP response; suitable for custom response parsing      |
| `default_wildcard_wildcard_response_stream`                  | *Optional[httpx.Response]*                                   | :heavy_minus_sign:                                           | Successful                                                   |
| `default_application_json_any`                               | *Optional[Any]*                                              | :heavy_minus_sign:                                           | Successful                                                   |
| `default_application_xml_res`                                | *Optional[str]*                                              | :heavy_minus_sign:                                           | Successful                                                   |
| `default_text_csv_res`                                       | *Optional[str]*                                              | :heavy_minus_sign:                                           | Successful                                                   |
| `default_text_plain_res`                                     | *Optional[str]*                                              | :heavy_minus_sign:                                           | Successful                                                   |