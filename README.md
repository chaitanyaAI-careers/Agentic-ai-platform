# Agentic AI Platform

**Governed Agentic AI · AI Platform Engineering · Human-in-the-Loop · Controlled Execution**

Agentic AI Platform explores controlled, observable, and governable AI-agent execution.

This repository is a curated public engineering showcase. The complete private development implementation is maintained separately.

## Architecture

PRD / User Goal → Planning → Task Decomposition → Agent Routing → Policy / Risk Evaluation → Human Approval → Controlled Execution → Sandbox / Validation → Review + Testing → Audit / Rollback / Completion

## Engineering Areas

- Multi-agent Planner / Coder / Reviewer / Tester workflows
- Task decomposition and routing
- Human-in-the-loop approvals
- Policy and execution gates
- Controlled and sandbox-oriented execution
- Auditability and rollback concepts
- LLM provider abstraction and model routing
- Evaluation and reliability engineering

## Public Showcase

The showcase directory contains simplified standalone examples of routing, governance, approvals, execution control, LLM abstraction, and evaluation.

The examples demonstrate engineering concepts without exposing the complete proprietary implementation.

## Implemented in the Private Development Project

- Multi-role agent workflows and work queues
- Human approval queues and execution authorization
- Policy gates and sandbox validation
- Controlled execution
- Audit logging and execution lineage
- Rollback/checkpoint workflows
- Memory abstractions
- Local LLM routing with Ollama
- Evaluation infrastructure
- FastAPI interfaces and operator workflows

## Currently Developing / Strengthening

- Real MCP server/client interoperability
- MCP discovery and schema validation
- Authorization-aware MCP invocation
- PostgreSQL durable workflow state
- Pause / persist / restart / resume
- Idempotent workflow execution
- Docker / Docker Compose
- Broader private-platform CI and release automation
- OpenTelemetry
- Structured logs and metrics
- End-to-end integration testing
- Agent evaluation benchmarks
- LangGraph comparison baseline

## Later-Stage Evaluation

- Kubernetes
- Infrastructure-as-code
- Broader distributed-agent interoperability

## Testing

This showcase includes representative automated tests and is verified through GitHub Actions CI. The private implementation maintains a substantially broader test suite.

## Intellectual Property

Only portfolio-safe representative material is included here. The complete commercial/private implementation and proprietary platform code are not published.

See NOTICE.md.
