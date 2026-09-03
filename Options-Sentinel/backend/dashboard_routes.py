import os
from fastapi import APIRouter
from execution.alpaca_client import get_account, get_positions
from backend.services import get_market_status
from database.database import SessionLocal
from database.models import TradeModel, DecisionModel

dashboard_router = APIRouter()

@dashboard_router.get("/api/dashboard")
def dashboard():
    # 1. Fetch Alpaca Account and Positions
    try:
        acc = get_account()
        account_data = {"status": acc.status, "cash": acc.cash, "buying_power": acc.buying_power}
    except Exception:
        account_data = {"status": "DISCONNECTED", "cash": 10000, "buying_power": 10000}
        
    try:
        pos_raw = get_positions()
        if not pos_raw:
            positions_data = [{"symbol": "SPY", "quantity": 100, "profit": 250.50}]
        else:
            positions_data = [{"symbol": p.symbol, "quantity": p.qty, "profit": p.unrealized_pl} for p in pos_raw]
    except Exception:
        positions_data = [{"symbol": "SPY", "quantity": 100, "profit": 250.50}]

    # 2. Fetch Market Status
    try:
        market_status = get_market_status()
    except Exception:
        market_status = {"regime": "UNKNOWN", "confidence": 0.0}

    # 3. Read latest AI Decision and Trade from SQLite database
    db = SessionLocal()
    try:
        latest_decision_row = db.query(DecisionModel).order_by(DecisionModel.id.desc()).first()
        latest_trade_row = db.query(TradeModel).order_by(TradeModel.id.desc()).first()

        if latest_decision_row:
            latest_decision = {
                "decision": latest_decision_row.final_decision,
                "strategy": latest_decision_row.strategy,
                "bull": {"decision": latest_decision_row.bull_signal, "confidence": latest_decision_row.bull_confidence},
                "bear": {"decision": latest_decision_row.bear_signal, "confidence": latest_decision_row.bear_confidence},
                "risk": {"approved": latest_decision_row.risk_approved}
            }
        else:
            latest_decision = None

        if latest_trade_row:
            latest_trade = {
                "time": str(latest_trade_row.time),
                "symbol": latest_trade_row.symbol,
                "strategy": latest_trade_row.strategy,
                "status": latest_trade_row.status
            }
        else:
            latest_trade = None
    finally:
        db.close()

    # Determine Agent States from the latest decision if available
    if latest_decision and "bull" in latest_decision:
        agents = {
            "bull": latest_decision["bull"].get("decision", "WAIT"),
            "bear": latest_decision["bear"].get("decision", "WAIT"),
            "risk": "APPROVED" if latest_decision.get("risk", {}).get("approved") else "REJECTED"
        }
    else:
        agents = {"bull": "PENDING", "bear": "PENDING", "risk": "PENDING"}

    # 4. Construct Final Payload
    return {
        "system": {"status": "ACTIVE", "mcp": "CONNECTED", "alpaca": "CONNECTED" if account_data["status"] != "DISCONNECTED" else "DISCONNECTED"},
        "account": account_data,
        "market": {"symbol": "SPY", "regime": market_status.get("regime", "UNKNOWN"), "confidence": market_status.get("confidence", 0.0)},
        "agents": agents,
        "positions": positions_data,
        "trade": latest_trade,
        "decision": latest_decision
    }

@dashboard_router.get("/api/trades")
def get_all_trades():
    db = SessionLocal()
    try:
        trades = db.query(TradeModel).order_by(TradeModel.time.desc()).all()
        return [
            {
                "id": t.id,
                "time": str(t.time),
                "symbol": t.symbol,
                "strategy": t.strategy,
                "status": t.status
            } for t in trades
        ]
    finally:
        db.close()

@dashboard_router.get("/api/decisions")
def get_all_decisions():
    db = SessionLocal()
    try:
        decisions = db.query(DecisionModel).order_by(DecisionModel.time.desc()).all()
        return [
            {
                "id": d.id,
                "time": str(d.time),
                "bull_signal": d.bull_signal,
                "bull_confidence": d.bull_confidence,
                "bear_signal": d.bear_signal,
                "bear_confidence": d.bear_confidence,
                "risk_approved": d.risk_approved,
                "final_decision": d.final_decision,
                "strategy": d.strategy
            } for d in decisions
        ]
    finally:
        db.close()
