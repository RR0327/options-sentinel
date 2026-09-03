from options.strategy import select_strategy
from options.spread import create_bull_call_spread
from options.payoff import calculate_payoff

def test_options():
    regime = "BULLISH"
    strategy = select_strategy(regime)
    
    spread = create_bull_call_spread("SPY", 560, 565, "2026-10-16")
    payoff = calculate_payoff(2.0, 5.0)
    
    print("Strategy:", strategy)
    print("Spread:", spread)
    print("Payoff:", payoff)
    
    assert strategy["strategy"] == "BULL_CALL_SPREAD"
    assert spread["buy_leg"]["strike"] == 560
    assert payoff["max_loss"] == 2.0
    assert payoff["max_profit"] == 3.0
