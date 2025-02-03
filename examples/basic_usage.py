import pandas as pd
import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hypolens.core.models import AnalysisConfig
from hypolens.core.types import TestType
from hypolens.tests.parametric import TTest, ANOVA

def create_sample_data():
    np.random.seed(42)
    control = np.random.normal(100, 15, 30)
    treatment = np.random.normal(110, 15, 30) 
    
    two_group_data = pd.DataFrame({
        'group': ['Control']*30 + ['Treatment']*30,
        'value': np.concatenate([control, treatment])
    })
    group_a = np.random.normal(100, 15, 25)
    group_b = np.random.normal(105, 15, 25)
    group_c = np.random.normal(115, 15, 25)
    
    multi_group_data = pd.DataFrame({
        'group': ['A']*25 + ['B']*25 + ['C']*25,
        'value': np.concatenate([group_a, group_b, group_c])
    })
    
    return two_group_data, multi_group_data

def run_parametric_examples():
    """Demonstrate parametric tests (t-test and ANOVA)"""
    print("\n=== Parametric Tests Examples ===")
    
    two_group_data, multi_group_data = create_sample_data()
    
    config = AnalysisConfig(
        alpha=0.05,
        test_type=TestType.PARAMETRIC,
    )
    
    print("\n1. Independent T-test Example:")
    t_test = TTest(config)
    t_result = t_test.run_test(
        data=two_group_data,
        group_cols=['group'],
        val_col='value'
    )
    
    print(f"Test: {t_result.test_name}")
    print(f"Statistic: {t_result.statistic:.3f}")
    print(f"P-value: {t_result.p_value}")
    print(f"Significant: {t_result.significant}")
    print(f"Effect size (Cohen's d): {t_result.effect_size:.3f}")

    print("\n2. One-way ANOVA Example:")
    anova = ANOVA(config)
    anova_result = anova.run_test(
        data=multi_group_data,
        group_cols=['group'],
        val_col='value'
    )
    
    print(f"Test: {anova_result.test_name}")
    print(f"F-statistic: {anova_result.statistic:.3f}")
    print(f"P-value: {anova_result.p_value:.3f}")
    print(f"Significant: {anova_result.significant}")
    print(f"Effect size (η²): {anova_result.effect_size:.3f}")
    print("Assumptions met:")



def main():
    """Run all examples"""
    print("Hypozen Basic Usage Examples")
    print("=" * 30)
    
    run_parametric_examples()

if __name__ == "__main__":
    main()