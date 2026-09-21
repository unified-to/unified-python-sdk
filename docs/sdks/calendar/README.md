# Calendar

## Overview

### Available Operations

* [create_calendar_calendar](#create_calendar_calendar) - Create a calendar
* [create_calendar_event](#create_calendar_event) - Create an event
* [create_calendar_link](#create_calendar_link) - Create a link
* [create_calendar_webinar](#create_calendar_webinar) - Create a webinar
* [get_calendar_calendar](#get_calendar_calendar) - Retrieve a calendar
* [get_calendar_event](#get_calendar_event) - Retrieve an event
* [get_calendar_link](#get_calendar_link) - Retrieve a link
* [get_calendar_recording](#get_calendar_recording) - Retrieve a recording
* [get_calendar_webinar](#get_calendar_webinar) - Retrieve a webinar
* [list_calendar_busies](#list_calendar_busies) - List all busies
* [list_calendar_calendars](#list_calendar_calendars) - List all calendars
* [list_calendar_events](#list_calendar_events) - List all events
* [list_calendar_links](#list_calendar_links) - List all links
* [list_calendar_recordings](#list_calendar_recordings) - List all recordings
* [list_calendar_webinars](#list_calendar_webinars) - List all webinars
* [patch_calendar_calendar](#patch_calendar_calendar) - Update a calendar
* [patch_calendar_event](#patch_calendar_event) - Update an event
* [patch_calendar_link](#patch_calendar_link) - Update a link
* [patch_calendar_webinar](#patch_calendar_webinar) - Update a webinar
* [remove_calendar_calendar](#remove_calendar_calendar) - Remove a calendar
* [remove_calendar_event](#remove_calendar_event) - Remove an event
* [remove_calendar_link](#remove_calendar_link) - Remove a link
* [remove_calendar_webinar](#remove_calendar_webinar) - Remove a webinar
* [update_calendar_calendar](#update_calendar_calendar) - Update a calendar
* [update_calendar_event](#update_calendar_event) - Update an event
* [update_calendar_link](#update_calendar_link) - Update a link
* [update_calendar_webinar](#update_calendar_webinar) - Update a webinar

## create_calendar_calendar

Create a calendar

### Example Usage

<!-- UsageSnippet language="python" operationID="createCalendarCalendar" method="post" path="/calendar/{connection_id}/calendar" example="calendar_calendar" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.calendar.create_calendar_calendar(request={
        "calendar_calendar": {
            "created_at": parse_datetime("2020-01-09T23:11:34.147Z"),
            "description": "Socius catena auxilium.",
            "id": "1a0eb48e-5a59-470b-a65d-fd0cda6db0ce",
            "is_primary": False,
            "name": "Acer supra vallum suasoria thesaurus omnis condico cognomen accendo vehemens.",
            "timezone": "America/Dawson_Creek",
            "updated_at": parse_datetime("2023-03-13T19:57:48.816Z"),
        },
        "connection_id": "<id>",
    })

    assert res.calendar_calendar is not None

    # Handle response
    print(res.calendar_calendar)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateCalendarCalendarRequest](../../models/operations/createcalendarcalendarrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.CreateCalendarCalendarResponse](../../models/operations/createcalendarcalendarresponse.md)**

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

    res = unified_to.calendar.create_calendar_event(request={
        "calendar_event": {
            "attachments": [],
            "conference": [],
            "created_at": "2019-08-04T14:33:51.814Z",
            "end_at": "2020-05-20T22:12:09.970Z",
            "id": "f70f46c0-5eab-43c2-9839-a9c19b73a838",
            "is_all_day": False,
            "is_free": False,
            "is_private": False,
            "location": "621 Boehm Prairie",
            "notes": "Aegre traho.",
            "recurrence": [
                {
                    "count": 8.0,
                    "end_at": parse_datetime("2025-12-27T22:46:26.224Z"),
                    "excluded_dates": [
                        "2025-10-02T13:25:08.884Z",
                        "2023-10-10T14:30:31.170Z",
                        "2024-02-16T17:50:08.837Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.MONTHLY,
                    "included_dates": [
                        "2021-02-17T07:44:37.075Z",
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
                    "end_at": parse_datetime("2025-05-01T17:56:22.216Z"),
                    "excluded_dates": [
                        "2020-04-29T05:20:30.053Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.DAILY,
                    "included_dates": [
                        "2020-09-11T09:30:54.291Z",
                        "2021-11-29T16:02:52.041Z",
                        "2019-12-22T20:30:47.527Z",
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
                    "end_at": parse_datetime("2020-11-05T01:46:57.692Z"),
                    "excluded_dates": [
                        "2023-01-12T19:11:43.400Z",
                        "2021-09-08T02:31:29.884Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.WEEKLY,
                    "included_dates": [
                        "2024-09-01T18:52:48.039Z",
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
            "recurring_event_id": "009a0eae-e5b4-4c9b-94aa-47bbdff410f3",
            "send_notifications": False,
            "start_at": "2020-05-20T13:04:53.606Z",
            "status": shared.CalendarEventStatus.CONFIRMED,
            "subject": "Sunt spargo tepidus bestia vigor credo coadunatio appello.",
            "timezone": "Asia/Bangkok",
            "updated_at": "2020-06-26T10:24:59.474Z",
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

## create_calendar_link

Create a link

### Example Usage

<!-- UsageSnippet language="python" operationID="createCalendarLink" method="post" path="/calendar/{connection_id}/link" example="calendar_link" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.calendar.create_calendar_link(request={
        "calendar_link": {
            "created_at": "2023-03-07T13:34:11.959Z",
            "description": "Vitium clibanus laboriosam uxor denuncio.",
            "duration": 74.0,
            "id": "d8083e56-d7c9-4e83-aba6-34fa2c21d0aa",
            "is_active": True,
            "name": "Sopor sopor ancilla animus anser dignissimos vito confero utilis.",
            "price_amount": 44.0,
            "price_currency": "USD",
            "updated_at": "2024-03-07T00:10:45.521Z",
            "url": "https://annual-apricot.info/",
        },
        "connection_id": "<id>",
    })

    assert res.calendar_link is not None

    # Handle response
    print(res.calendar_link)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateCalendarLinkRequest](../../models/operations/createcalendarlinkrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateCalendarLinkResponse](../../models/operations/createcalendarlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_calendar_webinar

Create a webinar

### Example Usage

<!-- UsageSnippet language="python" operationID="createCalendarWebinar" method="post" path="/calendar/{connection_id}/webinar" example="calendar_webinar" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.calendar.create_calendar_webinar(request={
        "calendar_webinar": {
            "conference": [],
            "created_at": parse_datetime("2022-07-06T11:45:14.631Z"),
            "end_at": parse_datetime("2025-10-05T09:39:32.834Z"),
            "has_polls": False,
            "has_recording": False,
            "id": "3eb0a521-d005-4963-9462-24e2e4845197",
            "is_auto_approve": False,
            "is_enabled": True,
            "is_webcast": False,
            "join_url": "https://robust-bathhouse.biz",
            "notes": "Curriculum ducimus assentator aspernatur ait.",
            "organizer": {
                "email": "Kelton_Dicki@yahoo.com",
                "name": "Walter Greenfelder",
            },
            "recurrence": [
                {
                    "count": 10.0,
                    "end_at": parse_datetime("2023-08-23T12:02:48.880Z"),
                    "excluded_dates": [
                        "2025-01-25T16:04:34.261Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.MONTHLY,
                    "included_dates": [
                        "2024-04-15T12:43:36.264Z",
                    ],
                    "interval": 8.0,
                    "on_days": [
                        shared.PropertyCalendarEventRecurrenceOnDays.SU,
                        shared.PropertyCalendarEventRecurrenceOnDays.FR,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                        shared.PropertyCalendarEventRecurrenceOnDays.WE,
                        shared.PropertyCalendarEventRecurrenceOnDays.MO,
                    ],
                    "on_month_days": [
                        -10.0,
                    ],
                    "on_months": [
                        -9.0,
                    ],
                    "on_weeks": [
                        10.0,
                        30.0,
                        -38.0,
                        30.0,
                        -22.0,
                        37.0,
                        -12.0,
                        27.0,
                        2.0,
                        15.0,
                        26.0,
                        18.0,
                        -43.0,
                        -33.0,
                        -27.0,
                        38.0,
                        28.0,
                        47.0,
                        -8.0,
                        24.0,
                        35.0,
                        -2.0,
                        7.0,
                        49.0,
                        38.0,
                        -41.0,
                        46.0,
                        -11.0,
                        -45.0,
                        0.0,
                        48.0,
                        34.0,
                    ],
                    "on_year_days": [
                        345.0,
                        -207.0,
                        230.0,
                        -10.0,
                        364.0,
                        -256.0,
                        -218.0,
                        -295.0,
                        290.0,
                        -250.0,
                        -315.0,
                        60.0,
                        205.0,
                        -247.0,
                        -318.0,
                        -211.0,
                        -13.0,
                        256.0,
                        -200.0,
                        -313.0,
                        336.0,
                        -332.0,
                        -90.0,
                        287.0,
                        -273.0,
                        156.0,
                        241.0,
                        -138.0,
                        -363.0,
                        -37.0,
                        -171.0,
                        -62.0,
                        -57.0,
                        280.0,
                        -322.0,
                        -79.0,
                        -364.0,
                        -201.0,
                        84.0,
                        341.0,
                        334.0,
                        -75.0,
                        332.0,
                        207.0,
                        337.0,
                        -244.0,
                        131.0,
                        -191.0,
                        164.0,
                        -235.0,
                        285.0,
                        -309.0,
                        -158.0,
                        306.0,
                        180.0,
                        -130.0,
                        -162.0,
                        -155.0,
                        3.0,
                        198.0,
                        26.0,
                        -366.0,
                        -191.0,
                        127.0,
                        -331.0,
                        -11.0,
                        -239.0,
                        -189.0,
                        243.0,
                        118.0,
                        346.0,
                        -174.0,
                        -146.0,
                        -161.0,
                        -330.0,
                        327.0,
                        192.0,
                        310.0,
                        316.0,
                        313.0,
                        -242.0,
                        -51.0,
                        -264.0,
                        -180.0,
                        -88.0,
                        305.0,
                        270.0,
                        358.0,
                        -173.0,
                        -298.0,
                        153.0,
                        -89.0,
                        155.0,
                        -45.0,
                        248.0,
                        -46.0,
                        -146.0,
                        300.0,
                        364.0,
                        -335.0,
                        356.0,
                        -18.0,
                        219.0,
                        324.0,
                        -239.0,
                        -106.0,
                        -298.0,
                        328.0,
                        362.0,
                        344.0,
                        -54.0,
                        133.0,
                        50.0,
                        112.0,
                        -212.0,
                        -179.0,
                        22.0,
                        -201.0,
                        -62.0,
                        -293.0,
                        9.0,
                        30.0,
                        -50.0,
                        126.0,
                        -72.0,
                        264.0,
                        28.0,
                        -1.0,
                        -207.0,
                        160.0,
                        -168.0,
                        3.0,
                        -176.0,
                        -19.0,
                        -157.0,
                        349.0,
                        100.0,
                        -201.0,
                        108.0,
                        -180.0,
                        51.0,
                        -73.0,
                        366.0,
                        74.0,
                        -226.0,
                        238.0,
                        121.0,
                        -193.0,
                        -125.0,
                        -109.0,
                        316.0,
                        -177.0,
                        -307.0,
                        31.0,
                        -76.0,
                        217.0,
                        -310.0,
                        227.0,
                        -360.0,
                        71.0,
                        255.0,
                        -325.0,
                        -214.0,
                        40.0,
                        42.0,
                        17.0,
                        -241.0,
                        -84.0,
                        -188.0,
                        302.0,
                        64.0,
                        94.0,
                        -362.0,
                        23.0,
                        166.0,
                        85.0,
                        71.0,
                        -74.0,
                        -47.0,
                        -119.0,
                        98.0,
                        40.0,
                        158.0,
                        -64.0,
                        175.0,
                        269.0,
                        127.0,
                        -143.0,
                        213.0,
                        -196.0,
                        121.0,
                        81.0,
                        -238.0,
                        288.0,
                        321.0,
                        276.0,
                        133.0,
                        22.0,
                        -213.0,
                        -157.0,
                        -280.0,
                        -35.0,
                        73.0,
                        -194.0,
                        65.0,
                        -180.0,
                        63.0,
                        -242.0,
                        -117.0,
                        148.0,
                        157.0,
                        -320.0,
                        318.0,
                        8.0,
                        210.0,
                        -21.0,
                        81.0,
                        205.0,
                        -258.0,
                        -40.0,
                        -114.0,
                        -253.0,
                        -263.0,
                        65.0,
                        185.0,
                        -24.0,
                        324.0,
                        -172.0,
                        25.0,
                        260.0,
                        211.0,
                        342.0,
                        -31.0,
                        -288.0,
                        -159.0,
                        -4.0,
                        -2.0,
                        -107.0,
                        -316.0,
                        -276.0,
                        331.0,
                        -114.0,
                        -20.0,
                        -320.0,
                        51.0,
                        -176.0,
                        -148.0,
                        -50.0,
                        -201.0,
                        -104.0,
                        153.0,
                        -273.0,
                        -189.0,
                        67.0,
                        209.0,
                        149.0,
                        49.0,
                        -136.0,
                        -125.0,
                        -169.0,
                        -324.0,
                        309.0,
                        -51.0,
                        288.0,
                        253.0,
                        175.0,
                        -146.0,
                        171.0,
                        -140.0,
                        58.0,
                        -212.0,
                        164.0,
                        270.0,
                        102.0,
                        70.0,
                        299.0,
                        89.0,
                        -280.0,
                        252.0,
                        -342.0,
                        240.0,
                        226.0,
                        68.0,
                        -30.0,
                        -232.0,
                        -358.0,
                        -166.0,
                        60.0,
                        140.0,
                        275.0,
                        13.0,
                        250.0,
                        -328.0,
                        -189.0,
                        -22.0,
                        7.0,
                        -235.0,
                        -322.0,
                        178.0,
                        167.0,
                        -104.0,
                        -61.0,
                        282.0,
                        -80.0,
                        -277.0,
                        108.0,
                        271.0,
                        -237.0,
                        297.0,
                        -135.0,
                        -135.0,
                        -323.0,
                        342.0,
                        -267.0,
                        -235.0,
                        173.0,
                        249.0,
                        -288.0,
                        257.0,
                        139.0,
                        -191.0,
                        -217.0,
                        10.0,
                        -117.0,
                        -297.0,
                        -196.0,
                        -206.0,
                        341.0,
                        166.0,
                        181.0,
                        129.0,
                        -207.0,
                        55.0,
                        86.0,
                    ],
                    "timezone": "Asia/Ust-Nera",
                    "week_start": shared.WeekStart.MO,
                },
                {
                    "count": 3.0,
                    "end_at": parse_datetime("2022-09-29T00:22:06.773Z"),
                    "excluded_dates": [
                        "2024-08-17T13:33:08.997Z",
                        "2024-08-02T07:46:19.987Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.DAILY,
                    "included_dates": [
                        "2024-03-13T01:54:56.111Z",
                        "2025-12-19T14:31:01.408Z",
                        "2023-08-06T11:38:08.986Z",
                    ],
                    "interval": 1.0,
                    "on_days": [
                        shared.PropertyCalendarEventRecurrenceOnDays.WE,
                        shared.PropertyCalendarEventRecurrenceOnDays.SU,
                        shared.PropertyCalendarEventRecurrenceOnDays.MO,
                        shared.PropertyCalendarEventRecurrenceOnDays.FR,
                    ],
                    "on_month_days": [
                        -15.0,
                    ],
                    "on_months": [
                        5.0,
                        12.0,
                        3.0,
                        12.0,
                        8.0,
                    ],
                    "on_weeks": [
                        -47.0,
                        44.0,
                    ],
                    "on_year_days": [
                        -117.0,
                        59.0,
                        -6.0,
                        187.0,
                        45.0,
                        70.0,
                        15.0,
                        255.0,
                        44.0,
                        -2.0,
                        25.0,
                        -175.0,
                        -240.0,
                        171.0,
                        -294.0,
                        19.0,
                        38.0,
                        -351.0,
                        170.0,
                        -10.0,
                        -269.0,
                        18.0,
                        -65.0,
                        -266.0,
                        -31.0,
                        328.0,
                        -361.0,
                        358.0,
                        -256.0,
                        -4.0,
                        -312.0,
                        82.0,
                        -2.0,
                        -75.0,
                        -281.0,
                        -304.0,
                        53.0,
                        -295.0,
                        366.0,
                        322.0,
                        -191.0,
                        26.0,
                        97.0,
                        53.0,
                        75.0,
                        -62.0,
                        -109.0,
                        66.0,
                        177.0,
                        -68.0,
                        175.0,
                        -280.0,
                        70.0,
                        -238.0,
                        109.0,
                        -304.0,
                        326.0,
                        -8.0,
                        -71.0,
                        -236.0,
                        225.0,
                        358.0,
                        20.0,
                        -5.0,
                        -102.0,
                        -134.0,
                        -204.0,
                        -116.0,
                        -353.0,
                        -273.0,
                        106.0,
                        284.0,
                        -137.0,
                        -324.0,
                        301.0,
                        -42.0,
                        -229.0,
                        271.0,
                        -293.0,
                        -343.0,
                        211.0,
                        47.0,
                        -254.0,
                        -154.0,
                        -182.0,
                        264.0,
                        120.0,
                        -11.0,
                        -307.0,
                        99.0,
                        227.0,
                        190.0,
                        -17.0,
                        -77.0,
                        -255.0,
                        -61.0,
                        -249.0,
                        -102.0,
                        70.0,
                        345.0,
                        -187.0,
                        -308.0,
                        194.0,
                        221.0,
                        268.0,
                        -169.0,
                        -190.0,
                        88.0,
                        10.0,
                        262.0,
                        177.0,
                        -314.0,
                        -151.0,
                        -295.0,
                    ],
                    "timezone": "Pacific/Wake",
                    "week_start": shared.WeekStart.TU,
                },
                {
                    "count": 8.0,
                    "end_at": parse_datetime("2026-06-27T23:52:37.583Z"),
                    "excluded_dates": [
                        "2023-06-11T21:57:35.693Z",
                        "2023-06-01T03:52:20.354Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.WEEKLY,
                    "included_dates": [
                        "2024-03-20T23:04:15.238Z",
                        "2023-08-12T04:22:34.437Z",
                        "2024-09-11T06:40:50.514Z",
                    ],
                    "interval": 8.0,
                    "on_days": [
                        shared.PropertyCalendarEventRecurrenceOnDays.SU,
                        shared.PropertyCalendarEventRecurrenceOnDays.MO,
                        shared.PropertyCalendarEventRecurrenceOnDays.TU,
                        shared.PropertyCalendarEventRecurrenceOnDays.FR,
                        shared.PropertyCalendarEventRecurrenceOnDays.MO,
                        shared.PropertyCalendarEventRecurrenceOnDays.TH,
                    ],
                    "on_month_days": [
                        -23.0,
                    ],
                    "on_months": [
                        11.0,
                        8.0,
                        9.0,
                        5.0,
                        -12.0,
                        -7.0,
                        -5.0,
                        10.0,
                        10.0,
                        -9.0,
                        -10.0,
                    ],
                    "on_weeks": [
                        -49.0,
                        46.0,
                        35.0,
                        -26.0,
                        2.0,
                        15.0,
                        15.0,
                        -26.0,
                        24.0,
                        -53.0,
                        36.0,
                        -43.0,
                        51.0,
                        -19.0,
                        -7.0,
                        -12.0,
                        28.0,
                        27.0,
                        35.0,
                        12.0,
                        -28.0,
                        -8.0,
                        -4.0,
                        -45.0,
                    ],
                    "on_year_days": [
                        84.0,
                        -251.0,
                        71.0,
                        181.0,
                        -163.0,
                        158.0,
                        301.0,
                        -299.0,
                        -184.0,
                        -331.0,
                        -152.0,
                        -129.0,
                        -237.0,
                        -303.0,
                        -24.0,
                        126.0,
                        -103.0,
                        146.0,
                        -346.0,
                        86.0,
                        -296.0,
                        -337.0,
                        -185.0,
                        16.0,
                        -270.0,
                        -126.0,
                        -295.0,
                        -231.0,
                        356.0,
                        -293.0,
                        115.0,
                        -265.0,
                        -293.0,
                        -34.0,
                        357.0,
                        313.0,
                        -343.0,
                        180.0,
                        -22.0,
                        -161.0,
                        350.0,
                        177.0,
                        190.0,
                        223.0,
                        -152.0,
                        -360.0,
                        -225.0,
                        -60.0,
                        -35.0,
                        353.0,
                        117.0,
                        -171.0,
                        -315.0,
                        -321.0,
                        -202.0,
                        345.0,
                        -1.0,
                        -148.0,
                        -168.0,
                        181.0,
                        -17.0,
                        282.0,
                        234.0,
                        31.0,
                        47.0,
                        -236.0,
                        366.0,
                        -251.0,
                        -232.0,
                        -308.0,
                        76.0,
                        -199.0,
                        184.0,
                        198.0,
                        225.0,
                        75.0,
                        6.0,
                        227.0,
                        -148.0,
                        259.0,
                        -146.0,
                        49.0,
                        -254.0,
                        341.0,
                        93.0,
                        138.0,
                        -164.0,
                        237.0,
                        4.0,
                        -287.0,
                        161.0,
                    ],
                    "timezone": "Africa/Bissau",
                    "week_start": shared.WeekStart.WE,
                },
            ],
            "registrant_password": "OxwWzr0C",
            "require_address": False,
            "require_job_title": False,
            "start_at": parse_datetime("2025-04-10T17:53:15.626Z"),
            "status": shared.CalendarWebinarStatus.TENTATIVE,
            "subject": "Harum culpa decipio ex cubo ancilla cresco.",
            "timezone": "Europe/Kaliningrad",
            "updated_at": parse_datetime("2026-08-31T16:38:14.935Z"),
            "web_url": "https://classic-recovery.biz",
        },
        "connection_id": "<id>",
    })

    assert res.calendar_webinar is not None

    # Handle response
    print(res.calendar_webinar)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateCalendarWebinarRequest](../../models/operations/createcalendarwebinarrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateCalendarWebinarResponse](../../models/operations/createcalendarwebinarresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_calendar_calendar

Retrieve a calendar

### Example Usage

<!-- UsageSnippet language="python" operationID="getCalendarCalendar" method="get" path="/calendar/{connection_id}/calendar/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.calendar.get_calendar_calendar(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_calendar is not None

    # Handle response
    print(res.calendar_calendar)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetCalendarCalendarRequest](../../models/operations/getcalendarcalendarrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetCalendarCalendarResponse](../../models/operations/getcalendarcalendarresponse.md)**

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

    res = unified_to.calendar.get_calendar_event(request={
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

## get_calendar_link

Retrieve a link

### Example Usage

<!-- UsageSnippet language="python" operationID="getCalendarLink" method="get" path="/calendar/{connection_id}/link/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.calendar.get_calendar_link(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_link is not None

    # Handle response
    print(res.calendar_link)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetCalendarLinkRequest](../../models/operations/getcalendarlinkrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetCalendarLinkResponse](../../models/operations/getcalendarlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_calendar_recording

Retrieve a recording

### Example Usage

<!-- UsageSnippet language="python" operationID="getCalendarRecording" method="get" path="/calendar/{connection_id}/recording/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.calendar.get_calendar_recording(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_recording is not None

    # Handle response
    print(res.calendar_recording)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetCalendarRecordingRequest](../../models/operations/getcalendarrecordingrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetCalendarRecordingResponse](../../models/operations/getcalendarrecordingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_calendar_webinar

Retrieve a webinar

### Example Usage

<!-- UsageSnippet language="python" operationID="getCalendarWebinar" method="get" path="/calendar/{connection_id}/webinar/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.calendar.get_calendar_webinar(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_webinar is not None

    # Handle response
    print(res.calendar_webinar)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetCalendarWebinarRequest](../../models/operations/getcalendarwebinarrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetCalendarWebinarResponse](../../models/operations/getcalendarwebinarresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_calendar_busies

List all busies

### Example Usage

<!-- UsageSnippet language="python" operationID="listCalendarBusies" method="get" path="/calendar/{connection_id}/busy" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.calendar.list_calendar_busies(request={
        "connection_id": "<id>",
    })

    assert res.calendar_busies is not None

    # Handle response
    print(res.calendar_busies)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListCalendarBusiesRequest](../../models/operations/listcalendarbusiesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListCalendarBusiesResponse](../../models/operations/listcalendarbusiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_calendar_calendars

List all calendars

### Example Usage

<!-- UsageSnippet language="python" operationID="listCalendarCalendars" method="get" path="/calendar/{connection_id}/calendar" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.calendar.list_calendar_calendars(request={
        "connection_id": "<id>",
    })

    assert res.calendar_calendars is not None

    # Handle response
    print(res.calendar_calendars)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListCalendarCalendarsRequest](../../models/operations/listcalendarcalendarsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListCalendarCalendarsResponse](../../models/operations/listcalendarcalendarsresponse.md)**

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

    res = unified_to.calendar.list_calendar_events(request={
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

## list_calendar_links

List all links

### Example Usage

<!-- UsageSnippet language="python" operationID="listCalendarLinks" method="get" path="/calendar/{connection_id}/link" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.calendar.list_calendar_links(request={
        "connection_id": "<id>",
    })

    assert res.calendar_links is not None

    # Handle response
    print(res.calendar_links)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListCalendarLinksRequest](../../models/operations/listcalendarlinksrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListCalendarLinksResponse](../../models/operations/listcalendarlinksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_calendar_recordings

List all recordings

### Example Usage

<!-- UsageSnippet language="python" operationID="listCalendarRecordings" method="get" path="/calendar/{connection_id}/recording" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.calendar.list_calendar_recordings(request={
        "connection_id": "<id>",
    })

    assert res.calendar_recordings is not None

    # Handle response
    print(res.calendar_recordings)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListCalendarRecordingsRequest](../../models/operations/listcalendarrecordingsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListCalendarRecordingsResponse](../../models/operations/listcalendarrecordingsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_calendar_webinars

List all webinars

### Example Usage

<!-- UsageSnippet language="python" operationID="listCalendarWebinars" method="get" path="/calendar/{connection_id}/webinar" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.calendar.list_calendar_webinars(request={
        "connection_id": "<id>",
    })

    assert res.calendar_webinars is not None

    # Handle response
    print(res.calendar_webinars)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListCalendarWebinarsRequest](../../models/operations/listcalendarwebinarsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListCalendarWebinarsResponse](../../models/operations/listcalendarwebinarsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_calendar_calendar

Update a calendar

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCalendarCalendar" method="patch" path="/calendar/{connection_id}/calendar/{id}" example="calendar_calendar" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.calendar.patch_calendar_calendar(request={
        "calendar_calendar": {
            "created_at": parse_datetime("2020-01-09T23:11:34.147Z"),
            "description": "Socius catena auxilium.",
            "id": "05672e3b-7cd1-4fcd-8c7b-aa835bca3c35",
            "is_primary": False,
            "name": "Acer supra vallum suasoria thesaurus omnis condico cognomen accendo vehemens.",
            "timezone": "America/Dawson_Creek",
            "updated_at": parse_datetime("2023-03-13T19:57:48.820Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_calendar is not None

    # Handle response
    print(res.calendar_calendar)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PatchCalendarCalendarRequest](../../models/operations/patchcalendarcalendarrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.PatchCalendarCalendarResponse](../../models/operations/patchcalendarcalendarresponse.md)**

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

    res = unified_to.calendar.patch_calendar_event(request={
        "calendar_event": {
            "attachments": [],
            "conference": [],
            "created_at": "2019-08-04T14:33:51.814Z",
            "end_at": "2020-05-20T22:12:09.976Z",
            "id": "3aefb04c-c6a1-4dec-b773-2993a61a654c",
            "is_all_day": False,
            "is_free": False,
            "is_private": False,
            "location": "621 Boehm Prairie",
            "notes": "Aegre traho.",
            "recurrence": [
                {
                    "count": 8.0,
                    "end_at": parse_datetime("2025-12-27T22:46:26.267Z"),
                    "excluded_dates": [
                        "2025-10-02T13:25:08.926Z",
                        "2023-10-10T14:30:31.199Z",
                        "2024-02-16T17:50:08.868Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.MONTHLY,
                    "included_dates": [
                        "2021-02-17T07:44:37.086Z",
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
                    "end_at": parse_datetime("2025-05-01T17:56:22.256Z"),
                    "excluded_dates": [
                        "2020-04-29T05:20:30.058Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.DAILY,
                    "included_dates": [
                        "2020-09-11T09:30:54.299Z",
                        "2021-11-29T16:02:52.057Z",
                        "2019-12-22T20:30:47.530Z",
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
                    "end_at": parse_datetime("2020-11-05T01:46:57.701Z"),
                    "excluded_dates": [
                        "2023-01-12T19:11:43.424Z",
                        "2021-09-08T02:31:29.899Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.WEEKLY,
                    "included_dates": [
                        "2024-09-01T18:52:48.074Z",
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
            "recurring_event_id": "46684a25-2b83-43e0-bd4a-14a99d099b8e",
            "send_notifications": False,
            "start_at": "2020-05-20T13:04:53.612Z",
            "status": shared.CalendarEventStatus.CONFIRMED,
            "subject": "Sunt spargo tepidus bestia vigor credo coadunatio appello.",
            "timezone": "Asia/Bangkok",
            "updated_at": "2020-06-26T10:24:59.480Z",
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

## patch_calendar_link

Update a link

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCalendarLink" method="patch" path="/calendar/{connection_id}/link/{id}" example="calendar_link" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.calendar.patch_calendar_link(request={
        "calendar_link": {
            "created_at": "2023-03-07T13:34:11.959Z",
            "description": "Vitium clibanus laboriosam uxor denuncio.",
            "duration": 74.0,
            "id": "6158108d-5979-48b8-a43b-e23ca21ffab4",
            "is_active": True,
            "name": "Sopor sopor ancilla animus anser dignissimos vito confero utilis.",
            "price_amount": 44.0,
            "price_currency": "USD",
            "updated_at": "2024-03-07T00:10:45.524Z",
            "url": "https://annual-apricot.info/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_link is not None

    # Handle response
    print(res.calendar_link)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchCalendarLinkRequest](../../models/operations/patchcalendarlinkrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchCalendarLinkResponse](../../models/operations/patchcalendarlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_calendar_webinar

Update a webinar

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCalendarWebinar" method="patch" path="/calendar/{connection_id}/webinar/{id}" example="calendar_webinar" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.calendar.patch_calendar_webinar(request={
        "calendar_webinar": {
            "conference": [],
            "created_at": parse_datetime("2022-07-06T11:45:14.631Z"),
            "end_at": parse_datetime("2025-10-05T09:39:32.879Z"),
            "has_polls": False,
            "has_recording": False,
            "id": "4a2424d9-2fc7-4247-973a-bf68830ef4bc",
            "is_auto_approve": False,
            "is_enabled": True,
            "is_webcast": False,
            "join_url": "https://robust-bathhouse.biz",
            "notes": "Curriculum ducimus assentator aspernatur ait.",
            "organizer": {
                "email": "Kelton_Dicki@yahoo.com",
                "name": "Walter Greenfelder",
            },
            "recurrence": [
                {
                    "count": 10.0,
                    "end_at": parse_datetime("2023-08-23T12:02:48.896Z"),
                    "excluded_dates": [
                        "2025-01-25T16:04:34.297Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.MONTHLY,
                    "included_dates": [
                        "2024-04-15T12:43:36.288Z",
                    ],
                    "interval": 8.0,
                    "on_days": [
                        shared.PropertyCalendarEventRecurrenceOnDays.SU,
                        shared.PropertyCalendarEventRecurrenceOnDays.FR,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                        shared.PropertyCalendarEventRecurrenceOnDays.WE,
                        shared.PropertyCalendarEventRecurrenceOnDays.MO,
                    ],
                    "on_month_days": [
                        -10.0,
                    ],
                    "on_months": [
                        -9.0,
                    ],
                    "on_weeks": [
                        10.0,
                        30.0,
                        -38.0,
                        30.0,
                        -22.0,
                        37.0,
                        -12.0,
                        27.0,
                        2.0,
                        15.0,
                        26.0,
                        18.0,
                        -43.0,
                        -33.0,
                        -27.0,
                        38.0,
                        28.0,
                        47.0,
                        -8.0,
                        24.0,
                        35.0,
                        -2.0,
                        7.0,
                        49.0,
                        38.0,
                        -41.0,
                        46.0,
                        -11.0,
                        -45.0,
                        0.0,
                        48.0,
                        34.0,
                    ],
                    "on_year_days": [
                        345.0,
                        -207.0,
                        230.0,
                        -10.0,
                        364.0,
                        -256.0,
                        -218.0,
                        -295.0,
                        290.0,
                        -250.0,
                        -315.0,
                        60.0,
                        205.0,
                        -247.0,
                        -318.0,
                        -211.0,
                        -13.0,
                        256.0,
                        -200.0,
                        -313.0,
                        336.0,
                        -332.0,
                        -90.0,
                        287.0,
                        -273.0,
                        156.0,
                        241.0,
                        -138.0,
                        -363.0,
                        -37.0,
                        -171.0,
                        -62.0,
                        -57.0,
                        280.0,
                        -322.0,
                        -79.0,
                        -364.0,
                        -201.0,
                        84.0,
                        341.0,
                        334.0,
                        -75.0,
                        332.0,
                        207.0,
                        337.0,
                        -244.0,
                        131.0,
                        -191.0,
                        164.0,
                        -235.0,
                        285.0,
                        -309.0,
                        -158.0,
                        306.0,
                        180.0,
                        -130.0,
                        -162.0,
                        -155.0,
                        3.0,
                        198.0,
                        26.0,
                        -366.0,
                        -191.0,
                        127.0,
                        -331.0,
                        -11.0,
                        -239.0,
                        -189.0,
                        243.0,
                        118.0,
                        346.0,
                        -174.0,
                        -146.0,
                        -161.0,
                        -330.0,
                        327.0,
                        192.0,
                        310.0,
                        316.0,
                        313.0,
                        -242.0,
                        -51.0,
                        -264.0,
                        -180.0,
                        -88.0,
                        305.0,
                        270.0,
                        358.0,
                        -173.0,
                        -298.0,
                        153.0,
                        -89.0,
                        155.0,
                        -45.0,
                        248.0,
                        -46.0,
                        -146.0,
                        300.0,
                        364.0,
                        -335.0,
                        356.0,
                        -18.0,
                        219.0,
                        324.0,
                        -239.0,
                        -106.0,
                        -298.0,
                        328.0,
                        362.0,
                        344.0,
                        -54.0,
                        133.0,
                        50.0,
                        112.0,
                        -212.0,
                        -179.0,
                        22.0,
                        -201.0,
                        -62.0,
                        -293.0,
                        9.0,
                        30.0,
                        -50.0,
                        126.0,
                        -72.0,
                        264.0,
                        28.0,
                        -1.0,
                        -207.0,
                        160.0,
                        -168.0,
                        3.0,
                        -176.0,
                        -19.0,
                        -157.0,
                        349.0,
                        100.0,
                        -201.0,
                        108.0,
                        -180.0,
                        51.0,
                        -73.0,
                        366.0,
                        74.0,
                        -226.0,
                        238.0,
                        121.0,
                        -193.0,
                        -125.0,
                        -109.0,
                        316.0,
                        -177.0,
                        -307.0,
                        31.0,
                        -76.0,
                        217.0,
                        -310.0,
                        227.0,
                        -360.0,
                        71.0,
                        255.0,
                        -325.0,
                        -214.0,
                        40.0,
                        42.0,
                        17.0,
                        -241.0,
                        -84.0,
                        -188.0,
                        302.0,
                        64.0,
                        94.0,
                        -362.0,
                        23.0,
                        166.0,
                        85.0,
                        71.0,
                        -74.0,
                        -47.0,
                        -119.0,
                        98.0,
                        40.0,
                        158.0,
                        -64.0,
                        175.0,
                        269.0,
                        127.0,
                        -143.0,
                        213.0,
                        -196.0,
                        121.0,
                        81.0,
                        -238.0,
                        288.0,
                        321.0,
                        276.0,
                        133.0,
                        22.0,
                        -213.0,
                        -157.0,
                        -280.0,
                        -35.0,
                        73.0,
                        -194.0,
                        65.0,
                        -180.0,
                        63.0,
                        -242.0,
                        -117.0,
                        148.0,
                        157.0,
                        -320.0,
                        318.0,
                        8.0,
                        210.0,
                        -21.0,
                        81.0,
                        205.0,
                        -258.0,
                        -40.0,
                        -114.0,
                        -253.0,
                        -263.0,
                        65.0,
                        185.0,
                        -24.0,
                        324.0,
                        -172.0,
                        25.0,
                        260.0,
                        211.0,
                        342.0,
                        -31.0,
                        -288.0,
                        -159.0,
                        -4.0,
                        -2.0,
                        -107.0,
                        -316.0,
                        -276.0,
                        331.0,
                        -114.0,
                        -20.0,
                        -320.0,
                        51.0,
                        -176.0,
                        -148.0,
                        -50.0,
                        -201.0,
                        -104.0,
                        153.0,
                        -273.0,
                        -189.0,
                        67.0,
                        209.0,
                        149.0,
                        49.0,
                        -136.0,
                        -125.0,
                        -169.0,
                        -324.0,
                        309.0,
                        -51.0,
                        288.0,
                        253.0,
                        175.0,
                        -146.0,
                        171.0,
                        -140.0,
                        58.0,
                        -212.0,
                        164.0,
                        270.0,
                        102.0,
                        70.0,
                        299.0,
                        89.0,
                        -280.0,
                        252.0,
                        -342.0,
                        240.0,
                        226.0,
                        68.0,
                        -30.0,
                        -232.0,
                        -358.0,
                        -166.0,
                        60.0,
                        140.0,
                        275.0,
                        13.0,
                        250.0,
                        -328.0,
                        -189.0,
                        -22.0,
                        7.0,
                        -235.0,
                        -322.0,
                        178.0,
                        167.0,
                        -104.0,
                        -61.0,
                        282.0,
                        -80.0,
                        -277.0,
                        108.0,
                        271.0,
                        -237.0,
                        297.0,
                        -135.0,
                        -135.0,
                        -323.0,
                        342.0,
                        -267.0,
                        -235.0,
                        173.0,
                        249.0,
                        -288.0,
                        257.0,
                        139.0,
                        -191.0,
                        -217.0,
                        10.0,
                        -117.0,
                        -297.0,
                        -196.0,
                        -206.0,
                        341.0,
                        166.0,
                        181.0,
                        129.0,
                        -207.0,
                        55.0,
                        86.0,
                    ],
                    "timezone": "Asia/Ust-Nera",
                    "week_start": shared.WeekStart.MO,
                },
                {
                    "count": 3.0,
                    "end_at": parse_datetime("2022-09-29T00:22:06.776Z"),
                    "excluded_dates": [
                        "2024-08-17T13:33:09.027Z",
                        "2024-08-02T07:46:20.015Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.DAILY,
                    "included_dates": [
                        "2024-03-13T01:54:56.135Z",
                        "2025-12-19T14:31:01.456Z",
                        "2023-08-06T11:38:09.001Z",
                    ],
                    "interval": 1.0,
                    "on_days": [
                        shared.PropertyCalendarEventRecurrenceOnDays.WE,
                        shared.PropertyCalendarEventRecurrenceOnDays.SU,
                        shared.PropertyCalendarEventRecurrenceOnDays.MO,
                        shared.PropertyCalendarEventRecurrenceOnDays.FR,
                    ],
                    "on_month_days": [
                        -15.0,
                    ],
                    "on_months": [
                        5.0,
                        12.0,
                        3.0,
                        12.0,
                        8.0,
                    ],
                    "on_weeks": [
                        -47.0,
                        44.0,
                    ],
                    "on_year_days": [
                        -117.0,
                        59.0,
                        -6.0,
                        187.0,
                        45.0,
                        70.0,
                        15.0,
                        255.0,
                        44.0,
                        -2.0,
                        25.0,
                        -175.0,
                        -240.0,
                        171.0,
                        -294.0,
                        19.0,
                        38.0,
                        -351.0,
                        170.0,
                        -10.0,
                        -269.0,
                        18.0,
                        -65.0,
                        -266.0,
                        -31.0,
                        328.0,
                        -361.0,
                        358.0,
                        -256.0,
                        -4.0,
                        -312.0,
                        82.0,
                        -2.0,
                        -75.0,
                        -281.0,
                        -304.0,
                        53.0,
                        -295.0,
                        366.0,
                        322.0,
                        -191.0,
                        26.0,
                        97.0,
                        53.0,
                        75.0,
                        -62.0,
                        -109.0,
                        66.0,
                        177.0,
                        -68.0,
                        175.0,
                        -280.0,
                        70.0,
                        -238.0,
                        109.0,
                        -304.0,
                        326.0,
                        -8.0,
                        -71.0,
                        -236.0,
                        225.0,
                        358.0,
                        20.0,
                        -5.0,
                        -102.0,
                        -134.0,
                        -204.0,
                        -116.0,
                        -353.0,
                        -273.0,
                        106.0,
                        284.0,
                        -137.0,
                        -324.0,
                        301.0,
                        -42.0,
                        -229.0,
                        271.0,
                        -293.0,
                        -343.0,
                        211.0,
                        47.0,
                        -254.0,
                        -154.0,
                        -182.0,
                        264.0,
                        120.0,
                        -11.0,
                        -307.0,
                        99.0,
                        227.0,
                        190.0,
                        -17.0,
                        -77.0,
                        -255.0,
                        -61.0,
                        -249.0,
                        -102.0,
                        70.0,
                        345.0,
                        -187.0,
                        -308.0,
                        194.0,
                        221.0,
                        268.0,
                        -169.0,
                        -190.0,
                        88.0,
                        10.0,
                        262.0,
                        177.0,
                        -314.0,
                        -151.0,
                        -295.0,
                    ],
                    "timezone": "Pacific/Wake",
                    "week_start": shared.WeekStart.TU,
                },
                {
                    "count": 8.0,
                    "end_at": parse_datetime("2026-06-27T23:52:37.638Z"),
                    "excluded_dates": [
                        "2023-06-11T21:57:35.706Z",
                        "2023-06-01T03:52:20.367Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.WEEKLY,
                    "included_dates": [
                        "2024-03-20T23:04:15.262Z",
                        "2023-08-12T04:22:34.452Z",
                        "2024-09-11T06:40:50.544Z",
                    ],
                    "interval": 8.0,
                    "on_days": [
                        shared.PropertyCalendarEventRecurrenceOnDays.SU,
                        shared.PropertyCalendarEventRecurrenceOnDays.MO,
                        shared.PropertyCalendarEventRecurrenceOnDays.TU,
                        shared.PropertyCalendarEventRecurrenceOnDays.FR,
                        shared.PropertyCalendarEventRecurrenceOnDays.MO,
                        shared.PropertyCalendarEventRecurrenceOnDays.TH,
                    ],
                    "on_month_days": [
                        -23.0,
                    ],
                    "on_months": [
                        11.0,
                        8.0,
                        9.0,
                        5.0,
                        -12.0,
                        -7.0,
                        -5.0,
                        10.0,
                        10.0,
                        -9.0,
                        -10.0,
                    ],
                    "on_weeks": [
                        -49.0,
                        46.0,
                        35.0,
                        -26.0,
                        2.0,
                        15.0,
                        15.0,
                        -26.0,
                        24.0,
                        -53.0,
                        36.0,
                        -43.0,
                        51.0,
                        -19.0,
                        -7.0,
                        -12.0,
                        28.0,
                        27.0,
                        35.0,
                        12.0,
                        -28.0,
                        -8.0,
                        -4.0,
                        -45.0,
                    ],
                    "on_year_days": [
                        84.0,
                        -251.0,
                        71.0,
                        181.0,
                        -163.0,
                        158.0,
                        301.0,
                        -299.0,
                        -184.0,
                        -331.0,
                        -152.0,
                        -129.0,
                        -237.0,
                        -303.0,
                        -24.0,
                        126.0,
                        -103.0,
                        146.0,
                        -346.0,
                        86.0,
                        -296.0,
                        -337.0,
                        -185.0,
                        16.0,
                        -270.0,
                        -126.0,
                        -295.0,
                        -231.0,
                        356.0,
                        -293.0,
                        115.0,
                        -265.0,
                        -293.0,
                        -34.0,
                        357.0,
                        313.0,
                        -343.0,
                        180.0,
                        -22.0,
                        -161.0,
                        350.0,
                        177.0,
                        190.0,
                        223.0,
                        -152.0,
                        -360.0,
                        -225.0,
                        -60.0,
                        -35.0,
                        353.0,
                        117.0,
                        -171.0,
                        -315.0,
                        -321.0,
                        -202.0,
                        345.0,
                        -1.0,
                        -148.0,
                        -168.0,
                        181.0,
                        -17.0,
                        282.0,
                        234.0,
                        31.0,
                        47.0,
                        -236.0,
                        366.0,
                        -251.0,
                        -232.0,
                        -308.0,
                        76.0,
                        -199.0,
                        184.0,
                        198.0,
                        225.0,
                        75.0,
                        6.0,
                        227.0,
                        -148.0,
                        259.0,
                        -146.0,
                        49.0,
                        -254.0,
                        341.0,
                        93.0,
                        138.0,
                        -164.0,
                        237.0,
                        4.0,
                        -287.0,
                        161.0,
                    ],
                    "timezone": "Africa/Bissau",
                    "week_start": shared.WeekStart.WE,
                },
            ],
            "registrant_password": "OxwWzr0C",
            "require_address": False,
            "require_job_title": False,
            "start_at": parse_datetime("2025-04-10T17:53:15.664Z"),
            "status": shared.CalendarWebinarStatus.TENTATIVE,
            "subject": "Harum culpa decipio ex cubo ancilla cresco.",
            "timezone": "Europe/Kaliningrad",
            "updated_at": parse_datetime("2026-08-31T16:38:14.993Z"),
            "web_url": "https://classic-recovery.biz",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_webinar is not None

    # Handle response
    print(res.calendar_webinar)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchCalendarWebinarRequest](../../models/operations/patchcalendarwebinarrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchCalendarWebinarResponse](../../models/operations/patchcalendarwebinarresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_calendar_calendar

Remove a calendar

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCalendarCalendar" method="delete" path="/calendar/{connection_id}/calendar/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.calendar.remove_calendar_calendar(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.RemoveCalendarCalendarRequest](../../models/operations/removecalendarcalendarrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.RemoveCalendarCalendarResponse](../../models/operations/removecalendarcalendarresponse.md)**

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

    res = unified_to.calendar.remove_calendar_event(request={
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

## remove_calendar_link

Remove a link

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCalendarLink" method="delete" path="/calendar/{connection_id}/link/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.calendar.remove_calendar_link(request={
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
| `request`                                                                                    | [operations.RemoveCalendarLinkRequest](../../models/operations/removecalendarlinkrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveCalendarLinkResponse](../../models/operations/removecalendarlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_calendar_webinar

Remove a webinar

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCalendarWebinar" method="delete" path="/calendar/{connection_id}/webinar/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.calendar.remove_calendar_webinar(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RemoveCalendarWebinarRequest](../../models/operations/removecalendarwebinarrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveCalendarWebinarResponse](../../models/operations/removecalendarwebinarresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_calendar_calendar

Update a calendar

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCalendarCalendar" method="put" path="/calendar/{connection_id}/calendar/{id}" example="calendar_calendar" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.calendar.update_calendar_calendar(request={
        "calendar_calendar": {
            "created_at": parse_datetime("2020-01-09T23:11:34.147Z"),
            "description": "Socius catena auxilium.",
            "id": "05672e3b-7cd1-4fcd-8c7b-aa835bca3c35",
            "is_primary": False,
            "name": "Acer supra vallum suasoria thesaurus omnis condico cognomen accendo vehemens.",
            "timezone": "America/Dawson_Creek",
            "updated_at": parse_datetime("2023-03-13T19:57:48.820Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_calendar is not None

    # Handle response
    print(res.calendar_calendar)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdateCalendarCalendarRequest](../../models/operations/updatecalendarcalendarrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.UpdateCalendarCalendarResponse](../../models/operations/updatecalendarcalendarresponse.md)**

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

    res = unified_to.calendar.update_calendar_event(request={
        "calendar_event": {
            "attachments": [],
            "conference": [],
            "created_at": "2019-08-04T14:33:51.814Z",
            "end_at": "2020-05-20T22:12:09.976Z",
            "id": "3aefb04c-c6a1-4dec-b773-2993a61a654c",
            "is_all_day": False,
            "is_free": False,
            "is_private": False,
            "location": "621 Boehm Prairie",
            "notes": "Aegre traho.",
            "recurrence": [
                {
                    "count": 8.0,
                    "end_at": parse_datetime("2025-12-27T22:46:26.267Z"),
                    "excluded_dates": [
                        "2025-10-02T13:25:08.926Z",
                        "2023-10-10T14:30:31.199Z",
                        "2024-02-16T17:50:08.868Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.MONTHLY,
                    "included_dates": [
                        "2021-02-17T07:44:37.086Z",
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
                    "end_at": parse_datetime("2025-05-01T17:56:22.256Z"),
                    "excluded_dates": [
                        "2020-04-29T05:20:30.058Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.DAILY,
                    "included_dates": [
                        "2020-09-11T09:30:54.299Z",
                        "2021-11-29T16:02:52.057Z",
                        "2019-12-22T20:30:47.530Z",
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
                    "end_at": parse_datetime("2020-11-05T01:46:57.701Z"),
                    "excluded_dates": [
                        "2023-01-12T19:11:43.424Z",
                        "2021-09-08T02:31:29.899Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.WEEKLY,
                    "included_dates": [
                        "2024-09-01T18:52:48.074Z",
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
            "recurring_event_id": "46684a25-2b83-43e0-bd4a-14a99d099b8e",
            "send_notifications": False,
            "start_at": "2020-05-20T13:04:53.612Z",
            "status": shared.CalendarEventStatus.CONFIRMED,
            "subject": "Sunt spargo tepidus bestia vigor credo coadunatio appello.",
            "timezone": "Asia/Bangkok",
            "updated_at": "2020-06-26T10:24:59.480Z",
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

## update_calendar_link

Update a link

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCalendarLink" method="put" path="/calendar/{connection_id}/link/{id}" example="calendar_link" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.calendar.update_calendar_link(request={
        "calendar_link": {
            "created_at": "2023-03-07T13:34:11.959Z",
            "description": "Vitium clibanus laboriosam uxor denuncio.",
            "duration": 74.0,
            "id": "6158108d-5979-48b8-a43b-e23ca21ffab4",
            "is_active": True,
            "name": "Sopor sopor ancilla animus anser dignissimos vito confero utilis.",
            "price_amount": 44.0,
            "price_currency": "USD",
            "updated_at": "2024-03-07T00:10:45.524Z",
            "url": "https://annual-apricot.info/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_link is not None

    # Handle response
    print(res.calendar_link)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateCalendarLinkRequest](../../models/operations/updatecalendarlinkrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateCalendarLinkResponse](../../models/operations/updatecalendarlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_calendar_webinar

Update a webinar

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCalendarWebinar" method="put" path="/calendar/{connection_id}/webinar/{id}" example="calendar_webinar" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.calendar.update_calendar_webinar(request={
        "calendar_webinar": {
            "conference": [],
            "created_at": parse_datetime("2022-07-06T11:45:14.631Z"),
            "end_at": parse_datetime("2025-10-05T09:39:32.879Z"),
            "has_polls": False,
            "has_recording": False,
            "id": "4a2424d9-2fc7-4247-973a-bf68830ef4bc",
            "is_auto_approve": False,
            "is_enabled": True,
            "is_webcast": False,
            "join_url": "https://robust-bathhouse.biz",
            "notes": "Curriculum ducimus assentator aspernatur ait.",
            "organizer": {
                "email": "Kelton_Dicki@yahoo.com",
                "name": "Walter Greenfelder",
            },
            "recurrence": [
                {
                    "count": 10.0,
                    "end_at": parse_datetime("2023-08-23T12:02:48.896Z"),
                    "excluded_dates": [
                        "2025-01-25T16:04:34.297Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.MONTHLY,
                    "included_dates": [
                        "2024-04-15T12:43:36.288Z",
                    ],
                    "interval": 8.0,
                    "on_days": [
                        shared.PropertyCalendarEventRecurrenceOnDays.SU,
                        shared.PropertyCalendarEventRecurrenceOnDays.FR,
                        shared.PropertyCalendarEventRecurrenceOnDays.SA,
                        shared.PropertyCalendarEventRecurrenceOnDays.WE,
                        shared.PropertyCalendarEventRecurrenceOnDays.MO,
                    ],
                    "on_month_days": [
                        -10.0,
                    ],
                    "on_months": [
                        -9.0,
                    ],
                    "on_weeks": [
                        10.0,
                        30.0,
                        -38.0,
                        30.0,
                        -22.0,
                        37.0,
                        -12.0,
                        27.0,
                        2.0,
                        15.0,
                        26.0,
                        18.0,
                        -43.0,
                        -33.0,
                        -27.0,
                        38.0,
                        28.0,
                        47.0,
                        -8.0,
                        24.0,
                        35.0,
                        -2.0,
                        7.0,
                        49.0,
                        38.0,
                        -41.0,
                        46.0,
                        -11.0,
                        -45.0,
                        0.0,
                        48.0,
                        34.0,
                    ],
                    "on_year_days": [
                        345.0,
                        -207.0,
                        230.0,
                        -10.0,
                        364.0,
                        -256.0,
                        -218.0,
                        -295.0,
                        290.0,
                        -250.0,
                        -315.0,
                        60.0,
                        205.0,
                        -247.0,
                        -318.0,
                        -211.0,
                        -13.0,
                        256.0,
                        -200.0,
                        -313.0,
                        336.0,
                        -332.0,
                        -90.0,
                        287.0,
                        -273.0,
                        156.0,
                        241.0,
                        -138.0,
                        -363.0,
                        -37.0,
                        -171.0,
                        -62.0,
                        -57.0,
                        280.0,
                        -322.0,
                        -79.0,
                        -364.0,
                        -201.0,
                        84.0,
                        341.0,
                        334.0,
                        -75.0,
                        332.0,
                        207.0,
                        337.0,
                        -244.0,
                        131.0,
                        -191.0,
                        164.0,
                        -235.0,
                        285.0,
                        -309.0,
                        -158.0,
                        306.0,
                        180.0,
                        -130.0,
                        -162.0,
                        -155.0,
                        3.0,
                        198.0,
                        26.0,
                        -366.0,
                        -191.0,
                        127.0,
                        -331.0,
                        -11.0,
                        -239.0,
                        -189.0,
                        243.0,
                        118.0,
                        346.0,
                        -174.0,
                        -146.0,
                        -161.0,
                        -330.0,
                        327.0,
                        192.0,
                        310.0,
                        316.0,
                        313.0,
                        -242.0,
                        -51.0,
                        -264.0,
                        -180.0,
                        -88.0,
                        305.0,
                        270.0,
                        358.0,
                        -173.0,
                        -298.0,
                        153.0,
                        -89.0,
                        155.0,
                        -45.0,
                        248.0,
                        -46.0,
                        -146.0,
                        300.0,
                        364.0,
                        -335.0,
                        356.0,
                        -18.0,
                        219.0,
                        324.0,
                        -239.0,
                        -106.0,
                        -298.0,
                        328.0,
                        362.0,
                        344.0,
                        -54.0,
                        133.0,
                        50.0,
                        112.0,
                        -212.0,
                        -179.0,
                        22.0,
                        -201.0,
                        -62.0,
                        -293.0,
                        9.0,
                        30.0,
                        -50.0,
                        126.0,
                        -72.0,
                        264.0,
                        28.0,
                        -1.0,
                        -207.0,
                        160.0,
                        -168.0,
                        3.0,
                        -176.0,
                        -19.0,
                        -157.0,
                        349.0,
                        100.0,
                        -201.0,
                        108.0,
                        -180.0,
                        51.0,
                        -73.0,
                        366.0,
                        74.0,
                        -226.0,
                        238.0,
                        121.0,
                        -193.0,
                        -125.0,
                        -109.0,
                        316.0,
                        -177.0,
                        -307.0,
                        31.0,
                        -76.0,
                        217.0,
                        -310.0,
                        227.0,
                        -360.0,
                        71.0,
                        255.0,
                        -325.0,
                        -214.0,
                        40.0,
                        42.0,
                        17.0,
                        -241.0,
                        -84.0,
                        -188.0,
                        302.0,
                        64.0,
                        94.0,
                        -362.0,
                        23.0,
                        166.0,
                        85.0,
                        71.0,
                        -74.0,
                        -47.0,
                        -119.0,
                        98.0,
                        40.0,
                        158.0,
                        -64.0,
                        175.0,
                        269.0,
                        127.0,
                        -143.0,
                        213.0,
                        -196.0,
                        121.0,
                        81.0,
                        -238.0,
                        288.0,
                        321.0,
                        276.0,
                        133.0,
                        22.0,
                        -213.0,
                        -157.0,
                        -280.0,
                        -35.0,
                        73.0,
                        -194.0,
                        65.0,
                        -180.0,
                        63.0,
                        -242.0,
                        -117.0,
                        148.0,
                        157.0,
                        -320.0,
                        318.0,
                        8.0,
                        210.0,
                        -21.0,
                        81.0,
                        205.0,
                        -258.0,
                        -40.0,
                        -114.0,
                        -253.0,
                        -263.0,
                        65.0,
                        185.0,
                        -24.0,
                        324.0,
                        -172.0,
                        25.0,
                        260.0,
                        211.0,
                        342.0,
                        -31.0,
                        -288.0,
                        -159.0,
                        -4.0,
                        -2.0,
                        -107.0,
                        -316.0,
                        -276.0,
                        331.0,
                        -114.0,
                        -20.0,
                        -320.0,
                        51.0,
                        -176.0,
                        -148.0,
                        -50.0,
                        -201.0,
                        -104.0,
                        153.0,
                        -273.0,
                        -189.0,
                        67.0,
                        209.0,
                        149.0,
                        49.0,
                        -136.0,
                        -125.0,
                        -169.0,
                        -324.0,
                        309.0,
                        -51.0,
                        288.0,
                        253.0,
                        175.0,
                        -146.0,
                        171.0,
                        -140.0,
                        58.0,
                        -212.0,
                        164.0,
                        270.0,
                        102.0,
                        70.0,
                        299.0,
                        89.0,
                        -280.0,
                        252.0,
                        -342.0,
                        240.0,
                        226.0,
                        68.0,
                        -30.0,
                        -232.0,
                        -358.0,
                        -166.0,
                        60.0,
                        140.0,
                        275.0,
                        13.0,
                        250.0,
                        -328.0,
                        -189.0,
                        -22.0,
                        7.0,
                        -235.0,
                        -322.0,
                        178.0,
                        167.0,
                        -104.0,
                        -61.0,
                        282.0,
                        -80.0,
                        -277.0,
                        108.0,
                        271.0,
                        -237.0,
                        297.0,
                        -135.0,
                        -135.0,
                        -323.0,
                        342.0,
                        -267.0,
                        -235.0,
                        173.0,
                        249.0,
                        -288.0,
                        257.0,
                        139.0,
                        -191.0,
                        -217.0,
                        10.0,
                        -117.0,
                        -297.0,
                        -196.0,
                        -206.0,
                        341.0,
                        166.0,
                        181.0,
                        129.0,
                        -207.0,
                        55.0,
                        86.0,
                    ],
                    "timezone": "Asia/Ust-Nera",
                    "week_start": shared.WeekStart.MO,
                },
                {
                    "count": 3.0,
                    "end_at": parse_datetime("2022-09-29T00:22:06.776Z"),
                    "excluded_dates": [
                        "2024-08-17T13:33:09.027Z",
                        "2024-08-02T07:46:20.015Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.DAILY,
                    "included_dates": [
                        "2024-03-13T01:54:56.135Z",
                        "2025-12-19T14:31:01.456Z",
                        "2023-08-06T11:38:09.001Z",
                    ],
                    "interval": 1.0,
                    "on_days": [
                        shared.PropertyCalendarEventRecurrenceOnDays.WE,
                        shared.PropertyCalendarEventRecurrenceOnDays.SU,
                        shared.PropertyCalendarEventRecurrenceOnDays.MO,
                        shared.PropertyCalendarEventRecurrenceOnDays.FR,
                    ],
                    "on_month_days": [
                        -15.0,
                    ],
                    "on_months": [
                        5.0,
                        12.0,
                        3.0,
                        12.0,
                        8.0,
                    ],
                    "on_weeks": [
                        -47.0,
                        44.0,
                    ],
                    "on_year_days": [
                        -117.0,
                        59.0,
                        -6.0,
                        187.0,
                        45.0,
                        70.0,
                        15.0,
                        255.0,
                        44.0,
                        -2.0,
                        25.0,
                        -175.0,
                        -240.0,
                        171.0,
                        -294.0,
                        19.0,
                        38.0,
                        -351.0,
                        170.0,
                        -10.0,
                        -269.0,
                        18.0,
                        -65.0,
                        -266.0,
                        -31.0,
                        328.0,
                        -361.0,
                        358.0,
                        -256.0,
                        -4.0,
                        -312.0,
                        82.0,
                        -2.0,
                        -75.0,
                        -281.0,
                        -304.0,
                        53.0,
                        -295.0,
                        366.0,
                        322.0,
                        -191.0,
                        26.0,
                        97.0,
                        53.0,
                        75.0,
                        -62.0,
                        -109.0,
                        66.0,
                        177.0,
                        -68.0,
                        175.0,
                        -280.0,
                        70.0,
                        -238.0,
                        109.0,
                        -304.0,
                        326.0,
                        -8.0,
                        -71.0,
                        -236.0,
                        225.0,
                        358.0,
                        20.0,
                        -5.0,
                        -102.0,
                        -134.0,
                        -204.0,
                        -116.0,
                        -353.0,
                        -273.0,
                        106.0,
                        284.0,
                        -137.0,
                        -324.0,
                        301.0,
                        -42.0,
                        -229.0,
                        271.0,
                        -293.0,
                        -343.0,
                        211.0,
                        47.0,
                        -254.0,
                        -154.0,
                        -182.0,
                        264.0,
                        120.0,
                        -11.0,
                        -307.0,
                        99.0,
                        227.0,
                        190.0,
                        -17.0,
                        -77.0,
                        -255.0,
                        -61.0,
                        -249.0,
                        -102.0,
                        70.0,
                        345.0,
                        -187.0,
                        -308.0,
                        194.0,
                        221.0,
                        268.0,
                        -169.0,
                        -190.0,
                        88.0,
                        10.0,
                        262.0,
                        177.0,
                        -314.0,
                        -151.0,
                        -295.0,
                    ],
                    "timezone": "Pacific/Wake",
                    "week_start": shared.WeekStart.TU,
                },
                {
                    "count": 8.0,
                    "end_at": parse_datetime("2026-06-27T23:52:37.638Z"),
                    "excluded_dates": [
                        "2023-06-11T21:57:35.706Z",
                        "2023-06-01T03:52:20.367Z",
                    ],
                    "frequency": shared.CalendarEventRecurrenceFrequency.WEEKLY,
                    "included_dates": [
                        "2024-03-20T23:04:15.262Z",
                        "2023-08-12T04:22:34.452Z",
                        "2024-09-11T06:40:50.544Z",
                    ],
                    "interval": 8.0,
                    "on_days": [
                        shared.PropertyCalendarEventRecurrenceOnDays.SU,
                        shared.PropertyCalendarEventRecurrenceOnDays.MO,
                        shared.PropertyCalendarEventRecurrenceOnDays.TU,
                        shared.PropertyCalendarEventRecurrenceOnDays.FR,
                        shared.PropertyCalendarEventRecurrenceOnDays.MO,
                        shared.PropertyCalendarEventRecurrenceOnDays.TH,
                    ],
                    "on_month_days": [
                        -23.0,
                    ],
                    "on_months": [
                        11.0,
                        8.0,
                        9.0,
                        5.0,
                        -12.0,
                        -7.0,
                        -5.0,
                        10.0,
                        10.0,
                        -9.0,
                        -10.0,
                    ],
                    "on_weeks": [
                        -49.0,
                        46.0,
                        35.0,
                        -26.0,
                        2.0,
                        15.0,
                        15.0,
                        -26.0,
                        24.0,
                        -53.0,
                        36.0,
                        -43.0,
                        51.0,
                        -19.0,
                        -7.0,
                        -12.0,
                        28.0,
                        27.0,
                        35.0,
                        12.0,
                        -28.0,
                        -8.0,
                        -4.0,
                        -45.0,
                    ],
                    "on_year_days": [
                        84.0,
                        -251.0,
                        71.0,
                        181.0,
                        -163.0,
                        158.0,
                        301.0,
                        -299.0,
                        -184.0,
                        -331.0,
                        -152.0,
                        -129.0,
                        -237.0,
                        -303.0,
                        -24.0,
                        126.0,
                        -103.0,
                        146.0,
                        -346.0,
                        86.0,
                        -296.0,
                        -337.0,
                        -185.0,
                        16.0,
                        -270.0,
                        -126.0,
                        -295.0,
                        -231.0,
                        356.0,
                        -293.0,
                        115.0,
                        -265.0,
                        -293.0,
                        -34.0,
                        357.0,
                        313.0,
                        -343.0,
                        180.0,
                        -22.0,
                        -161.0,
                        350.0,
                        177.0,
                        190.0,
                        223.0,
                        -152.0,
                        -360.0,
                        -225.0,
                        -60.0,
                        -35.0,
                        353.0,
                        117.0,
                        -171.0,
                        -315.0,
                        -321.0,
                        -202.0,
                        345.0,
                        -1.0,
                        -148.0,
                        -168.0,
                        181.0,
                        -17.0,
                        282.0,
                        234.0,
                        31.0,
                        47.0,
                        -236.0,
                        366.0,
                        -251.0,
                        -232.0,
                        -308.0,
                        76.0,
                        -199.0,
                        184.0,
                        198.0,
                        225.0,
                        75.0,
                        6.0,
                        227.0,
                        -148.0,
                        259.0,
                        -146.0,
                        49.0,
                        -254.0,
                        341.0,
                        93.0,
                        138.0,
                        -164.0,
                        237.0,
                        4.0,
                        -287.0,
                        161.0,
                    ],
                    "timezone": "Africa/Bissau",
                    "week_start": shared.WeekStart.WE,
                },
            ],
            "registrant_password": "OxwWzr0C",
            "require_address": False,
            "require_job_title": False,
            "start_at": parse_datetime("2025-04-10T17:53:15.664Z"),
            "status": shared.CalendarWebinarStatus.TENTATIVE,
            "subject": "Harum culpa decipio ex cubo ancilla cresco.",
            "timezone": "Europe/Kaliningrad",
            "updated_at": parse_datetime("2026-08-31T16:38:14.993Z"),
            "web_url": "https://classic-recovery.biz",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_webinar is not None

    # Handle response
    print(res.calendar_webinar)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateCalendarWebinarRequest](../../models/operations/updatecalendarwebinarrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateCalendarWebinarResponse](../../models/operations/updatecalendarwebinarresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |