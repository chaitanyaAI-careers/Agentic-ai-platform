from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class EvaluationCase:
    expected: str
    actual: str


@dataclass(frozen=True)
class EvaluationSummary:
    total: int
    passed: int
    pass_rate: float


def evaluate(cases: Iterable[EvaluationCase]) -> EvaluationSummary:
    items = list(cases)

    passed = sum(
        1
        for case in items
        if case.expected.strip().lower()
        == case.actual.strip().lower()
    )

    total = len(items)

    return EvaluationSummary(
        total=total,
        passed=passed,
        pass_rate=(passed / total) if total else 0.0,
    )
