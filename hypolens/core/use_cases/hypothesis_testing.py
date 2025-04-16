import pandas as pd
from hypolens.core.entities.result import Result
from hypolens.core.interfaces.tester_interface import TesterInterface
from hypolens.core.interfaces.parametric_converter_interface import ParametricConverterInterface

class HypothesisTesting:
    def __init__(self, tester: TesterInterface, converter: ParametricConverterInterface = None):
        self.converter = converter
        self.tester = tester

    def test(self, data1: pd.DataFrame, data2: pd.DataFrame, alpha: float = 0.05, is_parametric: bool = True):
        if is_parametric:
            return self.tester.test(data1, data2, alpha)
        else:
            if self.converter:
                transformed_data1 = self.converter.convert(data1)
                transformed_data2 = self.converter.convert(data2)
                return self.tester.test(transformed_data1, transformed_data2, alpha)
            else:
                raise ValueError("Converter is required for non-parametric to parametric")