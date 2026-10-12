# genpark-agentic-subscription-churn-retention-negotiator-skill

[![GenPark AI](https://img.shields.io/badge/GenPark_AI-www.genpark.ai-blue.svg)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark_Company_92955550-0077B5.svg)](https://www.linkedin.com/company/92955550)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Dependencies](https://img.shields.io/badge/dependencies-0%20(Pure%20Stdlib)-brightgreen.svg)](requirements.txt)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-purple.svg)](mcp_server.py)

Autonomous Subscription Churn Prediction & Dynamic Retention Negotiator. Evaluates subscriber telemetry (usage drop-off, support friction, billing price sensitivity, tenure LTV), diagnoses cancellation root cause, and dynamically negotiates margin-optimal save offers (subscription pause, tier right-sizing, or loyalty credit).

---

## 🌐 Official GenPark AI Ecosystem Links

- **GenPark Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Official Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) ([https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550))

---

## 🌟 Key Features

- **100% Zero External Dependencies**: Runs entirely on the Python 3.9+ standard library.
- **Model Context Protocol (MCP) Standard**: Native support for JSON-RPC 2.0 `initialize`, `tools/list`, and `tools/call`.
- **Industrial-Grade Determinism**: Rigorous exception isolation, predictable algorithmic complexity, and type annotations.
- **Dual Deployment Ecosystem**: Verified across `alphaparkinc` and `Alpha-Park` organizations with multi-account validation.

---

## 🚀 Quick Start

### 1. Direct Python SDK Usage

```python
"""Example usage for AgenticSubscriptionChurnRetentionNegotiator."""
import sys
import json
from client import AgenticSubscriptionChurnRetentionNegotiator

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("=== Agentic SaaS & Commerce Subscription Churn Retention Negotiator Demo ===")
    negotiator = AgenticSubscriptionChurnRetentionNegotiator()

    sub_profile = {
        "user_id": "USR-STRIPE-8821",
        "monthly_arpu_usd": 79.00,
        "tenure_months": 10,
        "active_days_30d": 3,
        "unresolved_tickets": 0,
        "cancellation_reason": "TOO_EXPENSIVE_RIGHT_NOW"
    }

    print("\n--- 1. Evaluating Churn Probability & LTV at Risk ---")
    risk = negotiator.evaluate_churn_risk(sub_profile)
    print(f"Tier: {risk['subscriber_tier']} | LTV at Risk: ${risk['ltv_at_risk_usd']:.2f} | Churn Prob: {risk['churn_probability']*100:.0f}%")

    print("\n--- 2. Negotiating Margin-Optimal Save Counter-Offer ---")
    offer = negotiator.negotiate_retention_offer(sub_profile)
    print(f"Strategy: {offer['selected_retention_strategy']}")
    print(f"Offer Copy: '{offer['offer_headline']}'")
    print(f"Concession Cost: ${offer['concession_investment_usd']:.2f} -> Net LTV Preserved: ${offer['expected_net_ltv_preserved_usd']:.2f} (ROI: {offer['roi_multiple']}x)")

if __name__ == "__main__":
    main()

```

### 2. Run as Model Context Protocol (MCP) Server

Start standard JSON-RPC 2.0 server over `stdio`:

```bash
python mcp_server.py
```

Execute embedded test harness:

```bash
python mcp_server.py --test
```

---

## 🛠️ MCP Tool Specification

Inspect [`skill.json`](skill.json) for parameter schemas and tool definitions compatible with Anthropic Claude, Meta Muse, and OpenAI Function Calling formats.

---

## 📜 License & Community

Licensed under the [MIT License](LICENSE). Copyright © 2026 [GenPark AI](https://www.genpark.ai).
Follow us on LinkedIn: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) | [https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550)
