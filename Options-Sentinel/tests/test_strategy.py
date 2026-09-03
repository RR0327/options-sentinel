from options.strategy import select_strategy

def test_strategy():
    bullish = select_strategy("BULLISH")
    bearish = select_strategy("BEARISH")
    neutral = select_strategy("NEUTRAL")
    
    assert bullish["strategy"] == "BULL_CALL_SPREAD"
    assert bearish["strategy"] == "BEAR_PUT_SPREAD"
    assert neutral["strategy"] == "NO_TRADE"
    print("Strategy tests passed")
