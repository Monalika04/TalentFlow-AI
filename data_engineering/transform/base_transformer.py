from abc import ABC
from abc import abstractmethod

import pandas as pd


class BaseTransformer(ABC):

    @abstractmethod
    def transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        pass