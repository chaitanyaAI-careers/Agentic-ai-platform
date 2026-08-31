from showcase.execution.controlled_execution_example import controlled_execute
from showcase.governance.policy_gate_example import PolicyDecision


def test_execution_waits_for_required_approval():
    calls = []

    decision = PolicyDecision(
        allowed=True,
        requires_human_approval=True,
        reason="Approval required.",
    )

    result = controlled_execute(
        lambda: calls.append("executed"),
        decision,
    )

    assert result.executed is False
    assert calls == []


def test_execution_runs_after_approval():
    calls = []

    decision = PolicyDecision(
        allowed=True,
        requires_human_approval=True,
        reason="Approval required.",
    )

    result = controlled_execute(
        lambda: calls.append("executed"),
        decision,
        human_approved=True,
    )

    assert result.executed is True
    assert calls == ["executed"]
