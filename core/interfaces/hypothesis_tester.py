from abc import ABC, abstractmethod
from core.entities.hypothesis import Hypothesis

class HypothesisTester(ABC):
    @abstractmethod
    def test(self, hypothesis: Hypothesis):
        pass