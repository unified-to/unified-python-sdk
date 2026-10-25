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

Creates a AtsCandidate. Provide the unified AtsCandidate fields in the request body; they are mapped to the provider's API. Returns the created AtsCandidate.

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
                "address1": "6790 S 1st Street",
                "city": "Ferrystad",
                "country_code": "US",
                "postal_code": "91605",
                "region": "Idaho",
                "region_code": "HI",
            },
            "company_name": "Lehner and Sons",
            "created_at": parse_datetime("2023-10-16T05:42:56.049Z"),
            "date_of_birth": parse_datetime("1994-07-05T19:48:57.631Z"),
            "education": [
                {
                    "degree": "emphasize tricky",
                    "end_at": parse_datetime("1978-04-14T07:58:36.326Z"),
                    "field_of_study": "curtus",
                    "institution": "Abbott - Batz",
                    "level": "phd",
                    "start_at": parse_datetime("1994-06-09T13:31:39.059Z"),
                },
                {
                    "degree": "blah cappelletti",
                    "end_at": parse_datetime("1989-09-06T03:32:39.901Z"),
                    "field_of_study": "crustulum",
                    "institution": "Herman, Franey and Lebsack",
                    "level": "highschool",
                    "start_at": parse_datetime("1992-11-28T20:23:20.311Z"),
                },
            ],
            "emails": [
                {
                    "email": "ardith.beatty@outlook.com",
                    "name": "Ardith Beatty",
                    "type": shared.AtsEmailType.HOME,
                },
            ],
            "experiences": [
                {
                    "company_name": "Kutch, Lind and Marks",
                    "end_at": parse_datetime("1974-03-01T17:02:58.824Z"),
                    "start_at": parse_datetime("1999-09-21T22:12:51.663Z"),
                    "title": "Lead Security Technician",
                },
                {
                    "company_name": "Trantow, Sipes and Witting",
                    "end_at": parse_datetime("2004-10-14T14:01:00.717Z"),
                    "start_at": parse_datetime("1996-12-15T04:12:04.582Z"),
                    "title": "Regional Applications Planner",
                },
            ],
            "first_name": "Ardith",
            "id": "0d60d2be-3da5-498e-9263-8f96a85592a9",
            "image_url": "https://avatars.githubusercontent.com/u/27464445",
            "job_ids": [],
            "last_name": "Beatty",
            "link_urls": [
                "https://www.linkedin.com/in/ardith-beatty",
            ],
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "d92cbed5-6b07-49a8-8ece-42f5c76e6d36",
                    "namespace": "custom",
                    "slug": "custom_field",
                    "value": "officia",
                },
            ],
            "name": "Ardith Beatty",
            "origin": shared.Origin.AGENCY,
            "skills": [
                "trepide",
                "voveo",
            ],
            "sources": [
                "vesper",
                "utroque",
            ],
            "summary": "Laborum trado carcer delibero patruus totam. Vita cohors cariosus trans denego barba rerum similique. Templum totam suus voluptatem cui depraedor virgo cui comminor commodi.",
            "tags": [
                "voro",
            ],
            "telephones": [
                {
                    "telephone": "(837) 251-3896",
                    "type": shared.AtsTelephoneType.MOBILE,
                },
            ],
            "title": "Customer Division Producer",
            "updated_at": parse_datetime("2024-04-29T10:45:17.319Z"),
            "web_url": "https://fragrant-husband.net/",
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

