import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from backtesting import Backtest, Strategy
from backtesting.lib import crossover

# Uses pandas' estimated weighted moving average function to create bands
def EMA(
    values, # Dataframe of price data
    n # Length/period of MA
):
    # Returns series of MA data - same size as input price series
    return pd.Series(values).ewm(span=n, adjust=False).mean()

class EmaCrossoverStrategy(Strategy):
    fast_n = 25
    slow_n = 75
    confluence = 350

    # Registers/initializes the indicators (fast and slow bands + high timeframe)
    def init(self):
        self.ema_fast = self.I(EMA, self.data.Close, self.fast_n)
        self.ema_slow = self.I(EMA, self.data.Close, self.slow_n)
        self.trend_support = self.I(EMA, self.data.Close, self.confluence)

    # Runs on each bar of price data
    def next(self):
        # Trend confirmation - ensures price is above/below 200 MA for long/short
        price = self.data.Close[-1]
        trend = self.trend_support[-1]
        in_uptrend = price > trend
        in_downtrend = price < trend
        
        # Closes positions early (hopefully) if price breaks through trend support
        if not in_uptrend and self.position.is_long:
            self.position.close()
        elif not in_downtrend and self.position.is_short:
            self.position.close()
        
        # Go long if bands cross bullishly
        if crossover(self.ema_fast, self.ema_slow):
            # Closes any open short position
            if self.position.is_short:
                self.position.close()

            # Executes position entry
            if in_uptrend and not self.position.is_long:
                self.buy(size=0.999)  # size = 100% of account capital

        # Go short if bands cross bearishly
        elif crossover(self.ema_slow, self.ema_fast):
            # Closes any open long position
            if self.position.is_long:
                self.position.close()
            
            # Executes position entry
            if in_downtrend and not self.position.is_short:
                self.sell(size=0.999)

# Reads historical price data into a dataframe with the datetimes as the indices
df = pd.read_csv("archive/btc_1d_data_2018_to_2025.csv", parse_dates=["Open time"], index_col="Open time")
df = df[~df.index.isna()] # Cleans data of any rows w/ missing timestamp
df = df.sort_index() # Ensures data is chronological

# Filters the price data for the parameters backtesting.py expects
df = df[["Open", "High", "Low", "Close", "Volume"]]

# Instantiates a backtesting object for this system with 10k capital and no fees
initial_cash = 100000
bt = Backtest(df, EmaCrossoverStrategy, cash=initial_cash, commission=0.002, finalize_trades=True)

# Executes backtesting and provides breakdown of relevant information
stats = bt.run()
print(stats)

# Extracts the exit, entry, and timestamp of each trade
trades_df = stats['_trades']

# Saves the trade data to a csv and saves it to the current directory
trades_df.to_csv('trades_executed.csv', index=False)

# Gets strategy's capital over time
equity_df = stats['_equity_curve']

# Creates data to simulate buying and holding throughout the tested period
buy_hold_equity = (df['Close'] / df['Close'].iloc[0]) * initial_cash

# Sets up a plot for the strategies' equity curves
fig, ax = plt.subplots(figsize=(12, 6))

# Plots crossover strategy
ax.plot(equity_df.index, equity_df['Equity'], label='Strategy Equity', linewidth=2)

# Plots buy & hold strategy
ax.plot(df.index, buy_hold_equity, label='Buy & Hold Equity', linewidth=2,)

# Formats axes to display notional value of account
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))

# Creates plot
plt.title('Strategy Performance vs. Buy & Hold BTC')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()