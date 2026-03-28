import data
import statergy
import matplotlib.pyplot as plt


def run_backtest(initial_capital):

    df = data.load_data()
    df = statergy.Crossover(df)

    # Daily returns
    df["Return"] = df["Close"].pct_change()
    # Strategy returns
    df["Strategy_Return"] = df["Position"] * df["Return"]
    df["Trade"] = df["Position"].diff()

    # Equity curve (compounded)
    cash = initial_capital
    shares = 0
    equity_list = []

    for i in range(len(df)):
        if df["Trade"].iloc[i] == 1:  # Buy
            shares = cash / df["Close"].iloc[i]
            cash = 0
        elif df["Trade"].iloc[i] == -1:  # Sell
            cash = shares * df["Close"].iloc[i]
            shares = 0

        equity = cash + shares * df["Close"].iloc[i]
        equity_list.append(equity)

    df["Equity"] = equity_list

    return df

#plt.plot(df["Date"], df["Equity"])
#plt.show()