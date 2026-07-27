from abc import ABC
from abc import abstractmethod


class BaseStage(ABC):

    @abstractmethod
    def execute(
        self,
        context: dict,
    ):
        pass