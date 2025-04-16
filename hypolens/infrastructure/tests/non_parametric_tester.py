from scipy.stats import mannwhitneyu
from hypolens.core.interfaces.tester_interface import TesterInterface
from hypolens.core.entities.result import Result

class NonParametricTester(TesterInterface):
    def test(self, data1, data2, alpha=0.05) -> Result:
        statistic, p_value = mannwhitneyu(data1, data2, alternative='two-sided')
        significant = p_value < alpha
        return Result("mannwhitneyu", statistic, p_value, alpha, significant)