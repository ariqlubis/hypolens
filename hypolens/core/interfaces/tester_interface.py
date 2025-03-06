from abc import ABC, abstractmethod
from hypozen.core.entities.test_result import Result

class TesterInterface(ABC):
    @abstractmethod
    def test(self, data1, data2, alpha=0.5) -> Result:
        pass