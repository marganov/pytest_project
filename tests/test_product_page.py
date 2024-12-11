import pytest
from ..pages.product_page import ProductPage

PRODUCT_PAGE_PROMO_NEW_YEAR = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_PAGE_PROMO_NEW_YEAR)
    page.open()
    page.should_be_promo_new_year_page()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()