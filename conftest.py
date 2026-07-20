"""
conftest.py — pytest fixtures shared across the entire test suite.
Handles driver lifecycle, test result capture, and Excel report generation.
"""
import time
import pytest
from appium import webdriver
from appium.options import UiAutomator2Options
from config.config import APPIUM_SERVER_URL, DESIRED_CAPS
from utils.excel_reporter import reporter


# ── Driver fixture (function-scoped = fresh per test) ─────────────────────────
@pytest.fixture(scope="function")
def driver(request):
    options = UiAutomator2Options()
    for key, value in DESIRED_CAPS.items():
        clean_key = key.replace("appium:", "")
        setattr(options, clean_key, value)
    options.platform_name = DESIRED_CAPS["platformName"]

    drv = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    drv.implicitly_wait(15)
    yield drv
    drv.quit()


# ── Session-scoped driver (shared across module) ───────────────────────────────
@pytest.fixture(scope="module")
def driver_module(request):
    options = UiAutomator2Options()
    for key, value in DESIRED_CAPS.items():
        clean_key = key.replace("appium:", "")
        setattr(options, clean_key, value)
    options.platform_name = DESIRED_CAPS["platformName"]

    drv = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    drv.implicitly_wait(15)
    yield drv
    drv.quit()


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
