"""MCP Server for Agentic Subscription Churn Retention Negotiator."""
import sys
import json
import time
from client import AgenticSubscriptionChurnRetentionNegotiator

negotiator = AgenticSubscriptionChurnRetentionNegotiator()

def handle_call_tool(params):
    name = params.get("name")
    args = params.get("arguments", {})
    if name != "negotiate_subscription_retention":
        raise ValueError(f"Unknown tool: {name}")

    action = args.get("action", "negotiate_retention_offer")
    profile = args.get("subscriber_profile", {})

    if action == "evaluate_churn_risk":
        return negotiator.evaluate_churn_risk(profile)
    elif action == "negotiate_retention_offer":
        return negotiator.negotiate_retention_offer(profile)
    else:
        raise ValueError(f"Invalid action: {action}")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print("Running self-test...")
        prof = {
            "user_id": "SUB-VIP-99",
            "monthly_arpu_usd": 99.0,
            "tenure_months": 14,
            "active_days_30d": 4,
            "cancellation_reason": "TOO_EXPENSIVE_FOR_BUDGET"
        }
        res = negotiator.negotiate_retention_offer(prof)
        assert res["risk_assessment"]["subscriber_tier"] == "HIGH_VALUE_VIP"
        assert "LOYALTY_DISCOUNT" in res["selected_retention_strategy"]
        assert res["expected_net_ltv_preserved_usd"] > 0
        print("Self-test PASSED!")
        sys.exit(0)

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            msg_id = req.get("id")
            method = req.get("method")
            if method == "initialize":
                resp = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {
                        "protocolVersion": "2024-11-05",
                        "serverInfo": {"name": "AgenticSubscriptionChurnRetentionNegotiator", "version": "1.0.0"},
                        "capabilities": {"tools": {}}
                    }
                }
            elif method == "tools/list":
                resp = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {
                        "tools": [{
                            "name": "negotiate_subscription_retention",
                            "description": "Compute subscriber churn risk and LTV, diagnose cancellation reason, and synthesize personalized retention counter-offers.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "action": {"type": "string", "enum": ["evaluate_churn_risk", "negotiate_retention_offer"]},
                                    "subscriber_profile": {"type": "object"}
                                },
                                "required": ["action"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                res = handle_call_tool(req.get("params", {}))
                resp = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
                }
            else:
                resp = {"jsonrpc": "2.0", "id": msg_id, "result": {}}
            print(json.dumps(resp), flush=True)
        except Exception as e:
            err_resp = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err_resp), flush=True)

if __name__ == "__main__":
    main()
