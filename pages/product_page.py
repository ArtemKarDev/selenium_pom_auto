from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        Add_to_basket_button = self.browser.find_element(*ProductPageLocators.add_to_basket_button)
        Add_to_basket_button.click()


    # def should_be_product_page(self):
    #     self.should_be_product_url()

