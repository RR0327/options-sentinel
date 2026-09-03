import ta

def calculate_indicators(df):
    df["sma50"] = ta.trend.sma_indicator(df["close"], window=50)
    df["rsi"] = ta.momentum.rsi(df["close"], window=14)
    return df
