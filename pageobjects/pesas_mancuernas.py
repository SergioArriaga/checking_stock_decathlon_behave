import os

from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class DecathPesasMancuernas(object):
    """
    Inits a Base Page View Page Model.
    """

    ADD_CART = (By.XPATH, '(//*[@data-anly="pdp-add-to-cart"])[1]')
    ACCEPT_COOKIES = (By.ID, 'didomi-notice-agree-button')
    PRICE = (By.XPATH, '//*[contains(@class,"product-summary-price")]//*[contains(@class, "prc__active-price svelte")]')

    def __init__(self, myDriver):
        self.driver = myDriver

        self.price_text = self.driver.find_element(*self.PRICE)
        self.add_card = self.driver.find_element(*self.ADD_CART)

    def wait_until_loaded(self, timeout=5):
        """
        Wait until page is loaded
        :returns: None
        """
        WebDriverWait(self.driver, timeout).until(presence_of_element_located(self.PRICE))
        WebDriverWait(self.driver, timeout).until(presence_of_element_located(self.ADD_CART))

    def accept_cookies(self):
        """
        Accept cookies if it is neccesary
        :return:
        """
        try:
            self.element_accept_cookies = self.driver.find_element(*self.ACCEPT_COOKIES)
            self.driver.implicitly_wait(10)
            if self.element_accept_cookies.is_displayed():
                self.driver.execute_script("arguments[0].scrollIntoView();", self.element_accept_cookies)
                self.element_accept_cookies.click()
        except NoSuchElementException:
            pass

    def get_price(self):
        """
        Return the price of the item displayed in web
        :return:
        """
        self.driver.implicitly_wait(5)

        if self.price_text.is_displayed():
            return self.price_text.text
        else:
            return None

    def element_add_to_cart_is_enabled(self):
        """
        Check if the element 'add to cart' is clickable
        :return:
        """
        self.driver.implicitly_wait(5)
        ActionChains(self.driver).move_to_element(self.add_card).perform()
        custom_path = os.path.abspath(os.path.join('_output', 'screenshots', 'screenKit_Mancuernas_pesas.png'))
        self.driver.get_screenshot_as_file(custom_path)
        try:
            WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.add_card))
            clickable = True
        except TimeoutException:
            clickable = False
        return clickable
