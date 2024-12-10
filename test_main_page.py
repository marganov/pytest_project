'''
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "


# Было так:
def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()


# Разбил а две функции:
def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(browser): 
   browser.get(link) 
   go_to_login_page(browser)
'''

import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    

def test_should_be_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()