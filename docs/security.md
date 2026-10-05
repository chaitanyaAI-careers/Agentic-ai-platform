# Security

Agentic AI Platform uses explicit execution and identity boundaries around sensitive operations.

Representative controls include:

- human approval for sensitive actions
- policy and risk evaluation before execution
- restricted tool permissions
- sandboxed / controlled execution
- authorization-aware MCP boundaries
- audit logging and execution lineage
- rollback and recovery controls
- durable workflow state
- model-provider abstraction
- secrets and identity boundaries

## Verified Broader Private Controls

The broader private implementation includes OAuth2/OIDC/JWT identity patterns, RBAC and SSO-ready integration boundaries, AWS IAM / Secrets Manager patterns, trace propagation, and controlled service-to-service execution.

These controls are maintained outside the recruiter-safe public showcase unless corresponding implementation is directly inspectable here.

No credentials, customer data, private runtime state, or proprietary execution internals are included in this public repository.
