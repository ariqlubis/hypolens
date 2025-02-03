from typing import Dict, List
import pandas as pd
import numpy as np
import pingouin as pg
from .base import BaseTest
from ..core.models import TestResult

class MannWhitneyU(BaseTest):
    """Mann-Whitney U test implementation using pingouin"""
    
    def run_test(self, data: pd.DataFrame, group_cols: List[str], val_col: str) -> TestResult:
        test_result = pg.mwu(
            data[data[group_cols[0]] == data[group_cols[0]].unique()[0]][val_col],
            data[data[group_cols[0]] == data[group_cols[0]].unique()[1]][val_col]
        )
        
        return TestResult(
            test_name="Mann-Whitney U",
            statistic=test_result['U-val'].iloc[0],
            p_value=test_result['p-val'].iloc[0],
            significant=test_result['p-val'].iloc[0] < self.config.alpha,
            group_sizes=self.get_group_sizes(data, group_cols, val_col),
            effect_size=pg.compute_effsize(
                data[data[group_cols[0]] == data[group_cols[0]].unique()[0]][val_col],
                data[data[group_cols[0]] == data[group_cols[0]].unique()[1]][val_col],
                eftype='cohen'
            )
        )

class KruskalWallis(BaseTest):
    """Kruskal-Wallis H test implementation using pingouin"""
    
    def run_test(self, data: pd.DataFrame, group_cols: List[str], val_col: str) -> TestResult:
        test_result = pg.kruskal(
            data=data,
            dv=val_col,
            between=group_cols
        )
        
        result = TestResult(
            test_name="Kruskal-Wallis H",
            statistic=test_result['H'].iloc[0],
            p_value=test_result['p-unc'].iloc[0],
            significant=test_result['p-unc'].iloc[0] < self.config.alpha,
            group_sizes=self.get_group_sizes(data, group_cols, val_col),
            effect_size=pg.compute_effsize(
                data=data,
                dv=val_col,
                between=group_cols[0],
                eftype='eta2'
            )
        )
        
        return result