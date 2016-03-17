from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class DriverCommands:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, selector):
        return self.driver.find_element(*selector)

    def find_elements(self, selector):
        elements = self.driver.find_elements(*selector)
        return elements

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

    def wait_for_element_visibility(self, selector, wait_time=None):
        try:
            return WebDriverWait(
                self.driver, wait_time).until(expected_conditions.visibility_of_element_located(selector))
        except TimeoutException:
            return False