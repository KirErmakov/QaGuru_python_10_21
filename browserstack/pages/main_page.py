from selene import browser, have
import allure
from appium.webdriver.common.appiumby import AppiumBy


class MainPage:

    @staticmethod
    def search_request(query):
        with allure.step(f'Android: Search for request: {query}'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(query)

    @staticmethod
    def select_query_result():
        with allure.step('Select search result'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).click()

    @staticmethod
    def check_result(query):
        with allure.step(f'Android: Verify search results for {query}'):
            results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
            results.should(have.size_greater_than(0))
            results.first.should(have.text(query))

    @staticmethod
    def search_request_ios(query):
        with allure.step(f'iOS: Search for request: {query}'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).send_keys(query + '\n')

    @staticmethod
    def check_result_ios(query):
        with allure.step(f'iOS: Verify search results for {query}'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(have.text(query))


main_page = MainPage()
