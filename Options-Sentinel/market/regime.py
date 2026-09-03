def detect_regime(df):
    latest = df.iloc[-1]
    price, sma, rsi = latest["close"], latest["sma50"], latest["rsi"]

    if price > sma and rsi > 55:
        return {"regime": "BULLISH", "confidence": 0.8}
    elif price < sma and rsi < 45:
        return {"regime": "BEARISH", "confidence": 0.8}
    else:
        return {"regime": "NEUTRAL", "confidence": 0.5}
