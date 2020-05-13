from selenium.webdriver.common.by import By


class PageLocators(object):

    chrome_url = "https://www.google.com"
    download_cta_hero = (By.ID, "js-download-hero")
    download_cta_bottom = (By.ID, "js-download-now")
    download_cta_nav = (By.ID, "js-download-header")
    tos_link_hero = (By.ID, "js-tos-link")
    privacy_link_hero = (By.ID, "js-privacy-link")
    productivity_page_link = (By.CSS_SELECTOR, "a[href='/chrome/productivity/']")
    built_in_page_link = (By.CSS_SELECTOR, "a[href='/chrome/googlebuiltin/']")
    security_page_link = (By.CSS_SELECTOR, "a[href='/chrome/security/']")
    anywhere_page_link = (By.CSS_SELECTOR, "a[href='/chrome/anywhere/']")
    privacy_page_link = (By.CSS_SELECTOR, "a[href='/chrome/privacy/']")
    other_platforms_link = (By.ID, "js-other-platform")
    language_selector = (By.ID, "language-selector")
    google_settings_cookie_link = (By.CSS_SELECTOR, "a[ga-event-label='cookie:google-settings']")
    learn_more_cookie_link = (By.CSS_SELECTOR, "a[ga-event-label='cookie:learn-more']")
    close_cookie_cta = (By.CSS_SELECTOR, "button[ga-event-label='cookie:ok-got-it']")