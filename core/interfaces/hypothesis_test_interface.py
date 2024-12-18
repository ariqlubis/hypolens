from abc import ABC, abstractmethod
from core.entities.hypothesis import Hypothesis

class ITestHypothesis(ABC):
    @abstractmethod
    def test(self, data: list) -> TestResult:
        pass