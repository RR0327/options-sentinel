from fastapi import APIRouter
from execution.alpaca_client import get_account, get_positions
from backend.services import get_market_status

router = APIRouter(prefix="/api")

@router.get("/status")
def status():
    return {"system": "Options Sentinel", "status": "ACTIVE"}

@router.get("/account")
def account():
    acc = get_account()
    return {"status": acc.status, "cash": acc.cash, "buying_power": acc.buying_power}

@router.get("/positions")
def positions():
    data = get_positions()
    return [{"symbol": p.symbol, "quantity": p.qty, "profit": p.unrealized_pl} for p in data]

@router.get("/market")
def market():
    return get_market_status()
