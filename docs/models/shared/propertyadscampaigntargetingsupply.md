# PropertyAdsCampaignTargetingSupply

Buy-side inventory: exchanges, deals, deal groups and seller authorization (DSPs)


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `authorized_seller_status`                                                               | [Optional[shared.AuthorizedSellerStatus]](../../models/shared/authorizedsellerstatus.md) | :heavy_minus_sign:                                                                       | ads.txt seller authorization to buy from                                                 |
| `deal_groups`                                                                            | List[[shared.TargetRef](../../models/shared/targetref.md)]                               | :heavy_minus_sign:                                                                       | Groups of deals (ads_target type DEAL_GROUP)                                             |
| `deals`                                                                                  | List[[shared.TargetRef](../../models/shared/targetref.md)]                               | :heavy_minus_sign:                                                                       | Deals / inventory packages (ads_target type DEAL)                                        |
| `exchanges`                                                                              | List[[shared.TargetRef](../../models/shared/targetref.md)]                               | :heavy_minus_sign:                                                                       | Public exchanges to buy on (ads_target type EXCHANGE)                                    |