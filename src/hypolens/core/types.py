from enum import Enum
from typing import TypeVar, Dict, List, Union, Optional

NumericData = Union[List[float], List[int]]
GroupData = Dict[str, NumericData]

class TestType(Enum):
    """Types of statistical tests"""
    PARAMETRIC = 'parametric'
    NON_PARAMETRIC = 'non_parametric'
    AUTO = 'auto'
    
class GroupType(Enum):
    """Types of group comparisons"""
    TWO_GROUP = 'two_group'
    MULTI_GROUP = 'mutli_group'