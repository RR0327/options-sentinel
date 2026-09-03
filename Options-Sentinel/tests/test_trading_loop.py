from automation.trading_loop import run_trading_cycle

def test_trading_loop():
    result = run_trading_cycle()
    print(result)
    assert result["tool"] == "submit_order"
    assert result["parameters"]["symbol"] == "SPY"
