from scipy.stats import shapiro
import pandas as pd

def check_normality(data: pd.DataFrame):
    results = {}
    for column in data.columns:
        stat, p_value = shapiro(data[column])
        results[column] = {"statistic": stat, "p_value": p_value, "normal": p_value >= 0.05}
    return results
