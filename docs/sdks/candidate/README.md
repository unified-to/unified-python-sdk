# Candidate

## Overview

### Available Operations

* [create_ats_candidate](#create_ats_candidate) - Create a candidate
* [get_ats_candidate](#get_ats_candidate) - Retrieve a candidate
* [list_ats_candidates](#list_ats_candidates) - List all candidates
* [patch_ats_candidate](#patch_ats_candidate) - Update a candidate
* [remove_ats_candidate](#remove_ats_candidate) - Remove a candidate
* [update_ats_candidate](#update_ats_candidate) - Update a candidate

## create_ats_candidate

Create a candidate

### Example Usage

<!-- UsageSnippet language="python" operationID="createAtsCandidate" method="post" path="/ats/{connection_id}/candidate" example="ats_candidate" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.candidate.create_ats_candidate(request={
        "ats_candidate": {
            "address": {
                "address1": "802 Roberts Squares",
                "address2": "Suite 550",
                "city": "Lake Raeganside",
                "country_code": "US",
                "postal_code": "44530-0054",
                "region": "Tennessee",
                "region_code": "NV",
            },
            "company_name": "Ferry, Legros and Feest",
            "created_at": parse_datetime("2023-10-16T05:42:56.049Z"),
            "education": [
                {
                    "degree": "mouser throughout",
                    "end_at": parse_datetime("1992-11-28T20:23:20.311Z"),
                    "field_of_study": "solutio",
                    "institution": "Heller - Lubowitz",
                    "level": "phd",
                    "start_at": parse_datetime("2001-03-26T08:12:11.510Z"),
                },
            ],
            "emails": [
                {
                    "email": "Ardith.Beatty@hotmail.com",
                    "name": "Opal Lindgren",
                    "type": shared.AtsEmailType.WORK,
                },
                {
                    "email": "Ardith_Beatty@gmail.com",
                    "name": "Kristi Nader",
                    "type": shared.AtsEmailType.OTHER,
                },
            ],
            "experiences": [
                {
                    "company_name": "Donnelly, Buckridge and Steuber",
                    "end_at": parse_datetime("1978-06-20T02:53:48.383Z"),
                    "start_at": parse_datetime("1980-02-06T17:16:53.798Z"),
                    "title": "Principal Brand Strategist",
                },
            ],
            "first_name": "Ardith",
            "id": "68c3fd3c-5615-4542-abde-7a32f3ba0366",
            "image_url": "https://loremflickr.com/40/3693?lock=5634712403880328",
            "job_ids": [],
            "last_name": "Beatty",
            "link_urls": [
                "https://sizzling-legislature.com",
                "https://soupy-interchange.net",
                "https://troubled-substitution.info",
            ],
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "96d1a861-579d-4484-a904-2fe8c8784c66",
                    "namespace": "custom",
                    "slug": "custom_field",
                    "value": "cariosus",
                },
            ],
            "name": "Ardith Beatty",
            "origin": shared.Origin.SOURCED,
            "skills": [
                "vita",
                "cohors",
            ],
            "sources": [
                "tactus",
            ],
            "summary": "Denego barba rerum similique via templum totam suus voluptatem. Depraedor virgo cui comminor commodi curvo. Chirographum pax spero nostrum damnatio averto pecus cervus aspicio absens.",
            "tags": [
                "aliquid",
            ],
            "telephones": [
                {
                    "telephone": "(779) 296-5994",
                    "type": shared.AtsTelephoneType.HOME,
                },
            ],
            "title": "Principal Implementation Analyst",
            "updated_at": parse_datetime("2024-04-23T02:43:11.790Z"),
            "web_url": "https://expert-lender.name/",
        },
        "connection_id": "<id>",
    })

    assert res.ats_candidate is not None

    # Handle response
    print(res.ats_candidate)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateAtsCandidateRequest](../../models/operations/createatscandidaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateAtsCandidateResponse](../../models/operations/createatscandidateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ats_candidate

Retrieve a candidate

### Example Usage

<!-- UsageSnippet language="python" operationID="getAtsCandidate" method="get" path="/ats/{connection_id}/candidate/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.candidate.get_ats_candidate(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_candidate is not None

    # Handle response
    print(res.ats_candidate)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetAtsCandidateRequest](../../models/operations/getatscandidaterequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetAtsCandidateResponse](../../models/operations/getatscandidateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ats_candidates

List all candidates

### Example Usage

<!-- UsageSnippet language="python" operationID="listAtsCandidates" method="get" path="/ats/{connection_id}/candidate" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.candidate.list_ats_candidates(request={
        "connection_id": "<id>",
    })

    assert res.ats_candidates is not None

    # Handle response
    print(res.ats_candidates)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListAtsCandidatesRequest](../../models/operations/listatscandidatesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListAtsCandidatesResponse](../../models/operations/listatscandidatesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ats_candidate

Update a candidate

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAtsCandidate" method="patch" path="/ats/{connection_id}/candidate/{id}" example="ats_candidate" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.candidate.patch_ats_candidate(request={
        "ats_candidate": {
            "address": {
                "address1": "802 Roberts Squares",
                "address2": "Suite 550",
                "city": "Lake Raeganside",
                "country_code": "US",
                "postal_code": "44530-0054",
                "region": "Tennessee",
                "region_code": "NV",
            },
            "company_name": "Ferry, Legros and Feest",
            "created_at": parse_datetime("2023-10-16T05:42:56.049Z"),
            "education": [
                {
                    "degree": "mouser throughout",
                    "end_at": parse_datetime("1992-11-28T20:23:20.311Z"),
                    "field_of_study": "solutio",
                    "institution": "Heller - Lubowitz",
                    "level": "phd",
                    "start_at": parse_datetime("2001-03-26T08:12:11.510Z"),
                },
            ],
            "emails": [
                {
                    "email": "Ardith.Beatty@hotmail.com",
                    "name": "Opal Lindgren",
                    "type": shared.AtsEmailType.WORK,
                },
                {
                    "email": "Ardith_Beatty@gmail.com",
                    "name": "Kristi Nader",
                    "type": shared.AtsEmailType.OTHER,
                },
            ],
            "experiences": [
                {
                    "company_name": "Donnelly, Buckridge and Steuber",
                    "end_at": parse_datetime("1978-06-20T02:53:48.383Z"),
                    "start_at": parse_datetime("1980-02-06T17:16:53.798Z"),
                    "title": "Principal Brand Strategist",
                },
            ],
            "first_name": "Ardith",
            "id": "ee88586c-5ee8-454c-b299-ed1c9c9a0b13",
            "image_url": "https://loremflickr.com/40/3693?lock=5634712403880328",
            "job_ids": [],
            "last_name": "Beatty",
            "link_urls": [
                "https://sizzling-legislature.com",
                "https://soupy-interchange.net",
                "https://troubled-substitution.info",
            ],
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "3102f38a-d84f-4ee1-b353-4317b7250d65",
                    "namespace": "custom",
                    "slug": "custom_field",
                    "value": "cariosus",
                },
            ],
            "name": "Ardith Beatty",
            "origin": shared.Origin.SOURCED,
            "skills": [
                "vita",
                "cohors",
            ],
            "sources": [
                "tactus",
            ],
            "summary": "Denego barba rerum similique via templum totam suus voluptatem. Depraedor virgo cui comminor commodi curvo. Chirographum pax spero nostrum damnatio averto pecus cervus aspicio absens.",
            "tags": [
                "aliquid",
            ],
            "telephones": [
                {
                    "telephone": "(779) 296-5994",
                    "type": shared.AtsTelephoneType.HOME,
                },
            ],
            "title": "Principal Implementation Analyst",
            "updated_at": parse_datetime("2024-04-23T02:43:11.796Z"),
            "web_url": "https://expert-lender.name/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_candidate is not None

    # Handle response
    print(res.ats_candidate)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchAtsCandidateRequest](../../models/operations/patchatscandidaterequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchAtsCandidateResponse](../../models/operations/patchatscandidateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ats_candidate

Remove a candidate

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAtsCandidate" method="delete" path="/ats/{connection_id}/candidate/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.candidate.remove_ats_candidate(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveAtsCandidateRequest](../../models/operations/removeatscandidaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveAtsCandidateResponse](../../models/operations/removeatscandidateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ats_candidate

Update a candidate

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAtsCandidate" method="put" path="/ats/{connection_id}/candidate/{id}" example="ats_candidate" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.candidate.update_ats_candidate(request={
        "ats_candidate": {
            "address": {
                "address1": "802 Roberts Squares",
                "address2": "Suite 550",
                "city": "Lake Raeganside",
                "country_code": "US",
                "postal_code": "44530-0054",
                "region": "Tennessee",
                "region_code": "NV",
            },
            "company_name": "Ferry, Legros and Feest",
            "created_at": parse_datetime("2023-10-16T05:42:56.049Z"),
            "education": [
                {
                    "degree": "mouser throughout",
                    "end_at": parse_datetime("1992-11-28T20:23:20.311Z"),
                    "field_of_study": "solutio",
                    "institution": "Heller - Lubowitz",
                    "level": "phd",
                    "start_at": parse_datetime("2001-03-26T08:12:11.510Z"),
                },
            ],
            "emails": [
                {
                    "email": "Ardith.Beatty@hotmail.com",
                    "name": "Opal Lindgren",
                    "type": shared.AtsEmailType.WORK,
                },
                {
                    "email": "Ardith_Beatty@gmail.com",
                    "name": "Kristi Nader",
                    "type": shared.AtsEmailType.OTHER,
                },
            ],
            "experiences": [
                {
                    "company_name": "Donnelly, Buckridge and Steuber",
                    "end_at": parse_datetime("1978-06-20T02:53:48.383Z"),
                    "start_at": parse_datetime("1980-02-06T17:16:53.798Z"),
                    "title": "Principal Brand Strategist",
                },
            ],
            "first_name": "Ardith",
            "id": "ee88586c-5ee8-454c-b299-ed1c9c9a0b13",
            "image_url": "https://loremflickr.com/40/3693?lock=5634712403880328",
            "job_ids": [],
            "last_name": "Beatty",
            "link_urls": [
                "https://sizzling-legislature.com",
                "https://soupy-interchange.net",
                "https://troubled-substitution.info",
            ],
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "3102f38a-d84f-4ee1-b353-4317b7250d65",
                    "namespace": "custom",
                    "slug": "custom_field",
                    "value": "cariosus",
                },
            ],
            "name": "Ardith Beatty",
            "origin": shared.Origin.SOURCED,
            "skills": [
                "vita",
                "cohors",
            ],
            "sources": [
                "tactus",
            ],
            "summary": "Denego barba rerum similique via templum totam suus voluptatem. Depraedor virgo cui comminor commodi curvo. Chirographum pax spero nostrum damnatio averto pecus cervus aspicio absens.",
            "tags": [
                "aliquid",
            ],
            "telephones": [
                {
                    "telephone": "(779) 296-5994",
                    "type": shared.AtsTelephoneType.HOME,
                },
            ],
            "title": "Principal Implementation Analyst",
            "updated_at": parse_datetime("2024-04-23T02:43:11.796Z"),
            "web_url": "https://expert-lender.name/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_candidate is not None

    # Handle response
    print(res.ats_candidate)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateAtsCandidateRequest](../../models/operations/updateatscandidaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateAtsCandidateResponse](../../models/operations/updateatscandidateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |