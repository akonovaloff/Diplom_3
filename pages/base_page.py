import allure
from playwright.sync_api import Page, Locator, expect
from abc import abstractmethod
from pages.header_page import HeaderPage
from api.burger_user import BurgerUser
from utils.urls import Urls

class BasePage:
    user: BurgerUser
    @property
    @abstractmethod
    def locators(self):
        pass

    @allure.step("Open page")
    def __init__(self, page: Page):
        self.pw: Page = page
        self.header = HeaderPage(self.pw)
        if self.pw.url == "about:blank":
            self.pw.goto(Urls.main_url)

    @allure.step("Click on an element")
    def click(self, element: Locator):
        element.scroll_into_view_if_needed(timeout=3000)
        element.hover()
        element.wait_for(timeout=3000, state='visible')
        allure.attach(element.screenshot(),
                      name="element-screenshot",
                      attachment_type=allure.attachment_type.PNG)
        element.click()
        self.pw.wait_for_load_state(state="networkidle", timeout=5000)


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
