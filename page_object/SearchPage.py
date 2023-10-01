import time
from page_object.PageObject import PageObject
from appium.webdriver.common.appiumby import AppiumBy

class SearchPage(PageObject):
    # Elements
    search_field_id = "com.sympla.tickets:id/search_bar_text"
    title_event_resource_id = "com.sympla.tickets:id/sympla_event_title"
    feedback_not_found_id = "com.sympla.tickets:id/app_empty_state_text"
    go_back_id = "com.sympla.tickets:id/search_bar_left_action_container"


    ## Text
    search_text = "Festival REC'n'Play 2023"
    not_found_event_search = "ZZZZZZZZ"
    not_found_expected_result = f"Não encontramos resultados relacionados a “{not_found_event_search}”. Que tal fazer uma nova busca?"
    # number_events_result_text = "Eventos (1)"
    # not_found_number_text = "Eventos (0)"



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
        
    def not_found_event(self):
        search_not_found = self.driver.find_element(by=AppiumBy.ID, value=self.search_field_id)
        search_not_found.click()
        search_not_found.send_keys(self.not_found_event_search)

        # Simula o enter do teclado
        self.driver.execute_script('mobile: performEditorAction', {'action': 'go'})

        feedback_result = self.driver.find_element(by=AppiumBy.ID, value=self.feedback_not_found_id).text

        # #number_event_result = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Eventos (0)")
        return feedback_result == self.not_found_expected_result
    
    def go_back(self):
        go_back = self.driver.find_element(by=AppiumBy.ID, value=self.go_back_id)
        go_back.click()

