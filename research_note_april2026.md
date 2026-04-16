# DeFi Yield Research Note - April 2026

**Date:** April 16, 2026  
**Focus:** Stablecoin Yield Volatility and Capital Efficiency

## Executive Summary
Analysis of current market data reveals a stark contrast between established "systemic" protocols like Compound and more aggressive yield-optimization layers like Morpho and Sparklend. While high-yield opportunities exist (reaching 4.12% - 5.21%), they often come at the cost of significantly lower liquidity and higher volatility.

## 1. Protocol Stability Analysis: Compound vs. Morpho
A comparison of USDC yields across protocols shows why **Compound V3** is considered the "gold standard" for stability:

| Protocol | APY (%) | 30d Avg APY | Volatility | Sharpe Ratio |
| :--- | :--- | :--- | :--- | :--- |
| **Compound V3 (Ethereum)** | 2.65% | 2.58% | **0.06** | **43.0** |
| **Morpho V1 (Base - Steak)** | 3.87% | 3.86% | 0.28 | 13.79 |
| **Morpho V1 (Ethereum - Steak)**| 2.43% | 2.76% | 0.78 | 3.54 |

### Why Compound is more stable:
1. **Single-Collateral Model**: Compound V3 (Comet) uses a "base asset" (USDC) with specific collateral types, reducing cross-asset contagion and utilization spikes.
2. **Institutional Trust**: $111M+ TVL in this specific pool with a TVL Score of 10/10.
3. **Reward Mechanics**: Morpho yields often rely on dynamic rebalancing or reward abstractions (MetaMorpho) which, while higher on average, react much more aggressively to market sentiment shifts, leading to ~5x - 13x higher volatility than Compound.

## 2. Investment Case Study: Rebalancing $100k USDC
**Scenario:** Moving $100,000 from Aave V3 (Arbitrum) to Sparklend (Ethereum).

### The Math:
- **Baseline (Aave V3):** 1.63% APY = **$1,630/year**
- **Target (Sparklend):** 4.12% APY = **$4,120/year**
- **Net Gain:** **+$2,490/year**

### The Tradeoffs:
> [!CAUTION]
> Yield is never free. The move from Aave to Sparklend involves serious risk considerations.

- **Trust Degradation**: Moving from a TVL Score of **9** (Aave) to **3** (Sparklend). This indicates much lower confidence in the protocol's safety or track record.
- **Liquidity Risk**: Aave's pool has **$93.3M** in liquidity. Sparklend has only **$1.9M**.
    - Your $100k would represent **5.2%** of the entire Sparklend pool.
    - Large deposits in small pools typically "crush" the yield (bringing it down as soon as you deposit).
- **Network Overhead**: Moving from Arbitrum (L2) to Ethereum (L1) increases your management costs (gas) by orders of magnitude.

## Conclusion
For large capital ($100k+), the stability and liquidity of Compound or Aave V3 remain the superior choice despite lower nominal yields. Sparklend's 4.12% is likely unsustainable for a position of this size due to pool depth constraints.
