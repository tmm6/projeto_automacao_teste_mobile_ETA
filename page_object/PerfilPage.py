import time
from page_object.PageObject import PageObject
from appium.webdriver.common.appiumby import AppiumBy


class PerfilPage(PageObject):
    # Elements
    support_option_id = "com.sympla.tickets:id/txtProfileSupport"
    support_title_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView"
    search_id = "Pesquisar"
    search_field_id = "com.sympla.tickets:id/search_src_text"
    search_result_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView[1]"
    search_title_result_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.widget.TextView[1]"


    ## Text
    support_title = "Suporte"
    search_text = "Como comprar ingressos pelo app"
    result_search = "Como comprar ingressos no app?"



    
    def __init__(self, driver):
        super().__init__(driver)

    def access_support(self):
        self.driver.find_element(by=AppiumBy.ID, value=self.support_option_id).click()
        time.sleep(3)
    
    def verify_support_page(self):
        result = self.driver.find_element(by=AppiumBy.XPATH, value=self.support_title_xpath).text
        return result == self.support_title
    
    def to_do_question(self):

        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=self.search_id).click()
        self.driver.find_element(by=AppiumBy.ID, value=self.search_field_id).send_keys(self.search_text)
        
        # Simula o enter do teclado
        self.driver.execute_script('mobile: performEditorAction', {'action': 'go'})

        # Clica no artigo
        self.driver.find_element(by=AppiumBy.XPATH, value=self.search_result_xpath).click()
        time.sleep(5)

        title_result_search = self.driver.find_element(by=AppiumBy.XPATH, value=self.search_title_result_xpath)

        return title_result_search.text == self.result_search
