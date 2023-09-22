import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.keys import Keys
import unittest

caps = {}
caps["platformName"] = "Android"
caps["appium:automationName"] = "uiautomator2"
caps["appium:deviceName"] = "Android"
caps["appium:appPackage"] = "com.sympla.tickets"
caps["appium:appActivity"] = "com.sympla.tickets.legacy.ui.splash.view.SplashActivity"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

options = UiAutomator2Options()
options.load_capabilities(caps)

class TestSearchEvent(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote("http://127.0.0.1:4723",  options=options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_search_event(self) -> None:
        time.sleep(5)
        search_element = self.driver.find_element(by=AppiumBy.ID, value="com.sympla.tickets:id/search_bar_text")
        search_element.click()
        search_element.send_keys("Festival REC'n'Play 2023")
        search_element.send_keys(Keys.RETURN)
        #self.driver.hide_keyboard()
        time.sleep(10)
