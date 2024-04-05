from browserstack.pages.main_page import main_page


def test_search():
    main_page.search_request('Appium')
    main_page.check_result('Appium')


def test_search_selene():
    main_page.search_request('Selene')
    main_page.select_query_result()
