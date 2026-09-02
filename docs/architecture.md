# Options Sentinel Architecture

## Overview

Options Sentinel is an autonomous AI options trading system designed
around a multi-agent decision architecture, deterministic risk controls,
and Alpaca MCP-based execution.

The system separates intelligence, safety, and execution
responsibilities.

## High-Level Architecture

``` text
                    Market Data
                         |
                         v
                 Market Analysis Layer
                         |
                         v
                  Market Agent
                         |
          +--------------+--------------+
          |                             |
          v                             v
     Bull Agent                    Bear Agent
          |                             |
          +--------------+--------------+
                         |
                         v
                  Risk Agent
                         |
                         v
                Decision Agent
                         |
                         v
                  Risk Gate
                         |
                         v
             Options Strategy Engine
                         |
                         v
                  MCP Client
                         |
                         v
              Alpaca MCP Server
                         |
                         v
             Alpaca Paper Trading
                         |
                         v
              Monitoring and Journal
```

## Core Components

### Market Layer

Responsible for:

-   Collecting market data
-   Calculating indicators
-   Detecting market regime

### Agent Layer

Contains specialised reasoning agents:

-   Market Agent
-   Bull Agent
-   Bear Agent
-   Risk Agent
-   Decision Agent

Each agent has a focused responsibility.

### Risk Layer

The risk layer is independent from AI reasoning.

Responsibilities:

-   Position sizing
-   Maximum loss validation
-   Exposure control
-   Trade approval or rejection

### Execution Layer

The execution layer communicates with Alpaca through MCP.

The AI system does not directly place trades.

Flow:

``` text
Decision
   |
Risk Approval
   |
MCP Tool Call
   |
Alpaca Execution
```

## Design Principles

1.  AI proposes, risk decides.
2.  Safety-critical decisions remain deterministic.
3.  Every decision should be explainable.
4.  Every trade should have an audit trail.
