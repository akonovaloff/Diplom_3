from typing import Any, Generator

import allure
from allure_commons.types import LabelType
import pytest

from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright
from utils.browser_config import BrowserConfig


@pytest.fixture(params=BrowserConfig.SUPPORTED_BROWSER)
def browser(request):
    browser_type = request.param
    allure.dynamic.tag(browser_type)
    return browser_type


@pytest.fixture()
def page(browser) -> Generator[Page, Any, None]:
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
