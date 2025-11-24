# EMA Crossover Backtester (Bitcoin)

This project implements and backtests a quantitative trading strategy using Exponential Moving Average (EMA) crossovers on historical Bitcoin data.  
The system is built in Python using pandas, matplotlib, and backtesting.py, and includes realistic 0.2% transaction costs to simulate real-market friction.

---

# Project Overview
The strategy seeks to capture medium-term momentum trends by trading Bitcoin based on the relationship between fast (25) and slow (75) EMAs filtered by a higher timeframe trend indicator (350 EMA).  

- Enters a long when the fast EMA crosses above the slow EMA during an uptrend  
- Enters a short when the fast EMA crosses below the slow EMA during a downtrend  
- Exits early if price violates the long-term EMA (trend support)  
- Allocates ~100% of account capital per position (no leverage)

The goal of this project is to demonstrate backtesting design, signal logic, and quantitative evaluation of trading systems.

---

# Dependencies

Install Python 3.9+ and required libraries:

pip install pandas matplotlib backtesting

---

# How to Run

Clone this repository onto your local and navigate into the src directory to run the code, as shown below.

cd BTC_MA_CROSS/src
python3 main.py

The script will:
1) Load data/btc_1d_data_2018_to_2025.csv
2) Execute the EMA crossover backtest with 0.2% commissions per transaction
3) Output a performance report in the terminal
4) Save trade history to results/trades_executed.csv
5) Display a chart comparing strategy equity vs. buy & hold

---

# Demonstrates:

- Building a backtesting environment from raw OHLCV data
- Implementing momentum-based technical indicators (EMAs)
- Evaluating performance with risk-adjusted metrics (Sharpe, Sortino, Calmar)
- Accounting for transaction costs and drawdowns
- Visualizing equity curves for analysis and benchmarking

---

# Authored by:

Vedant Narayan
For educational and quantitative research purposes
