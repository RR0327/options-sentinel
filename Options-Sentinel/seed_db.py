import os
import sys
from datetime import datetime, timedelta

# Add the project root to sys.path so we can import from backend and database
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.database import SessionLocal, engine
from database.models import Base, TradeModel, DecisionModel

def seed_database():
    print("Checking if database needs seeding...")
    db = SessionLocal()
    
    # Check if data already exists to avoid duplicates on every restart
    if db.query(TradeModel).first():
        print("Database already contains data. Skipping seeding.")
        db.close()
        return
        
    print("Database is empty. Seeding with dummy data...")
    
    # 1. Seed Decisions (AI Agents)
    decisions = []
    base_time = datetime.now() - timedelta(hours=24)
    for i in range(15):
        d_time = base_time + timedelta(minutes=i * 90)
        dec = DecisionModel(
            time=d_time,
            bull_signal="BUY CALL",
            bull_confidence=0.75 + (i * 0.01),
            bear_signal="WAIT",
            bear_confidence=0.4,
            risk_approved=True if i % 3 != 0 else False,
            final_decision="BUY CALL" if i % 3 != 0 else "WAIT",
            strategy="Bull Call Spread"
        )
        decisions.append(dec)
        
    db.add_all(decisions)
    
    # 2. Seed Trades (Trade Journal)
    trades = []
    trade_time = datetime.now() - timedelta(hours=23)
    for i in range(8):
        t_time = trade_time + timedelta(hours=i * 2)
        trade = TradeModel(
            time=t_time,
            symbol="SPY",
            strategy="Bull Call Spread" if i % 2 == 0 else "Iron Condor",
            status="FILLED" if i < 7 else "PENDING",
        )
        trades.append(trade)
        
    db.add_all(trades)
    
    db.commit()
    db.close()
    print("Successfully seeded 15 decisions and 8 trades.")

if __name__ == "__main__":
    seed_database()
