# PatchSigningDocumentResponse


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `content_type`                                                             | *str*                                                                      | :heavy_check_mark:                                                         | HTTP response content type for this operation                              |
| `signing_document`                                                         | [Optional[shared.SigningDocument]](../../models/shared/signingdocument.md) | :heavy_minus_sign:                                                         | Successful                                                                 |
| `status_code`                                                              | *int*                                                                      | :heavy_check_mark:                                                         | HTTP response status code for this operation                               |
| `raw_response`                                                             | [httpx.Response](https://www.python-httpx.org/api/#response)               | :heavy_check_mark:                                                         | Raw HTTP response; suitable for custom response parsing                    |