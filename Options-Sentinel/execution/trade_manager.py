class TradeManager:
    def __init__(self):
        self.active_trades = []
        
    def add_trade(self, trade):
        self.active_trades.append(trade)
        
    def get_active_trades(self):
        return self.active_trades
