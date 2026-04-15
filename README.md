# Yield Scanner DeFi

A lightweight, no-nonsense Python script to fetch, compare, and analyze live DeFi yield data across top lending protocols using the [DeFiLlama API](https://defillama.com/).

## Features
- **Live Data**: Fetches real-time APY and TVL data without needing API keys or authentication.
- **Filtering**: Specifically targets highly liquid stablecoins (USDC, USDT, DAI) and ETH variants across major chains (Ethereum, Base, Arbitrum).
- **Protocol Comparison**: Compares rates between Aave V3, Compound V3, Morpho, and Spark.
- **Spread Analysis**: Highlights the difference between the best and worst yields for the same asset.
- **CSV Export**: Automatically neatly formats and saves all filtered data into `yield_data.csv` for further spreadsheet analysis.

## Requirements

Ensure you have Python 3 installed. You can install the required dependencies using `pip`:

```bash
pip install pandas requests tabulate
```

## Usage

Simply run the script from your terminal:

```bash
python yield_scanner.py
```

### Example Output Preview

1. **Best Yield Opportunities**: Prints the top 10 highest-yielding pools.
2. **Spread Analysis**: Checks the maximum and minimum APY for each distinct asset, highlighting where you might want to rebalance your holdings.
3. **APY by Protocol**: Shows at a glance which protocol is currently offering the best average returns.
4. **CSV Backup**: Generates `yield_data.csv` containing every captured datapoint.

## Customization
If you want to track different protocols, chains, or assets, simply edit the configuration variables at the top of `yield_scanner.py`:
```python
TARGET_PROTOCOLS = ["aave-v3", "compound-v3", "morpho", "spark"]
TARGET_CHAINS = ["Ethereum", "Base", "Arbitrum"]
# Adjust `is_relevant_asset` and `has_decent_tvl` inside the `filter_pools` function
```
