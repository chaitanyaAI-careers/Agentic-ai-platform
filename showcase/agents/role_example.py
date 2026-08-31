from dataclasses import dataclass
from enum import Enum


class AgentRole(str, Enum):
    PLANNER = "planner"
    CODER = "coder"
    REVIEWER = "reviewer"
    TESTER = "tester"


@dataclass(frozen=True)
class AgentTask:
    task_id: str
    description: str
    requested_role: AgentRole | None = None


def route_task(task: AgentTask) -> AgentRole:
    if task.requested_role:
        return task.requested_role

    text = task.description.lower()

    if any(word in text for word in ("test", "pytest", "verify")):
        return AgentRole.TESTER

    if any(word in text for word in ("review", "audit", "inspect")):
        return AgentRole.REVIEWER

    if any(word in text for word in ("implement", "code", "build")):
        return AgentRole.CODER

    return AgentRole.PLANNER
