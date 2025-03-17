import allure
from playwright.sync_api import Page, Playwright, Locator, expect
from abc import abstractmethod
from pages.header_page import Header
from api.burger_user import BurgerUser


class BasePage:
    user: BurgerUser

    @property
    @abstractmethod
    def url(self) -> str:
        pass

    @property
    @abstractmethod
    def locators(self):
        pass


    @allure.step("Open page")
    def __init__(self, page: Page, url: str = None):
        self.pw: Page = page
        if url is not None:
            self.pw.goto(url=url)
        self.header = Header(self.pw)
        allure.attach(page.screenshot(),
                      name="page-screenshot",
                      attachment_type=allure.attachment_type.PNG)

    @staticmethod
    @allure.step("Click on an element")
    def click(element: Locator):
        element.scroll_into_view_if_needed()
        element.hover()
        element.wait_for(timeout=3000, state='visible')
        allure.attach(element.screenshot(),
                      name="element-screenshot",
                      attachment_type=allure.attachment_type.PNG)
        element.click()

    @staticmethod
    @allure.step("Type text")
    def type(element: Locator, text: str):
        element.type(text=text)
        allure.attach(element.screenshot(),
                      name="element-screenshot",
                      attachment_type=allure.attachment_type.PNG)

    @allure.step("Expecting page to have url")
    def expect_to_have_url(self, url: str):
        expect(self.pw).to_have_url(url, timeout=5000)

