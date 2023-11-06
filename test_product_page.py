
from .pages.base_page import BasePage
from .pages.product_page import ProductPage

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoAlertPresentException
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_product_to_basket()          # выполняем метод страницы — добавляем товар в корзину
    page.solve_quiz_and_get_code()

    # проверить сообщение о добавлении товара
    # проверить Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара    
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()





    # pytest -s test_product_page.py