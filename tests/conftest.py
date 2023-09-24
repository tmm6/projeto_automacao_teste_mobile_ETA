
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from appium.options.android import UiAutomator2Options


@pytest.fixture()
def init_app():
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

    driver = webdriver.Remote("http://127.0.0.1:4723",  options=options)
    # Espera 3 segundos para sair da animacao e acessar a home do aplicativo
    driver.implicitly_wait(3)
    yield driver
    driver.quit()