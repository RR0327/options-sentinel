def make_decision(bull, bear, risk):
    if bull["decision"] == "BUY" and risk["approved"] is True:
        return {"decision": "TRADE", "strategy": bull["strategy"],
                "reason": "Bull case accepted after risk review"}
    return {"decision": "NO_TRADE", "reason": "Conditions not satisfied"}
