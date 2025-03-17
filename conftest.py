from typing import Any, Generator

# framework
import allure

from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright

# project
from utils.browser_config import BrowserConfig
from api.burger_user import BurgerUser
from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage
from pages.base_page import BasePage
from pages.feed_page import FeedPage
from pages.profile_page import ProfilePage
import pytest


@pytest.fixture()
def constructor_page(pw) -> ConstructorPage:
    return ConstructorPage(pw)


@pytest.fixture()
def base_page(pw) -> BasePage:
    return BasePage(pw)


@pytest.fixture()
def feed_page(pw) -> FeedPage:
    return FeedPage(pw)


@pytest.fixture()
def profile_page(pw) -> ProfilePage:
    return ProfilePage(pw)


@pytest.fixture()
def login_user():
    def do_login_user(playwright: Page, user: BurgerUser):
        page = LoginPage(playwright)
        page.email_input.type(user.email)
        page.password_input.type(user.password)
        page.login_button.click()
        page.pw.wait_for_load_state(state="networkidle", timeout=5000)
        return playwright

    return do_login_user


@pytest.fixture
def new_user() -> Generator[BurgerUser, Any, None]:
    """Generate new user data: email, password, name"""
    user = BurgerUser()
    yield user


@pytest.fixture()
def existing_user() -> Generator[BurgerUser, Any, None]:
    user = BurgerUser()
    response = user.registration()
    assert response.success, "The user must be registered before tests"
    yield user


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
