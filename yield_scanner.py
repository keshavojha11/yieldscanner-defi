import requests
import pandas as pd
from tabulate import tabulate
from datetime import datetime

# Protocols we care about
TARGET_PROTOCOLS = ["aave-v3", "compound-v3", "morpho", "spark"]
TARGET_CHAINS = ["Ethereum", "Base", "Arbitrum"]

def fetch_yields():
    print("Fetching live yield data from DeFiLlama...")
    url = "https://yields.llama.fi/pools"
    response = requests.get(url)
    data = response.json()
    return data["data"]

def filter_pools(pools):
    results = []
    for pool in pools:
        protocol = pool.get("project", "").lower()
        chain = pool.get("chain", "")
        symbol = pool.get("symbol", "")
        apy = pool.get("apy", 0)
        tvl = pool.get("tvlUsd", 0)

        # Only stablecoins and ETH, filter by protocol and chain
        is_target_protocol = any(t in protocol for t in TARGET_PROTOCOLS)
        is_target_chain = chain in TARGET_CHAINS
        is_relevant_asset = any(s in symbol.upper() for s in ["USDC", "USDT", "DAI", "ETH", "WETH"])
        has_decent_tvl = tvl > 1_000_000  # at least $1M TVL

        if is_target_protocol and is_target_chain and is_relevant_asset and has_decent_tvl:
            results.append({
                "Protocol": pool.get("project"),
                "Chain": chain,
                "Asset": symbol,
                "APY (%)": round(apy, 2),
                "TVL ($M)": round(tvl / 1_000_000, 1),
            })

    return results

def analyze_spreads(df):
    print("\n--- BEST YIELD OPPORTUNITIES ---")
    top = df.sort_values("APY (%)", ascending=False).head(10)
    print(tabulate(top, headers="keys", tablefmt="rounded_outline", showindex=False))

    print("\n--- SPREAD ANALYSIS (Max - Min APY per Asset) ---")
    spread = df.groupby("Asset")["APY (%)"].agg(["max", "min"])
    spread["spread"] = (spread["max"] - spread["min"]).round(2)
    spread = spread.sort_values("spread", ascending=False)
    print(tabulate(spread, headers=["Asset", "Max APY", "Min APY", "Spread (%)"], tablefmt="rounded_outline"))

    print("\n--- APY BY PROTOCOL ---")
    proto = df.groupby("Protocol")["APY (%)"].mean().round(2).sort_values(ascending=False)
    print(tabulate(proto.reset_index(), headers=["Protocol", "Avg APY (%)"], tablefmt="rounded_outline", showindex=False))

def main():
    print(f"\n=== DeFi Yield Scanner ===")
    print(f"Run time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    pools = fetch_yields()
    filtered = filter_pools(pools)

    if not filtered:
        print("No pools found. Check filters.")
        return

    df = pd.DataFrame(filtered)
    analyze_spreads(df)
    df.to_csv("yield_data.csv", index=False)
    print(f"\nData saved to yield_data.csv ({len(df)} pools)")

if __name__ == "__main__":
    main()