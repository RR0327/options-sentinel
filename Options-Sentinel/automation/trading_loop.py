from agents.market_agent import analyse_market
from agents.bull_agent import analyse_bull_case
from agents.bear_agent import analyse_bear_case
from agents.risk_agent import analyse_risk
from agents.decision_agent import make_decision
from risk.risk_gate import risk_gate
from options.strategy import select_strategy
from execution.order_manager import OrderManager

def run_trading_cycle():
    market = {"regime": "BULLISH", "confidence": 0.8}
    market_result = analyse_market(market)
    bull = analyse_bull_case(market_result)
    bear = analyse_bear_case(market_result)
    risk = analyse_risk(bull)
    decision = make_decision(bull, bear, risk)
    
    if decision["decision"] == "TRADE":
        approval = risk_gate({"confidence": bull["confidence"], "max_loss": 300})
        if approval["status"] == "APPROVED":
            manager = OrderManager()
            result = manager.submit_trade({"symbol": "SPY", "strategy": decision["strategy"], "quantity": 1})
            return result
    return {"status": "NO_TRADE"}
