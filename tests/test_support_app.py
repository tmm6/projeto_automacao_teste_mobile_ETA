import time
from appium.webdriver.webdriver import WebDriver
from page_object.MenuPage import MenuPage
from page_object.PerfilPage import PerfilPage

class TestSupportApp():

    def test_support_app(self, init_app: WebDriver):
        time.sleep(5)
        menu = MenuPage(init_app)
        menu.access_perfil()

        perfil = PerfilPage(menu.driver)
        perfil.access_support()
        assert perfil.verify_support_page(), 'Tela diferente de Suporte'

        