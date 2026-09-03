import json

FILE = "database/decisions.json"

def save_decision(decision):
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
    except Exception:
        data = []
    data.append(decision)
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)
