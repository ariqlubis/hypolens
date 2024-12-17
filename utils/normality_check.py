import scipy.stats as stats
from scipy.stats import kstest, norm, anderson
from statmodels.stats.diagnostic import lilliefors

def check_normality(data):
    stat, p_value_shapiro = stats.shapiro(data)

    if p_value_shapiro > 0.05: # Support H0: Normal Distribution
        return True

    result_ad = anderson(data)
    if result_ad.statistic < result_ad.critical_values[2]:
        return True

    stat_ks, p_value_ks = kstest(data, norm.cdf)
    if p_value_ks > 0.05:
        return True