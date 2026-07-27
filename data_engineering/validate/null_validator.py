import pandas as pd

from .base_validator import BaseValidator

from .validation_result import (
    ValidationResult,
)


class NullValidator(BaseValidator):

    def __init__(self, columns):

        self.columns = columns

    def validate(
        self,
        dataframe: pd.DataFrame,
    ):

        failed = dataframe[self.columns]\
            .isnull()\
            .any(axis=1)\
            .sum()

        return ValidationResult(

            validation_name="Null Check",

            passed=failed == 0,

            total_rows=len(dataframe),

            failed_rows=int(failed),

            message=f"{failed} null rows",

        )