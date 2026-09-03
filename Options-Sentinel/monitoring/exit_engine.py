def check_exit(position):
    pnl = float(position["unrealized_pl"])
    if pnl >= 200:
        return {"action": "EXIT", "reason": "Take profit reached"}
    if pnl <= -100:
        return {"action": "EXIT", "reason": "Stop loss reached"}
    return {"action": "HOLD", "reason": "Position healthy"}
