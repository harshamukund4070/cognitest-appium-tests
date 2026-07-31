import time
import os
import pytest
from utils.excel_reporter import reporter

# ── Auto-record each test result ──────────────────────────────────────────────
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report  = outcome.get_result()

    if report.when == "call":
        start     = item._start_time if hasattr(item, "_start_time") else 0
        duration  = time.time() - start

        # Map pytest outcome → PASS/FAIL/SKIP
        if report.passed:
            status = "PASS"
            error  = ""
        elif report.failed:
            status = "FAIL"
            error  = str(report.longrepr)[:300] if report.longrepr else ""
        else:
            status = "SKIP"
            error  = ""

        module    = item.module.__name__ if hasattr(item, "module") else "Unknown"
        test_id   = len(reporter.results) + 1
        steps     = item.function.__doc__ or ""

        reporter.record(
            test_id=test_id,
            module=module,
            test_name=item.name,
            status=status,
            duration=duration,
            error_msg=error,
            steps=steps,
        )

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    item._start_time = time.time()

# ── Save Excel after entire session ───────────────────────────────────────────
def pytest_sessionfinish(session, exitstatus):
    reporter.save()
