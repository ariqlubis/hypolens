import pandas as pd 
from hypozen.core.interfaces.parametric_converter_interface import ParametricConverterInterface

class ParametricConverter(ParametricConverterInterface):
    def convert(self, data: pd.DataFrame) -> pd.DataFrame:
        from scipy.stats import boxcox
        transformed_data = data.copy
        for col in data.select_dtypes(include=['int', 'float']).columns:
            transformed_data[col], _ = boxcox(data[col] + 1)
            
        return transformed_data