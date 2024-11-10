import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import FirefoxProfile

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    lang_name = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None
    if (lang_name is not None and browser_name == "chrome"):
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': lang_name})
        browser = webdriver.Chrome(options=options)
        print("\nstart chrome browser for test..")
    elif (lang_name is not None and browser_name == "firefox"):
         fp = webdriver.FirefoxProfile()
         fp.set_preference("intl.accept_languages", lang_name)
         browser = webdriver.Firefox(firefox_profile=fp)
         print("\nstart firefox browser for test..")
    elif lang_name is None:
        raise pytest.UsageError("--fill language code")
    else:
         raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()