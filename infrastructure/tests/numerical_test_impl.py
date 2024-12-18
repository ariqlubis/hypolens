from scipy.stats import ttest_ind, mannwhitneyu
from core.interfaces.hypothesis_tester import ITestHypothesis
from core.entities.test_result import TestResult

class TTestHypothesis(ITestHypothesis):
    def test(self, data: list) -> TestResult:
        stat, p_value = ttest_ind(data[0], data[1])
        return TestResult(stat, p_value)


class MWUHypothesis(ITestHypothesis):
    def test(self, data: list) -> TestResult:
        stat, p_value = mannwhitneyu(data[0], data[1])
        return TestResult(stat, p_value)