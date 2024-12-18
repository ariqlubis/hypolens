from utils.normality_check import check_normality
from core.entities.test_result import TestResult
from core.interfaces.hypothesis_tester import HypothesisTester

class HypothesisTesting:
    def __init__(self, tester: HyphotesisTester):
        self.tester = tester

    def run_test(self, hypothesis):
        if check_normality(hypothesis.data[0]):
            pass