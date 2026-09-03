from market.data_provider import get_stock_data
from market.indicators import calculate_indicators

def test_indicators():
    df = get_stock_data("SPY")
    df_indicators = calculate_indicators(df)
    print(df_indicators[["close", "sma50", "rsi"]].tail())
    assert "sma50" in df_indicators.columns
    assert "rsi" in df_indicators.columns
