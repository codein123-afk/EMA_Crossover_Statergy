# 📊 SBI EMA Crossover Strategy

![Python](https://img.shields.io/badge/Python-3.8+-blue) ![License](https://img.shields.io/badge/license-MIT-green)

A trend-following strategy backtested on State Bank of India (SBI) using an EMA 20 / EMA 200 crossover signal. Built with a modular structure — data loading, signal generation, and backtesting are in separate files.

## How it works

The strategy uses the difference between a fast EMA (20-day) and slow EMA (200-day) to detect trend changes.

| Signal | Condition | Meaning |
|---|---|---|
| Buy (golden cross) | EMA 20 crosses above EMA 200 | Uptrend starting |
| Sell (death cross) | EMA 20 crosses below EMA 200 | Downtrend starting |

Position is held long between a buy and the next sell signal.

## Strategy details

- **Stock**: SBI (loaded from local `Sbi.xlsx`)
- **Signal**: EMA 20 vs EMA 200 crossover
- **Position**: long only, fully invested on each buy
- **Starting capital**: ₹1,00,000
- **Equity curve**: share-count based tracking

## Project structure
```
sbi-ema-crossover/
├── data.py          # Loads Excel, computes SMA & EMA indicators
├── statergy.py      # Generates crossover buy/sell signals
├── whole.ipynb      # Main notebook — backtest + equity curve plot
├── Data/
│   └── Sbi.xlsx     # Raw OHLC price data (required)
└── README.md
```

## Requirements
```
pip install pandas matplotlib openpyxl
```

## Usage

Place your SBI price data at `Data/Sbi.xlsx` with columns `DATE` and `CLOSE`, then run:
```bash
jupyter notebook whole.ipynb
```

## Indicators computed

- SMA 20, SMA 50, SMA 200
- EMA 20 (alpha = 0.5), EMA 50, EMA 200 (span-based)
- EMA diff (EMA 20 − EMA 200) for crossover detection

## Limitations

- Data loaded from local Excel file — not fetched automatically
- Long only — no shorting on death cross
- No transaction costs or slippage modelled
- No benchmark comparison (e.g. buy-and-hold SBI)

## Disclaimer

For educational purposes only. Not financial advice.
