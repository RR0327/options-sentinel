# Options Sentinel Demo Flow

## Purpose

This document describes the recommended demonstration sequence for
presenting Options Sentinel.

## Demo Sequence

### 1. System Startup

Start:

-   Alpaca MCP Server
-   FastAPI Backend
-   Autonomous Agent Runner

Expected status:

``` text
MCP: Connected
Alpaca: Connected
Agent: Active
```

------------------------------------------------------------------------

### 2. Market Analysis

The system collects market information.

Example output:

``` text
Symbol: SPY

Market Regime:
BULLISH

Confidence:
82%
```

------------------------------------------------------------------------

### 3. Multi-Agent Analysis

The agents analyse the opportunity.

Example:

``` text
Bull Agent:
Positive trend detected

Bear Agent:
Possible reversal risk

Risk Agent:
Trade within limits
```

------------------------------------------------------------------------

### 4. Decision Stage

The Decision Agent combines the analysis.

Example:

``` text
Decision:
TRADE

Strategy:
Bull Call Spread
```

------------------------------------------------------------------------

### 5. Risk Validation

The Risk Gate checks:

-   Maximum loss
-   Position size
-   Exposure
-   Confidence

Possible outputs:

``` text
APPROVED
```

or

``` text
REJECTED
```

------------------------------------------------------------------------

### 6. MCP Execution

Approved trades follow:

``` text
Options Sentinel

        |

MCP Client

        |

Alpaca MCP Server

        |

Alpaca Paper Trading
```

------------------------------------------------------------------------

### 7. Monitoring

The system records:

-   Trade decision
-   Strategy
-   Risk evaluation
-   Execution result

This creates an explainable trading history.
