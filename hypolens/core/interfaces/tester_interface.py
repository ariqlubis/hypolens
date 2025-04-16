from abc import ABC, abstractmethod
from hypolens.core.entities.result import Result

class TesterInterface(ABC):
    @abstractmethod
    def test(self, data1, data2, alpha=0.05) -> Result:
        pass