from typing import Union
import pandas as pd

class Hypothesis:
    """
    
    """
    def __init__(self, data: Union[pd.DataFrame, list], alpha: float = 0.05, columns: list = None, is_categorical: bool = False):
        self.alpha = alpha
        self.is_categorical = is_categorical

        if isinstance(data, pd.DataFrame):
            if not columns:
                raise ValueError("You must specify columns for comparison in a DataFrame.")
            self.data = [data[col].dropna().tolist() for col in columns]
        else:
            self.data = data

