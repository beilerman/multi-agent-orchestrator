Execute a multi-agent orchestration workflow for the following task: $ARGUMENTS

Follow these steps exactly:

## Step 1: Architect
Read `orchestrator/architect.md` for your role instructions.
Analyze the task and create a detailed technical plan.
Write the plan to `orchestrator/state/plan.md`.

## Step 2: Implementer
Read `orchestrator/implementer.md` for your role instructions.
Read the plan from `orchestrator/state/plan.md`.
Write or edit the project source code as specified.
Log your implementation notes to `orchestrator/state/impl-notes.md`.

## Step 3: Tester
Read `orchestrator/tester.md` for your role instructions.
Read the plan and implementation notes.
Write tests, run them, and log results to `orchestrator/state/test-report.md`.

## Step 4: Synthesize
Review all artifacts in `orchestrator/state/`.
If tests failed, re-run Steps 2-3 to fix issues.
Once all tests pass, summarize the results for the user.
