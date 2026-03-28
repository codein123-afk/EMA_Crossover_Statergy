import backtest
import performance

initial_capital = 200000

df = backtest.run_backtest(initial_capital)

results = performance.performance(df, initial_capital)

print("\nPerformance Summary")
print("-------------------")

for key, value in results.items():
    if "Return" in key or "Drawdown" in key or "Volatility" in key:
        print(f"{key}: {value*100:.2f}%")
    else:
        print(f"{key}: {value:.2f}")