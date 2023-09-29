import time
from page_object.PageObject import PageObject
from appium.webdriver.common.appiumby import AppiumBy

class SearchPage(PageObject):
    # Elements
    search_field_id = "com.sympla.tickets:id/search_bar_text"
    title_event_resource_id = "com.sympla.tickets:id/sympla_event_title"

    ## Text
    search_text = "Festival REC'n'Play 2023"


    def __init__(self, driver):
        super().__init__(driver)

    def search_event(self):
        search = self.driver.find_element(by=AppiumBy.ID, value=self.search_field_id)
        search.click()
        search.send_keys(self.search_text)

        # Simula o enter do teclado
        self.driver.execute_script('mobile: performEditorAction', {'action': 'go'})

        event = self.select_option(self.search_text, self.title_event_resource_id)

        if event:
            return True
        else:
            return False