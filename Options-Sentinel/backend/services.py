from market.data_provider import get_stock_data
from market.indicators import calculate_indicators
from market.regime import detect_regime

def get_market_status(symbol="SPY"):
    df = get_stock_data(symbol)
    df = calculate_indicators(df)
    return detect_regime(df)
