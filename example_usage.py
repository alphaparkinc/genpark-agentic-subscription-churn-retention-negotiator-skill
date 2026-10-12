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
