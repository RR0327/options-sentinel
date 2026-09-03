from execution.alpaca_client import get_account

def test_connection():
    account = get_account()
    print(account.status)
    print(account.cash)
