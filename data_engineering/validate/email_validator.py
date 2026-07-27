import re

from .base_validator import BaseValidator

from .validation_result import (
    ValidationResult,
)


class EmailValidator(BaseValidator):

    EMAIL_REGEX = (
        r'^[A-Za-z0-9._%+-]+'
        r'@[A-Za-z0-9.-]+'
        r'\.[A-Za-z]{2,}$'
    )

    def validate(
        self,
        dataframe,
    ):

        failed = (
            ~dataframe["email"]
            .astype(str)
            .str.match(
                self.EMAIL_REGEX
            )
        ).sum()

        return ValidationResult(

            validation_name="Email Check",

            passed=failed == 0,

            total_rows=len(dataframe),

            failed_rows=int(failed),

            message=f"{failed} invalid emails",

        )