from appium.webdriver.webdriver import WebDriver
from page_object.MenuPage import MenuPage
from page_object.PerfilPage import PerfilPage

class Test_SupportApp():

    def test_access_support_app(self, init_app):
        menu = MenuPage(init_app)
        menu.access_perfil()

        perfil = PerfilPage(menu.driver)
        perfil.access_support()
        assert perfil.verify_support_page(), "Tela diferente de Suporte"

    def test_search_question_support(self, init_app):
        menu = MenuPage(init_app)
        menu.access_perfil()

        perfil = PerfilPage(menu.driver)
        perfil.access_support()
        
        assert perfil.to_do_question(), "Resultado da busca incorreta"