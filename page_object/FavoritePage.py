from page_object.PageObject import PageObject
from appium.webdriver.common.appiumby import AppiumBy


class FavoritePage(PageObject):
    # Elements
    favorite_icon_resource_id = "com.sympla.tickets:id/floating_fav_button_image"
    event_title_id = "com.sympla.tickets:id/sympla_event_title"
    remove_favorite_id = "com.sympla.tickets:id/floating_fav_button_image"
    feedback_no_favorite_id = "com.sympla.tickets:id/app_empty_state_text"

    ## Texts
    event_title_text = "Festival REC'n'Play 2023"
    no_favorite_text = "Nenhum evento favoritado"

    def __init__(self, driver):
        super().__init__(driver)

    def favorite_event(self):
        self.driver.find_element(by=AppiumBy.ID, value=self.favorite_icon_resource_id).click()

    def verify_favorites(self):
        favorite_event_title = self.driver.find_element(by=AppiumBy.ID, value=self.event_title_id).text
        return favorite_event_title == self.event_title_text
    
    def remove_favorite(self):
        self.driver.find_element(by=AppiumBy.ID, value=self.remove_favorite_id).click()

    def verify_empty_favorites_list(self):
        no_favorites = self.driver.find_element(by=AppiumBy.ID, value=self.feedback_no_favorite_id).text
        return no_favorites == self.no_favorite_text


