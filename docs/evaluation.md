# Evaluation

Evaluation is treated as an engineering control rather than assuming that an agent or model output is correct.

Representative evaluation areas include:

- task-routing correctness
- policy behavior
- approval behavior
- execution outcomes
- reviewer and tester outcomes
- regression detection
- model and tool behavior
- checkpoint / recovery behavior
- end-to-end task completion

## Public Showcase

The public repository includes a small deterministic evaluation example so behavior can be inspected without exposing the broader private platform.

## Verified Broader Evaluation Evidence

The broader private implementation has produced:

- **94.8% agent task completion** across evaluation suites
- **3,950+ passing regression tests**

These figures describe the broader private implementation, not the smaller public showcase.

Current evidence-building work focuses on additional load, concurrency, recovery, and operational SLO measurements rather than treating evaluation as an informal visual check.
