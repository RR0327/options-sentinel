import json
from datetime import datetime

FILE = "database/trades.json"

def save_trade(trade):
    trade["time"] = str(datetime.now())
    try:
        with open(FILE, "r") as f:
            trades = json.load(f)
    except Exception:
        trades = []
    trades.append(trade)
    with open(FILE, "w") as f:
        json.dump(trades, f, indent=4)
