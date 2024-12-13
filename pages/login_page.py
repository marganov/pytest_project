from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self._should_be_login_url()
        self._should_be_login_form()
        self._should_be_register_form()

    def _should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Login URL is not presented"

    def _should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def _should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
    
    
    def register_new_user(self, email, password):
        """Регистрирует нового пользователя"""
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT).click()
    