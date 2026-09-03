def calculate_payoff(debit, strike_difference):
    max_loss = debit
    max_profit = strike_difference - debit
    return {"max_loss": max_loss, "max_profit": max_profit}
