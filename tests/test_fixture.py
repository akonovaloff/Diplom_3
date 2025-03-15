from conftest import pw
from utils.urls import Urls
from pages.locators import Locators as Loc


class TestFixture:
    def test_page(self, pw):
        pw.goto(Urls.main_url)
        pw.locator(Loc.Header.constructor).hover()
        pw.wait_for_timeout(500)
        pw.locator(Loc.Header.constructor).click()
        pw.wait_for_timeout(3000)
