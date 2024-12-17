from core.interfaces.hypothesis_tester import HypothesisTester
from scipy.stats import ttest_ind, mannwhitneyu
from utils.normality_check import check_normality

class HypothesisTesterImplementation(HypothesisTester):
    def test(self, hypothesis):
        if check_normality(hypothesis.data[0]) and check_normality(hypothesis.data[1]):
            return self.parametric_test(hypothesis)
        else:
            return self.non_parametric_test(hypothesis)


    def parametric_test(self, hypothesis):
        stat, p_value = ttest_ind(hypothesis.data[0], hypothesis.data[1])
        return {
            "statistic": stat,
            "p_value": p_value
        }

    def non_parametric_test(self, hypothesis):
        stat, p_value = mannwhitneyu(hypothesis.data[0], hypothesis.data[1])
        return {
            "statistic": stat,
            "p_value": p_value
        }