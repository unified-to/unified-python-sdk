# Report

## Overview

### Available Operations

* [get_accounting_report2](#get_accounting_report2) - Retrieve a report
* [list_accounting_reports2](#list_accounting_reports2) - List all reports
* [list_ads_reports2](#list_ads_reports2) - List all reports
* [list_analytics_reports2](#list_analytics_reports2) - List all reports
* [list_martech_reports2](#list_martech_reports2) - List all reports

## get_accounting_report2

Retrieve a report

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingReport2" method="get" path="/accounting/{connection_id}/report/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.report.get_accounting_report2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_report is not None

    # Handle response
    print(res.accounting_report)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingReport2Request](../../models/operations/getaccountingreport2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetAccountingReport2Response](../../models/operations/getaccountingreport2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_reports2

List all reports

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingReports2" method="get" path="/accounting/{connection_id}/report" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.report.list_accounting_reports2(request={
        "connection_id": "<id>",
    })

    assert res.accounting_reports is not None

    # Handle response
    print(res.accounting_reports)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountingReports2Request](../../models/operations/listaccountingreports2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListAccountingReports2Response](../../models/operations/listaccountingreports2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ads_reports2

List all reports

### Example Usage

<!-- UsageSnippet language="python" operationID="listAdsReports2" method="get" path="/ads/{connection_id}/report" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.report.list_ads_reports2(request={
        "connection_id": "<id>",
    })

    assert res.ads_reports is not None

    # Handle response
    print(res.ads_reports)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListAdsReports2Request](../../models/operations/listadsreports2request.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListAdsReports2Response](../../models/operations/listadsreports2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_analytics_reports2

List all reports

### Example Usage

<!-- UsageSnippet language="python" operationID="listAnalyticsReports2" method="get" path="/analytics/{connection_id}/report" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.report.list_analytics_reports2(request={
        "connection_id": "<id>",
    })

    assert res.analytics_reports is not None

    # Handle response
    print(res.analytics_reports)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListAnalyticsReports2Request](../../models/operations/listanalyticsreports2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListAnalyticsReports2Response](../../models/operations/listanalyticsreports2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_martech_reports2

List all reports

### Example Usage

<!-- UsageSnippet language="python" operationID="listMartechReports2" method="get" path="/martech/{connection_id}/report" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.report.list_martech_reports2(request={
        "connection_id": "<id>",
    })

    assert res.marketing_reports is not None

    # Handle response
    print(res.marketing_reports)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListMartechReports2Request](../../models/operations/listmartechreports2request.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListMartechReports2Response](../../models/operations/listmartechreports2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |