from dataclasses import dataclass
from typing import Callable

from showcase.governance.policy_gate_example import PolicyDecision


@dataclass(frozen=True)
class ExecutionResult:
    executed: bool
    message: str


def controlled_execute(
    action: Callable[[], None],
    decision: PolicyDecision,
    *,
    human_approved: bool = False,
) -> ExecutionResult:
    if not decision.allowed:
        return ExecutionResult(
            executed=False,
            message="Blocked by policy.",
        )

    if decision.requires_human_approval and not human_approved:
        return ExecutionResult(
            executed=False,
            message="Waiting for human approval.",
        )

    action()

    return ExecutionResult(
        executed=True,
        message="Execution completed.",
    )
