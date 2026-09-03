from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from config.settings import ALPACA_API_KEY, ALPACA_SECRET_KEY

client = StockHistoricalDataClient(ALPACA_API_KEY, ALPACA_SECRET_KEY)

def get_stock_data(symbol="SPY"):
    request = StockBarsRequest(
        symbol_or_symbols=symbol,
        timeframe=TimeFrame.Day,
        limit=100
    )
    bars = client.get_stock_bars(request)
    return bars.df
