# Hris
(*hris*)

## Overview

### Available Operations

* [create_hris_company](#create_hris_company) - Create a company
* [create_hris_employee](#create_hris_employee) - Create an employee
* [create_hris_group](#create_hris_group) - Create a group
* [create_hris_location](#create_hris_location) - Create a location
* [get_hris_company](#get_hris_company) - Retrieve a company
* [get_hris_employee](#get_hris_employee) - Retrieve an employee
* [get_hris_group](#get_hris_group) - Retrieve a group
* [get_hris_location](#get_hris_location) - Retrieve a location
* [get_hris_payslip](#get_hris_payslip) - Retrieve a payslip
* [get_hris_timeoff](#get_hris_timeoff) - Retrieve a timeoff
* [list_hris_companies](#list_hris_companies) - List all companies
* [list_hris_employees](#list_hris_employees) - List all employees
* [list_hris_groups](#list_hris_groups) - List all groups
* [list_hris_locations](#list_hris_locations) - List all locations
* [list_hris_payslips](#list_hris_payslips) - List all payslips
* [list_hris_timeoffs](#list_hris_timeoffs) - List all timeoffs
* [patch_hris_company](#patch_hris_company) - Update a company
* [patch_hris_employee](#patch_hris_employee) - Update an employee
* [patch_hris_group](#patch_hris_group) - Update a group
* [patch_hris_location](#patch_hris_location) - Update a location
* [remove_hris_company](#remove_hris_company) - Remove a company
* [remove_hris_employee](#remove_hris_employee) - Remove an employee
* [remove_hris_group](#remove_hris_group) - Remove a group
* [remove_hris_location](#remove_hris_location) - Remove a location
* [update_hris_company](#update_hris_company) - Update a company
* [update_hris_employee](#update_hris_employee) - Update an employee
* [update_hris_group](#update_hris_group) - Update a group
* [update_hris_location](#update_hris_location) - Update a location

## create_hris_company

Create a company

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.create_hris_company(request={
    "connection_id": "<value>",
})

if res.hris_company is not None:
    # handle response
    pass

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

## create_hris_employee

Create an employee

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.create_hris_employee(request={
    "connection_id": "<value>",
})

if res.hris_employee is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateHrisEmployeeRequest](../../models/operations/createhrisemployeerequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateHrisEmployeeResponse](../../models/operations/createhrisemployeeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_hris_group

Create a group

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.create_hris_group(request={
    "connection_id": "<value>",
})

if res.hris_group is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateHrisGroupRequest](../../models/operations/createhrisgrouprequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.CreateHrisGroupResponse](../../models/operations/createhrisgroupresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_hris_location

Create a location

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.create_hris_location(request={
    "connection_id": "<value>",
})

if res.hris_location is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateHrisLocationRequest](../../models/operations/createhrislocationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateHrisLocationResponse](../../models/operations/createhrislocationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_company

Retrieve a company

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.get_hris_company(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res.hris_company is not None:
    # handle response
    pass

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

## get_hris_employee

Retrieve an employee

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.get_hris_employee(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res.hris_employee is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetHrisEmployeeRequest](../../models/operations/gethrisemployeerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetHrisEmployeeResponse](../../models/operations/gethrisemployeeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_group

Retrieve a group

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.get_hris_group(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res.hris_group is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetHrisGroupRequest](../../models/operations/gethrisgrouprequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GetHrisGroupResponse](../../models/operations/gethrisgroupresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_location

Retrieve a location

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.get_hris_location(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res.hris_location is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetHrisLocationRequest](../../models/operations/gethrislocationrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetHrisLocationResponse](../../models/operations/gethrislocationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_payslip

Retrieve a payslip

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.get_hris_payslip(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res.hris_payslip is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetHrisPayslipRequest](../../models/operations/gethrispaysliprequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetHrisPayslipResponse](../../models/operations/gethrispayslipresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_timeoff

Retrieve a timeoff

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.get_hris_timeoff(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res.hris_timeoff is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetHrisTimeoffRequest](../../models/operations/gethristimeoffrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetHrisTimeoffResponse](../../models/operations/gethristimeoffresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_companies

List all companies

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.list_hris_companies(request={
    "connection_id": "<value>",
})

if res.hris_companies is not None:
    # handle response
    pass

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

## list_hris_employees

List all employees

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.list_hris_employees(request={
    "connection_id": "<value>",
})

if res.hris_employees is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListHrisEmployeesRequest](../../models/operations/listhrisemployeesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListHrisEmployeesResponse](../../models/operations/listhrisemployeesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_groups

List all groups

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.list_hris_groups(request={
    "connection_id": "<value>",
})

if res.hris_groups is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListHrisGroupsRequest](../../models/operations/listhrisgroupsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListHrisGroupsResponse](../../models/operations/listhrisgroupsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_locations

List all locations

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.list_hris_locations(request={
    "connection_id": "<value>",
})

if res.hris_locations is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListHrisLocationsRequest](../../models/operations/listhrislocationsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListHrisLocationsResponse](../../models/operations/listhrislocationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_payslips

List all payslips

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.list_hris_payslips(request={
    "connection_id": "<value>",
})

if res.hris_payslips is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListHrisPayslipsRequest](../../models/operations/listhrispayslipsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListHrisPayslipsResponse](../../models/operations/listhrispayslipsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_timeoffs

List all timeoffs

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.list_hris_timeoffs(request={
    "connection_id": "<value>",
})

if res.hris_timeoffs is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListHrisTimeoffsRequest](../../models/operations/listhristimeoffsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListHrisTimeoffsResponse](../../models/operations/listhristimeoffsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_company

Update a company

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.patch_hris_company(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res.hris_company is not None:
    # handle response
    pass

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

## patch_hris_employee

Update an employee

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.patch_hris_employee(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res.hris_employee is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchHrisEmployeeRequest](../../models/operations/patchhrisemployeerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchHrisEmployeeResponse](../../models/operations/patchhrisemployeeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_group

Update a group

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.patch_hris_group(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res.hris_group is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchHrisGroupRequest](../../models/operations/patchhrisgrouprequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.PatchHrisGroupResponse](../../models/operations/patchhrisgroupresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_location

Update a location

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.patch_hris_location(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res.hris_location is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchHrisLocationRequest](../../models/operations/patchhrislocationrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchHrisLocationResponse](../../models/operations/patchhrislocationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_company

Remove a company

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.remove_hris_company(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res is not None:
    # handle response
    pass

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

## remove_hris_employee

Remove an employee

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.remove_hris_employee(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveHrisEmployeeRequest](../../models/operations/removehrisemployeerequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveHrisEmployeeResponse](../../models/operations/removehrisemployeeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_group

Remove a group

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.remove_hris_group(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.RemoveHrisGroupRequest](../../models/operations/removehrisgrouprequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.RemoveHrisGroupResponse](../../models/operations/removehrisgroupresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_location

Remove a location

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.remove_hris_location(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveHrisLocationRequest](../../models/operations/removehrislocationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveHrisLocationResponse](../../models/operations/removehrislocationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_company

Update a company

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.update_hris_company(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res.hris_company is not None:
    # handle response
    pass

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

## update_hris_employee

Update an employee

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.update_hris_employee(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res.hris_employee is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateHrisEmployeeRequest](../../models/operations/updatehrisemployeerequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateHrisEmployeeResponse](../../models/operations/updatehrisemployeeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_group

Update a group

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.update_hris_group(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res.hris_group is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateHrisGroupRequest](../../models/operations/updatehrisgrouprequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.UpdateHrisGroupResponse](../../models/operations/updatehrisgroupresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_location

Update a location

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.hris.update_hris_location(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res.hris_location is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateHrisLocationRequest](../../models/operations/updatehrislocationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateHrisLocationResponse](../../models/operations/updatehrislocationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |