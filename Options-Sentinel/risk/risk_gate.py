from risk.risk_engine import evaluate_trade

def risk_gate(trade):
    result = evaluate_trade(trade)
    if result["approved"]:
        return {"status": "APPROVED", "message": result["reason"]}
    return {"status": "REJECTED", "message": result["reason"]}
