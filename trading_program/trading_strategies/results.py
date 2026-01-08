import pandas as pd
import numpy as np

from run import StrategyControllier

original_data = pd.read_csv('historical_stock_data/Banks/BY_2023-06-01_2025-06-01.csv')
log_data = np.log(original_data['close']).copy()

output = StrategyControllier(log_data,20,5).run()

print(output)