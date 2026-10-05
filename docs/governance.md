# Governance

The platform is designed so that an AI recommendation does not automatically authorize an action.

## Publicly Demonstrated Controls

The recruiter-safe showcase demonstrates the separation between:

- agent proposal
- policy / risk evaluation
- human approval
- controlled execution
- deterministic evaluation

The public policy-gate example demonstrates this separation without exposing the complete governance engine.

## Verified Broader Private Governance

The broader private implementation includes:

- explicit planning / authorization / execution / validation boundaries
- risk classification and policy gates
- human-in-the-loop approvals
- sandboxed execution boundaries
- authorization-aware MCP invocation
- OAuth2/OIDC/JWT identity patterns
- RBAC and SSO-ready integration boundaries
- execution lineage and audit records
- checkpointed state, rollback, and recovery controls
- secrets and least-authority patterns across model, tool, and service boundaries

The key design rule is that model output can propose actions but does not become authoritative application state or permission by itself.

Public and private evidence remain intentionally separated so governance claims map to their actual implementation surface.
