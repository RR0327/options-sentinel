from datetime import datetime
from database.database import SessionLocal
from database.models import DecisionModel

def save_decision(decision):
    db = SessionLocal()
    try:
        bull = decision.get("bull", {})
        bear = decision.get("bear", {})
        risk = decision.get("risk", {})

        db_decision = DecisionModel(
            time=datetime.utcnow(),
            bull_signal=bull.get("decision", "UNKNOWN"),
            bull_confidence=bull.get("confidence", 0.0),
            bear_signal=bear.get("decision", "UNKNOWN"),
            bear_confidence=bear.get("confidence", 0.0),
            risk_approved=risk.get("approved", False),
            final_decision=decision.get("decision", "UNKNOWN"),
            strategy=decision.get("strategy", "UNKNOWN")
        )
        db.add(db_decision)
        db.commit()
    except Exception as e:
        print(f"Error saving decision to DB: {e}")
        db.rollback()
    finally:
        db.close()
