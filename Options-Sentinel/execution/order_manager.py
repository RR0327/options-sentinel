from execution.mcp_connector import MCPConnector

class OrderManager:
    def __init__(self):
        self.mcp = MCPConnector()
        self.mcp.connect()
        
    def submit_trade(self, order):
        return self.mcp.execute_tool("submit_order", order)
