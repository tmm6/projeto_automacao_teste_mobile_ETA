from page_object.PageObject import PageObject
from appium.webdriver.common.appiumby import AppiumBy


class MenuPage(PageObject):
    # Elements
    menu_list_id = "com.sympla.tickets:id/bottom_navigation_item_title"

    perfil_option = "Perfil"
    
    def __init__(self, driver):
        super().__init__(driver)

    # Metodo para selecionar uma opcao do menu.
    def select_option(self, menu_option):
        options_list = self.driver.find_elements(by=AppiumBy.ID, value=self.menu_list_id)
        
        for item in options_list:
            if item.text == menu_option:
                return item
    
    # Metodo para clicar no menu Perfil.      
    def access_perfil(self):
        perfil = self.select_option(self.perfil_option)
        perfil.click()