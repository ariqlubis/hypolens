class TestResult:
    def __init__(self, statistic: float, p_value: float, is_significant: bool):
        """
        Represents the result of a hypothesis test.
        Args:
            stat (float): Test statistic value.
            p_value (float): P-value of the test.
        """ 
        self.statistic = statistic
        self.p_value = p_value
        self.is_significant = is_significant
        
    def __repr__(self):
        result = "Significant" if self.is_significant else "Not Significant"
        return f"TestResult(hypothesis={self.hypothesis_name}, p_value={self.p_value:.4f}, result={result})"
    