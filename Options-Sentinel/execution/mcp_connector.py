class MCPConnector:
    def __init__(self):
        self.server_running = False
        
    def connect(self):
        self.server_running = True
        return {"status": "MCP connected"}
        
    def execute_tool(self, tool_name, parameters):
        if not self.server_running:
            raise Exception("MCP server not connected")
        return {"tool": tool_name, "parameters": parameters}
