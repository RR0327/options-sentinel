# Options Sentinel - Operating Guide & Build Log

## 1. Project Overview
Options Sentinel is a paper-trading autonomous options agent. It pulls live Alpaca options chains, runs a scheduled multi-agent debate (bull vs. bear) gated by hard risk limits, executes via an MCP connector, logs and journals every decision, and exposes everything through a real-time dashboard endpoint.

### Architecture
```text
Market Data -> AI Agents -> Risk Gate -> Options Engine -> Alpaca MCP -> Paper Trading
```

### Key Features
- **Multi-Agent Analysis:** Rule-based Bull vs. Bear debate for market sentiment.
- **Risk-Controlled Execution:** Hard risk limits prevent the AI from making catastrophic trades.
- **Options Spreads Selection:** Automatically constructs valid option spreads (e.g., BULL_CALL_SPREAD) based on the closest target delta and maximum liquidity.
- **MCP Integration:** Uses the Model Context Protocol (MCP) to interact securely with Alpaca.
- **Trade Audit Trail:** Saves full decision logic, entry points, and P&L monitoring to a local database.

---

## 2. Environment Setup & Configuration

Before running any commands, you must configure your environment and activate your virtual environment.

### 2.1 Activate Virtual Environment
Open a terminal in the `Options-Sentinel` folder and run:
```powershell
.\venv\Scripts\activate
```
*(You should see `(venv)` appear at the beginning of your command prompt, indicating it's active).*

### 2.2 Configure `.env`
Ensure your `.env` file contains your paper trading credentials. **Never commit these keys!**
```env
ALPACA_API_KEY=your_key_here
ALPACA_SECRET_KEY=your_secret_here
ALPACA_PAPER=true
```

### 2.3 Install Dependencies
```powershell
pip install -r requirements.txt
```

---

## 3. Running the System

Options Sentinel consists of a FastAPI backend (providing data endpoints) and a scheduled autonomous trading loop.

### 3.1 Start the FastAPI Backend
Start the server in a dedicated terminal window:
```powershell
cd Options-Sentinel
uvicorn backend.main:app --reload
```
*(The `--reload` flag automatically restarts the server if you make code changes).*

### 3.2 Start the Autonomous Scheduler
The scheduler repeatedly runs the trading loop (Market -> AI -> Risk -> Execute) during market hours.
In a new terminal (with the virtual environment activated), run:
```powershell
cd Options-Sentinel
python -m automation.scheduler
```

### 3.3 View the Frontend Dashboard
The dashboard visualizes the current system state, pulling live from the FastAPI backend.
1. Open your file explorer and navigate to `Options-Sentinel/dashboard/`.
2. Double-click on `index.html` to open it in your browser.
3. The dashboard will automatically fetch your live stats directly from your backend endpoints.

---

## 4. Testing Everything (End-to-End Validation)

You can validate every component of the system using automated tests, API endpoints, or the frontend UI.

### 4.1 Automated Tests (Pytest)
Pytest exercises the internal modules individually and together.
```powershell
# Test the Alpaca Connection
pytest -s tests/test_connection.py

# Test the Market Data & Regime Detection
pytest -s tests/test_market.py
pytest -s tests/test_regime.py

# Test the AI Agent Chain & Risk Gate
pytest -s tests/test_agents.py
pytest -s tests/test_risk.py

# Test Options Strategy & Monitoring
pytest -s tests/test_options.py
pytest -s tests/test_monitoring.py

# Full Integration Test (One Command)
pytest -s tests/test_full_system.py
```

### 4.2 API Endpoint Testing (Swagger UI)
The system exposes a unified `/api/dashboard` endpoint for the frontend.
1. Ensure the backend is running (`uvicorn backend.main:app --reload`).
2. Open Swagger UI at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
3. Locate the `GET /api/dashboard` endpoint and click **Try it out** -> **Execute**.

**Sample Output (JSON Response):**
```json
{
    "system": {"status": "ACTIVE", "mcp": "CONNECTED", "alpaca": "CONNECTED"},
    "market": {"symbol": "SPY", "regime": "BULLISH", "confidence": 0.82},
    "agents": {"bull": "BUY", "bear": "CAUTION", "risk": "APPROVED"},
    "trade": {"strategy": "BULL_CALL_SPREAD", "status": "READY"}
}
```

### 4.3 Frontend UI Testing
The `dashboard/app.js` file handles the visual representation.
- **Sample Input (Network Request):** The frontend issues a `fetch('http://127.0.0.1:8000/api/dashboard')` command.
- **Sample Output (UI Render):** Once the JSON is received, DOM elements (e.g., `#system-status`, `#market-regime`) are populated dynamically, updating the on-screen dashboard blocks.

---

## 5. Hackathon Demo Script (6-Scene Order)

If presenting this project, follow this curated flow to demonstrate full capabilities:

1. **System Health:** Open the dashboard and show the **ACTIVE** system status and connected MCP/Alpaca indicators.
2. **Market Intelligence:** Show the live Market Regime (e.g., "BULLISH") and its algorithmic confidence score.
3. **AI Agent Debate:** Walk through the Bull/Bear opinions (e.g., Bull says BUY, Bear says CAUTION) and demonstrate that the Risk Agent ultimately gave APPROVAL based on strict position-sizing limits.
4. **Strategy Formulation:** Highlight the chosen strategy (e.g., `BULL_CALL_SPREAD`) generated by the Options Engine.
5. **MCP Execution:** Switch to the Alpaca Paper Trading dashboard (Orders tab) and show the order successfully submitted via the MCP Connector.
6. **Trade Journal:** Open `database/trades.json` and `database/decisions.json` to prove every decision and logic branch was durably recorded for compliance.
