import pandas as pd
import pandas_ta as ta

class RSICalculator:
    def __init__(self, length: int = 14):
        self.length = length

    def calculate(self, data):
        df = pd.DataFrame(data)
        df['close'] = df['close'].astype(float)
        rsi = ta.rsi(df['close'], length=self.length)
        return rsi.iloc[-1]
