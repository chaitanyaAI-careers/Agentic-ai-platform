# Architecture

Agentic AI Platform follows a control-plane-first architecture for governed agent execution.

## Core Flow

PRD / Goal → Planning → Task Decomposition → Agent Routing → Policy Evaluation → Human Approval → Controlled Tool / MCP Execution → Validation → Review / Testing → Evaluation → Audit / Recovery / Completion

## Design Principles

- Separate agent reasoning from execution authorization.
- Require explicit controls around state-changing actions.
- Keep policy evaluation independent from model output.
- Preserve traceability across execution lifecycles.
- Treat review, testing, rollback, checkpointing, and recovery as first-class capabilities.
- Support interchangeable model providers behind stable interfaces.
- Keep durable workflow state outside transient model context.
- Keep public evidence separate from broader private implementation.

## Evidence-Aware Architecture

### Public Showcase

The public repository demonstrates representative contracts for:

- role routing
- approval and risk controls
- controlled-execution boundaries
- provider abstraction
- deterministic evaluation
- automated tests and GitHub Actions CI

### Verified Broader Private Implementation

The separately maintained private implementation includes:

- LangGraph TypedDict state graphs across Planner / Coder / Reviewer / Tester roles
- conditional routing, durable checkpoints, graph interrupts, rollback, and recovery
- PostgreSQL-backed workflow state and persistent execution history
- custom MCP server/client interoperability using JSON-RPC and schema-aware tool/context handling
- sandboxed execution boundaries
- LiteLLM model routing across hosted and local providers
- Redis background workers and Kafka event streams
- OAuth2/OIDC/JWT identity patterns with RBAC and SSO-ready integration boundaries
- Langfuse/OpenTelemetry tracing
- Dockerized services, Kubernetes/Helm deployment patterns, Terraform, and AWS infrastructure

## Measured Evidence

- 94.8% agent task completion across evaluation suites
- 3,950+ passing regression tests in the broader private implementation

The public showcase intentionally represents a smaller recruiter-safe subset. The metrics and broader stack above are not presented as code directly contained in this repository.
