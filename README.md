# Bitcoin EMA Crossover Backtester

This is a quantitative research project focused on evaluating an Exponential Moving Average (EMA) crossover strategy on historical Bitcoin price data.  

The program ingests & cleans 1D BTC price action from 2018-2025, backtests the system, visualizes its performance compared to holding BTC over the same period, and exports information on the executed trades for further analysis.

---

## Strategy Summary

Motivating Question: Bitcoin is one of the best performing assets of the last decade, but it's large price swings decrease its attractiveness as an investment. How can I determine with high probability when a "bull" or "bear" market is starting so I can trade directionally and limit downside potential?

Hypothesis: I can use "slow" and "fast" moving averages to identify trend shifts, with a bullish shift signified by the fast band crossing above the slow band and vice versa. When executing this strategy, I can limit the "whipsaw" effect of mean reversion environments by filtering potential trades based on higher timeframe trend support.

Indicators:
- 25 Day EMA: Fast Band
- 75 Day EMA: Slow Band
- 350 Day (50 Week) EMA: Trend Support

Rules:
- Entry:
  - Go Long: Fast EMA crosses above the slow EMA while price is above the trend support
  - Go Short: Fast EMA crosses below the slow EMA while price is below the trend support
- Exit:
  - Early Invalidation: Price violates the trend support (closes below while long or above while short)
  - Typical Invalidation: Trend shift
- Risk Management:
  - Allocates ~100% of account capital per position (models long-term spot investing; no leverage)
- Fees:
  - 0.2% commission per transaction (reasonable estimate for the maker fee on a major crypto exchange)
- Initial Capital:
  - $100,000

---

## Repository Structure

backtester/
- BTC_MA_Cross/
  - data/                         # Historical BTC OHLCV datasets
    - btc_1d_data_2018_to_2025.csv
    - btc_1h_data_2018_to_2025.csv
    - btc_4h_data_2018_to_2025.csv
    - btc_15m_data_2018_to_2025.csv
  - results/                      # Backtest's trade log
    - trades_executed.csv       
  - src/                          # Backtester implementation
    - main.py                   
  - .gitignore

---

## Tech Stack

Python 3.9+

pandas - data handling

matplotlib - visualization

backtesting.py - event-driven backtesting engine

---

## Installation & Setup

git clone https://github.com/vedant-42/backtester.git

cd backtester

pip install pandas matplotlib backtesting

---

## Running the Backtest

cd BTC_MA_Cross/src

python3 main.py

---

## The script will:

1) Load BTC's historical 1D price action from data/btc_1d_data_2018_to_2025.csv
2) Execute the EMA crossover strategy
3) Apply 0.2% commissions per transaction
4) Output a performance report in the terminal
5) Save trade history to results/trades_executed.csv
6) Display a chart comparing strategy equity vs. buy & hold benchmark

---

## Relevant Stats

Sharpe Ratio - 0.71: Indicates smoother risk-adjusted returns relative to buying and holding BTC; higher returns and decreased volatility

Sortino Ratio - 1.84, Profit Factor - 10.54: Demonstrates limited downside volatility and asymmetric returns

Beta - 0.07: Low linear correlation to BTC due to flipping directional bias (rather than true market neutrality)

CAGR (Compounded Annual Growth Rate) - 51.46%: Increased annualized returns relative to BTC due to effective directional trading

Max Drawdown - 37.37%: Caused by chop/whipsaw rather than the deep pullbacks of BTC; consistent with low beta and evident in equity curve

Calmar Ratio - 1.38: Strategy consistently compounded relative to its worst historical drawdown, indicating sustainable performance

---

## Project Demonstrates

- Building a backtesting environment from raw OHLCV data
- Implementing momentum-based technical indicators (EMAs)
- Evaluating performance with risk-adjusted metrics (Sharpe, Sortino, Calmar)
- Accounting for transaction costs and drawdowns
- Visualizing equity curves for analysis and benchmarking

---

## Authored by

Vedant Narayan 

For educational and quantitative research purposes; I wouldn't recommend mortgaging your house to go all in on this
