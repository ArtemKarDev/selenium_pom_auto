from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        Add_to_basket_button = self.browser.find_element(*ProductPageLocators.add_to_basket_button)
        Add_to_basket_button.click()

    # проверика сообщение о добавлении товара
    def should_be_message_page(self):
        # проверяем присутсвие элемента на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), ('Product name i not presented')
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), ('Massage about adding is not presented')
        # Затем получаем текст элементов для проверки
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        # Проверяем, что название товара присутствует в сообщении о добавлении
        assert product_name in message, "No product name in the message"
    
    # проверика Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара
    def should_be_massage_basket_total(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        # Затем получаем текст элементов для проверки
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        # Проверяем, что цена товара присутствует в сообщении со стоимостью корзины
        assert product_price in message_basket_total, "No product price in the message"        