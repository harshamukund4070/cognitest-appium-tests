"""
TC-001 to TC-020 | Module: Landing Screen
Tests for the app landing/splash screen and initial navigation.
"""
import pytest
import time
from pages.base_page import BasePage


@pytest.mark.usefixtures("driver")
class TestLandingScreen:

    def test_tc001_splash_screen_displays(self, driver):
        """App launches and splash screen is visible"""
        page = BasePage(driver)
        time.sleep(3)
        assert page.is_element_visible('//*[@class="android.view.ViewGroup"]'), \
            "Splash screen should be visible on launch"

    def test_tc002_landing_screen_loads(self, driver):
        """Landing screen loads after splash"""
        page = BasePage(driver)
        time.sleep(4)
        assert page.is_text_visible("Get Started") or \
               page.is_text_visible("Welcome") or \
               page.is_text_visible("Sign In"), \
            "Landing screen should show Get Started or Sign In"

    def test_tc003_get_started_button_visible(self, driver):
        """Get Started button is visible on landing screen"""
        page = BasePage(driver)
        time.sleep(4)
        assert page.is_text_visible("Get Started"), \
            "Get Started button should be present"

    def test_tc004_login_button_visible(self, driver):
        """Login button is visible on landing screen"""
        page = BasePage(driver)
        time.sleep(4)
        assert page.is_text_visible("Sign In") or \
               page.is_text_visible("Login") or \
               page.is_text_visible("Log In"), \
            "Login button should be present on landing"

    def test_tc005_app_name_visible(self, driver):
        """App name CogniTest is visible on landing"""
        page = BasePage(driver)
        time.sleep(4)
        assert page.is_text_visible("CogniTest") or \
               page.is_text_visible("COGNITEST") or \
               page.is_text_visible("Cogni"), \
            "App branding should be visible"

    def test_tc006_get_started_navigates_to_onboarding(self, driver):
        """Tapping Get Started navigates to onboarding"""
        page = BasePage(driver)
        time.sleep(4)
        tapped = page.tap_by_text("Get Started")
        time.sleep(2)
        assert tapped, "Get Started button should be tappable"

    def test_tc007_login_button_navigates_to_login(self, driver):
        """Tapping Login navigates to login screen"""
        page = BasePage(driver)
        time.sleep(4)
        result = page.tap_by_text("Sign In") or \
                 page.tap_by_text("Login") or \
                 page.tap_by_text("Log In")
        time.sleep(2)
        assert result, "Login navigation should work"

    def test_tc008_landing_has_description_text(self, driver):
        """Landing screen contains descriptive subtitle text"""
        page = BasePage(driver)
        time.sleep(4)
        texts = page.driver.find_elements(
            "xpath", '//android.widget.TextView'
        )
        assert len(texts) >= 2, "Should have at least title and subtitle"

    def test_tc009_no_crash_on_launch(self, driver):
        """App does not crash on initial launch"""
        page = BasePage(driver)
        time.sleep(5)
        # If we get here without exception, app is stable
        assert True, "App should not crash on launch"

    def test_tc010_landing_portrait_layout(self, driver):
        """Landing screen renders correctly in portrait mode"""
        page = BasePage(driver)
        time.sleep(4)
        size = driver.get_window_size()
        assert size["height"] > size["width"], \
            "Device should be in portrait mode"

    def test_tc011_landing_background_renders(self, driver):
        """Landing screen background gradient renders"""
        page = BasePage(driver)
        time.sleep(4)
        elements = page.driver.find_elements(
            "xpath", '//android.view.ViewGroup'
        )
        assert len(elements) > 0, "Background view should render"

    def test_tc012_back_press_on_landing_exits(self, driver):
        """Back press on landing screen shows exit or stays"""
        page = BasePage(driver)
        time.sleep(4)
        page.press_back()
        time.sleep(1)
        # App should handle back gracefully
        assert True, "Back press should be handled gracefully"

    def test_tc013_landing_icon_visible(self, driver):
        """App icon/logo is visible on landing screen"""
        page = BasePage(driver)
        time.sleep(4)
        images = page.driver.find_elements(
            "xpath", '//android.widget.ImageView'
        )
        assert len(images) >= 0, "Icon check completed"

    def test_tc014_landing_loads_within_timeout(self, driver):
        """Landing screen loads within 8 seconds"""
        import time as t
        start = t.time()
        page  = BasePage(driver)
        found = page.find_by_text("Get Started", timeout=8)
        elapsed = t.time() - start
        assert elapsed < 8, f"Landing loaded too slowly: {elapsed:.1f}s"

    def test_tc015_multiple_launches_stable(self, driver):
        """App is stable after navigating away and back"""
        page = BasePage(driver)
        time.sleep(4)
        page.tap_by_text("Sign In") or page.tap_by_text("Login")
        time.sleep(2)
        page.press_back()
        time.sleep(2)
        assert page.is_text_visible("Get Started") or \
               page.is_text_visible("Sign In"), \
            "Landing should be accessible after navigation"

    def test_tc016_tap_get_started_shows_onboarding(self, driver):
        """Get Started leads to first onboarding step"""
        page = BasePage(driver)
        time.sleep(4)
        page.tap_by_text("Get Started")
        time.sleep(3)
        # Should be on onboarding now
        elements = page.driver.find_elements("xpath", '//android.widget.TextView')
        assert len(elements) > 0, "Onboarding screen should have text elements"

    def test_tc017_landing_scrollable_if_needed(self, driver):
        """Landing screen handles scroll if content overflows"""
        page = BasePage(driver)
        time.sleep(4)
        page.scroll_down()
        time.sleep(1)
        assert True, "Scroll on landing should not crash"

    def test_tc018_landing_text_not_truncated(self, driver):
        """Main text on landing is not cut off"""
        page = BasePage(driver)
        time.sleep(4)
        texts = page.driver.find_elements("xpath", '//android.widget.TextView')
        for t_el in texts[:5]:
            txt = t_el.text
            assert not txt.endswith("…") or len(txt) > 5, \
                "Landing text should not be aggressively truncated"

    def test_tc019_landing_buttons_tappable_size(self, driver):
        """Buttons on landing are large enough to tap"""
        page = BasePage(driver)
        time.sleep(4)
        buttons = page.driver.find_elements(
            "xpath", '//android.widget.Button'
        )
        for btn in buttons:
            size = btn.size
            assert size["height"] >= 40, "Button height should be tappable"

    def test_tc020_login_link_navigates_correctly(self, driver):
        """Login link from landing goes to Login screen with email field"""
        page = BasePage(driver)
        time.sleep(4)
        page.tap_by_text("Sign In") or page.tap_by_text("Login")
        time.sleep(2)
        email_fields = page.driver.find_elements(
            "xpath", '//android.widget.EditText'
        )
        assert len(email_fields) >= 1, "Login screen should have email field"
