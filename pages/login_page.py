from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in BasePage.current_url, "Login url is not present"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.Login_form), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.Register_form), "Registration form is not present"