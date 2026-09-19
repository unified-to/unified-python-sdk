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

Create an event

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
            "id": "1fbf1d07-8e8b-4550-9a5b-13e814d1ecec",
            "metadata": {
                "key": {},
            },
            "name": "Xk707ttsb51v",
            "updated_at": parse_datetime("2023-09-22T03:59:44.371Z"),
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

Create an event

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
            "end_at": "2020-05-20T17:12:37.976Z",
            "id": "dbfb8859-7c40-48b3-8e82-4d75514c5c87",
            "is_all_day": False,
            "is_free": False,
            "is_private": False,
            "location": "621 Boehm Prairie",
            "notes": "Aegre traho.",
            "recurrence": [
                {
                    "count": 8.0,
                    "end_at": parse_datetime("2025-12-26T06:34:54.337Z"),
                    "excluded_dates": [
                        "2025-09-30T22:42:44.909Z",
                        "2023-10-09T12:14:01.306Z",
                        "2024-02-15T13:20:24.716Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.MONTHLY,
                    "included_dates": [
                        "2021-02-16T22:04:02.460Z",
                    ],
                    "interval": 4.0,
                    "on_days": [
                        shared.PropertyCalendarEventRecurrenceOnDays.TH,
                        shared.PropertyCalendarEventRecurrenceOnDays.MO,
                        shared.PropertyCalendarEventRecurrenceOnDays.TH,
                    ],
                    "on_month_days": [
                        -26.0,
                    ],
                    "on_months": [
                        12.0,
                        9.0,
                        -1.0,
                        0.0,
                        1.0,
                        6.0,
                        -10.0,
                        9.0,
                        0.0,
                        4.0,
                        -2.0,
                    ],
                    "on_weeks": [
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
                    ],
                    "on_year_days": [
                        -35.0,
                        14.0,
                        -338.0,
                        175.0,
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
                    ],
                    "timezone": "Asia/Ho_Chi_Minh",
                    "week_start": shared.WeekStart.SU,
                },
                {
                    "count": 9.0,
                    "end_at": parse_datetime("2025-04-30T05:52:39.868Z"),
                    "excluded_dates": [
                        "2020-04-29T00:43:21.543Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.DAILY,
                    "included_dates": [
                        "2020-09-11T02:34:17.915Z",
                        "2021-11-29T01:27:53.237Z",
                        "2019-12-22T18:06:05.559Z",
                    ],
                    "interval": 1.0,
                    "on_days": [
                        shared.PropertyCalendarEventRecurrenceOnDays.WE,
                        shared.PropertyCalendarEventRecurrenceOnDays.TU,
                        shared.PropertyCalendarEventRecurrenceOnDays.WE,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                    ],
                    "on_month_days": [
                        1.0,
                    ],
                    "on_months": [
                        4.0,
                        0.0,
                        -3.0,
                    ],
                    "on_weeks": [
                        -7.0,
                        -19.0,
                        50.0,
                        -37.0,
                        43.0,
                        -48.0,
                        -30.0,
                        34.0,
                        36.0,
                        -33.0,
                        24.0,
                        -4.0,
                    ],
                    "on_year_days": [
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
                        -35.0,
                        -121.0,
                        262.0,
                        32.0,
                        190.0,
                        107.0,
                        -145.0,
                        91.0,
                        313.0,
                        -48.0,
                        277.0,
                        104.0,
                        342.0,
                        297.0,
                        -216.0,
                        346.0,
                        -257.0,
                        307.0,
                        -44.0,
                        264.0,
                        -153.0,
                        -268.0,
                        92.0,
                        152.0,
                        -182.0,
                        -334.0,
                        89.0,
                        343.0,
                        -320.0,
                        -36.0,
                        84.0,
                        340.0,
                        -88.0,
                        -278.0,
                        202.0,
                        291.0,
                        95.0,
                        -234.0,
                        -304.0,
                        -157.0,
                        -82.0,
                        -339.0,
                        83.0,
                        2.0,
                        -238.0,
                        -204.0,
                        206.0,
                        -273.0,
                        -78.0,
                        -21.0,
                        270.0,
                        -266.0,
                        -276.0,
                        154.0,
                        -97.0,
                        -43.0,
                        -3.0,
                        191.0,
                        -302.0,
                        290.0,
                        -118.0,
                        -125.0,
                        -294.0,
                        115.0,
                        -73.0,
                        -244.0,
                        127.0,
                        26.0,
                        251.0,
                        47.0,
                        -157.0,
                        22.0,
                        -361.0,
                        318.0,
                        352.0,
                        358.0,
                        167.0,
                        210.0,
                        -185.0,
                        327.0,
                        117.0,
                        350.0,
                        -170.0,
                        -144.0,
                        -14.0,
                        -37.0,
                        318.0,
                        243.0,
                        33.0,
                        90.0,
                        319.0,
                        -270.0,
                        229.0,
                        122.0,
                        287.0,
                        -90.0,
                        -69.0,
                        -134.0,
                        -184.0,
                        25.0,
                        -178.0,
                        -89.0,
                        -273.0,
                        -49.0,
                        -362.0,
                        -9.0,
                        -71.0,
                        -347.0,
                        353.0,
                        342.0,
                        133.0,
                        -116.0,
                        231.0,
                        -231.0,
                        51.0,
                        288.0,
                        186.0,
                        -328.0,
                        275.0,
                        81.0,
                        94.0,
                        -263.0,
                        114.0,
                        13.0,
                        -357.0,
                        171.0,
                        -242.0,
                        -85.0,
                        -362.0,
                        108.0,
                        164.0,
                        69.0,
                        15.0,
                        57.0,
                        -287.0,
                        100.0,
                        165.0,
                        205.0,
                        204.0,
                        -78.0,
                        360.0,
                        -80.0,
                        -120.0,
                        -255.0,
                        -77.0,
                        110.0,
                        -26.0,
                        -149.0,
                        -254.0,
                        95.0,
                        32.0,
                        -57.0,
                        -195.0,
                        100.0,
                        221.0,
                        74.0,
                        274.0,
                        15.0,
                        353.0,
                        204.0,
                        -365.0,
                        315.0,
                        344.0,
                        199.0,
                        -59.0,
                        272.0,
                        173.0,
                        -40.0,
                        -318.0,
                        -330.0,
                        -365.0,
                        -272.0,
                        -149.0,
                        -27.0,
                        -334.0,
                        -277.0,
                        344.0,
                        351.0,
                        -310.0,
                        264.0,
                        281.0,
                        176.0,
                        191.0,
                        -183.0,
                        288.0,
                        -112.0,
                        -55.0,
                        -166.0,
                        258.0,
                        194.0,
                        59.0,
                    ],
                    "timezone": "America/Guadeloupe",
                    "week_start": shared.WeekStart.TU,
                },
                {
                    "count": 1.0,
                    "end_at": parse_datetime("2020-11-04T17:53:56.516Z"),
                    "excluded_dates": [
                        "2023-01-11T21:34:37.555Z",
                        "2021-09-07T13:21:42.126Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.WEEKLY,
                    "included_dates": [
                        "2024-08-31T10:58:44.143Z",
                    ],
                    "interval": 9.0,
                    "on_days": [
                        shared.PropertyCalendarEventRecurrenceOnDays.TU,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                    ],
                    "on_month_days": [
                        -2.0,
                    ],
                    "on_months": [
                        -4.0,
                        8.0,
                        0.0,
                        9.0,
                        4.0,
                        -11.0,
                        7.0,
                        1.0,
                        -5.0,
                    ],
                    "on_weeks": [
                        -36.0,
                        -31.0,
                        -16.0,
                        -6.0,
                        44.0,
                        -37.0,
                        14.0,
                        38.0,
                        -27.0,
                        -22.0,
                        -2.0,
                        24.0,
                        7.0,
                        50.0,
                        46.0,
                        52.0,
                        20.0,
                        37.0,
                        31.0,
                        48.0,
                        35.0,
                        -46.0,
                        13.0,
                        22.0,
                        53.0,
                        20.0,
                        -28.0,
                        -2.0,
                        39.0,
                        13.0,
                        4.0,
                        0.0,
                        7.0,
                        -38.0,
                        -35.0,
                        41.0,
                        49.0,
                        12.0,
                        17.0,
                        8.0,
                        49.0,
                        -47.0,
                        46.0,
                        25.0,
                        14.0,
                        -26.0,
                        -37.0,
                        -25.0,
                        -41.0,
                        27.0,
                        28.0,
                        -19.0,
                    ],
                    "on_year_days": [
                        -256.0,
                        -328.0,
                        -312.0,
                        50.0,
                        -251.0,
                        -338.0,
                        -315.0,
                        214.0,
                        129.0,
                        -263.0,
                        -108.0,
                        -11.0,
                        206.0,
                        -29.0,
                        -159.0,
                        -29.0,
                        -264.0,
                        295.0,
                        -231.0,
                        53.0,
                        34.0,
                        -366.0,
                        326.0,
                        -202.0,
                        151.0,
                        79.0,
                        -66.0,
                        11.0,
                        -42.0,
                        73.0,
                        338.0,
                        -155.0,
                        197.0,
                        260.0,
                        356.0,
                        -323.0,
                        -213.0,
                        -332.0,
                        -305.0,
                        -182.0,
                        -253.0,
                        -276.0,
                        -285.0,
                        96.0,
                        -336.0,
                        269.0,
                        -233.0,
                        250.0,
                        -112.0,
                        -307.0,
                        -96.0,
                        54.0,
                        267.0,
                        318.0,
                        -66.0,
                        11.0,
                        -303.0,
                        231.0,
                        165.0,
                        -297.0,
                        -348.0,
                        -355.0,
                        364.0,
                        312.0,
                        -26.0,
                        111.0,
                        162.0,
                        280.0,
                        312.0,
                        337.0,
                        235.0,
                        68.0,
                        -282.0,
                        363.0,
                        212.0,
                        -328.0,
                        9.0,
                        -24.0,
                        -163.0,
                        -101.0,
                        -79.0,
                        -264.0,
                        -157.0,
                        188.0,
                        290.0,
                        51.0,
                        -213.0,
                        216.0,
                        230.0,
                        -270.0,
                        -211.0,
                        -156.0,
                        -165.0,
                        -305.0,
                        -45.0,
                        224.0,
                        -248.0,
                        65.0,
                        9.0,
                        274.0,
                        -299.0,
                        -228.0,
                        33.0,
                        -42.0,
                        356.0,
                        -311.0,
                        241.0,
                        261.0,
                        -136.0,
                        -252.0,
                        166.0,
                        208.0,
                        -126.0,
                        64.0,
                        323.0,
                        -104.0,
                        -106.0,
                        -248.0,
                        -41.0,
                        -109.0,
                        245.0,
                        47.0,
                        205.0,
                        358.0,
                        -296.0,
                        214.0,
                        -157.0,
                        -313.0,
                        -303.0,
                        -54.0,
                        -229.0,
                        231.0,
                        -94.0,
                        -198.0,
                        338.0,
                        199.0,
                        5.0,
                        42.0,
                        309.0,
                        73.0,
                        56.0,
                        -120.0,
                        351.0,
                        6.0,
                        -193.0,
                        21.0,
                        78.0,
                        57.0,
                        -269.0,
                        -76.0,
                        -299.0,
                        295.0,
                        -278.0,
                        11.0,
                        121.0,
                        -323.0,
                        156.0,
                        67.0,
                        152.0,
                        284.0,
                        108.0,
                        -7.0,
                        329.0,
                        -32.0,
                        333.0,
                        -338.0,
                        148.0,
                        -42.0,
                        151.0,
                        145.0,
                        -34.0,
                        -36.0,
                        296.0,
                        -198.0,
                        -317.0,
                        -161.0,
                        -253.0,
                        328.0,
                        -57.0,
                        134.0,
                        -289.0,
                        229.0,
                        44.0,
                        16.0,
                        -256.0,
                        289.0,
                        -234.0,
                        197.0,
                        333.0,
                        228.0,
                        -143.0,
                        -202.0,
                        -172.0,
                        -262.0,
                        -203.0,
                        -83.0,
                        -242.0,
                        -173.0,
                        336.0,
                        298.0,
                        -319.0,
                        66.0,
                        254.0,
                        214.0,
                        -118.0,
                        -216.0,
                        -168.0,
                        44.0,
                        -243.0,
                        207.0,
                        -28.0,
                        -4.0,
                        -272.0,
                        79.0,
                    ],
                    "timezone": "Atlantic/Reykjavik",
                    "week_start": shared.WeekStart.TU,
                },
            ],
            "recurring_event_id": "bd28e1ea-fb99-454e-89c0-6be3542789d1",
            "send_notifications": False,
            "start_at": "2020-05-20T08:05:45.139Z",
            "status": shared.CalendarEventStatus.CONFIRMED,
            "subject": "Sunt spargo tepidus bestia vigor credo coadunatio appello.",
            "timezone": "Asia/Bangkok",
            "updated_at": "2020-06-26T04:47:47.416Z",
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

Create an event

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

Create an event

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
                "start_at": parse_datetime("2024-11-18T11:19:34.109Z"),
            },
            "created_at": parse_datetime("2020-07-14T04:53:23.784Z"),
            "id": "89b14599-9944-4b9e-975f-84ffcca3203d",
            "type": shared.CrmEventType.CALL,
            "updated_at": parse_datetime("2026-09-09T14:23:44.575Z"),
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

Retrieve an event

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

Retrieve an event

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

Retrieve an event

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

Retrieve an event

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

Retrieve an event

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

List all events

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

List all events

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

List all events

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

List all events

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

List all events

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

Update an event

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
            "end_at": "2020-05-20T17:12:37.979Z",
            "id": "67215e17-405a-4402-bfdf-b40ac9978bb3",
            "is_all_day": False,
            "is_free": False,
            "is_private": False,
            "location": "621 Boehm Prairie",
            "notes": "Aegre traho.",
            "recurrence": [
                {
                    "count": 8.0,
                    "end_at": parse_datetime("2025-12-26T06:34:54.364Z"),
                    "excluded_dates": [
                        "2025-09-30T22:42:44.936Z",
                        "2023-10-09T12:14:01.324Z",
                        "2024-02-15T13:20:24.736Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.MONTHLY,
                    "included_dates": [
                        "2021-02-16T22:04:02.467Z",
                    ],
                    "interval": 4.0,
                    "on_days": [
                        shared.PropertyCalendarEventRecurrenceOnDays.TH,
                        shared.PropertyCalendarEventRecurrenceOnDays.MO,
                        shared.PropertyCalendarEventRecurrenceOnDays.TH,
                    ],
                    "on_month_days": [
                        -26.0,
                    ],
                    "on_months": [
                        12.0,
                        9.0,
                        -1.0,
                        0.0,
                        1.0,
                        6.0,
                        -10.0,
                        9.0,
                        0.0,
                        4.0,
                        -2.0,
                    ],
                    "on_weeks": [
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
                    ],
                    "on_year_days": [
                        -35.0,
                        14.0,
                        -338.0,
                        175.0,
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
                    ],
                    "timezone": "Asia/Ho_Chi_Minh",
                    "week_start": shared.WeekStart.SU,
                },
                {
                    "count": 9.0,
                    "end_at": parse_datetime("2025-04-30T05:52:39.892Z"),
                    "excluded_dates": [
                        "2020-04-29T00:43:21.546Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.DAILY,
                    "included_dates": [
                        "2020-09-11T02:34:17.920Z",
                        "2021-11-29T01:27:53.247Z",
                        "2019-12-22T18:06:05.561Z",
                    ],
                    "interval": 1.0,
                    "on_days": [
                        shared.PropertyCalendarEventRecurrenceOnDays.WE,
                        shared.PropertyCalendarEventRecurrenceOnDays.TU,
                        shared.PropertyCalendarEventRecurrenceOnDays.WE,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                    ],
                    "on_month_days": [
                        1.0,
                    ],
                    "on_months": [
                        4.0,
                        0.0,
                        -3.0,
                    ],
                    "on_weeks": [
                        -7.0,
                        -19.0,
                        50.0,
                        -37.0,
                        43.0,
                        -48.0,
                        -30.0,
                        34.0,
                        36.0,
                        -33.0,
                        24.0,
                        -4.0,
                    ],
                    "on_year_days": [
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
                        -35.0,
                        -121.0,
                        262.0,
                        32.0,
                        190.0,
                        107.0,
                        -145.0,
                        91.0,
                        313.0,
                        -48.0,
                        277.0,
                        104.0,
                        342.0,
                        297.0,
                        -216.0,
                        346.0,
                        -257.0,
                        307.0,
                        -44.0,
                        264.0,
                        -153.0,
                        -268.0,
                        92.0,
                        152.0,
                        -182.0,
                        -334.0,
                        89.0,
                        343.0,
                        -320.0,
                        -36.0,
                        84.0,
                        340.0,
                        -88.0,
                        -278.0,
                        202.0,
                        291.0,
                        95.0,
                        -234.0,
                        -304.0,
                        -157.0,
                        -82.0,
                        -339.0,
                        83.0,
                        2.0,
                        -238.0,
                        -204.0,
                        206.0,
                        -273.0,
                        -78.0,
                        -21.0,
                        270.0,
                        -266.0,
                        -276.0,
                        154.0,
                        -97.0,
                        -43.0,
                        -3.0,
                        191.0,
                        -302.0,
                        290.0,
                        -118.0,
                        -125.0,
                        -294.0,
                        115.0,
                        -73.0,
                        -244.0,
                        127.0,
                        26.0,
                        251.0,
                        47.0,
                        -157.0,
                        22.0,
                        -361.0,
                        318.0,
                        352.0,
                        358.0,
                        167.0,
                        210.0,
                        -185.0,
                        327.0,
                        117.0,
                        350.0,
                        -170.0,
                        -144.0,
                        -14.0,
                        -37.0,
                        318.0,
                        243.0,
                        33.0,
                        90.0,
                        319.0,
                        -270.0,
                        229.0,
                        122.0,
                        287.0,
                        -90.0,
                        -69.0,
                        -134.0,
                        -184.0,
                        25.0,
                        -178.0,
                        -89.0,
                        -273.0,
                        -49.0,
                        -362.0,
                        -9.0,
                        -71.0,
                        -347.0,
                        353.0,
                        342.0,
                        133.0,
                        -116.0,
                        231.0,
                        -231.0,
                        51.0,
                        288.0,
                        186.0,
                        -328.0,
                        275.0,
                        81.0,
                        94.0,
                        -263.0,
                        114.0,
                        13.0,
                        -357.0,
                        171.0,
                        -242.0,
                        -85.0,
                        -362.0,
                        108.0,
                        164.0,
                        69.0,
                        15.0,
                        57.0,
                        -287.0,
                        100.0,
                        165.0,
                        205.0,
                        204.0,
                        -78.0,
                        360.0,
                        -80.0,
                        -120.0,
                        -255.0,
                        -77.0,
                        110.0,
                        -26.0,
                        -149.0,
                        -254.0,
                        95.0,
                        32.0,
                        -57.0,
                        -195.0,
                        100.0,
                        221.0,
                        74.0,
                        274.0,
                        15.0,
                        353.0,
                        204.0,
                        -365.0,
                        315.0,
                        344.0,
                        199.0,
                        -59.0,
                        272.0,
                        173.0,
                        -40.0,
                        -318.0,
                        -330.0,
                        -365.0,
                        -272.0,
                        -149.0,
                        -27.0,
                        -334.0,
                        -277.0,
                        344.0,
                        351.0,
                        -310.0,
                        264.0,
                        281.0,
                        176.0,
                        191.0,
                        -183.0,
                        288.0,
                        -112.0,
                        -55.0,
                        -166.0,
                        258.0,
                        194.0,
                        59.0,
                    ],
                    "timezone": "America/Guadeloupe",
                    "week_start": shared.WeekStart.TU,
                },
                {
                    "count": 1.0,
                    "end_at": parse_datetime("2020-11-04T17:53:56.521Z"),
                    "excluded_dates": [
                        "2023-01-11T21:34:37.570Z",
                        "2021-09-07T13:21:42.135Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.WEEKLY,
                    "included_dates": [
                        "2024-08-31T10:58:44.165Z",
                    ],
                    "interval": 9.0,
                    "on_days": [
                        shared.PropertyCalendarEventRecurrenceOnDays.TU,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                    ],
                    "on_month_days": [
                        -2.0,
                    ],
                    "on_months": [
                        -4.0,
                        8.0,
                        0.0,
                        9.0,
                        4.0,
                        -11.0,
                        7.0,
                        1.0,
                        -5.0,
                    ],
                    "on_weeks": [
                        -36.0,
                        -31.0,
                        -16.0,
                        -6.0,
                        44.0,
                        -37.0,
                        14.0,
                        38.0,
                        -27.0,
                        -22.0,
                        -2.0,
                        24.0,
                        7.0,
                        50.0,
                        46.0,
                        52.0,
                        20.0,
                        37.0,
                        31.0,
                        48.0,
                        35.0,
                        -46.0,
                        13.0,
                        22.0,
                        53.0,
                        20.0,
                        -28.0,
                        -2.0,
                        39.0,
                        13.0,
                        4.0,
                        0.0,
                        7.0,
                        -38.0,
                        -35.0,
                        41.0,
                        49.0,
                        12.0,
                        17.0,
                        8.0,
                        49.0,
                        -47.0,
                        46.0,
                        25.0,
                        14.0,
                        -26.0,
                        -37.0,
                        -25.0,
                        -41.0,
                        27.0,
                        28.0,
                        -19.0,
                    ],
                    "on_year_days": [
                        -256.0,
                        -328.0,
                        -312.0,
                        50.0,
                        -251.0,
                        -338.0,
                        -315.0,
                        214.0,
                        129.0,
                        -263.0,
                        -108.0,
                        -11.0,
                        206.0,
                        -29.0,
                        -159.0,
                        -29.0,
                        -264.0,
                        295.0,
                        -231.0,
                        53.0,
                        34.0,
                        -366.0,
                        326.0,
                        -202.0,
                        151.0,
                        79.0,
                        -66.0,
                        11.0,
                        -42.0,
                        73.0,
                        338.0,
                        -155.0,
                        197.0,
                        260.0,
                        356.0,
                        -323.0,
                        -213.0,
                        -332.0,
                        -305.0,
                        -182.0,
                        -253.0,
                        -276.0,
                        -285.0,
                        96.0,
                        -336.0,
                        269.0,
                        -233.0,
                        250.0,
                        -112.0,
                        -307.0,
                        -96.0,
                        54.0,
                        267.0,
                        318.0,
                        -66.0,
                        11.0,
                        -303.0,
                        231.0,
                        165.0,
                        -297.0,
                        -348.0,
                        -355.0,
                        364.0,
                        312.0,
                        -26.0,
                        111.0,
                        162.0,
                        280.0,
                        312.0,
                        337.0,
                        235.0,
                        68.0,
                        -282.0,
                        363.0,
                        212.0,
                        -328.0,
                        9.0,
                        -24.0,
                        -163.0,
                        -101.0,
                        -79.0,
                        -264.0,
                        -157.0,
                        188.0,
                        290.0,
                        51.0,
                        -213.0,
                        216.0,
                        230.0,
                        -270.0,
                        -211.0,
                        -156.0,
                        -165.0,
                        -305.0,
                        -45.0,
                        224.0,
                        -248.0,
                        65.0,
                        9.0,
                        274.0,
                        -299.0,
                        -228.0,
                        33.0,
                        -42.0,
                        356.0,
                        -311.0,
                        241.0,
                        261.0,
                        -136.0,
                        -252.0,
                        166.0,
                        208.0,
                        -126.0,
                        64.0,
                        323.0,
                        -104.0,
                        -106.0,
                        -248.0,
                        -41.0,
                        -109.0,
                        245.0,
                        47.0,
                        205.0,
                        358.0,
                        -296.0,
                        214.0,
                        -157.0,
                        -313.0,
                        -303.0,
                        -54.0,
                        -229.0,
                        231.0,
                        -94.0,
                        -198.0,
                        338.0,
                        199.0,
                        5.0,
                        42.0,
                        309.0,
                        73.0,
                        56.0,
                        -120.0,
                        351.0,
                        6.0,
                        -193.0,
                        21.0,
                        78.0,
                        57.0,
                        -269.0,
                        -76.0,
                        -299.0,
                        295.0,
                        -278.0,
                        11.0,
                        121.0,
                        -323.0,
                        156.0,
                        67.0,
                        152.0,
                        284.0,
                        108.0,
                        -7.0,
                        329.0,
                        -32.0,
                        333.0,
                        -338.0,
                        148.0,
                        -42.0,
                        151.0,
                        145.0,
                        -34.0,
                        -36.0,
                        296.0,
                        -198.0,
                        -317.0,
                        -161.0,
                        -253.0,
                        328.0,
                        -57.0,
                        134.0,
                        -289.0,
                        229.0,
                        44.0,
                        16.0,
                        -256.0,
                        289.0,
                        -234.0,
                        197.0,
                        333.0,
                        228.0,
                        -143.0,
                        -202.0,
                        -172.0,
                        -262.0,
                        -203.0,
                        -83.0,
                        -242.0,
                        -173.0,
                        336.0,
                        298.0,
                        -319.0,
                        66.0,
                        254.0,
                        214.0,
                        -118.0,
                        -216.0,
                        -168.0,
                        44.0,
                        -243.0,
                        207.0,
                        -28.0,
                        -4.0,
                        -272.0,
                        79.0,
                    ],
                    "timezone": "Atlantic/Reykjavik",
                    "week_start": shared.WeekStart.TU,
                },
            ],
            "recurring_event_id": "cf746b0c-9906-4960-97c6-ccd79704eb13",
            "send_notifications": False,
            "start_at": "2020-05-20T08:05:45.142Z",
            "status": shared.CalendarEventStatus.CONFIRMED,
            "subject": "Sunt spargo tepidus bestia vigor credo coadunatio appello.",
            "timezone": "Asia/Bangkok",
            "updated_at": "2020-06-26T04:47:47.420Z",
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

Update an event

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

Update an event

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
                "start_at": parse_datetime("2024-11-18T11:19:34.135Z"),
            },
            "created_at": parse_datetime("2020-07-14T04:53:23.784Z"),
            "id": "1d29b6fd-b86d-4afb-b957-db2a97784312",
            "type": shared.CrmEventType.CALL,
            "updated_at": parse_datetime("2026-09-09T14:23:44.613Z"),
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

Update an event

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
            "id": "e311e53e-97c5-4259-9cd3-ecc62982f37f",
            "is_replacing_original": False,
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

Remove an event

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

Remove an event

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

Remove an event

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

Update an event

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
            "end_at": "2020-05-20T17:12:37.979Z",
            "id": "67215e17-405a-4402-bfdf-b40ac9978bb3",
            "is_all_day": False,
            "is_free": False,
            "is_private": False,
            "location": "621 Boehm Prairie",
            "notes": "Aegre traho.",
            "recurrence": [
                {
                    "count": 8.0,
                    "end_at": parse_datetime("2025-12-26T06:34:54.364Z"),
                    "excluded_dates": [
                        "2025-09-30T22:42:44.936Z",
                        "2023-10-09T12:14:01.324Z",
                        "2024-02-15T13:20:24.736Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.MONTHLY,
                    "included_dates": [
                        "2021-02-16T22:04:02.467Z",
                    ],
                    "interval": 4.0,
                    "on_days": [
                        shared.PropertyCalendarEventRecurrenceOnDays.TH,
                        shared.PropertyCalendarEventRecurrenceOnDays.MO,
                        shared.PropertyCalendarEventRecurrenceOnDays.TH,
                    ],
                    "on_month_days": [
                        -26.0,
                    ],
                    "on_months": [
                        12.0,
                        9.0,
                        -1.0,
                        0.0,
                        1.0,
                        6.0,
                        -10.0,
                        9.0,
                        0.0,
                        4.0,
                        -2.0,
                    ],
                    "on_weeks": [
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
                    ],
                    "on_year_days": [
                        -35.0,
                        14.0,
                        -338.0,
                        175.0,
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
                    ],
                    "timezone": "Asia/Ho_Chi_Minh",
                    "week_start": shared.WeekStart.SU,
                },
                {
                    "count": 9.0,
                    "end_at": parse_datetime("2025-04-30T05:52:39.892Z"),
                    "excluded_dates": [
                        "2020-04-29T00:43:21.546Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.DAILY,
                    "included_dates": [
                        "2020-09-11T02:34:17.920Z",
                        "2021-11-29T01:27:53.247Z",
                        "2019-12-22T18:06:05.561Z",
                    ],
                    "interval": 1.0,
                    "on_days": [
                        shared.PropertyCalendarEventRecurrenceOnDays.WE,
                        shared.PropertyCalendarEventRecurrenceOnDays.TU,
                        shared.PropertyCalendarEventRecurrenceOnDays.WE,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                    ],
                    "on_month_days": [
                        1.0,
                    ],
                    "on_months": [
                        4.0,
                        0.0,
                        -3.0,
                    ],
                    "on_weeks": [
                        -7.0,
                        -19.0,
                        50.0,
                        -37.0,
                        43.0,
                        -48.0,
                        -30.0,
                        34.0,
                        36.0,
                        -33.0,
                        24.0,
                        -4.0,
                    ],
                    "on_year_days": [
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
                        -35.0,
                        -121.0,
                        262.0,
                        32.0,
                        190.0,
                        107.0,
                        -145.0,
                        91.0,
                        313.0,
                        -48.0,
                        277.0,
                        104.0,
                        342.0,
                        297.0,
                        -216.0,
                        346.0,
                        -257.0,
                        307.0,
                        -44.0,
                        264.0,
                        -153.0,
                        -268.0,
                        92.0,
                        152.0,
                        -182.0,
                        -334.0,
                        89.0,
                        343.0,
                        -320.0,
                        -36.0,
                        84.0,
                        340.0,
                        -88.0,
                        -278.0,
                        202.0,
                        291.0,
                        95.0,
                        -234.0,
                        -304.0,
                        -157.0,
                        -82.0,
                        -339.0,
                        83.0,
                        2.0,
                        -238.0,
                        -204.0,
                        206.0,
                        -273.0,
                        -78.0,
                        -21.0,
                        270.0,
                        -266.0,
                        -276.0,
                        154.0,
                        -97.0,
                        -43.0,
                        -3.0,
                        191.0,
                        -302.0,
                        290.0,
                        -118.0,
                        -125.0,
                        -294.0,
                        115.0,
                        -73.0,
                        -244.0,
                        127.0,
                        26.0,
                        251.0,
                        47.0,
                        -157.0,
                        22.0,
                        -361.0,
                        318.0,
                        352.0,
                        358.0,
                        167.0,
                        210.0,
                        -185.0,
                        327.0,
                        117.0,
                        350.0,
                        -170.0,
                        -144.0,
                        -14.0,
                        -37.0,
                        318.0,
                        243.0,
                        33.0,
                        90.0,
                        319.0,
                        -270.0,
                        229.0,
                        122.0,
                        287.0,
                        -90.0,
                        -69.0,
                        -134.0,
                        -184.0,
                        25.0,
                        -178.0,
                        -89.0,
                        -273.0,
                        -49.0,
                        -362.0,
                        -9.0,
                        -71.0,
                        -347.0,
                        353.0,
                        342.0,
                        133.0,
                        -116.0,
                        231.0,
                        -231.0,
                        51.0,
                        288.0,
                        186.0,
                        -328.0,
                        275.0,
                        81.0,
                        94.0,
                        -263.0,
                        114.0,
                        13.0,
                        -357.0,
                        171.0,
                        -242.0,
                        -85.0,
                        -362.0,
                        108.0,
                        164.0,
                        69.0,
                        15.0,
                        57.0,
                        -287.0,
                        100.0,
                        165.0,
                        205.0,
                        204.0,
                        -78.0,
                        360.0,
                        -80.0,
                        -120.0,
                        -255.0,
                        -77.0,
                        110.0,
                        -26.0,
                        -149.0,
                        -254.0,
                        95.0,
                        32.0,
                        -57.0,
                        -195.0,
                        100.0,
                        221.0,
                        74.0,
                        274.0,
                        15.0,
                        353.0,
                        204.0,
                        -365.0,
                        315.0,
                        344.0,
                        199.0,
                        -59.0,
                        272.0,
                        173.0,
                        -40.0,
                        -318.0,
                        -330.0,
                        -365.0,
                        -272.0,
                        -149.0,
                        -27.0,
                        -334.0,
                        -277.0,
                        344.0,
                        351.0,
                        -310.0,
                        264.0,
                        281.0,
                        176.0,
                        191.0,
                        -183.0,
                        288.0,
                        -112.0,
                        -55.0,
                        -166.0,
                        258.0,
                        194.0,
                        59.0,
                    ],
                    "timezone": "America/Guadeloupe",
                    "week_start": shared.WeekStart.TU,
                },
                {
                    "count": 1.0,
                    "end_at": parse_datetime("2020-11-04T17:53:56.521Z"),
                    "excluded_dates": [
                        "2023-01-11T21:34:37.570Z",
                        "2021-09-07T13:21:42.135Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.WEEKLY,
                    "included_dates": [
                        "2024-08-31T10:58:44.165Z",
                    ],
                    "interval": 9.0,
                    "on_days": [
                        shared.PropertyCalendarEventRecurrenceOnDays.TU,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                    ],
                    "on_month_days": [
                        -2.0,
                    ],
                    "on_months": [
                        -4.0,
                        8.0,
                        0.0,
                        9.0,
                        4.0,
                        -11.0,
                        7.0,
                        1.0,
                        -5.0,
                    ],
                    "on_weeks": [
                        -36.0,
                        -31.0,
                        -16.0,
                        -6.0,
                        44.0,
                        -37.0,
                        14.0,
                        38.0,
                        -27.0,
                        -22.0,
                        -2.0,
                        24.0,
                        7.0,
                        50.0,
                        46.0,
                        52.0,
                        20.0,
                        37.0,
                        31.0,
                        48.0,
                        35.0,
                        -46.0,
                        13.0,
                        22.0,
                        53.0,
                        20.0,
                        -28.0,
                        -2.0,
                        39.0,
                        13.0,
                        4.0,
                        0.0,
                        7.0,
                        -38.0,
                        -35.0,
                        41.0,
                        49.0,
                        12.0,
                        17.0,
                        8.0,
                        49.0,
                        -47.0,
                        46.0,
                        25.0,
                        14.0,
                        -26.0,
                        -37.0,
                        -25.0,
                        -41.0,
                        27.0,
                        28.0,
                        -19.0,
                    ],
                    "on_year_days": [
                        -256.0,
                        -328.0,
                        -312.0,
                        50.0,
                        -251.0,
                        -338.0,
                        -315.0,
                        214.0,
                        129.0,
                        -263.0,
                        -108.0,
                        -11.0,
                        206.0,
                        -29.0,
                        -159.0,
                        -29.0,
                        -264.0,
                        295.0,
                        -231.0,
                        53.0,
                        34.0,
                        -366.0,
                        326.0,
                        -202.0,
                        151.0,
                        79.0,
                        -66.0,
                        11.0,
                        -42.0,
                        73.0,
                        338.0,
                        -155.0,
                        197.0,
                        260.0,
                        356.0,
                        -323.0,
                        -213.0,
                        -332.0,
                        -305.0,
                        -182.0,
                        -253.0,
                        -276.0,
                        -285.0,
                        96.0,
                        -336.0,
                        269.0,
                        -233.0,
                        250.0,
                        -112.0,
                        -307.0,
                        -96.0,
                        54.0,
                        267.0,
                        318.0,
                        -66.0,
                        11.0,
                        -303.0,
                        231.0,
                        165.0,
                        -297.0,
                        -348.0,
                        -355.0,
                        364.0,
                        312.0,
                        -26.0,
                        111.0,
                        162.0,
                        280.0,
                        312.0,
                        337.0,
                        235.0,
                        68.0,
                        -282.0,
                        363.0,
                        212.0,
                        -328.0,
                        9.0,
                        -24.0,
                        -163.0,
                        -101.0,
                        -79.0,
                        -264.0,
                        -157.0,
                        188.0,
                        290.0,
                        51.0,
                        -213.0,
                        216.0,
                        230.0,
                        -270.0,
                        -211.0,
                        -156.0,
                        -165.0,
                        -305.0,
                        -45.0,
                        224.0,
                        -248.0,
                        65.0,
                        9.0,
                        274.0,
                        -299.0,
                        -228.0,
                        33.0,
                        -42.0,
                        356.0,
                        -311.0,
                        241.0,
                        261.0,
                        -136.0,
                        -252.0,
                        166.0,
                        208.0,
                        -126.0,
                        64.0,
                        323.0,
                        -104.0,
                        -106.0,
                        -248.0,
                        -41.0,
                        -109.0,
                        245.0,
                        47.0,
                        205.0,
                        358.0,
                        -296.0,
                        214.0,
                        -157.0,
                        -313.0,
                        -303.0,
                        -54.0,
                        -229.0,
                        231.0,
                        -94.0,
                        -198.0,
                        338.0,
                        199.0,
                        5.0,
                        42.0,
                        309.0,
                        73.0,
                        56.0,
                        -120.0,
                        351.0,
                        6.0,
                        -193.0,
                        21.0,
                        78.0,
                        57.0,
                        -269.0,
                        -76.0,
                        -299.0,
                        295.0,
                        -278.0,
                        11.0,
                        121.0,
                        -323.0,
                        156.0,
                        67.0,
                        152.0,
                        284.0,
                        108.0,
                        -7.0,
                        329.0,
                        -32.0,
                        333.0,
                        -338.0,
                        148.0,
                        -42.0,
                        151.0,
                        145.0,
                        -34.0,
                        -36.0,
                        296.0,
                        -198.0,
                        -317.0,
                        -161.0,
                        -253.0,
                        328.0,
                        -57.0,
                        134.0,
                        -289.0,
                        229.0,
                        44.0,
                        16.0,
                        -256.0,
                        289.0,
                        -234.0,
                        197.0,
                        333.0,
                        228.0,
                        -143.0,
                        -202.0,
                        -172.0,
                        -262.0,
                        -203.0,
                        -83.0,
                        -242.0,
                        -173.0,
                        336.0,
                        298.0,
                        -319.0,
                        66.0,
                        254.0,
                        214.0,
                        -118.0,
                        -216.0,
                        -168.0,
                        44.0,
                        -243.0,
                        207.0,
                        -28.0,
                        -4.0,
                        -272.0,
                        79.0,
                    ],
                    "timezone": "Atlantic/Reykjavik",
                    "week_start": shared.WeekStart.TU,
                },
            ],
            "recurring_event_id": "cf746b0c-9906-4960-97c6-ccd79704eb13",
            "send_notifications": False,
            "start_at": "2020-05-20T08:05:45.142Z",
            "status": shared.CalendarEventStatus.CONFIRMED,
            "subject": "Sunt spargo tepidus bestia vigor credo coadunatio appello.",
            "timezone": "Asia/Bangkok",
            "updated_at": "2020-06-26T04:47:47.420Z",
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

Update an event

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

Update an event

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
                "start_at": parse_datetime("2024-11-18T11:19:34.135Z"),
            },
            "created_at": parse_datetime("2020-07-14T04:53:23.784Z"),
            "id": "1d29b6fd-b86d-4afb-b957-db2a97784312",
            "type": shared.CrmEventType.CALL,
            "updated_at": parse_datetime("2026-09-09T14:23:44.613Z"),
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

Update an event

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
            "id": "e311e53e-97c5-4259-9cd3-ecc62982f37f",
            "is_replacing_original": False,
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