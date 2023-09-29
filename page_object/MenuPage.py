from page_object.PageObject import PageObject
from appium.webdriver.common.appiumby import AppiumBy


class MenuPage(PageObject):
    # Elements
    menu_list_id = "com.sympla.tickets:id/bottom_navigation_item_title"

    perfil_option = "Perfil"
    
    def __init__(self, driver):
        super().__init__(driver)
    
    # Metodo para clicar no menu Perfil.      
    def access_perfil(self):
        perfil = self.select_option(self.perfil_option, self.menu_list_id)
        perfil.click()