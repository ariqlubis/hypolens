from abc import ABC, abstractmethod
from typing import Dict, List, Optional
import pandas as pd
import numpy as np
import pingouin as pg
from ..core.models import TestResult, AnalysisConfig
from ..core.types import GroupType

class BaseTest(ABC):
    """Base class for statistical tests"""
    
    def __init__(self, config: AnalysisConfig):
        self.config = config
    
    @abstractmethod
    def run_test(self, data: pd.DataFrame, group_cols: List[str], val_col: str) -> TestResult:
        """Run the statistical test"""
        pass
    
    def check_assumptions(self, data: pd.DataFrame, group_cols: List[str], val_col: str) -> Dict[str, bool]:
        """Check test assumptions"""
        # Using pingouin for normality and homogeneity tests
        assumptions = {}
        
        # Test normality for each group
        for name, group in data.groupby(group_cols):
            if isinstance(name, tuple):
                group_name = '_'.join(str(x) for x in name)
            else:
                group_name = str(name)
            normality_test = pg.normality(group[val_col], method='shapiro')
            assumptions[f'normality_{group_name}'] = bool(normality_test)
        
        # Test homogeneity of variances
        if len(set(data[group_cols[0]])) > 1:  # Only if we have multiple groups
            homogeneity = pg.homoscedasticity(
                data=data,
                dv=val_col,
                group=group_cols[0],
                method='levene'
            )
            assumptions['homogeneity'] = bool(homogeneity)
            
        return assumptions
    
    def get_group_sizes(self, data: pd.DataFrame, group_cols: List[str], val_col: str) -> Dict[str, int]:
        """Get size of each group"""
        sizes = {}
        for name, group in data.groupby(group_cols):
            if isinstance(name, tuple):
                name = '_'.join(str(x) for x in name)
            sizes[str(name)] = len(group[val_col].dropna())
        return sizes