
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):

# Гость открывает главную страницу 
# Переходит в корзину по кнопке в шапке сайта
# Ожидаем, что в корзине нет товаров
# Ожидаем, что есть текст о том что корзина пуста     










    # команда для запуска 
    # pytest -v  --language=en test_main_page.py
    # --tb=line  опция - нужно выводить только одну строку из лога каждого упавшего теста