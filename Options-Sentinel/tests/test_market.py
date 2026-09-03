from market.data_provider import get_stock_data

def test_market():
    df = get_stock_data("SPY")
    print(df.head())
    assert not df.empty
