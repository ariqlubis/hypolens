from core.utils.normality_check import check_normality
from infrastructure.tests.numerical_test_impl import TTestHypothesis, MannWhitneyUHypothesis
from infrastructure.tests.categorical_test_impl import ChiSquareTest, FisherExactTest, KruskalWallisTest
from core.entities.hypothesis import Hypothesis
from core.entities.test_result import TestResult

class HypothesisTesting:
    def __init__(self):
        self.parametric_test  = TTestHypothesis()
        self.non_parametric_test = MannWhitneyUHypothesis()
        self.chi_square_test = ChiSquareTest()
        self.kruskal_test = KruskalWallisTest()
        self.fisher_test = FisherExactTest()
        
        
    def run_test(self, hypothesis: Hypothesis) -> TestResult:
        """
        Runs the appropriate hypothesis test based on the data type and characteristics.
        """
        data = hypothesis.data
        
        if not data or len(data) < 2:
            raise ValueError("Hypothesis testing requires at least two groups / datasets")
        
        if hypothesis.is_categorical:
            if len(data) == 2 and all(len(d) == 2 for d in data):
                return self.fisher_test.test(data)
            
            elif len(data) > 2:
                return self.kruskal_test.test(data)
            
            else:
                return self.chi_square_test.test(data)
            
        else:
            if all(check_normality(d) for d in data):
                return self.parametric_test.test(data)
            
            else:
                return self.non_parametric_test.test(data)
        
        