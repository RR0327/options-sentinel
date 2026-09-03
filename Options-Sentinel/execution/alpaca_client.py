from alpaca.trading.client import TradingClient
from config.settings import ALPACA_API_KEY, ALPACA_SECRET_KEY

trading_client = TradingClient(ALPACA_API_KEY, ALPACA_SECRET_KEY, paper=True)

def get_account():
    return trading_client.get_account()

def get_positions():
    return trading_client.get_all_positions()
