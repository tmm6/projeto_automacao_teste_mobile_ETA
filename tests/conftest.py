
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from page_object.FavoritePage import FavoritePage
from page_object.MenuPage import MenuPage
from page_object.SearchPage import SearchPage


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

# Desfavorita um evento apos os testes.
@pytest.fixture()
def after_favorite_event(init_app):
    menu = MenuPage(init_app)
    yield init_app
    menu.access_favorites()
    favorite = FavoritePage(menu.driver)
    favorite.remove_favorite()

# Favorita um evento antes do teste.
@pytest.fixture()
def before_favorite_event(init_app):
    search = SearchPage(init_app)
    search.search_event()
        
    favorite = FavoritePage(search.driver)
    favorite.favorite_event()

    search = SearchPage(favorite.driver)
    search.go_back()
    
    yield init_app