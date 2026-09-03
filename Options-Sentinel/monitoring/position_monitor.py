from execution.alpaca_client import get_positions

def get_open_positions():
    positions = get_positions()
    result = []
    for position in positions:
        result.append({
            "symbol": position.symbol,
            "quantity": position.qty,
            "entry_price": position.avg_entry_price,
            "current_price": position.current_price,
            "unrealized_pl": position.unrealized_pl
        })
    return result
