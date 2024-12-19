import pandas as pd
from abc import ABC, abstractmethod

class ParametricConverterInterface(ABC):
    @abstractmethod
    def convert(self, data: pd.DataFrame) -> pd.DataFrame:
        pass