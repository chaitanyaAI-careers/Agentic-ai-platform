from dataclasses import dataclass
from enum import Enum


class ApprovalStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


@dataclass
class ApprovalRequest:
    request_id: str
    action: str
    reason: str
    status: ApprovalStatus = ApprovalStatus.PENDING


def approve(request: ApprovalRequest) -> ApprovalRequest:
    request.status = ApprovalStatus.APPROVED
    return request


def reject(request: ApprovalRequest) -> ApprovalRequest:
    request.status = ApprovalStatus.REJECTED
    return request
