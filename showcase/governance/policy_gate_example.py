from dataclasses import dataclass
from enum import Enum


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass(frozen=True)
class PolicyDecision:
    allowed: bool
    requires_human_approval: bool
    reason: str


def evaluate_action(
    risk: RiskLevel,
    *,
    modifies_files: bool = False,
    external_effect: bool = False,
) -> PolicyDecision:
    if risk is RiskLevel.HIGH or external_effect:
        return PolicyDecision(
            allowed=True,
            requires_human_approval=True,
            reason="Sensitive action requires explicit human approval.",
        )

    if risk is RiskLevel.MEDIUM or modifies_files:
        return PolicyDecision(
            allowed=True,
            requires_human_approval=True,
            reason="State-changing action requires review.",
        )

    return PolicyDecision(
        allowed=True,
        requires_human_approval=False,
        reason="Low-risk read-only action.",
    )
