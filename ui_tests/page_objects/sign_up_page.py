from .base_page import BasePage


class SignUpPage(BasePage):
    URL = "https://thecatapi.com/signup"

    def navigate_to_sign_up(self):
        self.navigate(self.URL)

    def email_input(self):
        return self.page.locator("input[placeholder='Enter your email']")

    def password_input(self):
        return self.page.query_selector("input[name='password']")

    def confirm_password_input(self):
        return self.page.query_selector("input[name='confirmPassword']")

    def sign_up_button(self):
        return self.page.query_selector("text=Submit")
