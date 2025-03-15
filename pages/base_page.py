from playwright.sync_api import Page, Playwright, Locator
from abc import abstractmethod
from pages.header import Header

class BasePage:
    @property
    @abstractmethod
    def url(self) -> str:
        pass

    @property
    @abstractmethod
    def locators(self):
        pass

    @abstractmethod
    def assign_page_elements_by_locators(self):
        pass

    def __init__(self, page: Page):
        self.pw: Page = page
        self.pw.goto(self.url)
        self.header = Header(self.pw)
        self.assign_page_elements_by_locators()

