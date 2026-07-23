"""
Appium Test Suite Configuration
CogniTest Android Application
"""
import os

# ─── Appium Server ────────────────────────────────────────────────────────────
APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")

# ─── App Under Test ───────────────────────────────────────────────────────────
APK_PATH = os.getenv(
    "APK_PATH",
    r"E:\PDD\app\build\outputs\apk\debug\app-debug.apk"
)

# ─── Device Capabilities ──────────────────────────────────────────────────────
DESIRED_CAPS = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": os.getenv("DEVICE_NAME", "Android Device"),
    "appium:app": APK_PATH,
    "appium:appPackage": "com.pdd.cognitest",
    "appium:appActivity": ".MainActivity",
    "appium:noReset": False,
    "appium:fullReset": False,
    "appium:newCommandTimeout": 120,
    "appium:androidInstallTimeout": 90000,
    "appium:uiautomator2ServerLaunchTimeout": 60000,
    "appium:autoGrantPermissions": True,
    "appium:ignoreHiddenApiPolicyError": True,
}

# ─── Test Credentials ─────────────────────────────────────────────────────────
TEST_EMAIL        = os.getenv("TEST_EMAIL", "test@cognitest.com")
TEST_PASSWORD     = os.getenv("TEST_PASSWORD", "Test@1234")
TEST_NEW_EMAIL    = os.getenv("TEST_NEW_EMAIL", "newuser@cognitest.com")
TEST_NEW_PASSWORD = os.getenv("TEST_NEW_PASSWORD", "NewPass@1234")
TEST_NAME         = os.getenv("TEST_NAME", "Test User")

# ─── Backend ──────────────────────────────────────────────────────────────────
BACKEND_URL = os.getenv("BACKEND_URL", "http://10.35.23.113:3001")

# ─── Timeouts ─────────────────────────────────────────────────────────────────
IMPLICIT_WAIT    = 15   # seconds
EXPLICIT_WAIT    = 20   # seconds
PAGE_LOAD_WAIT   = 5    # seconds
ANIMATION_WAIT   = 2    # seconds

# ─── Reports ──────────────────────────────────────────────────────────────────
REPORTS_DIR      = os.path.join(os.getcwd(), "reports")
EXCEL_REPORT     = os.path.join(REPORTS_DIR, "cognitest_e2e_report.xlsx")
SCREENSHOTS_DIR  = os.path.join(REPORTS_DIR, "screenshots")
