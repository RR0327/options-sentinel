def analyse_market(market_data):
    regime = market_data["regime"]
    confidence = market_data["confidence"]
    return {
        "market_condition": regime,
        "confidence": confidence,
        "summary": f"Market is {regime} with {confidence*100}% confidence"
    }
