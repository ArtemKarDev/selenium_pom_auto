from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    Login_form = (By.CSS_SELECTOR, "#login_form")
    Register_form = (By.CSS_SELECTOR, "#register_form")

    Login_email = (By.CSS_SELECTOR, "#id_login-username")
    Login_pass = (By.CSS_SELECTOR, "#id_login-password")
    Reg_email = (By.CSS_SELECTOR, "#id_registration-email")
    Reg_pass1 = (By.CSS_SELECTOR, "#id_registration-password1")
    Reg_pass2 = (By.CSS_SELECTOR, "#id_registration-password2")
    
class ProductPageLocators():
    add_to_basket_button = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
