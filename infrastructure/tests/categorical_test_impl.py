from scipy.stats import chi2_contingency, fisher_exact, kruskal
from core.interfaces.hypothesis_test_interface import ITestHypothesis
from core.entities.test_result import TestResult
import numpy as np

class ChiSquareTest(ITestHypothesis):
    def test(self, data: list) -> TestResult:
        contingency_table = np.array(data)
        stat, p_value, _, _ = chi2_contingency(contingency_table)
        return TestResult(stat, p_value)

class FisherExactTest(ITestHypothesis):
    def test(self, data: list) -> TestResult:
        contingency_table = np.array(data)
        if contingency_table.shape != (2, 2):
            raise ValueError("Fisher's Exact Test can only be applied to 2x2 tables.")
        stat, p_value = fisher_exact(contingency_table)
        return TestResult(stat, p_value)

class KruskalWallisTest(ITestHypothesis):
    def test(self, data: list) -> TestResult:
        stat, p_value = kruskal(*data)
        return TestResult(stat, p_value)