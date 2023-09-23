import time
from page_object.PageObject import PageObject
from appium.webdriver.common.appiumby import AppiumBy


class PerfilPage(PageObject):
    # Elements
    support_option_id = "com.sympla.tickets:id/txtProfileSupport"
    support_title_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView"

    ## Text
    support_title = "Suporte"


    
    def __init__(self, driver):
        super().__init__(driver)

    def access_support(self):
        self.driver.find_element(by=AppiumBy.ID, value=self.support_option_id).click()
        time.sleep(3)
    
    def verify_support_page(self):
        result = self.driver.find_element(by=AppiumBy.XPATH, value=self.support_title_xpath).text
        return result == self.support_title