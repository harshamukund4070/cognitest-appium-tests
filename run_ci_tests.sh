#!/bin/bash
set -e

echo "=== Emulator Boot Status ==="
adb wait-for-device || true
adb shell input keyevent 82 || true

# Install APK if present
if [ -f "app-debug.apk" ] && [ -s "app-debug.apk" ]; then
  echo "=== Installing CogniTest APK ==="
  adb install -r app-debug.apk || true
else
  echo "=== Skipping APK installation (file missing or empty) ==="
fi

# Create reports directories
mkdir -p reports/screenshots

# Set APK path in config
export APK_PATH=$(pwd)/app-debug.apk

# Set local backend coordinates for execution
export BACKEND_URL=http://localhost:3001
export API_BASE_URL=http://localhost:3001

# Set PythonPath to workspace root to resolve module imports (like utils)
export PYTHONPATH=$(pwd)

# Clear existing logs
> reports/test_output.log

echo "=== Running Python Vulnerability Check (Bandit SAST) ==="
bandit -r . -x "./venv,./.git,./.github" -f txt -o reports/sast_vulnerabilities.txt || true
echo "Security scan complete. Summary saved to reports/sast_vulnerabilities.txt."

# ── 1. Backend REST API Tests (100 tests) ───────────────────
echo "=== Running REST API Verification Suite ==="
export EXCEL_REPORT_PATH=$(pwd)/reports/api_e2e_report.xlsx
pytest api_tests/tests \
  --html=reports/api_report.html \
  --self-contained-html \
  -v --tb=short \
  -o "log_cli=true" \
  2>&1 | tee -a reports/test_output.log || true

# ── 2. Web Frontend E2E (Selenium - 300 tests) ───────────────
echo "=== Running Web Frontend E2E (Selenium) Suite ==="
export EXCEL_REPORT_PATH=$(pwd)/reports/selenium_e2e_report.xlsx
pytest selenium_tests/tests \
  --html=reports/selenium_report.html \
  --self-contained-html \
  -v --tb=short \
  -o "log_cli=true" \
  2>&1 | tee -a reports/test_output.log || true

# ── 3. Android Mobile E2E (Appium - 300 tests) ───────────────
echo "=== Running Android Mobile E2E (Appium) Suite ==="
export EXCEL_REPORT_PATH=$(pwd)/reports/appium_e2e_report.xlsx
pytest appium_tests/tests \
  --html=reports/appium_report.html \
  --self-contained-html \
  -v --tb=short \
  -o "log_cli=true" \
  2>&1 | tee -a reports/test_output.log || true

echo "=== Running Baseline System Load Testing (100 VUs x 1 Min) ==="
python3 load_tests/run_load_test.py || true

echo "=== E2E Test Suite Run Complete ==="
