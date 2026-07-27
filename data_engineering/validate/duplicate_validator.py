import pandas as pd

from .base_validator import BaseValidator

from .validation_result import (
    ValidationResult,
)


class DuplicateValidator(BaseValidator):

    def __init__(self, columns):

        self.columns = columns

    def validate(
        self,
        dataframe: pd.DataFrame,
    ):

        duplicates = dataframe.duplicated(
            subset=self.columns
        )

        failed = duplicates.sum()

        return ValidationResult(

            validation_name="Duplicate Check",

            passed=failed == 0,

            total_rows=len(dataframe),

            failed_rows=int(failed),

            message=f"{failed} duplicate rows",

        )