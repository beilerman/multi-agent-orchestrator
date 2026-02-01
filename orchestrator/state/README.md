# Orchestrator State Directory

This directory is used for inter-agent communication. Agents read and write files here to pass artifacts between workflow phases.

## Files

- `plan.md` — Written by the **Architect** agent. Contains the technical plan and acceptance criteria.
- `impl-notes.md` — Written by the **Implementer** agent. Contains implementation decisions and notes.
- `test-report.md` — Written by the **Tester** agent. Contains test results and recommendations.

## Rules

- Each agent should only write to its designated output file(s).
- Agents should read (but not modify) other agents' files.
- The Leader orchestrator coordinates the order of execution.
