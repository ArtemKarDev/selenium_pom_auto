from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        Add_to_basket_button = self.browser.find_element(*ProductPageLocators.add_to_basket_button)
        Add_to_basket_button.click()

    # проверика сообщение о добавлении товара
    def should_be_message_about_adding(self):
        # проверяем присутсвие элемента на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), ('Product name i not presented')
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), ('Massage about adding is not presented')
        # Затем получаем текст элементов для проверки
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        # Проверяем, что название товара присутствует в сообщении о добавлении
        assert product_name == message, "No product name in the message"
    
    # проверка Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара
    def should_be_message_basket_total(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        # Затем получаем текст элементов для проверки
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        # Проверяем, что цена товара присутствует в сообщении со стоимостью корзины
        assert product_price == message_basket_total, "No product price in the message"        

    # проверка того что элемент появляется , хотя не должен
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be."

    # проверка того что элемент исчезает
    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared."