Retrieves a single AtsCandidate by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Returns a list of AtsCandidates. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Updates the AtsCandidate identified by `id`. Provide the unified AtsCandidate fields to change in the request body.

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
                "address1": "6790 S 1st Street",
                "city": "Ferrystad",
                "country_code": "US",
                "postal_code": "91605",
                "region": "Idaho",
                "region_code": "HI",
            },
            "company_name": "Lehner and Sons",
            "created_at": parse_datetime("2023-10-16T05:42:56.049Z"),
            "date_of_birth": parse_datetime("1994-07-05T19:48:57.631Z"),
            "education": [
                {
                    "degree": "emphasize tricky",
                    "end_at": parse_datetime("1978-04-14T07:58:36.326Z"),
                    "field_of_study": "curtus",
                    "institution": "Abbott - Batz",
                    "level": "phd",
                    "start_at": parse_datetime("1994-06-09T13:31:39.059Z"),
                },
                {
                    "degree": "blah cappelletti",
                    "end_at": parse_datetime("1989-09-06T03:32:39.901Z"),
                    "field_of_study": "crustulum",
                    "institution": "Herman, Franey and Lebsack",
                    "level": "highschool",
                    "start_at": parse_datetime("1992-11-28T20:23:20.311Z"),
                },
            ],
            "emails": [
                {
                    "email": "ardith.beatty@outlook.com",
                    "name": "Ardith Beatty",
                    "type": shared.AtsEmailType.HOME,
                },
            ],
            "experiences": [
                {
                    "company_name": "Kutch, Lind and Marks",
                    "end_at": parse_datetime("1974-03-01T17:02:58.824Z"),
                    "start_at": parse_datetime("1999-09-21T22:12:51.663Z"),
                    "title": "Lead Security Technician",
                },
                {
                    "company_name": "Trantow, Sipes and Witting",
                    "end_at": parse_datetime("2004-10-14T14:01:00.717Z"),
                    "start_at": parse_datetime("1996-12-15T04:12:04.582Z"),
                    "title": "Regional Applications Planner",
                },
            ],
            "first_name": "Ardith",
            "id": "39146b2f-81a8-414b-a68a-7599c694f59a",
            "image_url": "https://avatars.githubusercontent.com/u/27464445",
            "job_ids": [],
            "last_name": "Beatty",
            "link_urls": [
                "https://www.linkedin.com/in/ardith-beatty",
            ],
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "5b7e6f94-7f28-427b-80ff-7d0f4bd5e44f",
                    "namespace": "custom",
                    "slug": "custom_field",
                    "value": "officia",
                },
            ],
            "name": "Ardith Beatty",
            "origin": shared.Origin.AGENCY,
            "skills": [
                "trepide",
                "voveo",
            ],
            "sources": [
                "vesper",
                "utroque",
            ],
            "summary": "Laborum trado carcer delibero patruus totam. Vita cohors cariosus trans denego barba rerum similique. Templum totam suus voluptatem cui depraedor virgo cui comminor commodi.",
            "tags": [
                "voro",
            ],
            "telephones": [
                {
                    "telephone": "(837) 251-3896",
                    "type": shared.AtsTelephoneType.MOBILE,
                },
            ],
            "title": "Customer Division Producer",
            "updated_at": parse_datetime("2024-04-29T10:45:17.328Z"),
            "web_url": "https://fragrant-husband.net/",
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

Deletes the AtsCandidate identified by `id`.

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

Updates the AtsCandidate identified by `id`. Provide the unified AtsCandidate fields to change in the request body.

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
                "address1": "6790 S 1st Street",
                "city": "Ferrystad",
                "country_code": "US",
                "postal_code": "91605",
                "region": "Idaho",
                "region_code": "HI",
            },
            "company_name": "Lehner and Sons",
            "created_at": parse_datetime("2023-10-16T05:42:56.049Z"),
            "date_of_birth": parse_datetime("1994-07-05T19:48:57.631Z"),
            "education": [
                {
                    "degree": "emphasize tricky",
                    "end_at": parse_datetime("1978-04-14T07:58:36.326Z"),
                    "field_of_study": "curtus",
                    "institution": "Abbott - Batz",
                    "level": "phd",
                    "start_at": parse_datetime("1994-06-09T13:31:39.059Z"),
                },
                {
                    "degree": "blah cappelletti",
                    "end_at": parse_datetime("1989-09-06T03:32:39.901Z"),
                    "field_of_study": "crustulum",
                    "institution": "Herman, Franey and Lebsack",
                    "level": "highschool",
                    "start_at": parse_datetime("1992-11-28T20:23:20.311Z"),
                },
            ],
            "emails": [
                {
                    "email": "ardith.beatty@outlook.com",
                    "name": "Ardith Beatty",
                    "type": shared.AtsEmailType.HOME,
                },
            ],
            "experiences": [
                {
                    "company_name": "Kutch, Lind and Marks",
                    "end_at": parse_datetime("1974-03-01T17:02:58.824Z"),
                    "start_at": parse_datetime("1999-09-21T22:12:51.663Z"),
                    "title": "Lead Security Technician",
                },
                {
                    "company_name": "Trantow, Sipes and Witting",
                    "end_at": parse_datetime("2004-10-14T14:01:00.717Z"),
                    "start_at": parse_datetime("1996-12-15T04:12:04.582Z"),
                    "title": "Regional Applications Planner",
                },
            ],
            "first_name": "Ardith",
            "id": "39146b2f-81a8-414b-a68a-7599c694f59a",
            "image_url": "https://avatars.githubusercontent.com/u/27464445",
            "job_ids": [],
            "last_name": "Beatty",
            "link_urls": [
                "https://www.linkedin.com/in/ardith-beatty",
            ],
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "5b7e6f94-7f28-427b-80ff-7d0f4bd5e44f",
                    "namespace": "custom",
                    "slug": "custom_field",
                    "value": "officia",
                },
            ],
            "name": "Ardith Beatty",
            "origin": shared.Origin.AGENCY,
            "skills": [
                "trepide",
                "voveo",
            ],
            "sources": [
                "vesper",
                "utroque",
            ],
            "summary": "Laborum trado carcer delibero patruus totam. Vita cohors cariosus trans denego barba rerum similique. Templum totam suus voluptatem cui depraedor virgo cui comminor commodi.",
            "tags": [
                "voro",
            ],
            "telephones": [
                {
                    "telephone": "(837) 251-3896",
                    "type": shared.AtsTelephoneType.MOBILE,
                },
            ],
            "title": "Customer Division Producer",
            "updated_at": parse_datetime("2024-04-29T10:45:17.328Z"),
            "web_url": "https://fragrant-husband.net/",
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