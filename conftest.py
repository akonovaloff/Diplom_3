from typing import Any, Generator

# framework
import allure
import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright

from burger_user import BurgerUser
# project
from utils.browser_config import BrowserConfig
from api.burger_user import BurgerUser


@pytest.fixture
def new_user() -> Generator[BurgerUser, Any, None]:
    """Generate new user data: email, password, name"""
    user = BurgerUser()
    yield user
    user.__del__()

@pytest.fixture()
def existing_user(new_user) -> BurgerUser:
    response = new_user.registration()
    assert response.success, "The user must be registered before tests"
    return new_user

@pytest.fixture(params=BrowserConfig.SUPPORTED_BROWSER)
def browser(request):
    browser_type = request.param
    allure.dynamic.tag(browser_type)
    return browser_type


@pytest.fixture()
def pw(browser) -> Generator[Page, Any, None]:
    playwright = sync_playwright().start()
    if browser == 'firefox':
        driver = get_firefox_browser(playwright)
        context = get_context(driver)
        page_data = context.new_page()
    elif browser == 'chrome':
        driver = get_chrome_browser(playwright)
        context = get_context(driver)
        page_data = context.new_page()
    else:
        driver = get_chrome_browser(playwright)
        context = get_context(driver)
        page_data = context.new_page()
    yield page_data
    for context in driver.contexts:
        context.close()
    driver.close()
    playwright.stop()


def get_firefox_browser(playwright) -> Browser:
    return playwright.firefox.launch(
        headless=BrowserConfig.IS_HEADLESS,
        slow_mo=BrowserConfig.SLOW_MO,
    )


def get_chrome_browser(playwright) -> Browser:
    return playwright.chromium.launch(
        headless=BrowserConfig.IS_HEADLESS,
        slow_mo=BrowserConfig.SLOW_MO
    )


def get_context(browser) -> BrowserContext:
    context = browser.new_context(
        viewport=BrowserConfig.PAGE_VIEWPORT_SIZE,
        locale=BrowserConfig.LOCALE
    )
    context.set_default_timeout(
        timeout=BrowserConfig.DEFAULT_TIMEOUT
    )
    return context
