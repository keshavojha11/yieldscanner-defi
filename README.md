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

---

## My Take (April 2026 Analysis)

> [!NOTE]
> For a more detailed breakdown, see the [Research Note - April 2026](research_note_april2026.md).

### 1. Stability: Compound vs. Morpho
**Q: Why does Compound USDC have such stable yield compared to Morpho's higher numbers?**

Compound V3 (Comet) utilizes a **conservative single-collateral model** that prioritizes institutional-grade stability. Its volatility (0.06) is exceptionally low because its utilization curves are tuned for steady state rather than aggressive optimization. **Morpho**, by contrast, is often built as an abstraction layer (like MetaMorpho vaults) that aggressively rebalances to capture the highest possible yield. While this leads to higher APYs, it also causes significant volatility (up to 13x higher than Compound) as it reacts to every minor shift in market liquidity and borrower demand.

### 2. Strategy: The $100,000 Rebalance
**Q: What's the tradeoff of moving $100k from Aave (1.63%) to a higher yield like 4.12%?**

*   **Extra Income:** You would earn an additional **$2,490 per year**.
*   **The Big Tradeoff:** You are trading **Security for Yield**. 
    *   **Trust:** Moving from Aave (TVL Score 9) to a smaller protocol like Sparklend (TVL Score 3) increases smart contract risk significantly.
    *   **Liquidity:** Aave's $93M pool easily absorbs $100k. A $1.9M pool (like the 4.12% target) would be heavily impacted by your deposit; $100k is >5% of the total pool, meaning the APY would likely drop as soon as you enter, and exiting quickly might be harder.

