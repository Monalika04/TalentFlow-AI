


from abc import ABC
from abc import abstractmethod

import pandas as pd


class BaseLoader(ABC):

    @abstractmethod
    def load(

        self,

        tables: dict[str, pd.DataFrame],

    ):

        pass