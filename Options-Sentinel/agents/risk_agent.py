def analyse_risk(trade):
    risk_score = 0.2
    if trade["confidence"] < 0.6:
        return {"approved": False, "reason": "Confidence too low"}
    return {"approved": True, "risk_score": risk_score, "reason": "Risk acceptable"}
