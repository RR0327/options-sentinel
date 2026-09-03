def calculate_position_size(account_balance, risk_percentage, max_loss_per_contract):
    allowed_risk = account_balance * risk_percentage
    quantity = allowed_risk // max_loss_per_contract
    return int(quantity)
