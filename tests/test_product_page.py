import pytest
from ..pages.product_page import ProductPage

product_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
another_product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", # упал
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

@pytest.mark.xfail
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.should_be_price()
    page.should_product_added_to_basket()
    page.should_be_equal_prices()

@pytest.mark.negative_checks
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

@pytest.mark.negative_checks
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.negative_checks
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_disappear_of_success_message()

@pytest.mark.guest_login
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.guest_login
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()