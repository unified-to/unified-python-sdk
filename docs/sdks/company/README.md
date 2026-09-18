# Company

## Overview

### Available Operations

* [create_ats_company](#create_ats_company) - Create a company
* [create_crm_company](#create_crm_company) - Create a company
* [create_hris_company](#create_hris_company) - Create a company
* [get_ats_company](#get_ats_company) - Retrieve a company
* [get_crm_company](#get_crm_company) - Retrieve a company
* [get_hris_company](#get_hris_company) - Retrieve a company
* [list_ats_companies](#list_ats_companies) - List all companies
* [list_crm_companies](#list_crm_companies) - List all companies
* [list_enrich_companies](#list_enrich_companies) - Retrieve enrichment information for a company
* [list_hris_companies](#list_hris_companies) - List all companies
* [patch_ats_company](#patch_ats_company) - Update a company
* [patch_crm_company](#patch_crm_company) - Update a company
* [patch_hris_company](#patch_hris_company) - Update a company
* [remove_ats_company](#remove_ats_company) - Remove a company
* [remove_crm_company](#remove_crm_company) - Remove a company
* [remove_hris_company](#remove_hris_company) - Remove a company
* [update_ats_company](#update_ats_company) - Update a company
* [update_crm_company](#update_crm_company) - Update a company
* [update_hris_company](#update_hris_company) - Update a company

## create_ats_company

Create a company

### Example Usage

<!-- UsageSnippet language="python" operationID="createAtsCompany" method="post" path="/ats/{connection_id}/company" example="ats_company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.company.create_ats_company(request={
        "ats_company": {
            "created_at": parse_datetime("2019-04-22T03:50:02.920Z"),
            "id": "78ced29d-f1a8-4c36-b440-5b1b3a3be5ab",
            "name": "Gulgowski, Dibbert and Wilderman",
            "phone": "1-602-210-4548",
            "updated_at": parse_datetime("2020-09-24T19:30:08.481Z"),
            "website_url": "https://somber-substitution.com/",
        },
        "connection_id": "<id>",
    })

    assert res.ats_company is not None

    # Handle response
    print(res.ats_company)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateAtsCompanyRequest](../../models/operations/createatscompanyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreateAtsCompanyResponse](../../models/operations/createatscompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_crm_company

Create a company

### Example Usage

<!-- UsageSnippet language="python" operationID="createCrmCompany" method="post" path="/crm/{connection_id}/company" example="crm_company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.company.create_crm_company(request={
        "crm_company": {
            "address": {
                "address1": "7261 Salisbury Road",
                "address2": "Apt. 778",
                "city": "Harrisburg",
                "country_code": "US",
                "postal_code": "56293-3678",
                "region": "Pennsylvania",
                "region_code": "ID",
            },
            "created_at": parse_datetime("2020-05-11T18:26:32.925Z"),
            "description": "Balbus crapula spiculum.",
            "domains": [
                "fussy-nerve.info",
                "sturdy-lobster.org",
                "greedy-offset.name",
            ],
            "emails": [
                {
                    "email": "Sandrine_Jacobi@hotmail.com",
                    "type": shared.CrmEmailType.WORK,
                },
                {
                    "email": "Sandrine_Jacobi@gmail.com",
                    "type": shared.CrmEmailType.WORK,
                },
                {
                    "email": "Sandrine.Jacobi@yahoo.com",
                    "type": shared.CrmEmailType.OTHER,
                },
            ],
            "employees": 967.0,
            "id": "c3d87ef6-a153-4be2-9146-799249ea7602",
            "industry": "Infrastructure",
            "is_active": True,
            "link_urls": [
                "https://blue-license.org",
                "https://minor-formation.com",
                "https://ecstatic-hammock.com",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "948c143e-6c56-4be0-a14d-eb68e77934a6",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "esse",
                },
            ],
            "name": "Goodwin and Sons",
            "tags": [
                "quaerat",
                "valeo",
            ],
            "telephones": [
                {
                    "telephone": "(432) 849-2690",
                    "type": shared.CrmTelephoneType.MOBILE,
                },
                {
                    "telephone": "(606) 871-2046",
                    "type": shared.CrmTelephoneType.OTHER,
                },
                {
                    "telephone": "(842) 258-9395",
                    "type": shared.CrmTelephoneType.MOBILE,
                },
            ],
            "timezone": "Europe/San_Marino",
            "updated_at": parse_datetime("2025-02-06T12:33:02.290Z"),
            "websites": [
                "https://wise-possession.org",
            ],
        },
        "connection_id": "<id>",
    })

    assert res.crm_company is not None

    # Handle response
    print(res.crm_company)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateCrmCompanyRequest](../../models/operations/createcrmcompanyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreateCrmCompanyResponse](../../models/operations/createcrmcompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_hris_company

Create a company

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisCompany" method="post" path="/hris/{connection_id}/company" example="hris_company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.company.create_hris_company(request={
        "hris_company": {
            "address": {
                "address1": "2549 Church Walk",
                "city": "Lake Nettiebury",
                "country_code": "US",
                "postal_code": "32877-4898",
                "region": "Idaho",
                "region_code": "PA",
            },
            "created_at": parse_datetime("2021-05-02T22:27:38.970Z"),
            "id": "a9419166-ed13-4cc3-9ca1-f086d2325ece",
            "legal_name": "Schultz LLC",
            "name": "Gottlieb Group",
            "updated_at": parse_datetime("2026-09-05T21:10:56.918Z"),
        },
        "connection_id": "<id>",
    })

    assert res.hris_company is not None

    # Handle response
    print(res.hris_company)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateHrisCompanyRequest](../../models/operations/createhriscompanyrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateHrisCompanyResponse](../../models/operations/createhriscompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ats_company

Retrieve a company

### Example Usage

<!-- UsageSnippet language="python" operationID="getAtsCompany" method="get" path="/ats/{connection_id}/company/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.company.get_ats_company(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_company is not None

    # Handle response
    print(res.ats_company)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetAtsCompanyRequest](../../models/operations/getatscompanyrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetAtsCompanyResponse](../../models/operations/getatscompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_crm_company

Retrieve a company

### Example Usage

<!-- UsageSnippet language="python" operationID="getCrmCompany" method="get" path="/crm/{connection_id}/company/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.company.get_crm_company(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_company is not None

    # Handle response
    print(res.crm_company)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetCrmCompanyRequest](../../models/operations/getcrmcompanyrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetCrmCompanyResponse](../../models/operations/getcrmcompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_company

Retrieve a company

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisCompany" method="get" path="/hris/{connection_id}/company/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.company.get_hris_company(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_company is not None

    # Handle response
    print(res.hris_company)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetHrisCompanyRequest](../../models/operations/gethriscompanyrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetHrisCompanyResponse](../../models/operations/gethriscompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ats_companies

List all companies

### Example Usage

<!-- UsageSnippet language="python" operationID="listAtsCompanies" method="get" path="/ats/{connection_id}/company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.company.list_ats_companies(request={
        "connection_id": "<id>",
    })

    assert res.ats_companies is not None

    # Handle response
    print(res.ats_companies)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListAtsCompaniesRequest](../../models/operations/listatscompaniesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListAtsCompaniesResponse](../../models/operations/listatscompaniesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_crm_companies

List all companies

### Example Usage

<!-- UsageSnippet language="python" operationID="listCrmCompanies" method="get" path="/crm/{connection_id}/company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.company.list_crm_companies(request={
        "connection_id": "<id>",
    })

    assert res.crm_companies is not None

    # Handle response
    print(res.crm_companies)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListCrmCompaniesRequest](../../models/operations/listcrmcompaniesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListCrmCompaniesResponse](../../models/operations/listcrmcompaniesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_enrich_companies

Retrieve enrichment information for a company

### Example Usage

<!-- UsageSnippet language="python" operationID="listEnrichCompanies" method="get" path="/enrich/{connection_id}/company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.company.list_enrich_companies(request={
        "connection_id": "<id>",
    })

    assert res.enrich_company is not None

    # Handle response
    print(res.enrich_company)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListEnrichCompaniesRequest](../../models/operations/listenrichcompaniesrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListEnrichCompaniesResponse](../../models/operations/listenrichcompaniesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_companies

List all companies

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisCompanies" method="get" path="/hris/{connection_id}/company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.company.list_hris_companies(request={
        "connection_id": "<id>",
    })

    assert res.hris_companies is not None

    # Handle response
    print(res.hris_companies)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListHrisCompaniesRequest](../../models/operations/listhriscompaniesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListHrisCompaniesResponse](../../models/operations/listhriscompaniesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ats_company

Update a company

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAtsCompany" method="patch" path="/ats/{connection_id}/company/{id}" example="ats_company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.company.patch_ats_company(request={
        "ats_company": {
            "created_at": parse_datetime("2019-04-22T03:50:02.920Z"),
            "id": "5e05144a-6f51-43b6-ac5c-236493b0ba10",
            "name": "Gulgowski, Dibbert and Wilderman",
            "phone": "1-602-210-4548",
            "updated_at": parse_datetime("2020-09-24T19:30:08.483Z"),
            "website_url": "https://somber-substitution.com/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_company is not None

    # Handle response
    print(res.ats_company)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchAtsCompanyRequest](../../models/operations/patchatscompanyrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchAtsCompanyResponse](../../models/operations/patchatscompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_crm_company

Update a company

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCrmCompany" method="patch" path="/crm/{connection_id}/company/{id}" example="crm_company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.company.patch_crm_company(request={
        "crm_company": {
            "address": {
                "address1": "7261 Salisbury Road",
                "address2": "Apt. 778",
                "city": "Harrisburg",
                "country_code": "US",
                "postal_code": "56293-3678",
                "region": "Pennsylvania",
                "region_code": "ID",
            },
            "created_at": parse_datetime("2020-05-11T18:26:32.925Z"),
            "description": "Balbus crapula spiculum.",
            "domains": [
                "fussy-nerve.info",
                "sturdy-lobster.org",
                "greedy-offset.name",
            ],
            "emails": [
                {
                    "email": "Sandrine_Jacobi@hotmail.com",
                    "type": shared.CrmEmailType.WORK,
                },
                {
                    "email": "Sandrine_Jacobi@gmail.com",
                    "type": shared.CrmEmailType.WORK,
                },
                {
                    "email": "Sandrine.Jacobi@yahoo.com",
                    "type": shared.CrmEmailType.OTHER,
                },
            ],
            "employees": 967.0,
            "id": "8e971de5-5467-4203-a88e-3b58bfad2c21",
            "industry": "Infrastructure",
            "is_active": True,
            "link_urls": [
                "https://blue-license.org",
                "https://minor-formation.com",
                "https://ecstatic-hammock.com",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "7a08cf1c-5e31-4ef7-8e4b-eeb389beadc4",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "esse",
                },
            ],
            "name": "Goodwin and Sons",
            "tags": [
                "quaerat",
                "valeo",
            ],
            "telephones": [
                {
                    "telephone": "(432) 849-2690",
                    "type": shared.CrmTelephoneType.MOBILE,
                },
                {
                    "telephone": "(606) 871-2046",
                    "type": shared.CrmTelephoneType.OTHER,
                },
                {
                    "telephone": "(842) 258-9395",
                    "type": shared.CrmTelephoneType.MOBILE,
                },
            ],
            "timezone": "Europe/San_Marino",
            "updated_at": parse_datetime("2025-02-06T12:33:02.306Z"),
            "websites": [
                "https://wise-possession.org",
            ],
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_company is not None

    # Handle response
    print(res.crm_company)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchCrmCompanyRequest](../../models/operations/patchcrmcompanyrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchCrmCompanyResponse](../../models/operations/patchcrmcompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_company

Update a company

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisCompany" method="patch" path="/hris/{connection_id}/company/{id}" example="hris_company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.company.patch_hris_company(request={
        "hris_company": {
            "address": {
                "address1": "2549 Church Walk",
                "city": "Lake Nettiebury",
                "country_code": "US",
                "postal_code": "32877-4898",
                "region": "Idaho",
                "region_code": "PA",
            },
            "created_at": parse_datetime("2021-05-02T22:27:38.970Z"),
            "id": "6d8a376c-449b-4d6f-8921-ca1ab6158e9a",
            "legal_name": "Schultz LLC",
            "name": "Gottlieb Group",
            "updated_at": parse_datetime("2026-09-05T21:10:56.930Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_company is not None

    # Handle response
    print(res.hris_company)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchHrisCompanyRequest](../../models/operations/patchhriscompanyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchHrisCompanyResponse](../../models/operations/patchhriscompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ats_company

Remove a company

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAtsCompany" method="delete" path="/ats/{connection_id}/company/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.company.remove_ats_company(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.RemoveAtsCompanyRequest](../../models/operations/removeatscompanyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemoveAtsCompanyResponse](../../models/operations/removeatscompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_crm_company

Remove a company

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCrmCompany" method="delete" path="/crm/{connection_id}/company/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.company.remove_crm_company(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.RemoveCrmCompanyRequest](../../models/operations/removecrmcompanyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemoveCrmCompanyResponse](../../models/operations/removecrmcompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_company

Remove a company

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisCompany" method="delete" path="/hris/{connection_id}/company/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.company.remove_hris_company(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveHrisCompanyRequest](../../models/operations/removehriscompanyrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveHrisCompanyResponse](../../models/operations/removehriscompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ats_company

Update a company

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAtsCompany" method="put" path="/ats/{connection_id}/company/{id}" example="ats_company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.company.update_ats_company(request={
        "ats_company": {
            "created_at": parse_datetime("2019-04-22T03:50:02.920Z"),
            "id": "5e05144a-6f51-43b6-ac5c-236493b0ba10",
            "name": "Gulgowski, Dibbert and Wilderman",
            "phone": "1-602-210-4548",
            "updated_at": parse_datetime("2020-09-24T19:30:08.483Z"),
            "website_url": "https://somber-substitution.com/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_company is not None

    # Handle response
    print(res.ats_company)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateAtsCompanyRequest](../../models/operations/updateatscompanyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdateAtsCompanyResponse](../../models/operations/updateatscompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_crm_company

Update a company

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCrmCompany" method="put" path="/crm/{connection_id}/company/{id}" example="crm_company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.company.update_crm_company(request={
        "crm_company": {
            "address": {
                "address1": "7261 Salisbury Road",
                "address2": "Apt. 778",
                "city": "Harrisburg",
                "country_code": "US",
                "postal_code": "56293-3678",
                "region": "Pennsylvania",
                "region_code": "ID",
            },
            "created_at": parse_datetime("2020-05-11T18:26:32.925Z"),
            "description": "Balbus crapula spiculum.",
            "domains": [
                "fussy-nerve.info",
                "sturdy-lobster.org",
                "greedy-offset.name",
            ],
            "emails": [
                {
                    "email": "Sandrine_Jacobi@hotmail.com",
                    "type": shared.CrmEmailType.WORK,
                },
                {
                    "email": "Sandrine_Jacobi@gmail.com",
                    "type": shared.CrmEmailType.WORK,
                },
                {
                    "email": "Sandrine.Jacobi@yahoo.com",
                    "type": shared.CrmEmailType.OTHER,
                },
            ],
            "employees": 967.0,
            "id": "8e971de5-5467-4203-a88e-3b58bfad2c21",
            "industry": "Infrastructure",
            "is_active": True,
            "link_urls": [
                "https://blue-license.org",
                "https://minor-formation.com",
                "https://ecstatic-hammock.com",
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "7a08cf1c-5e31-4ef7-8e4b-eeb389beadc4",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "esse",
                },
            ],
            "name": "Goodwin and Sons",
            "tags": [
                "quaerat",
                "valeo",
            ],
            "telephones": [
                {
                    "telephone": "(432) 849-2690",
                    "type": shared.CrmTelephoneType.MOBILE,
                },
                {
                    "telephone": "(606) 871-2046",
                    "type": shared.CrmTelephoneType.OTHER,
                },
                {
                    "telephone": "(842) 258-9395",
                    "type": shared.CrmTelephoneType.MOBILE,
                },
            ],
            "timezone": "Europe/San_Marino",
            "updated_at": parse_datetime("2025-02-06T12:33:02.306Z"),
            "websites": [
                "https://wise-possession.org",
            ],
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_company is not None

    # Handle response
    print(res.crm_company)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateCrmCompanyRequest](../../models/operations/updatecrmcompanyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdateCrmCompanyResponse](../../models/operations/updatecrmcompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_company

Update a company

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisCompany" method="put" path="/hris/{connection_id}/company/{id}" example="hris_company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.company.update_hris_company(request={
        "hris_company": {
            "address": {
                "address1": "2549 Church Walk",
                "city": "Lake Nettiebury",
                "country_code": "US",
                "postal_code": "32877-4898",
                "region": "Idaho",
                "region_code": "PA",
            },
            "created_at": parse_datetime("2021-05-02T22:27:38.970Z"),
            "id": "6d8a376c-449b-4d6f-8921-ca1ab6158e9a",
            "legal_name": "Schultz LLC",
            "name": "Gottlieb Group",
            "updated_at": parse_datetime("2026-09-05T21:10:56.930Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_company is not None

    # Handle response
    print(res.hris_company)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateHrisCompanyRequest](../../models/operations/updatehriscompanyrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateHrisCompanyResponse](../../models/operations/updatehriscompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |