#!/bin/bash
set -e

echo "=== Emulator Boot Status ==="
adb wait-for-device
adb shell input keyevent 82

# Install APK if present
if [ -f "app-debug.apk" ] && [ -s "app-debug.apk" ]; then
  echo "=== Installing CogniTest APK ==="
  adb install -r app-debug.apk
else
  echo "=== Skipping APK installation (file missing or empty) ==="
fi

# Create reports directories
mkdir -p reports/screenshots

# Set APK path in config
export APK_PATH=$(pwd)/app-debug.apk

echo "=== Running Appium Test Suite ==="
if [ -n "$1" ]; then
  pytest "tests/$1" \
    --html=reports/pytest_report.html \
    --self-contained-html \
    -v --tb=short \
    --reruns=1 --reruns-delay=3 \
    -o "log_cli=true" \
    2>&1 | tee reports/test_output.log || true
else
  pytest tests/ \
    --html=reports/pytest_report.html \
    --self-contained-html \
    -v --tb=short \
    --reruns=1 --reruns-delay=3 \
    -o "log_cli=true" \
    2>&1 | tee reports/test_output.log || true
fi

echo "=== E2E Test Suite Run Complete ==="
