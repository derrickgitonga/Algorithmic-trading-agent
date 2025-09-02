# Algorithmic Financial Investment Agent

An automated, rule-based trading bot designed to analyze the EUR/USD forex market and execute trades using candlestick patterns and price action strategies.

##  Overview

This project creates a financial investment agent that automates trading decisions. The agent leverages the **Smart Money Concept (SMC)**, specifically focusing on **pin bar candlestick patterns** formed at key **support and resistance levels** to identify high-probability trading opportunities on the 30-minute timeframe.

By eliminating emotional bias and processing market data with speed and precision, the agent aims to provide a structured, disciplined approach to forex trading, making it accessible for both novice and experienced investors.

## Features

*   **Automated Data Fetching:** Retrieves real-time EUR/USD price data using the Yahoo Finance API.
*   **Pin Bar Recognition:** Implements a robust rule-based model to accurately identify bullish and bearish pin bar candlestick patterns.
*   **Support & Resistance Detection:** Algorithmically identifies significant historical price levels where market reversals are likely to occur.
*   **Confluence-Based Execution:** Only executes trades when a pin bar forms in close proximity (within 3 pips) of a detected support or resistance level.
*   **Risk Management:** Automatically sets stop-loss (10 pips) and take-profit (20 pips) orders for every trade, enforcing a consistent 1:2 risk-reward ratio.
*   **Fully Automated Trading:** Connects to a MetaTrader 5 account to place and manage trades without human intervention.
*   **Scheduled Operation:** Runs analysis and execution cycles every 30 minutes.

## Core Strategy & Rules

The agent's logic is built on a strict set of rules derived from technical analysis:

1.  **Pin Bar Identification:** A candlestick is classified as a pin bar if:
    *   Its total range is at least 4 pips.
    *   One wick is at least 1.5 times longer than the opposite wick.
    *   The long wick is at least 90% the size of the candle's body.

2.  **Support/Resistance Identification:** Levels are found by segmenting historical data into chunks, finding extreme high/low points in each chunk, and fitting a line of best fit through these points.

3.  **Trade Trigger:** A trade is only executed if a valid pin bar forms within 3 pips of a support (for bullish pin bars) or resistance (for bearish pin bars) level.

4.  **Trade Execution:**
    *   **Bullish Pin Bar at Support:** Place BUY order. `Stop Loss = Support Level - 0.0010`, `Take Profit = Support Level + 0.0020`.
    *   **Bearish Pin Bar at Resistance:** Place SELL order. `Stop Loss = Resistance Level + 0.0010`, `Take Profit = Resistance Level - 0.0020`.

## ⚙️ Installation & Setup

### Prerequisites

*   Python 3.8+
*   A MetaTrader 5 account (Demo recommended for testing)
*   Yahoo Finance API access (via `yfinance`)

### Steps

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd algorithmic-trading-bot
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Key dependencies: `pandas`, `yfinance`, `schedule`, `MetaTrader5`*

4.  **Configure MetaTrader 5:**
    *   Ensure MetaTrader 5 is installed and running on your machine.
    *   The agent uses the `MetaTrader5` Python package to connect. Configure your login credentials and server details within the script.

5.  **Run the agent:**
    ```bash
    python main.py
    ```

## Performance & Backtesting

In a simulated backtest over one month, the strategy demonstrated strong performance:

*   **Total Trades:** 20
*   **Winning Trades:** 15
*   **Losing Trades:** 5
*   **Win Rate:** 75%
*   **Net Pips Gained:** 250

**Disclaimer:** Past performance is not indicative of future results. This simulation assumes ideal market conditions and does not account for slippage, commission, or spread costs. Always test thoroughly in a demo environment before deploying real capital.

## Project Structure

```
algorithmic-trading-bot/
│
├── main.py                 # Main script orchestrating the entire process
├── pinbar_detector.py      # Module for identifying pin bar patterns
├── snr_detector.py         # Module for detecting support & resistance levels
├── trade_executor.py       # Module handling MT5 connection and order placement
├── requirements.txt        # Project dependencies
└── README.md              # This file
```

## 🔮 Future Recommendations

As outlined in the project paper, potential enhancements include:
*   **Notifications:** Integrate SMS/Telegram alerts for trade executions and system events.
*   **Machine Learning:** Enhance pattern recognition and level validation using ML models (e.g., Random Forest, CNN).
*   **Advanced Backtesting:** Build a dedicated module for robust historical strategy testing.
*   **Multi-Asset & Multi-Timeframe Support:** Extend the bot to trade various instruments (stocks, crypto) and across different timeframes for signal confirmation.
*   **User Interface (UI):** Develop a web or desktop dashboard for monitoring performance and adjusting parameters easily.


## Disclaimer

This software is intended for **educational and research purposes only**. It is not financial advice. Automated trading carries significant risk, and you can lose your capital. You are solely responsible for any trading decisions you make. Always test any strategy in a demo account before using real funds.

## License

This project is licensed for academic use. Please contact the authors for permissions.

---
