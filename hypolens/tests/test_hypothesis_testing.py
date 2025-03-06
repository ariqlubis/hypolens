import unittest
from hypozen.core.use_cases.hypothesis_testing import HypothesisTesting
from hypozen.core.entities.test_result import Result
from hypozen.infrastructure.tests.scipy_parametric_tester import ScipyParametricTester

class TestHypothesisTesting(unittest.TestCase):

    def test_hypothesis_testing(self):
        tester = ScipyParametricTester()
        hypothesis_testing = HypothesisTesting(tester)
        
        result = hypothesis_testing.test([1, 2, 3], [4, 5, 6])
        
        self.assertIsInstance(result, Result)

if __name__ == '__main__':
    unittest.main()
