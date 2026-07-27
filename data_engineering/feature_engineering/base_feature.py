from abc import ABC
from abc import abstractmethod

import pandas as pd


class BaseFeature(ABC):

    @abstractmethod
    def engineer(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        pass