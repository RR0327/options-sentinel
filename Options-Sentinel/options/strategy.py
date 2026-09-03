def select_strategy(market_regime):
    if market_regime == "BULLISH":
        return {"strategy": "BULL_CALL_SPREAD", "direction": "LONG"}
    elif market_regime == "BEARISH":
        return {"strategy": "BEAR_PUT_SPREAD", "direction": "SHORT"}
    else:
        return {"strategy": "NO_TRADE", "direction": "NONE"}
