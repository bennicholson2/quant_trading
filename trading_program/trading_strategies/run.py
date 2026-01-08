import pandas as pd
import numpy as np

from execution import ExecutionMachine
from algorithm import MAStateMachine

class StrategyControllier:
    def __init__(self,log_prices,short_window,long_window):
        self.log_prices = log_prices
        self.signaller = MAStateMachine(long_window,short_window)
        self.executor = ExecutionMachine()

    def run(self):
        self.states = self.signaller.generate_signals(self.log_prices)
        self.signals = self.executor.get_execution_signals(self.states)

        return self.combine_results()
    
    def combine_results(self):
        return pd.DataFrame({
            'Price':self.log_prices,
            'State':self.states,
            'Signal': self.signals
        })