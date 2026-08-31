from showcase.governance.policy_gate_example import RiskLevel, evaluate_action


def test_low_risk_read_only_action_needs_no_approval():
    decision = evaluate_action(RiskLevel.LOW)

    assert decision.allowed is True
    assert decision.requires_human_approval is False


def test_high_risk_action_requires_human_approval():
    decision = evaluate_action(RiskLevel.HIGH)

    assert decision.allowed is True
    assert decision.requires_human_approval is True
