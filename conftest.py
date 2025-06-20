import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default= "en",
                     help="Choose language: en or fr")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        print("\n[SETUP] Запуск Chrome браузера...")
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        service = ChromeService(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=chrome_options)

    elif browser_name == "firefox":
        print("\n[SETUP] Запуск Firefox браузера...")
        firefox_options = FirefoxOptions()
        firefox_options.binary_location = r"C:\Users\User\.cache\selenium\firefox\win64\139.0.4\firefox.exe"
        firefox_options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=firefox_options
        )

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser

    print("\n[TEARDOWN] Закрытие браузера...")
    browser.quit()