from .base_page import BasePage


class DocumentationPage(BasePage):
    URL = "https://docs.thecatapi.com/"

    def navigate_to_documentation(self):
        self.navigate(self.URL)

    def api_key_input(self):
        return self.page.query_selector("[placeholder='Enter your API key here...']")
