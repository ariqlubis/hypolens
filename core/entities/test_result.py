class TestResult:
    def __init__(self, statistic: float, p_value: float):
        """
        Represents the result of a hypothesis test.
        Args:
            stat (float): Test statistic value.
            p_value (float): P-value of the test.
        """ 
        self.statistic = statistic
        self.p_value = p_value
        
    def is_significant(self, alpha: float) -> bool:
        """
        Determines if the test result is statistically significant.
        Args:
            alpha (float): Significance level.
        Returns:
            bool: True if significant, False otherwise.
        """
        return self.p_value < alpha