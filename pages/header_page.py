from playwright.sync_api import Page
from pages.locators import Locators as Loc


class Header:
    locators = Loc.Header

    def __init__(self, pw: Page):
        self.constructor_button = pw.locator(self.locators.constructor)
        self.login_button = pw.locator(self.locators.login)
        self.feed_button = pw.locator(self.locators.feed)
        self.logo = pw.locator(self.locators.logo)
