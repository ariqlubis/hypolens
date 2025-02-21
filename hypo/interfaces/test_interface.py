from typing import Protocol
import pandas as pd

class StatisticalTest(Protocol):
    def run(self, data: pd.DataFrame, group_col: str, value_col: str):
        ...

class AssumptionChecker(Protocol):
    def check_normality(self, data: pd.DataFrame, col: str) -> bool:
        ...