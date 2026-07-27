from .duplicate_validator import (
    DuplicateValidator,
)

from .null_validator import (
    NullValidator,
)

from .email_validator import (
    EmailValidator,
)

from .range_validator import (
    RangeValidator,
)


class PipelineValidator:

    def validate_candidates(
        self,
        dataframe,
    ):

        validators = [

            DuplicateValidator(
                ["email"]
            ),

            NullValidator(
                [
                    "first_name",
                    "email",
                ]
            ),

            EmailValidator(),

            RangeValidator(
                "total_experience",
                0,
                50,
            ),

        ]

        results = []

        for validator in validators:

            results.append(
                validator.validate(
                    dataframe
                )
            )

        return results