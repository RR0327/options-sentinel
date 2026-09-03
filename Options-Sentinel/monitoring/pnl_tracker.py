def calculate_return(entry, current):
    profit = current - entry
    percentage = (profit / entry) * 100
    return {"profit": profit, "percentage": round(percentage, 2)}
