@echo off
echo ================================================
echo   CogniTest Android - Appium E2E Test Runner
echo ================================================
echo.

REM Create reports directory
if not exist "reports" mkdir reports
if not exist "reports\screenshots" mkdir reports\screenshots

echo [1/4] Installing dependencies...
pip install -r requirements.txt --quiet

echo [2/4] Checking Appium server...
curl -s http://127.0.0.1:4723/status > nul 2>&1
if errorlevel 1 (
    echo    Appium server not running! Start it with: appium
    echo    Then re-run this script.
    pause
    exit /b 1
)
echo    Appium server is running.

echo [3/4] Checking device connection...
adb devices

echo [4/4] Running 300 test cases...
echo.

set TEST_EMAIL=test@cognitest.com
set TEST_PASSWORD=Test@1234
set BACKEND_URL=http://10.35.23.113:3001

pytest tests/ ^
    -v ^
    --html=reports/pytest_report.html ^
    --self-contained-html ^
    --tb=short ^
    --reruns=1 ^
    --reruns-delay=2 ^
    2>&1 | tee reports/test_output.log

echo.
echo ================================================
echo   Test run complete!
echo   Excel Report : reports\cognitest_e2e_report.xlsx
echo   HTML Report  : reports\pytest_report.html
echo   Screenshots  : reports\screenshots\
echo ================================================
pause
