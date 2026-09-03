from market.data_provider import get_stock_data
from market.indicators import calculate_indicators
from market.regime import detect_regime

def test_regime():
    df = get_stock_data("SPY")
    df = calculate_indicators(df)
    regime = detect_regime(df)
    print(regime)
    assert "regime" in regime
    assert "confidence" in regime
