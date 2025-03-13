from typing import Any, Generator

import pytest

from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright
from utils.browser_config import BrowserConfig

@pytest.fixture(params=["chrome", "firefox"])
def page(request) -> Generator[Page, Any, None]:
    browser_type = request.param
    playwright = sync_playwright().start()
    if browser_type == 'firefox':
        browser = get_firefox_browser(playwright)
        context = get_context(browser)
        page_data = context.new_page()
    elif browser_type == 'chrome':
        browser = get_chrome_browser(playwright)
        context = get_context(browser)
        page_data = context.new_page()
    else:
        browser = get_chrome_browser(playwright)
        context = get_context(browser)
        page_data = context.new_page()
    yield page_data
    for context in browser.contexts:
        context.close()
    browser.close()
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
