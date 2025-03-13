from conftest import page
from utils.urls import Urls
from pages.locators import Locators as Loc


class TestFixture:
    def test_page(self, page):
        page.goto(Urls.main_url)
        page.locator(Loc.Header.constructor).hover()
        page.wait_for_timeout(500)
        page.locator(Loc.Header.constructor).click()
        page.wait_for_timeout(3000)
