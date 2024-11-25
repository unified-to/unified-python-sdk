# CreatePassthroughRawRequest


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `connection_id`                                        | *str*                                                  | :heavy_check_mark:                                     | ID of the connection                                   |
| `path`                                                 | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `request_body`                                         | *Optional[Union[bytes, IO[bytes], io.BufferedReader]]* | :heavy_minus_sign:                                     | integration-specific payload                           |