from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DriverCommands:

    def __init__(self, driver):
        self.driver = driver
        self.wait_time = 5

    def find_element(self, selector):
        return self.driver.find_element(*selector)

    def click_element(self, selector):
        element = self.find_element(selector)
        element.click()

    def fill_in(self, selector, value):
        element = self.find_element(selector)
        element.clear()
        element.send_keys(value)

    def get_text_from_element(self, selector):
        element = self.find_element(selector)
        return element.text

    def check_checkbox_is_selected(self, selector):
        element = self.find_element(selector)
        return element.is_selected()

    def wait_for_element_visibility(self, *selector, wait=None):
        wait = wait or self.wait_time
        try:
            element = WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(selector))
            return element
        except (TimeoutException, NoSuchElementException):
            raise AssertionError( 'Could not find element' + str(selector))

