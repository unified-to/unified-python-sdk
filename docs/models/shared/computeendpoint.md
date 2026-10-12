# ComputeEndpoint


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `is_auth_required`                                           | *Optional[bool]*                                             | :heavy_minus_sign:                                           | Whether the URL requires a vendor access token               |
| `port`                                                       | *Optional[float]*                                            | :heavy_minus_sign:                                           | The port inside the instance                                 |
| `protocol`                                                   | [Optional[shared.Protocol]](../../models/shared/protocol.md) | :heavy_minus_sign:                                           | The protocol served on this port                             |
| `url`                                                        | *Optional[str]*                                              | :heavy_minus_sign:                                           | Public or proxied URL for this port                          |