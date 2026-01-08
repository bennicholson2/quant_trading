import numpy as np
import pandas as pd

class MAStateMachine:
    def __init__(self,long_window,short_window):
        """
        Takes in log time series data and performs trading strategy
        """
        self.short_window = short_window
        self.long_window = long_window
    
    def generate_signals(self,log_prices):
        """
        long_window: The sliding window for the longer time period
        short_window: The sliding window for the shorter period
        """
        long_ma_ts = log_prices.rolling(window=self.long_window).mean()
        short_ma_ts = log_prices.rolling(window=self.short_window).mean()

        # let the states represent the current direction of momentum
        states = np.sign(long_ma_ts - short_ma_ts).fillna(0)

        return states