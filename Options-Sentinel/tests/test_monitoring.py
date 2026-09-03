from monitoring.exit_engine import check_exit

def test_monitoring():
    position = {"unrealized_pl": 250}
    action = check_exit(position)
    print(action)
    assert action["action"] == "EXIT"
    assert action["reason"] == "Take profit reached"
