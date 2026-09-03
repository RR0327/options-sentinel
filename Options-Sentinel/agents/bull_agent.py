def analyse_bull_case(market):
    if market["market_condition"] == "BULLISH":
        return {
            "decision": "BUY",
            "strategy": "BULL_CALL_SPREAD",
            "confidence": 0.8,
            "reasons": ["Price above moving average", "Positive market regime"]
        }
    return {"decision": "NO_TRADE", "confidence": 0.3, "reasons": ["Market is not bullish"]}
