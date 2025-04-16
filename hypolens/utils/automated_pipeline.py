import pandas as pd
from hypolens.core.use_cases.hypothesis_testing import HypothesisTesting
from hypolens.infrastructure.tests.scipy_parametric_tester import ScipyParametricTester
from hypolens.infrastructure.tests.non_parametric_tester import NonParametricTester
from hypolens.infrastructure.converters.parametric_converter import ParametricConverter
from hypolens.utils.normality_check import check_normality


def run_automated_testing(data1: pd.DataFrame, data2: pd.DataFrame, alpha: float = 0.05) -> pd.DataFrame:
    parametric_tester = ScipyParametricTester()
    non_parametric_tester = NonParametricTester()
    converter = ParametricConverter()

    normality1 = check_normality(data1)
    normality2 = check_normality(data2)

    results = []

    for feature in data1.columns:
        if feature not in data2.columns:
            continue

        d1 = pd.DataFrame({feature: data1[feature]})
        d2 = pd.DataFrame({feature: data2[feature]})

        is_normal = normality1[feature]["normal"] and normality2[feature]["normal"]

        if is_normal:
            tester = HypothesisTesting(tester=parametric_tester)
            result = tester.test(d1, d2, alpha=alpha, is_parametric=True)
        else:
            tester = HypothesisTesting(tester=non_parametric_tester, converter=converter)
            result = tester.test(d1, d2, alpha=alpha, is_parametric=False)

        results.append({
            "feature": feature,
            "method": result.method,
            "statistic": result.statistic,
            "p_value": result.p_value,
            "alpha": result.alpha,
            "significant": result.significant,
            "normal": is_normal
        })

    return pd.DataFrame(results)
