from .base_page import BasePage
from .locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException
import pyperclip


class ProductPage(BasePage):
    def should_be_promo_new_year_page(self):
        self.should_be_promo_new_year_url()
        self.should_be_add_to_basket_button()

    def should_be_promo_new_year_url(self):
        assert "?promo=newYear" in self.browser.current_url, "It's not promo URL"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button is not presented"

    def click_add_to_basket_button(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()

    def solve_quiz_and_get_code(self):
        """Решает формулу на капче и копирует код в буфер обмена (Ctrl+C)"""
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            pyperclip.copy(alert_text.split()[-1])
            print(f"Ваш код: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("Alert отсутствует")