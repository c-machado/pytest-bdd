from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class ThankYouPage(BasePage):

    URL = "https://www.google.com"
    # DOWNLOAD_CTA_RETRY = (By.CSS_SELECTOR, "a[ga-event-category='retry-download']")
    DOWNLOAD_CTA_RETRY = (By.ID, "js-download-again")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def is_visible_retry_download_link(self):
        base_page = BasePage(self.browser)
        base_page.wait_for_element_visible(*self.DOWNLOAD_CTA_RETRY)
        retry_download_chrome = self.browser.find_element(*self.DOWNLOAD_CTA_RETRY)
        retry_download_chrome.click()
