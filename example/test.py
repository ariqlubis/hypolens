import pandas as pd
import numpy as np
from hypolens.utils.automated_pipeline import run_automated_testing

# Simulasi data
np.random.seed(42)
df1 = pd.DataFrame(np.random.normal(5, 2, (100, 10)), columns=[f'feature_{i+1}' for i in range(10)])
df2 = pd.DataFrame(np.random.normal(5.5, 2, (100, 10)), columns=[f'feature_{i+1}' for i in range(10)])


result = run_automated_testing(df1, df2)
print(result)
