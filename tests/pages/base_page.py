from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage(object):

    # It takes in the browser, which will be passed in from the test case
    def __init__(self, browser):
        # Set my local self.browser variable to be whatever browser it's passed in
        self.browser = browser

    def find_element(self, *locator):
        if locator.__len__() == 2:
            return self.browser.find_element(*locator)
        return self.browser.find_element(*(locator[1], locator[2] % locator[0]))

    def wait_for_element_visible(self, *locator):
        wait = WebDriverWait(self.browser, 10)
        if locator.__len__() == 2:
            return wait.until(expected_conditions.visibility_of_element_located(locator[1]))

    def wait_for_element_not_visible(self, *locator):
        wait = WebDriverWait(self.browser, 10)
        if locator.__len__() == 2:
            return wait.until(expected_conditions.invisibility_of_element_located(locator[0]))
        return wait.until(expected_conditions.invisibility_of_element_located(locator[1]))

