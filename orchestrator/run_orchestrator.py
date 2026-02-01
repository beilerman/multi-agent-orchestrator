import os
from pathlib import Path

STATE_DIR = Path("orchestrator/state")
STATE_DIR.mkdir(parents=True, exist_ok=True)

PLAN_FILE = STATE_DIR / "plan.md"
IMPL_FILE = STATE_DIR / "impl-notes.md"
TEST_FILE = STATE_DIR / "test-report.md"


def read(path: Path) -> str:
    """Read a file if it exists, otherwise return empty string."""
    return path.read_text() if path.exists() else ""


def write(path: Path, content: str) -> None:
    """Write content to a file."""
    path.write_text(content)


def main(user_request: str):
    """
    Multi-agent orchestrator entrypoint.

    The Leader agent will:
    - Call run_architect, run_implementer, run_tester
    - Decide when each is needed
    - Synthesize the final result for the user
    """
    print(f"User request: {user_request}\n")

    # Leader: decide workflow; default = simple pipeline
    run_architect(user_request)
    run_implementer()
    run_tester()
    final_summary = synthesize_result(user_request)

    print("\n=== FINAL SUMMARY ===\n")
    print(final_summary)


def run_architect(user_request: str):
    """
    Invoked by the Leader.

    In Claude Code, select this function and ask the Architect sub-agent
    to implement it according to orchestrator/architect.md.
    """
    # Placeholder: Architect agent will overwrite this logic
    write(PLAN_FILE, f"# Plan\n\nUser request:\n{user_request}\n")


def run_implementer():
    """
    Implementer reads PLAN_FILE and edits project code.
    It can also log implementation details to IMPL_FILE.
    """
    plan = read(PLAN_FILE)
    if not plan:
        raise RuntimeError("No plan found; Architect must run first.")
    # Placeholder: Implementer agent will replace this
    write(IMPL_FILE, f"# Implementation Notes\n\nUsed plan:\n{plan}\n")


def run_tester():
    """
    Tester writes tests, runs them, and logs findings.
    """
    impl_notes = read(IMPL_FILE)
    # Placeholder: Tester agent will replace this
    write(TEST_FILE, f"# Test Report\n\nImplementation notes:\n{impl_notes}\n")


def synthesize_result(user_request: str) -> str:
    """
    Leader reads plan, impl, and test artifacts and produces
    a final user-facing summary.

    In practice, have the Leader agent rewrite this function
    or its return value.
    """
    plan = read(PLAN_FILE)
    impl = read(IMPL_FILE)
    test = read(TEST_FILE)

    return (
        f"Request: {user_request}\n\n"
        "Plan:\n" + plan + "\n\n"
        "Implementation summary:\n" + impl + "\n\n"
        "Test report:\n" + test + "\n"
    )


if __name__ == "__main__":
    main("Build a small FastAPI service with auth and tests")
