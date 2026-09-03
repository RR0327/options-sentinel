def create_bull_call_spread(symbol, buy_strike, sell_strike, expiration):
    return {
        "symbol": symbol,
        "strategy": "BULL_CALL_SPREAD",
        "buy_leg": {"type": "CALL", "strike": buy_strike, "side": "BUY"},
        "sell_leg": {"type": "CALL", "strike": sell_strike, "side": "SELL"},
        "expiration": expiration
    }
