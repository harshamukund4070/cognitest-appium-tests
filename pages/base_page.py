"""
Base Page Object — common Appium interactions shared by all page objects.
"""
import time
import os
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException, NoSuchElementException, WebDriverException
)
from appium.webdriver.common.appiumby import AppiumBy
from config.config import EXPLICIT_WAIT, ANIMATION_WAIT, SCREENSHOTS_DIR


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)
        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

    # ── Finders ───────────────────────────────────────────────────────────────
    def find_by_text(self, text, timeout=EXPLICIT_WAIT):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, f'//*[@text="{text}"]')
                )
            )
        except TimeoutException:
            return None

    def find_by_content_desc(self, desc, timeout=EXPLICIT_WAIT):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.ACCESSIBILITY_ID, desc)
                )
            )
        except TimeoutException:
            return None

    def find_by_xpath(self, xpath, timeout=EXPLICIT_WAIT):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((AppiumBy.XPATH, xpath))
            )
        except TimeoutException:
            return None

    def find_all_by_class(self, class_name):
        try:
            return self.driver.find_elements(AppiumBy.CLASS_NAME, class_name)
        except Exception:
            return []

    # ── Interactions ──────────────────────────────────────────────────────────
    def tap(self, element):
        if element:
            element.click()
            time.sleep(ANIMATION_WAIT)
            return True
        return False

    def tap_by_text(self, text, timeout=EXPLICIT_WAIT):
        el = self.find_by_text(text, timeout)
        return self.tap(el)

    def tap_by_content_desc(self, desc):
        el = self.find_by_content_desc(desc)
        return self.tap(el)

    def type_text(self, element, text, clear_first=True):
        if element:
            if clear_first:
                element.clear()
            element.send_keys(text)
            time.sleep(0.5)

    def type_into_field(self, xpath_or_text, text, by="xpath"):
        if by == "text":
            el = self.find_by_xpath(
                f'//android.widget.EditText[@text="{xpath_or_text}"]'
            )
        else:
            el = self.find_by_xpath(xpath_or_text)
        self.type_text(el, text)

    # ── Scroll helpers ────────────────────────────────────────────────────────
    def scroll_down(self, swipes=1):
        size = self.driver.get_window_size()
        start_x = size['width'] // 2
        start_y = int(size['height'] * 0.7)
        end_y   = int(size['height'] * 0.3)
        for _ in range(swipes):
            self.driver.swipe(start_x, start_y, start_x, end_y, 800)
            time.sleep(0.5)

    def scroll_up(self, swipes=1):
        size = self.driver.get_window_size()
        start_x = size['width'] // 2
        start_y = int(size['height'] * 0.3)
        end_y   = int(size['height'] * 0.7)
        for _ in range(swipes):
            self.driver.swipe(start_x, start_y, start_x, end_y, 800)
            time.sleep(0.5)

    def scroll_to_text(self, text):
        try:
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true))'
                f'.scrollIntoView(new UiSelector().text("{text}"))'
            )
            return True
        except Exception:
            return False

    # ── Assertions ────────────────────────────────────────────────────────────
    def is_text_visible(self, text, timeout=EXPLICIT_WAIT):
        return self.find_by_text(text, timeout) is not None

    def is_element_visible(self, xpath, timeout=EXPLICIT_WAIT):
        return self.find_by_xpath(xpath, timeout) is not None

    def get_text_of(self, xpath):
        el = self.find_by_xpath(xpath)
        return el.text if el else ""

    # ── Navigation ────────────────────────────────────────────────────────────
    def press_back(self):
        self.driver.back()
        time.sleep(ANIMATION_WAIT)

    def wait_for_screen(self, text, timeout=EXPLICIT_WAIT):
        return self.find_by_text(text, timeout) is not None

    # ── Screenshot ────────────────────────────────────────────────────────────
    def take_screenshot(self, name="screenshot"):
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(SCREENSHOTS_DIR, f"{name}_{ts}.png")
        self.driver.save_screenshot(filename)
        return filename

    # ── Input helpers ─────────────────────────────────────────────────────────
    def get_all_edit_texts(self):
        return self.driver.find_elements(
            AppiumBy.CLASS_NAME, "android.widget.EditText"
        )

    def get_all_buttons(self):
        return self.driver.find_elements(
            AppiumBy.XPATH, '//android.widget.Button'
        )

    def hide_keyboard(self):
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass

    def wait_seconds(self, seconds):
        time.sleep(seconds)
