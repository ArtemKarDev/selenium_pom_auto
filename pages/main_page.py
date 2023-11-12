from .base_page import BasePage

from .locators import MainPageLocators


class MainPage(BasePage):
    # заглушка 
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
