from risk.limits import MAX_RISK_PER_TRADE

def evaluate_trade(trade):
    confidence = trade["confidence"]
    max_loss = trade["max_loss"]
    
    if confidence < 0.6:
        return {"approved": False, "reason": "Low confidence"}
    if max_loss > 500:
        return {"approved": False, "reason": "Risk exceeds limit"}
    return {"approved": True, "reason": "Risk acceptable"}
