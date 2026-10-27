# Event

## Overview

### Available Operations

* [create_analytics_event](#create_analytics_event) - Create an event
* [create_calendar_event](#create_calendar_event) - Create an event
* [create_cdp_event](#create_cdp_event) - Create an event
* [create_crm_event](#create_crm_event) - Create an event
* [get_analytics_event](#get_analytics_event) - Retrieve an event
* [get_calendar_event](#get_calendar_event) - Retrieve an event
* [get_cdp_event](#get_cdp_event) - Retrieve an event
* [get_clubs_event](#get_clubs_event) - Retrieve an event
* [get_crm_event](#get_crm_event) - Retrieve an event
* [list_analytics_events](#list_analytics_events) - List all events
* [list_calendar_events](#list_calendar_events) - List all events
* [list_cdp_events](#list_cdp_events) - List all events
* [list_clubs_events](#list_clubs_events) - List all events
* [list_crm_events](#list_crm_events) - List all events
* [patch_calendar_event](#patch_calendar_event) - Update an event
* [patch_cdp_event](#patch_cdp_event) - Update an event
* [patch_crm_event](#patch_crm_event) - Update an event
* [patch_messaging_event](#patch_messaging_event) - Update an event
* [remove_calendar_event](#remove_calendar_event) - Remove an event
* [remove_cdp_event](#remove_cdp_event) - Remove an event
* [remove_crm_event](#remove_crm_event) - Remove an event
* [update_calendar_event](#update_calendar_event) - Update an event
* [update_cdp_event](#update_cdp_event) - Update an event
* [update_crm_event](#update_crm_event) - Update an event
* [update_messaging_event](#update_messaging_event) - Update an event

## create_analytics_event

Creates a AnalyticsEvent. Provide the unified AnalyticsEvent fields in the request body; they are mapped to the provider's API. Returns the created AnalyticsEvent.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAnalyticsEvent" method="post" path="/analytics/{connection_id}/event" example="analytics_event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.create_analytics_event(request={
        "analytics_event": {
            "created_at": parse_datetime("2023-06-21T03:13:22.954Z"),
            "event_type": shared.EventType.SCREEN_VIEW,
            "id": "b8582067-e48e-47e5-8bc5-19a70bb21193",
            "metadata": {
                "key": {},
            },
            "name": "page_view",
            "page_url": "https://golden-carboxyl.biz",
            "updated_at": parse_datetime("2023-09-25T03:26:50.143Z"),
        },
        "connection_id": "<id>",
    })

    assert res.analytics_event is not None

    # Handle response
    print(res.analytics_event)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateAnalyticsEventRequest](../../models/operations/createanalyticseventrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateAnalyticsEventResponse](../../models/operations/createanalyticseventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_calendar_event

Creates a CalendarEvent. Provide the unified CalendarEvent fields in the request body; they are mapped to the provider's API. Returns the created CalendarEvent.

### Example Usage

<!-- UsageSnippet language="python" operationID="createCalendarEvent" method="post" path="/calendar/{connection_id}/event" example="calendar_event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.create_calendar_event(request={
        "calendar_event": {
            "attachments": [],
            "conference": [],
            "created_at": "2019-08-04T14:33:51.814Z",
            "end_at": "2020-05-24T22:44:20.075Z",
            "has_conference": False,
            "id": "63cd1dda-eefa-46e5-9055-49b591ea10eb",
            "is_all_day": False,
            "is_free": False,
            "is_private": False,
            "location": "621 Boehm Prairie",
            "metadata": [],
            "notes": "Aegre traho.",
            "recurrence": [
                {
                    "count": 4.0,
                    "end_at": parse_datetime("2025-03-29T05:53:46.696Z"),
                    "excluded_dates": [
                        "2024-02-06T10:42:43.729Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.YEARLY,
                    "included_dates": [
                        "2023-07-10T06:08:32.261Z",
                        "2025-01-28T08:41:14.001Z",
                        "2024-04-05T18:48:27.908Z",
                    ],
                    "interval": 7.0,
                    "on_days": [
                        shared.PropertyCalendarEventRecurrenceOnDays.TU,
                        shared.PropertyCalendarEventRecurrenceOnDays.TH,
                        shared.PropertyCalendarEventRecurrenceOnDays.MO,
                        shared.PropertyCalendarEventRecurrenceOnDays.TH,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                    ],
                    "on_month_days": [
                        -3.0,
                    ],
                    "on_months": [
                        0.0,
                        1.0,
                        6.0,
                        -10.0,
                        9.0,
                        0.0,
                    ],
                    "on_weeks": [
                        -8.0,
                        3.0,
                        -7.0,
                        51.0,
                        -3.0,
                        -41.0,
                        15.0,
                        46.0,
                        -1.0,
                        46.0,
                        42.0,
                        11.0,
                        12.0,
                        -35.0,
                        -15.0,
                        -3.0,
                        -42.0,
                        50.0,
                        3.0,
                        -15.0,
                        -10.0,
                        6.0,
                        -53.0,
                        5.0,
                        -32.0,
                        -22.0,
                        43.0,
                        -44.0,
                        -23.0,
                        -21.0,
                        -18.0,
                        13.0,
                        -5.0,
                        2.0,
                        -49.0,
                    ],
                    "on_year_days": [
                        -87.0,
                        339.0,
                        341.0,
                        287.0,
                        -17.0,
                        319.0,
                        -3.0,
                        238.0,
                        -115.0,
                        -116.0,
                        283.0,
                        -61.0,
                        -254.0,
                        86.0,
                        -163.0,
                        5.0,
                        -171.0,
                        -99.0,
                        279.0,
                        19.0,
                        303.0,
                        -106.0,
                        90.0,
                        109.0,
                        -185.0,
                        -285.0,
                        -83.0,
                        -236.0,
                        66.0,
                        -215.0,
                        178.0,
                        64.0,
                        78.0,
                        5.0,
                        -251.0,
                        -79.0,
                        -271.0,
                        33.0,
                        320.0,
                        67.0,
                        -84.0,
                        -355.0,
                        -364.0,
                        348.0,
                        271.0,
                        -304.0,
                        -199.0,
                        106.0,
                        -345.0,
                        24.0,
                        -89.0,
                        -109.0,
                        -314.0,
                        365.0,
                        38.0,
                        -42.0,
                        123.0,
                        56.0,
                        -3.0,
                        31.0,
                        101.0,
                        326.0,
                        -160.0,
                        -101.0,
                        -267.0,
                        -309.0,
                        -363.0,
                        125.0,
                        -182.0,
                        363.0,
                        324.0,
                        36.0,
                        -269.0,
                        -79.0,
                        -60.0,
                        272.0,
                        -254.0,
                        -160.0,
                        -82.0,
                        19.0,
                        42.0,
                        69.0,
                        -104.0,
                        333.0,
                        236.0,
                        -287.0,
                        296.0,
                        261.0,
                        241.0,
                        348.0,
                        -72.0,
                        159.0,
                        -127.0,
                        229.0,
                        -158.0,
                        190.0,
                        -173.0,
                        -84.0,
                        -96.0,
                        176.0,
                        339.0,
                        -48.0,
                        287.0,
                        -46.0,
                        -101.0,
                        246.0,
                        -8.0,
                        -74.0,
                        338.0,
                        -51.0,
                        -42.0,
                        -128.0,
                        -169.0,
                        -174.0,
                        168.0,
                        -85.0,
                        37.0,
                        169.0,
                        -105.0,
                        231.0,
                        -250.0,
                        -286.0,
                        -7.0,
                        -121.0,
                        321.0,
                        278.0,
                        -120.0,
                        -96.0,
                        360.0,
                        337.0,
                        -258.0,
                        -179.0,
                        324.0,
                        -204.0,
                        327.0,
                        15.0,
                        365.0,
                        191.0,
                        -345.0,
                        -345.0,
                        56.0,
                        217.0,
                        60.0,
                        -264.0,
                        -248.0,
                        -316.0,
                        191.0,
                        -189.0,
                        -152.0,
                        -296.0,
                        194.0,
                        -42.0,
                        -21.0,
                        -218.0,
                        171.0,
                        -15.0,
                        301.0,
                        37.0,
                        -167.0,
                        18.0,
                        248.0,
                        -263.0,
                        27.0,
                        14.0,
                        59.0,
                        219.0,
                        -284.0,
                        221.0,
                        -76.0,
                        277.0,
                        183.0,
                        200.0,
                        -12.0,
                        -28.0,
                        -79.0,
                        150.0,
                        320.0,
                        -152.0,
                        -15.0,
                        -42.0,
                        -125.0,
                        -4.0,
                        269.0,
                        290.0,
                        52.0,
                        320.0,
                        344.0,
                        13.0,
                        -69.0,
                        255.0,
                        -154.0,
                        -281.0,
                        158.0,
                        25.0,
                        240.0,
                        -339.0,
                        96.0,
                        204.0,
                        324.0,
                        221.0,
                        37.0,
                        -333.0,
                        87.0,
                        354.0,
                        -365.0,
                        -203.0,
                        -341.0,
                        -79.0,
                        -208.0,
                        135.0,
                        132.0,
                        -351.0,
                        39.0,
                        -87.0,
                        -297.0,
                        -66.0,
                        346.0,
                        69.0,
                        -177.0,
                        235.0,
                        295.0,
                        -366.0,
                        -55.0,
                        -297.0,
                        -308.0,
                        -294.0,
                        -208.0,
                        141.0,
                        267.0,
                        64.0,
                        100.0,
                        -355.0,
                        -335.0,
                        280.0,
                        224.0,
                        259.0,
                        1.0,
                        -146.0,
                        48.0,
                        335.0,
                        363.0,
                        308.0,
                        -224.0,
                        109.0,
                        -10.0,
                        -89.0,
                        -211.0,
                        -47.0,
                        -130.0,
                        341.0,
                        -250.0,
                        295.0,
                        -329.0,
                        -205.0,
                        231.0,
                        247.0,
                        -228.0,
                        166.0,
                        -28.0,
                        36.0,
                        277.0,
                        -115.0,
                        100.0,
                        2.0,
                        81.0,
                        -66.0,
                        31.0,
                        -39.0,
                        -319.0,
                        -251.0,
                        -254.0,
                    ],
                    "timezone": "Asia/Ho_Chi_Minh",
                    "week_start": shared.WeekStart.TU,
                },
            ],
            "start_at": "2020-05-24T13:29:28.766Z",
            "status": shared.CalendarEventStatus.CONFIRMED,
            "subject": "Sunt spargo tepidus bestia vigor credo coadunatio appello.",
            "timezone": "Asia/Bangkok",
            "updated_at": "2020-06-30T23:05:33.147Z",
            "web_url": "https://another-pinstripe.com",
        },
        "connection_id": "<id>",
    })

    assert res.calendar_event is not None

    # Handle response
    print(res.calendar_event)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateCalendarEventRequest](../../models/operations/createcalendareventrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreateCalendarEventResponse](../../models/operations/createcalendareventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_cdp_event

Creates a CdpEvent. Provide the unified CdpEvent fields in the request body; they are mapped to the provider's API. Returns the created CdpEvent.

### Example Usage

<!-- UsageSnippet language="python" operationID="createCdpEvent" method="post" path="/cdp/{connection_id}/event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.create_cdp_event(request={
        "cdp_event": {},
        "connection_id": "<id>",
    })

    assert res.cdp_event is not None

    # Handle response
    print(res.cdp_event)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateCdpEventRequest](../../models/operations/createcdpeventrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.CreateCdpEventResponse](../../models/operations/createcdpeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_crm_event

Creates a CrmEvent. Provide the unified CrmEvent fields in the request body; they are mapped to the provider's API. Returns the created CrmEvent.

### Example Usage

<!-- UsageSnippet language="python" operationID="createCrmEvent" method="post" path="/crm/{connection_id}/event" example="crm_event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.create_crm_event(request={
        "crm_event": {
            "call": {
                "description": "Arbitro aptus.",
                "duration": 64.0,
                "start_at": parse_datetime("2024-12-15T04:00:07.444Z"),
            },
            "created_at": parse_datetime("2020-07-14T04:53:23.784Z"),
            "id": "fb27d7bb-884f-44eb-9e09-fff3810b6b73",
            "metadata": [],
            "type": shared.CrmEventType.CALL,
            "updated_at": parse_datetime("2026-10-17T09:21:14.984Z"),
        },
        "connection_id": "<id>",
    })

    assert res.crm_event is not None

    # Handle response
    print(res.crm_event)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateCrmEventRequest](../../models/operations/createcrmeventrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.CreateCrmEventResponse](../../models/operations/createcrmeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_analytics_event

Retrieves a single AnalyticsEvent by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAnalyticsEvent" method="get" path="/analytics/{connection_id}/event/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.get_analytics_event(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_event is not None

    # Handle response
    print(res.analytics_event)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetAnalyticsEventRequest](../../models/operations/getanalyticseventrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetAnalyticsEventResponse](../../models/operations/getanalyticseventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_calendar_event

Retrieves a single CalendarEvent by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCalendarEvent" method="get" path="/calendar/{connection_id}/event/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.get_calendar_event(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_event is not None

    # Handle response
    print(res.calendar_event)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetCalendarEventRequest](../../models/operations/getcalendareventrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetCalendarEventResponse](../../models/operations/getcalendareventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_cdp_event

Retrieves a single CdpEvent by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCdpEvent" method="get" path="/cdp/{connection_id}/event/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.get_cdp_event(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_event is not None

    # Handle response
    print(res.cdp_event)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetCdpEventRequest](../../models/operations/getcdpeventrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.GetCdpEventResponse](../../models/operations/getcdpeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_clubs_event

Retrieves a single ClubsEvent by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getClubsEvent" method="get" path="/clubs/{connection_id}/event/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.get_clubs_event(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.clubs_event is not None

    # Handle response
    print(res.clubs_event)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetClubsEventRequest](../../models/operations/getclubseventrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetClubsEventResponse](../../models/operations/getclubseventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_crm_event

Retrieves a single CrmEvent by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCrmEvent" method="get" path="/crm/{connection_id}/event/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.get_crm_event(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_event is not None

    # Handle response
    print(res.crm_event)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetCrmEventRequest](../../models/operations/getcrmeventrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.GetCrmEventResponse](../../models/operations/getcrmeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_analytics_events

Returns a list of AnalyticsEvents. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAnalyticsEvents" method="get" path="/analytics/{connection_id}/event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.list_analytics_events(request={
        "connection_id": "<id>",
    })

    assert res.analytics_events is not None

    # Handle response
    print(res.analytics_events)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListAnalyticsEventsRequest](../../models/operations/listanalyticseventsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListAnalyticsEventsResponse](../../models/operations/listanalyticseventsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_calendar_events

Returns a list of CalendarEvents. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listCalendarEvents" method="get" path="/calendar/{connection_id}/event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.list_calendar_events(request={
        "connection_id": "<id>",
    })

    assert res.calendar_events is not None

    # Handle response
    print(res.calendar_events)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListCalendarEventsRequest](../../models/operations/listcalendareventsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListCalendarEventsResponse](../../models/operations/listcalendareventsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_cdp_events

Returns a list of CdpEvents. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listCdpEvents" method="get" path="/cdp/{connection_id}/event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.list_cdp_events(request={
        "connection_id": "<id>",
    })

    assert res.cdp_events is not None

    # Handle response
    print(res.cdp_events)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListCdpEventsRequest](../../models/operations/listcdpeventsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.ListCdpEventsResponse](../../models/operations/listcdpeventsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_clubs_events

Returns a list of ClubsEvents. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listClubsEvents" method="get" path="/clubs/{connection_id}/event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.list_clubs_events(request={
        "connection_id": "<id>",
    })

    assert res.clubs_events is not None

    # Handle response
    print(res.clubs_events)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListClubsEventsRequest](../../models/operations/listclubseventsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListClubsEventsResponse](../../models/operations/listclubseventsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_crm_events

Returns a list of CrmEvents. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listCrmEvents" method="get" path="/crm/{connection_id}/event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.list_crm_events(request={
        "connection_id": "<id>",
    })

    assert res.crm_events is not None

    # Handle response
    print(res.crm_events)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListCrmEventsRequest](../../models/operations/listcrmeventsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.ListCrmEventsResponse](../../models/operations/listcrmeventsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_calendar_event

Updates the CalendarEvent identified by `id`. Provide the unified CalendarEvent fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCalendarEvent" method="patch" path="/calendar/{connection_id}/event/{id}" example="calendar_event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.patch_calendar_event(request={
        "calendar_event": {
            "attachments": [],
            "conference": [],
            "created_at": "2019-08-04T14:33:51.814Z",
            "end_at": "2020-05-24T22:44:20.080Z",
            "has_conference": False,
            "id": "5e96629b-ee8e-4a72-9228-af009ff076d8",
            "is_all_day": False,
            "is_free": False,
            "is_private": False,
            "location": "621 Boehm Prairie",
            "metadata": [],
            "notes": "Aegre traho.",
            "recurrence": [
                {
                    "count": 4.0,
                    "end_at": parse_datetime("2025-03-29T05:53:46.737Z"),
                    "excluded_dates": [
                        "2024-02-06T10:42:43.761Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.YEARLY,
                    "included_dates": [
                        "2023-07-10T06:08:32.289Z",
                        "2025-01-28T08:41:14.040Z",
                        "2024-04-05T18:48:27.942Z",
                    ],
                    "interval": 7.0,
                    "on_days": [
                        shared.PropertyCalendarEventRecurrenceOnDays.TU,
                        shared.PropertyCalendarEventRecurrenceOnDays.TH,
                        shared.PropertyCalendarEventRecurrenceOnDays.MO,
                        shared.PropertyCalendarEventRecurrenceOnDays.TH,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                    ],
                    "on_month_days": [
                        -3.0,
                    ],
                    "on_months": [
                        0.0,
                        1.0,
                        6.0,
                        -10.0,
                        9.0,
                        0.0,
                    ],
                    "on_weeks": [
                        -8.0,
                        3.0,
                        -7.0,
                        51.0,
                        -3.0,
                        -41.0,
                        15.0,
                        46.0,
                        -1.0,
                        46.0,
                        42.0,
                        11.0,
                        12.0,
                        -35.0,
                        -15.0,
                        -3.0,
                        -42.0,
                        50.0,
                        3.0,
                        -15.0,
                        -10.0,
                        6.0,
                        -53.0,
                        5.0,
                        -32.0,
                        -22.0,
                        43.0,
                        -44.0,
                        -23.0,
                        -21.0,
                        -18.0,
                        13.0,
                        -5.0,
                        2.0,
                        -49.0,
                    ],
                    "on_year_days": [
                        -87.0,
                        339.0,
                        341.0,
                        287.0,
                        -17.0,
                        319.0,
                        -3.0,
                        238.0,
                        -115.0,
                        -116.0,
                        283.0,
                        -61.0,
                        -254.0,
                        86.0,
                        -163.0,
                        5.0,
                        -171.0,
                        -99.0,
                        279.0,
                        19.0,
                        303.0,
                        -106.0,
                        90.0,
                        109.0,
                        -185.0,
                        -285.0,
                        -83.0,
                        -236.0,
                        66.0,
                        -215.0,
                        178.0,
                        64.0,
                        78.0,
                        5.0,
                        -251.0,
                        -79.0,
                        -271.0,
                        33.0,
                        320.0,
                        67.0,
                        -84.0,
                        -355.0,
                        -364.0,
                        348.0,
                        271.0,
                        -304.0,
                        -199.0,
                        106.0,
                        -345.0,
                        24.0,
                        -89.0,
                        -109.0,
                        -314.0,
                        365.0,
                        38.0,
                        -42.0,
                        123.0,
                        56.0,
                        -3.0,
                        31.0,
                        101.0,
                        326.0,
                        -160.0,
                        -101.0,
                        -267.0,
                        -309.0,
                        -363.0,
                        125.0,
                        -182.0,
                        363.0,
                        324.0,
                        36.0,
                        -269.0,
                        -79.0,
                        -60.0,
                        272.0,
                        -254.0,
                        -160.0,
                        -82.0,
                        19.0,
                        42.0,
                        69.0,
                        -104.0,
                        333.0,
                        236.0,
                        -287.0,
                        296.0,
                        261.0,
                        241.0,
                        348.0,
                        -72.0,
                        159.0,
                        -127.0,
                        229.0,
                        -158.0,
                        190.0,
                        -173.0,
                        -84.0,
                        -96.0,
                        176.0,
                        339.0,
                        -48.0,
                        287.0,
                        -46.0,
                        -101.0,
                        246.0,
                        -8.0,
                        -74.0,
                        338.0,
                        -51.0,
                        -42.0,
                        -128.0,
                        -169.0,
                        -174.0,
                        168.0,
                        -85.0,
                        37.0,
                        169.0,
                        -105.0,
                        231.0,
                        -250.0,
                        -286.0,
                        -7.0,
                        -121.0,
                        321.0,
                        278.0,
                        -120.0,
                        -96.0,
                        360.0,
                        337.0,
                        -258.0,
                        -179.0,
                        324.0,
                        -204.0,
                        327.0,
                        15.0,
                        365.0,
                        191.0,
                        -345.0,
                        -345.0,
                        56.0,
                        217.0,
                        60.0,
                        -264.0,
                        -248.0,
                        -316.0,
                        191.0,
                        -189.0,
                        -152.0,
                        -296.0,
                        194.0,
                        -42.0,
                        -21.0,
                        -218.0,
                        171.0,
                        -15.0,
                        301.0,
                        37.0,
                        -167.0,
                        18.0,
                        248.0,
                        -263.0,
                        27.0,
                        14.0,
                        59.0,
                        219.0,
                        -284.0,
                        221.0,
                        -76.0,
                        277.0,
                        183.0,
                        200.0,
                        -12.0,
                        -28.0,
                        -79.0,
                        150.0,
                        320.0,
                        -152.0,
                        -15.0,
                        -42.0,
                        -125.0,
                        -4.0,
                        269.0,
                        290.0,
                        52.0,
                        320.0,
                        344.0,
                        13.0,
                        -69.0,
                        255.0,
                        -154.0,
                        -281.0,
                        158.0,
                        25.0,
                        240.0,
                        -339.0,
                        96.0,
                        204.0,
                        324.0,
                        221.0,
                        37.0,
                        -333.0,
                        87.0,
                        354.0,
                        -365.0,
                        -203.0,
                        -341.0,
                        -79.0,
                        -208.0,
                        135.0,
                        132.0,
                        -351.0,
                        39.0,
                        -87.0,
                        -297.0,
                        -66.0,
                        346.0,
                        69.0,
                        -177.0,
                        235.0,
                        295.0,
                        -366.0,
                        -55.0,
                        -297.0,
                        -308.0,
                        -294.0,
                        -208.0,
                        141.0,
                        267.0,
                        64.0,
                        100.0,
                        -355.0,
                        -335.0,
                        280.0,
                        224.0,
                        259.0,
                        1.0,
                        -146.0,
                        48.0,
                        335.0,
                        363.0,
                        308.0,
                        -224.0,
                        109.0,
                        -10.0,
                        -89.0,
                        -211.0,
                        -47.0,
                        -130.0,
                        341.0,
                        -250.0,
                        295.0,
                        -329.0,
                        -205.0,
                        231.0,
                        247.0,
                        -228.0,
                        166.0,
                        -28.0,
                        36.0,
                        277.0,
                        -115.0,
                        100.0,
                        2.0,
                        81.0,
                        -66.0,
                        31.0,
                        -39.0,
                        -319.0,
                        -251.0,
                        -254.0,
                    ],
                    "timezone": "Asia/Ho_Chi_Minh",
                    "week_start": shared.WeekStart.TU,
                },
            ],
            "start_at": "2020-05-24T13:29:28.771Z",
            "status": shared.CalendarEventStatus.CONFIRMED,
            "subject": "Sunt spargo tepidus bestia vigor credo coadunatio appello.",
            "timezone": "Asia/Bangkok",
            "updated_at": "2020-06-30T23:05:33.153Z",
            "web_url": "https://another-pinstripe.com",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_event is not None

    # Handle response
    print(res.calendar_event)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchCalendarEventRequest](../../models/operations/patchcalendareventrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.PatchCalendarEventResponse](../../models/operations/patchcalendareventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_cdp_event

Updates the CdpEvent identified by `id`. Provide the unified CdpEvent fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCdpEvent" method="patch" path="/cdp/{connection_id}/event/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.patch_cdp_event(request={
        "cdp_event": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_event is not None

    # Handle response
    print(res.cdp_event)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.PatchCdpEventRequest](../../models/operations/patchcdpeventrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.PatchCdpEventResponse](../../models/operations/patchcdpeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_crm_event

Updates the CrmEvent identified by `id`. Provide the unified CrmEvent fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCrmEvent" method="patch" path="/crm/{connection_id}/event/{id}" example="crm_event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.patch_crm_event(request={
        "crm_event": {
            "call": {
                "description": "Arbitro aptus.",
                "duration": 64.0,
                "start_at": parse_datetime("2024-12-15T04:00:07.469Z"),
            },
            "created_at": parse_datetime("2020-07-14T04:53:23.784Z"),
            "id": "952c5b0a-53ab-4ec8-83ce-17f9042757b8",
            "metadata": [],
            "type": shared.CrmEventType.CALL,
            "updated_at": parse_datetime("2026-10-17T09:21:15.020Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_event is not None

    # Handle response
    print(res.crm_event)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.PatchCrmEventRequest](../../models/operations/patchcrmeventrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.PatchCrmEventResponse](../../models/operations/patchcrmeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_messaging_event

Updates the MessagingEvent identified by `id`. Provide the unified MessagingEvent fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchMessagingEvent" method="patch" path="/messaging/{connection_id}/event/{id}" example="messaging_event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.patch_messaging_event(request={
        "messaging_event": {
            "channel": {
                "id": "",
                "name": "",
            },
            "created_at": parse_datetime("2019-05-30T19:44:46.461Z"),
            "id": "24081c8e-33f4-4875-bcd3-2cc5fa9303d0",
            "is_replacing_original": False,
            "metadata": [],
            "type": shared.MessagingEventType.BUTTON_CLICK,
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.messaging_event is not None

    # Handle response
    print(res.messaging_event)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchMessagingEventRequest](../../models/operations/patchmessagingeventrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchMessagingEventResponse](../../models/operations/patchmessagingeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_calendar_event

Deletes the CalendarEvent identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCalendarEvent" method="delete" path="/calendar/{connection_id}/event/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.remove_calendar_event(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.RemoveCalendarEventRequest](../../models/operations/removecalendareventrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.RemoveCalendarEventResponse](../../models/operations/removecalendareventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_cdp_event

Deletes the CdpEvent identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCdpEvent" method="delete" path="/cdp/{connection_id}/event/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.remove_cdp_event(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.RemoveCdpEventRequest](../../models/operations/removecdpeventrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.RemoveCdpEventResponse](../../models/operations/removecdpeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_crm_event

Deletes the CrmEvent identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCrmEvent" method="delete" path="/crm/{connection_id}/event/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.remove_crm_event(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.RemoveCrmEventRequest](../../models/operations/removecrmeventrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.RemoveCrmEventResponse](../../models/operations/removecrmeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_calendar_event

Updates the CalendarEvent identified by `id`. Provide the unified CalendarEvent fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCalendarEvent" method="put" path="/calendar/{connection_id}/event/{id}" example="calendar_event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.update_calendar_event(request={
        "calendar_event": {
            "attachments": [],
            "conference": [],
            "created_at": "2019-08-04T14:33:51.814Z",
            "end_at": "2020-05-24T22:44:20.080Z",
            "has_conference": False,
            "id": "5e96629b-ee8e-4a72-9228-af009ff076d8",
            "is_all_day": False,
            "is_free": False,
            "is_private": False,
            "location": "621 Boehm Prairie",
            "metadata": [],
            "notes": "Aegre traho.",
            "recurrence": [
                {
                    "count": 4.0,
                    "end_at": parse_datetime("2025-03-29T05:53:46.737Z"),
                    "excluded_dates": [
                        "2024-02-06T10:42:43.761Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.YEARLY,
                    "included_dates": [
                        "2023-07-10T06:08:32.289Z",
                        "2025-01-28T08:41:14.040Z",
                        "2024-04-05T18:48:27.942Z",
                    ],
                    "interval": 7.0,
                    "on_days": [
                        shared.PropertyCalendarEventRecurrenceOnDays.TU,
                        shared.PropertyCalendarEventRecurrenceOnDays.TH,
                        shared.PropertyCalendarEventRecurrenceOnDays.MO,
                        shared.PropertyCalendarEventRecurrenceOnDays.TH,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                    ],
                    "on_month_days": [
                        -3.0,
                    ],
                    "on_months": [
                        0.0,
                        1.0,
                        6.0,
                        -10.0,
                        9.0,
                        0.0,
                    ],
                    "on_weeks": [
                        -8.0,
                        3.0,
                        -7.0,
                        51.0,
                        -3.0,
                        -41.0,
                        15.0,
                        46.0,
                        -1.0,
                        46.0,
                        42.0,
                        11.0,
                        12.0,
                        -35.0,
                        -15.0,
                        -3.0,
                        -42.0,
                        50.0,
                        3.0,
                        -15.0,
                        -10.0,
                        6.0,
                        -53.0,
                        5.0,
                        -32.0,
                        -22.0,
                        43.0,
                        -44.0,
                        -23.0,
                        -21.0,
                        -18.0,
                        13.0,
                        -5.0,
                        2.0,
                        -49.0,
                    ],
                    "on_year_days": [
                        -87.0,
                        339.0,
                        341.0,
                        287.0,
                        -17.0,
                        319.0,
                        -3.0,
                        238.0,
                        -115.0,
                        -116.0,
                        283.0,
                        -61.0,
                        -254.0,
                        86.0,
                        -163.0,
                        5.0,
                        -171.0,
                        -99.0,
                        279.0,
                        19.0,
                        303.0,
                        -106.0,
                        90.0,
                        109.0,
                        -185.0,
                        -285.0,
                        -83.0,
                        -236.0,
                        66.0,
                        -215.0,
                        178.0,
                        64.0,
                        78.0,
                        5.0,
                        -251.0,
                        -79.0,
                        -271.0,
                        33.0,
                        320.0,
                        67.0,
                        -84.0,
                        -355.0,
                        -364.0,
                        348.0,
                        271.0,
                        -304.0,
                        -199.0,
                        106.0,
                        -345.0,
                        24.0,
                        -89.0,
                        -109.0,
                        -314.0,
                        365.0,
                        38.0,
                        -42.0,
                        123.0,
                        56.0,
                        -3.0,
                        31.0,
                        101.0,
                        326.0,
                        -160.0,
                        -101.0,
                        -267.0,
                        -309.0,
                        -363.0,
                        125.0,
                        -182.0,
                        363.0,
                        324.0,
                        36.0,
                        -269.0,
                        -79.0,
                        -60.0,
                        272.0,
                        -254.0,
                        -160.0,
                        -82.0,
                        19.0,
                        42.0,
                        69.0,
                        -104.0,
                        333.0,
                        236.0,
                        -287.0,
                        296.0,
                        261.0,
                        241.0,
                        348.0,
                        -72.0,
                        159.0,
                        -127.0,
                        229.0,
                        -158.0,
                        190.0,
                        -173.0,
                        -84.0,
                        -96.0,
                        176.0,
                        339.0,
                        -48.0,
                        287.0,
                        -46.0,
                        -101.0,
                        246.0,
                        -8.0,
                        -74.0,
                        338.0,
                        -51.0,
                        -42.0,
                        -128.0,
                        -169.0,
                        -174.0,
                        168.0,
                        -85.0,
                        37.0,
                        169.0,
                        -105.0,
                        231.0,
                        -250.0,
                        -286.0,
                        -7.0,
                        -121.0,
                        321.0,
                        278.0,
                        -120.0,
                        -96.0,
                        360.0,
                        337.0,
                        -258.0,
                        -179.0,
                        324.0,
                        -204.0,
                        327.0,
                        15.0,
                        365.0,
                        191.0,
                        -345.0,
                        -345.0,
                        56.0,
                        217.0,
                        60.0,
                        -264.0,
                        -248.0,
                        -316.0,
                        191.0,
                        -189.0,
                        -152.0,
                        -296.0,
                        194.0,
                        -42.0,
                        -21.0,
                        -218.0,
                        171.0,
                        -15.0,
                        301.0,
                        37.0,
                        -167.0,
                        18.0,
                        248.0,
                        -263.0,
                        27.0,
                        14.0,
                        59.0,
                        219.0,
                        -284.0,
                        221.0,
                        -76.0,
                        277.0,
                        183.0,
                        200.0,
                        -12.0,
                        -28.0,
                        -79.0,
                        150.0,
                        320.0,
                        -152.0,
                        -15.0,
                        -42.0,
                        -125.0,
                        -4.0,
                        269.0,
                        290.0,
                        52.0,
                        320.0,
                        344.0,
                        13.0,
                        -69.0,
                        255.0,
                        -154.0,
                        -281.0,
                        158.0,
                        25.0,
                        240.0,
                        -339.0,
                        96.0,
                        204.0,
                        324.0,
                        221.0,
                        37.0,
                        -333.0,
                        87.0,
                        354.0,
                        -365.0,
                        -203.0,
                        -341.0,
                        -79.0,
                        -208.0,
                        135.0,
                        132.0,
                        -351.0,
                        39.0,
                        -87.0,
                        -297.0,
                        -66.0,
                        346.0,
                        69.0,
                        -177.0,
                        235.0,
                        295.0,
                        -366.0,
                        -55.0,
                        -297.0,
                        -308.0,
                        -294.0,
                        -208.0,
                        141.0,
                        267.0,
                        64.0,
                        100.0,
                        -355.0,
                        -335.0,
                        280.0,
                        224.0,
                        259.0,
                        1.0,
                        -146.0,
                        48.0,
                        335.0,
                        363.0,
                        308.0,
                        -224.0,
                        109.0,
                        -10.0,
                        -89.0,
                        -211.0,
                        -47.0,
                        -130.0,
                        341.0,
                        -250.0,
                        295.0,
                        -329.0,
                        -205.0,
                        231.0,
                        247.0,
                        -228.0,
                        166.0,
                        -28.0,
                        36.0,
                        277.0,
                        -115.0,
                        100.0,
                        2.0,
                        81.0,
                        -66.0,
                        31.0,
                        -39.0,
                        -319.0,
                        -251.0,
                        -254.0,
                    ],
                    "timezone": "Asia/Ho_Chi_Minh",
                    "week_start": shared.WeekStart.TU,
                },
            ],
            "start_at": "2020-05-24T13:29:28.771Z",
            "status": shared.CalendarEventStatus.CONFIRMED,
            "subject": "Sunt spargo tepidus bestia vigor credo coadunatio appello.",
            "timezone": "Asia/Bangkok",
            "updated_at": "2020-06-30T23:05:33.153Z",
            "web_url": "https://another-pinstripe.com",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_event is not None

    # Handle response
    print(res.calendar_event)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateCalendarEventRequest](../../models/operations/updatecalendareventrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.UpdateCalendarEventResponse](../../models/operations/updatecalendareventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_cdp_event

Updates the CdpEvent identified by `id`. Provide the unified CdpEvent fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCdpEvent" method="put" path="/cdp/{connection_id}/event/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.update_cdp_event(request={
        "cdp_event": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_event is not None

    # Handle response
    print(res.cdp_event)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateCdpEventRequest](../../models/operations/updatecdpeventrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.UpdateCdpEventResponse](../../models/operations/updatecdpeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_crm_event

Updates the CrmEvent identified by `id`. Provide the unified CrmEvent fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCrmEvent" method="put" path="/crm/{connection_id}/event/{id}" example="crm_event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.update_crm_event(request={
        "crm_event": {
            "call": {
                "description": "Arbitro aptus.",
                "duration": 64.0,
                "start_at": parse_datetime("2024-12-15T04:00:07.469Z"),
            },
            "created_at": parse_datetime("2020-07-14T04:53:23.784Z"),
            "id": "952c5b0a-53ab-4ec8-83ce-17f9042757b8",
            "metadata": [],
            "type": shared.CrmEventType.CALL,
            "updated_at": parse_datetime("2026-10-17T09:21:15.020Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_event is not None

    # Handle response
    print(res.crm_event)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateCrmEventRequest](../../models/operations/updatecrmeventrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.UpdateCrmEventResponse](../../models/operations/updatecrmeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_messaging_event

Updates the MessagingEvent identified by `id`. Provide the unified MessagingEvent fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateMessagingEvent" method="put" path="/messaging/{connection_id}/event/{id}" example="messaging_event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.event.update_messaging_event(request={
        "messaging_event": {
            "channel": {
                "id": "",
                "name": "",
            },
            "created_at": parse_datetime("2019-05-30T19:44:46.461Z"),
            "id": "24081c8e-33f4-4875-bcd3-2cc5fa9303d0",
            "is_replacing_original": False,
            "metadata": [],
            "type": shared.MessagingEventType.BUTTON_CLICK,
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.messaging_event is not None

    # Handle response
    print(res.messaging_event)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateMessagingEventRequest](../../models/operations/updatemessagingeventrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateMessagingEventResponse](../../models/operations/updatemessagingeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |