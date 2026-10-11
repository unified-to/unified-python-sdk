# CdpConsent


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `purpose`                                                                         | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | The consent purpose or objective (eg. marketing, analytics)                       |
| `status`                                                                          | [Optional[shared.CdpConsentStatus]](../../models/shared/cdpconsentstatus.md)      | :heavy_minus_sign:                                                                | The consent status for this purpose                                               |
| `updated_at`                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)              | :heavy_minus_sign:                                                                | When the consent status was last updated (ISO-8601 / YYYY-MM-DDTHH:MM:SSZ format) |