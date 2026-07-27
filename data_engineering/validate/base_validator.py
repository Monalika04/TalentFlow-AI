from abc import ABC
from abc import abstractmethod

import pandas as pd

from .validation_result import (
    ValidationResult,
)


class BaseValidator(ABC):

    @abstractmethod
    def validate(
        self,
        dataframe: pd.DataFrame,
    ) -> ValidationResult:

        pass