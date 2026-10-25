# HealthcareDocumentType

Unified, normalized kind of clinical document (OTHER when unmappable)

## Example Usage

```python
from unified_python_sdk.models.shared import HealthcareDocumentType

value = HealthcareDocumentType.PROGRESS_NOTE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                   | Value                  |
| ---------------------- | ---------------------- |
| `PROGRESS_NOTE`        | PROGRESS_NOTE          |
| `CONSULTATION_NOTE`    | CONSULTATION_NOTE      |
| `HISTORY_AND_PHYSICAL` | HISTORY_AND_PHYSICAL   |
| `DISCHARGE_SUMMARY`    | DISCHARGE_SUMMARY      |
| `PROCEDURE_NOTE`       | PROCEDURE_NOTE         |
| `REFERRAL_NOTE`        | REFERRAL_NOTE          |
| `SUMMARY`              | SUMMARY                |
| `LABORATORY_REPORT`    | LABORATORY_REPORT      |
| `IMAGING_REPORT`       | IMAGING_REPORT         |
| `CONSENT`              | CONSENT                |
| `OTHER`                | OTHER                  |