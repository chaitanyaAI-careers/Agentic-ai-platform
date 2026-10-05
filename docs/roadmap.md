# Engineering Roadmap

## Verified Broader Private Implementation

- LangGraph Planner / Coder / Reviewer / Tester typed-state workflows
- conditional routing and task decomposition
- human approval queues and execution authorization
- policy and risk gates
- sandboxed / controlled execution
- MCP server/client interoperability with JSON-RPC and schema-aware handling
- PostgreSQL durable workflow state
- checkpoint, pause/resume, rollback, and recovery behavior
- LiteLLM model routing across hosted and local providers
- Redis background workers
- Kafka event streams
- OAuth2/OIDC/JWT identity patterns with RBAC and SSO-ready boundaries
- Langfuse / OpenTelemetry tracing
- FastAPI/Pydantic service interfaces
- Dockerized services
- Kubernetes / Helm deployment patterns
- Terraform-managed AWS infrastructure
- audit logging and execution lineage
- evaluation infrastructure and broad regression coverage

## Publicly Verifiable Showcase

- role routing
- approval and risk controls
- controlled-execution boundaries
- provider abstraction
- deterministic evaluation
- automated tests
- GitHub Actions CI

## Measured Evidence

- 94.8% agent task completion across evaluation suites
- 3,950+ passing regression tests in the broader private implementation

## Current Evidence-Building Priorities

- additional load and concurrency measurements
- explicit SLO / error-budget reporting
- recovery-time and fault-injection measurements
- autoscaling and infrastructure-efficiency evidence
- additional public-safe implementation samples where proprietary boundaries allow

## Evidence Rule

A capability is labeled public only when directly inspectable in this repository. Broader implemented capabilities remain labeled private, and future measurements remain future evidence until reproduced.
