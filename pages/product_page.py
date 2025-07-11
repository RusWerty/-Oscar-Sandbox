from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_correct_product_added(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME),
            message="Success message with product name not visible"
        )
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        assert product_name == success_message, \
            f"Expected product '{product_name}' in success message, but got '{success_message}'"

    def should_be_correct_price_in_basket(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.BASKET_TOTAL_MESSAGE),
            message="Basket total message not visible"
        )
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        assert product_price == basket_total, \
            f"Expected basket total '{product_price}', but got '{basket_total}'"