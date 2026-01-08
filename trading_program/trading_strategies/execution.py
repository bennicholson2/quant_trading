import pandas as pd

class ExecutionMachine:
    def __init__(self): 
        """
        Signals: a series of signals (states)
        """
        # update the last state 
        self.last_state = 0 

    def get_execution_signals(self,state_series):
        """
        Given the states what is the execution algorithm
        """
        delta = state_series.diff().fillna(0)

        signals = pd.Series(0,index=state_series.index)
        signals[delta==2] = 1
        signals[delta==-2] = -1

        return signals