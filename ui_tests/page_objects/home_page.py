from ui_tests.page_objects.base_page import BasePage


class HomePage(BasePage):
    URL = "https://thecatapi.com/"

    def navigate_to_home(self):
        self.navigate(self.URL)

    def get_started_button(self):
        return self.page.query_selector("text=Get Free Access")
