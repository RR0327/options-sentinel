from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from database.database import Base
from datetime import datetime

class TradeModel(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    time = Column(DateTime, default=datetime.utcnow)
    symbol = Column(String, index=True)
    strategy = Column(String)
    status = Column(String)

class DecisionModel(Base):
    __tablename__ = "decisions"

    id = Column(Integer, primary_key=True, index=True)
    time = Column(DateTime, default=datetime.utcnow)
    bull_signal = Column(String)
    bull_confidence = Column(Float)
    bear_signal = Column(String)
    bear_confidence = Column(Float)
    risk_approved = Column(Boolean)
    final_decision = Column(String)
    strategy = Column(String)
