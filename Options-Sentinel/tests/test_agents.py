from agents.market_agent import analyse_market
from agents.bull_agent import analyse_bull_case
from agents.bear_agent import analyse_bear_case
from agents.risk_agent import analyse_risk
from agents.decision_agent import make_decision

def test_agents():
    market_data = {"regime": "BULLISH", "confidence": 0.8}
    market = analyse_market(market_data)
    bull = analyse_bull_case(market)
    bear = analyse_bear_case(market)
    risk = analyse_risk(bull)
    decision = make_decision(bull, bear, risk)
    
    print(decision)
    assert decision["decision"] == "TRADE"
    assert decision["strategy"] == "BULL_CALL_SPREAD"
