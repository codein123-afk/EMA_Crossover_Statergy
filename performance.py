import numpy as np

def performance(df, initial_capital):

    results = {}

    # Total Return
    total_return = df["Equity"].iloc[-1] / initial_capital - 1
    results["Total Return"] = total_return

    # Annualized Return
    num_days = len(df)
    annual_return = (1 + total_return) ** (252 / num_days) - 1
    results["Annual Return"] = annual_return

    # Annualized Volatility
    daily_vol = df["Strategy_Return"].std()
    annual_vol = daily_vol * np.sqrt(252)
    results["Annual Volatility"] = annual_vol

    # Sharpe Ratio (risk-free = 0)
    sharpe = annual_return / annual_vol if annual_vol != 0 else 0
    results["Sharpe Ratio"] = sharpe

    # Max Drawdown
    peak = df["Equity"].cummax()
    drawdown = (df["Equity"] - peak) / peak
    max_drawdown = drawdown.min()
    results["Max Drawdown"] = max_drawdown

    # Number of Trades
    num_trades = (df["Trade"] == -1).sum()
    results["Number of Trades"] = num_trades

    return results



