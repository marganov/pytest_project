import pytest
from ..pages.product_page import ProductPage

product_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.should_be_price()
    page.should_product_added_to_basket()
    page.should_be_equal_prices()