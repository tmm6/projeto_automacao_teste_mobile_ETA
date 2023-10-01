from appium.webdriver.common.appiumby import AppiumBy
class PageObject:
    def __init__(self, driver):
        self.driver = driver

    # Metodo para selecionar uma opcao de uma lista.
    def select_option(self, option, element):
        options_list = self.driver.find_elements(by=AppiumBy.ID, value=element)
        
        for item in options_list:
            if item.text == option:
                return item
    
    # Simula o enter do teclado   
    def enter_keyboard(self):
        self.driver.execute_script('mobile: performEditorAction', {'action': 'go'})
