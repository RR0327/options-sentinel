def analyse_bear_case(market):
    if market["market_condition"] == "BULLISH":
        return {"decision": "CAUTION", "confidence": 0.4,
                "warnings": ["Trend can reverse", "Market uncertainty exists"]}
    return {"decision": "SELL", "confidence": 0.7, "warnings": ["Bearish market detected"]}
