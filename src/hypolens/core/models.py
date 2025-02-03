from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from datetime import datetime
import pandas as pd
from .types import TestType

@dataclass
class TestResult:
    """Result of a statistical test"""
    test_name: str
    statistic: float
    p_value: float
    group_sizes: Dict[str, int]
    significant: bool = False
    effect_size: Optional[float] = None
    confidence_interval: Optional[tuple] = None
    assumptions_met: Optional[Dict[str, bool]] = None
    post_hoc_results: Optional[pd.DataFrame] = None
    descriptive_stats: Optional[pd.DataFrame] = None
    timestamp: datetime = datetime.now()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert result to dictionary format"""
        return {
            'test_name': self.test_name,
            'statistic': self.statistic,
            'p_value': self.p_value,
            'significant': self.significant,
            'group_sizes': self.group_sizes,
            'effect_size': self.effect_size,
            'confidence_interval': self.confidence_interval,
            'assumptions_met': self.assumptions_met,
            'timestamp': self.timestamp.isoformat()
        }
        
@dataclass
class AnalysisConfig:
    """Configuration for analysis"""
    alpha: float = 0.05
    test_type: TestType = TestType.AUTO
    check_assumptions: bool = True
    calculate_effect_size: bool = True
    run_post_hoc: bool = False
    paired: bool = False