from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form.well")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form.well")

    # Поля логина
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "#login_form input#id_login-username")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#login_form input#id_login-password")
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#login_form button[name='login_submit']")

    # Поля регистрации
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, "#register_form input#id_registration-email")
    REGISTER_PASSWORD1_INPUT = (By.CSS_SELECTOR, "#register_form input#id_registration-password1")
    REGISTER_PASSWORD2_INPUT = (By.CSS_SELECTOR, "#register_form input#id_registration-password2")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#register_form button[name='registration_submit']")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:first-child .alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-mini")