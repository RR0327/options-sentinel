# Options Sentinel - Operating Guide

This guide covers how to operate the Options Sentinel project, including running the backend server, testing the API endpoints, checking the raw Alpaca connection, and utilizing the Alpaca MCP server.

## 1. Environment Setup (Always run this first)

Before running any Python commands, you must activate your virtual environment.

Open a terminal in the `Options-Sentinel` folder and run:
```powershell
.\venv\Scripts\activate
```
*(You should see `(venv)` appear at the beginning of your command prompt, indicating it's active).*

---

## 2. Running the FastAPI Backend

The backend is built with FastAPI and is located in the `backend/` folder. 

**To start the server:**
```powershell
uvicorn backend.main:app --reload
```
The `--reload` flag means the server will automatically restart if you make any changes to the code.

**To view the interactive API documentation:**
Open your web browser and navigate to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
This is an automatically generated Swagger UI where you can test your endpoints visually.

### Available API Endpoints

1. **Status Endpoint (`GET /`)**
   - **URL:** `http://127.0.0.1:8000/`
   - **Purpose:** Checks if the server is running.
   - **Test via PowerShell:**
     ```powershell
     Invoke-RestMethod -Uri http://127.0.0.1:8000/
     ```

2. **Test Input/Output Endpoint (`POST /test`)**
   - **URL:** `http://127.0.0.1:8000/test`
   - **Purpose:** Demonstrates how to send JSON data to the server and get a response.
   - **Test via PowerShell (Invoke-RestMethod):**
     ```powershell
     Invoke-RestMethod -Uri http://127.0.0.1:8000/test -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"message": "Testing Options Sentinel", "number": 10}'
     ```
   - **Alternative Test via cURL (Windows CMD/PowerShell):**
     ```powershell
     curl.exe -X POST http://127.0.0.1:8000/test -H "Content-Type: application/json" -d "{\`"message\`": \`"Testing Options Sentinel\`", \`"number\`": 10}"
     ```
   - **Expected JSON Response:**
     ```json
     {
       "received_message": "Testing Options Sentinel",
       "doubled_number": 20,
       "status": "success"
     }
     ```

---

## 3. Testing the Alpaca Connection

To ensure your `.env` API keys are working correctly with Alpaca's paper trading environment:

**Run the test script:**
```powershell
python test_alpaca.py
```
**Expected Output:**
```text
Account Status: ACTIVE
Cash: 100000
Buying Power: 100000
```
If this fails, double-check that your `ALPACA_API_KEY` and `ALPACA_SECRET_KEY` inside the `Options-Sentinel/.env` file are correct.

---

## 4. Operating the Alpaca MCP Server (AI Integration)

You also have the **Alpaca MCP Server (v2)** located in the sibling folder `alpaca-mcp-server/`. This server bridges your AI agents (like Claude or Cursor) to the Alpaca API so they can manage trades or check balances for you.

Because this is the new V2 Python server, it runs differently than older tutorials might suggest (no `npm` required).

**How to connect it to your IDE (e.g., Cursor):**
1. Open your IDE Settings and go to the **MCP** (Model Context Protocol) section.
2. Add a new MCP server with the following settings:
   - **Type:** `stdio`
   - **Command:** `uvx`
   - **Arguments:** `alpaca-mcp-server`
   - **Environment Variables:**
     - `ALPACA_API_KEY` = (Your Key)
     - `ALPACA_SECRET_KEY` = (Your Secret Key)
3. Restart your IDE to apply the changes.

Once configured, you can directly ask the AI in your editor chat:
> *"Show my Alpaca paper account balance."*
> *"What is the current quote for AAPL via Alpaca?"*

The AI will automatically invoke the server and retrieve real data for you. For more detailed instructions and configuration formats, refer to the `mcp_test.py` file.

---

## 5. Next Work: Operating the Core Modules (Phase 5 - 7)

With the core codebase scaffolded, the project now has internal Market Data, AI Agent Reasoning, and a Risk Gate. You can operate these modules directly via tests.

**Test the Market Data Engine:**
```powershell
pytest -s tests/test_market.py
pytest -s tests/test_indicators.py
pytest -s tests/test_regime.py
```
*(This pulls live/historical data from Alpaca, calculates technical indicators, and determines if the market is Bullish, Bearish, or Neutral).*

**Test the AI Agent Chain:**
```powershell
pytest -s tests/test_agents.py
```
*(This forces a 'Bullish' market state through the Market Agent -> Bull Agent -> Bear Agent -> Risk Agent -> Decision Agent, resulting in a simulated trade decision).*

**Test the Risk Gate (The Final Authority):**
```powershell
pytest -s tests/test_risk.py
```
*(This tests that the `risk_gate` will correctly `APPROVE` safe trades within the $500 max loss limit, and instantly `REJECT` bad trades with low confidence or high risk).*

---

## 6. Phase 8-12: The Autonomous Loop and Dashboard

With the final phases complete, the system now features real Options Contract construction, Position Monitoring, an active Trade Journal, and an autonomous trading cycle that runs from start to finish.

**Test the Options Engine:**
```powershell
pytest -s tests/test_options.py
```
*(Confirms that the system converts a "BULLISH" sentiment into a concrete "BULL_CALL_SPREAD" JSON order block).*

**Test the Trade Lifecycle Monitoring:**
```powershell
pytest -s tests/test_monitoring.py
```
*(Tests the exit engine and verifies that trades are correctly logged to `database/trades.json` and `database/decisions.json`).*

**Test the Full Autonomous Trading Loop:**
```powershell
pytest -s tests/test_trading_loop.py
```
*(This triggers the master loop inside `automation/trading_loop.py` which hits every single module sequentially: Market Data -> Agent Debate -> Risk Gate -> Options Spread -> Order Manager -> MCP Connector).*

### Viewing the Real-Time Dashboard
You can now visualize your account, live market sentiment, and active positions through the lightweight HTML dashboard built in Phase 11.

1. Make sure your FastAPI backend is running: `uvicorn backend.main:app --reload`
2. Open your file explorer, navigate to `Options-Sentinel/dashboard/`.
3. Double click on `index.html` to open it in Google Chrome or any browser.
4. The dashboard will automatically fetch your live stats directly from your backend endpoints every 60 seconds!
