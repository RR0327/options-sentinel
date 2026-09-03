from execution.mcp_connector import AlpacaMCPClient

def test_execution():
    client = AlpacaMCPClient()
    conn_status = client.connect()
    print(conn_status)
    
    order = {"symbol": "SPY", "strategy": "BULL_CALL_SPREAD"}
    order_status = client.send_order(order)
    print(order_status)
    
    assert conn_status["status"] == "connected"
    assert order_status["status"] == "order_sent"
    assert order_status["order"] == order
