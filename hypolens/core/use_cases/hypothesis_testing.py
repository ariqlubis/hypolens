from hypozen.core.entities.test_result import Result
from hypozen.core.interfaces.tester_interface import TesterInterface
from hypozen.core.interfaces.parametric_converter_interface import ParametricConverterInterface
import pandas as pd

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