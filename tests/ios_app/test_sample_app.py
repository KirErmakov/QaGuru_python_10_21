from browserstack.pages.main_page import main_page


def test_sample_ios_app():
    main_page.search_request_ios('Python')
    main_page.check_result_ios('Python')
