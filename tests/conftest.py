import pytest
import config
import allure
from utils import attach
from appium import webdriver
from selene import browser
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions


def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="android",
                     help="Platform to run tests on (android/ios)")


@pytest.fixture(scope='function', autouse=True)
def mobile_management(request):
    with allure.step('Set options'):
        platform = request.config.getoption('--platform')

        if platform == 'android':
            options = UiAutomator2Options().load_capabilities({
                # Specify device and os_version for testing
                "platformName": "android",
                "platformVersion": "9.0",
                "deviceName": "Google Pixel 3",

                # Set URL of the application under test
                "app": "bs://sample.app",

                # Set other BrowserStack capabilities
                'bstack:options': {
                    "projectName": "First Python project",
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack first_test",

                    # Set your access credentials
                    "userName": config.config.USER_NAME,
                    "accessKey": config.config.ACCESS_KEY
                }
            })

        elif platform == 'ios':
            options = XCUITestOptions().load_capabilities({
                # Specify device and os_version for testing
                "platformName": "ios",
                "platformVersion": "16.0",
                "deviceName": "iPhone 12 Pro",

                # Set URL of the application under test
                "app": "bs://sample.app",

                # Set other BrowserStack capabilities
                'bstack:options': {
                    "projectName": "Second Python project",
                    "buildName": "browserstack-build-2",
                    "sessionName": "BStack second_test",

                    # Set your access credentials
                    "userName": config.config.USER_NAME,
                    "accessKey": config.config.ACCESS_KEY
                }
            })

    browser.config.driver = webdriver.Remote(config.config.URL, options=options)
    browser.config.timeout = config.config.TIMEOUT

    yield

    with allure.step('Add screenshot'):
        attach.add_screenshot(browser)

    with allure.step('Add video'):
        attach.add_video(browser)

    with allure.step('Close driver'):
        browser.quit()
