from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class ChromeHomePage(BasePage):

    privacy_link_hero = (By.ID, "js-privacy-link")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def click_to_download(self, clickable_element):
        self.find_element(*clickable_element).click()

    def is_element_visible(self, element):
        visible_element = self.browser.find_element(*element)
        return visible_element.get_attribute("href")
        # self.browser.execute_script("arguments[0].click;", visible_element)


