import scipy.stats as stats
from scipy.stats import kstest, norm, anderson
from statmodels.stats.diagnostic import lilliefors
from typing import List

def check_normality(data: List[float], alpha: float = 0.05) -> bool:
    """
    Checks if data follows a normal distribution using the Shapiro-Wilk test.
    Args:
        data (List[float]): The dataset to check.
        alpha (float): Significance level for the test.
    Returns:
        bool: True if data is normal, False otherwise.
    """
    stat, p_value_shapiro = stats.shapiro(data)
    return p_value_shapiro > alpha