from scipy.stats import ttest_ind
from hypozen.core.interfaces.tester_interface import TesterInterface
from hypozen.core.entities.test_result import Result

class ScipyParametricTester(TesterInterface):
    def test(self, data1, data2, alpha=0.05) -> Result:
        statistic, p_value = ttest_ind(data1, data2)
        significant = p_value < alpha
        
        return Result('ttest', statistic, p_value, alpha, significant)