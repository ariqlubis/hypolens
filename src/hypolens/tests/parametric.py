from typing import List
import pandas as pd
import pingouin as pg
from .base import BaseTest
from ..core.models import TestResult

class TTest(BaseTest):
    """Independent t-test implementation"""
    
    def run_test(self, 
                 data: pd.DataFrame, 
                 group_cols: List[str], 
                 val_col: str
                 ) -> TestResult:
        
        test_results = pg.ttest( 
            data[data[group_cols[0]] == data[group_cols[0]].unique()[0]][val_col],
            data[data[group_cols[0]] == data[group_cols[0]].unique()[1]][val_col],
            paired=self.config.paired
        )
        
        return TestResult(
            test_name="T-test",
            statistic=test_results['T'].iloc[0],
            p_value=test_results['p-val'],
            significant=test_results['p-val'].iloc[0] < self.config.alpha,
            group_sizes=self.get_group_sizes(data, group_cols, val_col),
            effect_size=test_results['cohen-d'].iloc[0],
        )
        
class ANOVA(BaseTest):
    """One-way ANOVA implementation"""
    
    def run_test(self,
                 data: pd.DataFrame,
                 group_cols: List[str],
                 val_col: str
                 ) -> TestResult:
        
        anova_result = pg.anova(
            data=data,
            dv=val_col,
            between=group_cols,
            detailed=True
        ) 
        
        return TestResult(
            test_name="One-way ANOVA",
            statistic=anova_result['F'].iloc[0],
            p_value=anova_result['p-unc'].iloc[0],
            significant=anova_result['p-unc'].iloc[0] < self.config.alpha,
            group_sizes=self.get_group_sizes(data, group_cols, val_col),
            effect_size=anova_result['np2'].iloc[0],
        )