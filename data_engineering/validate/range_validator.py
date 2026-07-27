from .base_validator import BaseValidator

from .validation_result import (
    ValidationResult,
)


class RangeValidator(BaseValidator):

    def __init__(
        self,
        column,
        minimum,
        maximum,
    ):

        self.column = column

        self.minimum = minimum

        self.maximum = maximum

    def validate(
        self,
        dataframe,
    ):

        failed = (
            (
                dataframe[self.column]
                < self.minimum
            )
            |
            (
                dataframe[self.column]
                > self.maximum
            )
        ).sum()

        return ValidationResult(

            validation_name=f"{self.column} Range",

            passed=failed == 0,

            total_rows=len(dataframe),

            failed_rows=int(failed),

            message=f"{failed} invalid values",

        )