from typing import List
import pandas as pd

class Hypothesis:
    def __init__(self, 
                 data: pd.DataFrame, 
                 columns: List[str],
                 alpha: float = 0.05,
                 is_categorical: bool = False):
        
        self.alpha = alpha
        self.is_categorical = is_categorical
        self.data = data
        self.columns = columns
        
    def __repr__(self):
        return f"Hypothesis(name={self.name}, alpha={self.alpha})"

