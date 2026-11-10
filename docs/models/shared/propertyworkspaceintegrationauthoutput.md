# PropertyWorkspaceIntegrationAuthOutput


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `client_id`                                                        | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | N/A                                                                |
| `consumer_key`                                                     | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | N/A                                                                |
| `needs_pkce`                                                       | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | opt-in PKCE for OAuth2 when the integration app or org requires it |
| `saml_idp_entity_id`                                               | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | the SAML IdP issuer/entity ID                                      |
| `saml_idp_url`                                                     | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | the SAML IdP SSO/login URL for end-user SAML login                 |
| `saml_pem`                                                         | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | the SAML IdP signing certificate; PEM X.509 in Base64 ASCII format |