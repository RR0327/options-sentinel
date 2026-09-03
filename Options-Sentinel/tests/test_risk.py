from risk.risk_gate import risk_gate

def test_risk():
    good_trade = {"confidence": 0.8, "max_loss": 300}
    bad_trade = {"confidence": 0.4, "max_loss": 800}
    
    good_result = risk_gate(good_trade)
    bad_result = risk_gate(bad_trade)
    
    print("Good trade:", good_result)
    print("Bad trade:", bad_result)
    
    assert good_result["status"] == "APPROVED"
    assert bad_result["status"] == "REJECTED"
