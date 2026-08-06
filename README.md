# 🧠 CogniTest: AI-Powered Cognitive Assessment & Diagnostic Ecosystem

[![Appium, Selenium & API E2E Verification](https://github.com/harshamukund4070/cognitest-appium-tests/actions/workflows/appium_e2e.yml/badge.svg)](https://github.com/harshamukund4070/cognitest-appium-tests/actions/workflows/appium_e2e.yml)

CogniTest is a state-of-the-art, full-stack medical diagnostics ecosystem combining native Android apps, web interfaces, and AI analytics to track, test, and diagnose cognitive health indicators (e.g., Alzheimer's, Dementia, and mild cognitive impairments).

---

## 📊 CogniTest Comprehensive Verification Dashboard
**Live verification report** generated dynamically from the latest test suite execution.

### Grand Total
| Component | Total | Passed | Failed | Pass Rate | Status |
|---|---|---|---|---|---|
| **Web Frontend E2E (Selenium)** | 300 | 300 | 0 | 100.0% | 🟢 PASSING |
| **Android Mobile E2E (Appium)** | 300 | 300 | 0 | 100.0% | 🟢 PASSING |
| **Backend REST API Tests** | 100 | 100 | 0 | 100.0% | 🟢 PASSING |
| **System Load Testing** | 100 VUs | 100 | 0 | 100.0% | 🟢 PASSING |
| **ALL COMBINED** | 800 | 800 | 0 | 100.0% | 🟢 PASSING |

---

### ⚡ CogniTest System Load Testing — Baseline (100 VUs x 1 Min)
100 Virtual Users running concurrently for 60 seconds against REST endpoints.

**Overall Result:** 🟢 **PASSED**

| Metric | Value | Interpretation |
|---|---|---|
| Requests per second | 1805.05 req/s | Server handled ~1805.0 requests/sec |
| Average response time | 4.01 ms | Typical client waits 4.0ms |
| Fastest response | 0.45 ms | Best-case latency |
| Slowest response | 1078.53 ms | Worst-case latency |
| p95 response time | 8.05 ms | 95% of users under 8.0ms |
| HTTP Error Rate | 0.00% | Ratio of failed requests |

#### ✅ Threshold Validation
* **p95 Response Time:** `< 3,000 ms` | **8.05 ms** | ✅ **PASS**
* **Avg Response Time:** `< 1,500 ms` | **4.01 ms** | ✅ **PASS**
* **HTTP Error Rate:** `< 10%` | **0.00%** | ✅ **PASS**
* **Check Pass Rate:** `> 85%` | **100.00%** | ✅ **PASS**

---

### 🌐 Web Frontend E2E — 300 Test Cases
* **Total:** 300 | **Passed:** 300 | **Failed:** 0 | **Pass Rate:** 100.0%

| Suite | Total | Passed | Failed | Pass Rate |
|---|---|---|---|---|
| Admin / Doctor Login | 80 | 80 | 0 | 100.0% |
| Analytics Dashboard Metrics | 80 | 80 | 0 | 100.0% |
| Patient Registry & Details | 80 | 80 | 0 | 100.0% |
| Web Settings & Preferences | 60 | 60 | 0 | 100.0% |

---

### 📱 Android Mobile E2E — 300 Test Cases
* **Total:** 300 | **Passed:** 300 | **Failed:** 0 | **Pass Rate:** 100.0%

| Suite | Total | Passed | Failed | Pass Rate |
|---|---|---|---|---|
| Splash & Branding | 20 | 20 | 0 | 100.0% |
| Auth Gateways | 50 | 50 | 0 | 100.0% |
| Onboarding Details | 40 | 40 | 0 | 100.0% |
| Dashboard Navigation | 40 | 40 | 0 | 100.0% |
| Cognitive Test Forms | 60 | 60 | 0 | 100.0% |
| Diagnostic Reports | 40 | 40 | 0 | 100.0% |
| Profile Settings & CogniAI | 50 | 50 | 0 | 100.0% |

---

### 🔧 Backend REST API Tests — 100 Test Cases
* **Total:** 100 | **Passed:** 100 | **Failed:** 0 | **Pass Rate:** 100.0%

| Suite | Total | Passed | Failed | Pass Rate |
|---|---|---|---|---|
| User Registration & Auth | 40 | 40 | 0 | 100.0% |
| User Profile Service | 20 | 20 | 0 | 100.0% |
| Cognitive Test Submissions | 20 | 20 | 0 | 100.0% |
| MRI Scan Analysis Service | 20 | 20 | 0 | 100.0% |

---

## 🔒 Security Auditing & SAST / DAST
The entire codebase undergoes regular security scanning integrated within the GitHub Actions pipeline:
* **SAST (Static Application Security Testing):** Bandit python checks found **339 issues** (High: 0, Medium: 5, Low: 334).
* **DAST (Dynamic Application Security Testing):** API penetration testing checks with OWASP ZAP.
* **Secret Scanning:** Banned hardcoded credentials and token leakage checks.

---

## 🛠️ Tech Stack & Architecture

| Component | Platform / Tech | Key Libraries |
|---|---|---|
| **Mobile App** | Android Native (Kotlin) | Jetpack Compose, Retrofit, Room Database |
| **Web Panel** | Next.js (TypeScript) | TailwindCSS, Recharts, Zustand |
| **Backend API** | NestJS (TypeScript) | Prisma ORM, PostgreSQL, Passport JWT |
| **Test Automation** | Python 3.11 | pytest, Selenium, Appium (UiAutomator2) |
| **CI/CD DevOps** | GitHub Actions | Android Emulator Runner, Upload Artifacts |
