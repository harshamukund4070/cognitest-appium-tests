"""
Selenium Configuration — settings for Web E2E testing.
"""
import os

BASE_URL = os.getenv("WEB_BASE_URL", "http://localhost:3000")
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 15
HEADLESS = os.getenv("HEADLESS_WEB", "true").lower() == "true"
