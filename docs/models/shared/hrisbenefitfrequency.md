# HrisBenefitFrequency

Frequency that costs accrue for this benefit. For insurance/benefits, usually "MONTHLY". For compensation, matches pay cycle (WEEKLY, BIWEEKLY, etc).

## Example Usage

```python
from unified_python_sdk.models.shared import HrisBenefitFrequency

value = HrisBenefitFrequency.ONE_TIME

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `ONE_TIME`    | ONE_TIME      |
| `DAY`         | DAY           |
| `QUARTER`     | QUARTER       |
| `YEAR`        | YEAR          |
| `HOUR`        | HOUR          |
| `MONTH`       | MONTH         |
| `WEEK`        | WEEK          |
| `BIWEEKLY`    | BIWEEKLY      |
| `SEMIMONTHLY` | SEMIMONTHLY   |