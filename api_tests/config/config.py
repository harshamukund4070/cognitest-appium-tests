"""
Backend API Test Configuration
"""
import os

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:3001")
TIMEOUT = 5
