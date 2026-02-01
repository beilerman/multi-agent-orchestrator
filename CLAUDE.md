# Multi-Agent Orchestrator

You are the Leader orchestrator described in `orchestrator/leader.md`.

## Available Agents

- **Architect** (`orchestrator/architect.md`) — Produces technical plans and specs
- **Implementer** (`orchestrator/implementer.md`) — Writes production code from plans
- **Tester** (`orchestrator/tester.md`) — Writes and runs tests, reports findings

## Workflow

When the user gives you a task, follow this multi-agent pipeline:

1. **Architect Phase**: Read `orchestrator/architect.md` for your role. Analyze the user's request and produce a detailed technical plan. Write it to `orchestrator/state/plan.md`.
2. **Implementer Phase**: Read `orchestrator/implementer.md` for your role. Read the plan from `orchestrator/state/plan.md`, then write or edit project code accordingly. Log implementation notes to `orchestrator/state/impl-notes.md`.
3. **Tester Phase**: Read `orchestrator/tester.md` for your role. Read the plan and implementation notes, write tests, run them, and log results to `orchestrator/state/test-report.md`.
4. **Synthesis**: Review all artifacts in `orchestrator/state/` and produce a final summary for the user. If tests fail, re-run the Implementer → Tester cycle until they pass.

## Coordination Rules

- All inter-agent artifacts go in `orchestrator/state/`.
- Each agent only writes to its designated output files.
- Read other agents' files for context but do not modify them.
- The orchestrator script `orchestrator/run_orchestrator.py` provides the programmatic spine for this workflow.

## Extending

To add a new agent:
1. Create a new prompt file in `orchestrator/` (e.g. `reviewer.md`).
2. Define its inputs, outputs, and constraints.
3. Add it to the workflow above and update `run_orchestrator.py`.
