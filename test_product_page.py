
from .pages.base_page import BasePage
from .pages.base_page import LoginPage
from .pages.product_page import ProductPage

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoAlertPresentException
import time
import pytest
#link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
#"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


# @pytest.mark.parametrize('numb', [*range(0,10)])  #,  pytest.param("bugged_link", marks=pytest.mark.xfail), "okay_link"])

@pytest.mark.parametrize('promo_offer', [*range(0,10)])

def test_guest_can_add_product_to_basket(browser, promo_offer):
    browser.delete_all_cookies() # очистка куков (для обнулеия корзины)
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_product_to_basket()          # выполняем метод страницы — добавляем товар в корзину
    page.solve_quiz_and_get_code()

    # проверить сообщение о добавлении товара
    # проверить Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара    
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()



    # pytest -s test_product_page.py

# @pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    browser.delete_all_cookies()  
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    # Открываем страницу товара 
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()   
    # Добавляем товар в корзину 
    page.add_product_to_basket()  
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()

# pytest -s test_guest_cant_see_success_message_after_adding_product_to_basket.py

# @pytest.mark.xfail
def test_guest_cant_see_success_message(browser): 
    browser.delete_all_cookies()  
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    #Открываем страницу товара 
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()     
    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()

# @pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser): 
    browser.delete_all_cookies()  
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    # Открываем страницу товара
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()   
    # Добавляем товар в корзину
    page.add_product_to_basket()  
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.should_disappeared()

# pytest -s test_message_disappeared_after_adding_product_to_baske.py

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page_login = LoginPage(browser, browser.current_url)
    page_login.should_be_login_page()



def test_guest_cant_see_product_in_basket_opened_from_product_page():

# Гость открывает страницу товара
# Переходит в корзину по кнопке в шапке 
# Ожидаем, что в корзине нет товаров
# Ожидаем, что есть текст о том что корзина пуста  