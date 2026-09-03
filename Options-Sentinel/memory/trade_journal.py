from datetime import datetime
from database.database import SessionLocal
from database.models import TradeModel

def save_trade(trade):
    db = SessionLocal()
    try:
        db_trade = TradeModel(
            time=datetime.utcnow(),
            symbol=trade.get("symbol", "SPY"),
            strategy=trade.get("strategy", "UNKNOWN"),
            status=trade.get("status", "UNKNOWN")
        )
        db.add(db_trade)
        db.commit()
    except Exception as e:
        print(f"Error saving trade to DB: {e}")
        db.rollback()
    finally:
        db.close()
