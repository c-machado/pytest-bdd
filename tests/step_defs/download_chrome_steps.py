from pytest_bdd import scenario, given, when, then
from ..pages.chrome_home_page import ChromeHomePage
from ..pages.locators import PageLocators
from ..pages.thank_you_page import ThankYouPage


# This function is executed after all the scenario steps
@scenario("../features/download_chrome.feature", "Download Chrome on Mac OS")
def test_download_mac_chrome():
    pass


# scenarios('../features/download_chrome.feature')
BASE_URL = "https://www.google.com"


@given('a user is at the "<chrome>" website on Mac')
def at_the_chrome_page(browser, chrome):
    chrome_url = BASE_URL + chrome
    browser.get(chrome_url)


@when("the user clicks on the Download button in the hero section")
def user_clicks_to_download_hero(browser):
    chrome_home_page = ChromeHomePage(browser)
    assert(chrome_home_page.is_element_visible(PageLocators.privacy_link_hero))
    assert(chrome_home_page.is_element_visible(PageLocators.tos_link_hero))
    chrome_home_page.click_to_download(PageLocators.download_cta_hero)


@then('the user is redirected to the thank you page')
def redirect_to_thank_you_page(browser):
    assert browser.current_url.__contains__(BASE_URL[:BASE_URL.find("/chrome/thank-you")])


@then("retry link is displayed on the thank you page")
def links_installation_thank_you_page(browser):
    thank_you_page = ThankYouPage(browser)
    thank_you_page.is_visible_retry_download_link()
