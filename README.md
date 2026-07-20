# 🧠 CogniTest Android — Appium E2E Test Suite

[![Appium E2E Tests](https://github.com/YOUR_USERNAME/cognitest-appium-tests/actions/workflows/appium_e2e.yml/badge.svg)](https://github.com/YOUR_USERNAME/cognitest-appium-tests/actions/workflows/appium_e2e.yml)

> **300 end-to-end test cases** for the CogniTest Android application.  
> Reports auto-generated: **Excel Analysis** + **HTML Report** + **Screenshots**.

---

## 📁 Project Structure

```
appium-tests/
├── .github/
│   └── workflows/
│       └── appium_e2e.yml        ← GitHub Actions CI/CD pipeline
├── config/
│   └── config.py                 ← Appium capabilities & test settings
├── pages/
│   └── base_page.py              ← Page Object Model base class
├── tests/
│   ├── test_01_landing.py        ← TC-001–020  Landing Screen (20 tests)
│   ├── test_02_auth.py           ← TC-021–070  Authentication (50 tests)
│   ├── test_03_onboarding.py     ← TC-071–110  Onboarding Flow (40 tests)
│   ├── test_04_home.py           ← TC-111–150  Home & Navigation (40 tests)
│   ├── test_05_cognitive_tests.py← TC-151–210  Cognitive Tests (60 tests)
│   ├── test_06_reports.py        ← TC-211–250  Reports & Analysis (40 tests)
│   └── test_07_settings_profile_ai.py ← TC-251–300 Settings/AI/MRI (50 tests)
├── utils/
│   └── excel_reporter.py         ← Excel report generator (5 sheets)
├── conftest.py                   ← Pytest fixtures + auto result capture
├── pytest.ini                    ← Pytest configuration
├── requirements.txt              ← Python dependencies
├── run_tests.bat                 ← One-click Windows test runner
└── reports/                      ← Auto-generated (gitignored)
    ├── cognitest_e2e_report.xlsx
    ├── pytest_report.html
    ├── test_output.log
    └── screenshots/
```

---

## 🚀 Quick Start (Local)

### Prerequisites
- Python 3.9+
- Node.js 18+
- Android Studio + SDK (API 30+)
- Android device or emulator connected

### 1. Install Appium
```bash
npm install -g appium@2.5.4
appium driver install uiautomator2
```

### 2. Install Python deps
```bash
cd appium-tests
pip install -r requirements.txt
```

### 3. Configure
Edit `config/config.py` or set environment variables:
```env
TEST_EMAIL=your@email.com
TEST_PASSWORD=YourPassword
DEVICE_NAME=Your Device Name
APK_PATH=E:\PDD\app\build\outputs\apk\debug\app-debug.apk
BACKEND_URL=http://10.35.23.113:3001
```

### 4. Start Appium & Run
```bash
# Terminal 1 - Start Appium
appium

# Terminal 2 - Run all 300 tests
run_tests.bat

# Or run specific module
pytest tests/test_02_auth.py -v

# Or run single test
pytest tests/test_02_auth.py::TestLogin::test_tc028_login_with_valid_credentials -v
```

---

## 🤖 GitHub Actions (CI/CD)

### Setup GitHub Repository

```bash
cd appium-tests
git add .
git commit -m "feat: add 300 Appium E2E test cases with Excel reports"
git remote add origin https://github.com/YOUR_USERNAME/cognitest-appium-tests.git
git push -u origin main
```

### GitHub Secrets to Configure
Go to **Settings → Secrets and variables → Actions** and add:

| Secret | Value |
|--------|-------|
| `TEST_EMAIL` | Your test account email |
| `TEST_PASSWORD` | Your test account password |
| `BACKEND_URL` | Backend URL (tunnel or public) |

### APK Upload
To include the APK in CI runs, add it as a GitHub Release asset named `app-debug.apk` and update the workflow download step, **OR** commit the APK directly (not recommended for large files — use Git LFS).

### Trigger Options
- **On push** to `main`/`develop` — runs automatically
- **On PR** — runs and comments results
- **Manual** — via Actions tab → "Run workflow" (optionally specify a test module)

---

## 📊 Reports

### Excel Report (`cognitest_e2e_report.xlsx`)
5 sheets generated automatically:

| Sheet | Contents |
|-------|----------|
| 📊 Summary | KPI cards: total, passed, failed, pass rate |
| 📋 Test Details | Every test with status, duration, steps, error |
| 📦 Module Summary | Pass rate per module with duration |
| ❌ Failed Tests | All failures with full error messages |
| 📈 Charts | Pie chart + bar chart of results |

### HTML Report (`pytest_report.html`)
Interactive pytest-html report with test details, durations, and tracebacks.

### Screenshots
Auto-saved on test failures to `reports/screenshots/`.

---

## 📋 Test Coverage (300 Test Cases)

| Module | TCs | Coverage |
|--------|-----|----------|
| Landing Screen | 20 | Splash, buttons, navigation, performance |
| Authentication | 50 | Login, SignUp, Forgot PW, OTP, validations |
| Onboarding | 40 | User type, personal info, medical, lifestyle |
| Home & Navigation | 40 | Dashboard, bottom nav, AI FAB, tabs |
| Cognitive Tests | 60 | All 10 test types, results, history |
| Reports & Analysis | 40 | Reports, trends, MRI results, downloads |
| Settings/Profile/AI | 50 | Settings, edit profile, CogniAI, MRI upload |
| **Total** | **300** | **Full E2E coverage** |

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| Appium | 2.5.4 | Mobile test automation |
| UiAutomator2 | latest | Android driver |
| pytest | 8.1.1 | Test framework |
| openpyxl | 3.1.2 | Excel report generation |
| pytest-html | 4.1.1 | HTML report |
| pytest-rerunfailures | 14.0 | Auto-retry flaky tests |
