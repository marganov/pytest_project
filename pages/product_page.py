from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button is not presented"

    def add_to_basket(self):
        # Добавляет товар в корзину
        button = self.browser.find_element(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()
        self.solve_quiz_and_get_code()

    def should_be_msg_product_added_to_basket(self):
        # Проверяет наличие сообщения об успешном добавлении товара в корзину
        return self.is_element_present(
            *ProductPageLocators.PRODUCT_WAS_ADDED_TO_BASKET), 'Отсутствует сообщение об успешном добавлении товара в корзину'

    def get_product_name(self):
        # Возвращает название товара
        return self.browser.find_element(*ProductPageLocators.NAME).text

    def get_name_of_product_was_added_to_basket(self):
        # Возвращает название товара, который был добавлен в корзину
        return self.browser.find_element(*ProductPageLocators.PRODUCT_WAS_ADDED_TO_BASKET).text

    def should_product_added_to_basket(self):
        # Проверяет, добавлен ли текущий товар в корзину
        assert self.get_product_name() == self.get_name_of_product_was_added_to_basket(
        ), 'В корзину добавлен не тот товар'

    def should_be_price(self):
        # Проверяет наличие цены товара
        assert self.is_element_present(
            *ProductPageLocators.PRICE), 'Отсутствует цена товара'

    def get_product_price(self):
        # Возвращает цену товара
        msg = self.browser.find_element(*ProductPageLocators.PRICE).text
        return float(re.search(r'\d+[.,]\d{2}', msg).group(0).replace(',', '.')) if msg else 0

    def should_be_basket_mini(self):
        # Проверяет наличие суммы цен товаров, добавленных в корзину
        return self.is_element_present(
            *ProductPageLocators.BASKET_MINI), 'Отсутствует сумма цен товаров, добавленных в корзину'

    def get_total_price(self):
        # Возвращает сумму цен товаров, добавленных в корзину
        msg = self.browser.find_element(*ProductPageLocators.BASKET_MINI).text
        return float(re.search(r'\d+[.,]\d{2}', msg).group(0).replace(',', '.')) if msg else None if msg else 0

    def should_be_equal_prices(self):
        # Проверяет равенство стоимости корзины и товара (ТЗ)
        product_price = self.get_product_price()
        total_price = self.get_total_price()
        assert product_price == total_price, 'Цена в корзине и цена продукта не сходятся. Продукт: {}. Корзина: {}'.format(
            product_price, total_price)

    def should_not_be_success_message(self):
        # Проверяет отсутствие сообщения об успехе
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Присутствует сообщение об успехе"

    def should_disappear_of_success_message(self):
        # Проверяет, что элемент исчез в искомое время
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Сообщение не исчезло"
